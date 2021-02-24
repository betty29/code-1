import inspect, types, dis

__all__ = ['export_nonlocals', 'nonlocals']

# http://www.jonathon-vogel.com/posts/patching_function_bytecode_with_python/
def find_code(code, f):
    i = 0
    while i < len(code):
        if f(code, i):
            return i
        elif code[i] < dis.HAVE_ARGUMENT:
            i += 1
        else:
            i += 3

# http://nedbatchelder.com/blog/201301/byterun_and_making_cells.html
def make_cell(value):
    return (lambda x: lambda: x)(value).func_closure[0]

globals().update(dis.opmap)

def export_nonlocals(*vars):
    def func(f):
        code = map(ord, f.func_code.co_code)
        varnames = list(f.func_code.co_varnames)
        names = list(f.func_code.co_names)
        cf=lambda c,i:c[i] in (LOAD_FAST,STORE_FAST) and varnames[c[i+1]] in vars
        while True:
            idx = find_code(code, cf)
            if idx is None:
                break
            code[idx] = LOAD_NAME if code[idx] == LOAD_FAST else STORE_NAME
            var = varnames[code[idx+1]]
            code[idx+1] = len(names)
            try:
                code[idx+1] = names.index(var)
            except ValueError:
                names.append(var)
        for i, var in enumerate(filter(varnames.__contains__, names)):
            varnames[varnames.index(var)] = '__anon_var_%d' % i
        rescode = types.CodeType(f.func_code.co_argcount, f.func_code.co_nlocals,
                                 f.func_code.co_stacksize,
                                 f.func_code.co_flags^0x01,
                                 ''.join(map(chr, code)), f.func_code.co_consts,
                                 tuple(names), tuple(varnames),
                                 f.func_code.co_filename, f.func_code.co_name,
                                 f.func_code.co_firstlineno,
                                 f.func_code.co_lnotab, f.func_code.co_freevars,
                                 f.func_code.co_cellvars)
        return types.FunctionType(rescode, dict(f.func_globals, __ns=True),
                                  f.func_name, f.func_defaults, f.func_closure)
    return func

def nonlocals(*vars):
    def func(f):
        caller = inspect.stack()[1][0]
        caller_vars = caller.f_globals
        caller_vars.update(caller.f_locals)
        code = map(ord, f.func_code.co_code)
        varmap = {}
        freevars = list(f.func_code.co_freevars)
        freec = len(freevars)
        freeoffs = len(f.func_code.co_cellvars)
        varnames = list(f.func_code.co_varnames)
        closure = list(f.func_closure or [])
        names = list(f.func_code.co_names)
        consts = list(f.func_code.co_consts)
        fglobals = {'__nonlocal_plocals': caller.f_locals}
        names.extend(fglobals.keys())
        plocals_pos = len(names)-1
        offs = 0
        def cf(c, i):
            if c[i] in (LOAD_FAST, STORE_FAST) and varnames[c[i+1]] in vars:
                return True
            elif c[i] in dis.hasjabs:
                c[i+1] += offs
        while True:
            idx = find_code(code, cf)
            if idx is None:
                break
            code[idx] = LOAD_DEREF if code[idx] == LOAD_FAST else STORE_DEREF
            var = varnames[code[idx+1]]
            code[idx+1] = len(freevars)
            try:
                code[idx+1] = freevars.index(var)
            except ValueError:
                freevars.append(var)
            code[idx+1] += freeoffs
            if code[idx] == STORE_DEREF and caller_vars.get('__ns') == True:
                const_id = len(consts)
                try:
                    const_id = consts.index(var)
                except ValueError:
                    consts.append(var)
                code.insert(idx, DUP_TOP)
                code[idx+4:idx+4] = [
                    LOAD_GLOBAL, plocals_pos, 0,
                    LOAD_CONST, const_id, 0,
                    STORE_SUBSCR
                ]
                offs += 4
        nlocals = len(freevars)-freec+f.func_code.co_nlocals
        closure.extend(map(make_cell, map(caller_vars.__getitem__,
                                       freevars[freec:])))
        rescode = types.CodeType(f.func_code.co_argcount, nlocals,
                                 f.func_code.co_stacksize, f.func_code.co_flags,
                                 ''.join(map(chr, code)), tuple(consts),
                                 tuple(names), tuple(varnames),
                                 f.func_code.co_filename, f.func_code.co_name,
                                 f.func_code.co_firstlineno,
                                 f.func_code.co_lnotab, tuple(freevars),
                                 f.func_code.co_cellvars)
        return types.FunctionType(rescode, dict(f.func_globals, **fglobals),
                                  f.func_name, f.func_defaults, tuple(closure))
    return func
