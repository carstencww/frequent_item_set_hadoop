#!/usr/bin/env python
import sys
from operator import itemgetter
import collections
from sets import *

wc={}
cnt=0
s=0.005
context=[]
HT_size = 100000
HT=[0]*HT_size

#first pass
for line in sys.stdin:
	cnt+=1
	line = line.strip()
	words = set(line.split(" "))
	words = list(words)
	words.sort()
	context.append(words)
	for i in range(len(words)):
		if wc.has_key(words[i]):
			wc[words[i]]= wc[words[i]] + 1
		else:
			wc[words[i]] = 1
		for j in range(i+1, len(words)):
			HT[hash(words[i]+words[j]) % 100000] +=1
thr=int(cnt*0.005)
#print("threshold",thr)
fw={}
for key,value in wc.iteritems():
	if value>=thr:
		fw[key] = value

wc={}

for i in range(len(HT)):
	if HT[i] >= thr:
		HT[i] = True
	else:
		HT[i] = False

#second pass
for words in context:
	for i in range(len(words)-1):
		if fw.has_key(words[i]):
			for j in range(i+1,len(words)):
				if HT[hash(words[i]+words[j]) % 100000] and fw.has_key(words[j]):
					pair=(words[i],words[j])
					try:
						wc[pair]+=1
					except:
						wc[pair]=0

for key,value in wc.iteritems():
	if value>thr:
		print(str(key)+'\t'+str(value))
print("__NumB"+'\t'+str(cnt))
