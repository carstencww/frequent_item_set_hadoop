#!/usr/bin/env python
import sys
from operator import itemgetter
import collections
me = None
thr=0
cnt=0
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    key, thr  = line.split('\t')
    if me is None:
        me = key
        cnt = 1
    else:
        if me == key:
            cnt += 1
        else:
            if cnt >= int(thr):
                print(me+'\t'+str(cnt))
            me = key
            cnt = 1
if cnt >= int(thr):
    print(me+'\t'+str(cnt))
