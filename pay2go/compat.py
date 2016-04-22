# coding: utf-8

import sys


_version = sys.version_info

is_py2 = (_version[0] == 2)
is_py3 = (_version[0] == 3)

if is_py2:
    from urllib import urlencode
elif is_py3:
    from urllib.parse import urlencode
