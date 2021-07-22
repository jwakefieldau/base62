```
% python3
Python 3.8.5 (default, May 27 2021, 13:30:53) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import base62
>>> base62.to_b62(61)
'z'
>>> base62.to_b62(62)
'10'
>>> base62.to_b62(0xffffffffffffffff)
'LygHa16AHYF'
>>> base62.from_b62('LygHa16AHYF')
18446744073709551615
>>> "%x" % base62.from_b62('LygHa16AHYF')
'ffffffffffffffff'
>>> 
```