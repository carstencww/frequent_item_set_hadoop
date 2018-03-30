#!/usr/bin/env python
import sys
from operator import itemgetter
import collections
from sets import *
wc={}
cnt=0
s=0.0025
context=[]
for line in sys.stdin:
	cnt+=1
	line = line.strip()
	words = set(line.split(" "))
	words = list(words)
	words.sort()
	context.append(words)
	for word in words:
		if wc.has_key(word):
			wc[word]= wc[word] + 1
		else:
			wc[word] = 1

thr=int(cnt*s)

fw=[]
for key,value in wc.iteritems():
	if value>thr:
		fw.append(key)
fw.sort()
wc={}
for i in range(len(fw)-1):
	for j in range(i+1, len(fw)):
		pair=(fw[i],fw[j])
		wc[pair]=0

for words in context:
	for i in range(len(words)-1):
		for j in range(i+1,len(words)):
			pair=(words[i],words[j])
			try:
				wc[pair]=wc[pair]+1
			except:
				pass

fw=0
fp={}
for key,value in wc.iteritems():
	if value>thr:
		fp[key]=value

wc={}
for words in context:
	for i in range(len(words)-2):
		for j in range(i+1,len(words)-1):
			if fp.has_key((words[i],words[j])):
				for k in range(j+1,len(words)):
					tri=(words[i],words[j],words[k])			
					p2 = (words[j],words[k])
					if fp.has_key(p2):
						try:
							wc[tri] = wc[tri] + 1
						except:
							wc[tri] = 0

for key,value in wc.iteritems():
	if value>thr:
		print(str(key)+'\t'+str(value))

print("__NumB"+'\t'+str(cnt))
