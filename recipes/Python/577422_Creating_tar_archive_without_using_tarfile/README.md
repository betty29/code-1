## Creating a tar archive (without using the tarfile module)  
Originally published: 2010-10-11 06:12:13  
Last updated: 2010-10-11 06:18:42  
Author: Benjamin Sergeant  
  
Creating a tar file is easy if you read the spec (you can look it up on wikipedia). Not every kind of files are supported (it support regular files, folders ans symlinks) and it's generating archives for the original tar file format (path length are limited to 100 chars, no extended attributes, ...). It wasn't tested very much but it was a fun hack :) ... I cheated just a little by looking at the python tarfile code from the stdlib for the checksum computation.

A tar file is very simple, it's a list of header/payload for each entry (file|folder|symlink) you want to archive. There's only a payload for file contents. The header is 512 bytes long and can be written in ascii. Numbers (attributes) needs to be written in octal. The files themselves needs to be written in chunks of 512 bytes, which mean you have to fill the last chunk with zeros when the file size is not a multiple of 512 bytes.

Use it like that: 

    python batar.py /tmp/foo.tar `find .` &&  tar tf /tmp/foo.tar # or xf if you want to extract it
