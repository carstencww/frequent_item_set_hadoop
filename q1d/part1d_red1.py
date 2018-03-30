#!/usr/bin/env python
import sys
from operator import itemgetter
import collections
me = None
cnt=0
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    key, res  = line.split('\t')
    if me is None:
        me = key
        if key=="__NumB":
            cnt+=int(res)
        else:
            print(key)
    else:
        if me == key:
            if key=="__NumB":
                cnt+=int(res)
        else:
            if me == "__NumB":
                print("__NumB"+'\t'+str(cnt))
            else:
                print(me)
            me = key
            if key=="__NumB":
                cnt+=int(res)
if me == "__NumB":
    print("__NumB"+'\t'+str(cnt))
else:
    print(me)
