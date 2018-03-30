#!/usr/bin/env python
import sys
from operator import itemgetter
import collections
from sets import *

capa={}
cnt=0
s=0.005

with open("./supp.txt","r") as ins:
	for line in ins:
		line = line.strip()
		if '_' in line:
			_ , cnt = line.split('\t')
		else:
			capa[line]=0

thr=int(int(cnt)*0.005)
for line in sys.stdin:
	line = line.strip()
	words = set(line.split(" "))
	words = list(words)
	words.sort()
	for i in range(len(words)-1):
		for j in range(i+1,len(words)):
			pair=(words[i],words[j])
			if capa.has_key(str(pair)):
				print(str(pair)+'\t'+str(thr))
