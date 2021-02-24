## Simple regex engine, elementary  Python  
Originally published: 2010-06-01 12:43:15  
Last updated: 2010-07-10 10:43:30  
Author: Joost Behrends  
  
A short engine for testing against a regex, understanding the 3 common quantifiers 
?,+,* (non-greedy) working on characters, ., [...], [^...], \\s, \\S, bracketed patterns and group designators \\N. Accepts unicode objects and fixed-width encoded strings 
(but problems with eventual comparisons of trailing bytes in multi-byte utf-letters).
Captures up to 10 groups ( (?:...) implemented), which can be used for back referencing and in xreplace(). Captured groups are accessible after the search in the global list xGroups. | is supported, but only in groups and needing nested=True. nested=False is making '(' and ')' common letters.

This is not about Python or for Python, there it has little use beside re. But regarding that re needs about 6,000 lines you might agree with the author, that these 176 lines are powerful. This was the reason to publish it as a recipe - as a kind of (fairly complete) minimal example of a regex tester and as an example for corresponding recursive structures in data (TokenListCache) and code.

Working on this improved the author's understanding of regular expressions - especially of  their eventual "greed". "Greedy" quantifiers are a concept, which has to be explained seperately and is coming unexpected: Whoever is scanning a text for `'<.*>'`, s/he will search SGML tags, not the whole text. Even with the star's "greediness" the code has to take care, that `'.*'` doesn't eat the whole text finding no match for `'<.*>'` at all. Thus the standard syntax with greedy quantifiers cannot be simpler to implement than this with its mere 3 lines 101, 111 and 121 preventing any greed. Perhaps it is faster - otherwise it is difficult to understand, why the concept "greed" is existing at all.

This engine might be useful here and then under circumstances with nothing else available. Its brevity eases translation to other languages and it can work with arbitrary characters for STAR or PERHAPS (for example).