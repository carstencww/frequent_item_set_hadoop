import sys
from operator import itemgetter
import collections
from sets import *
wc={}
cnt=0
s=0.005
with open("../shakespeare_basket/shakespeare-basket1","r") as ins:

	for line in ins:
		cnt+=1
		line = line.strip()
		words = set(line.split(" "))
		words = list(words)
		for word in words:
			if wc.has_key(word):
				wc[word]= wc[word] + 1
			else:
				wc[word] = 1

with open("../shakespeare_basket/shakespeare_basket2","r") as ins:

	for line in ins:
		cnt+=1
		line = line.strip()
		words = set(line.split(" "))
		words = list(words)
		for word in words:
			if wc.has_key(word):
				wc[word]= wc[word] + 1
			else:
				wc[word] = 1


thr=int(cnt*0.005)
#print("threshold",thr)
fw=[]
for key,value in wc.iteritems():
	if value>=thr:
		fw.append(key)
fw.sort()
wc={}
for i in range(len(fw)-1):
	for j in range(i+1, len(fw)):
		pair=(fw[i],fw[j])
		wc[pair]=0
#print(fw)

with open("../shakespeare_basket/shakespeare-basket1","r") as ins:
	for line in ins:
		line = line.strip()
		words = set(line.split(" "))
		words = list(words)
		words.sort()
		for i in range(len(words)-1):
			for j in range(i+1,len(words)):
				pair=(words[i],words[j])
				try:
					wc[pair]=wc[pair]+1
				except:
					pass

with open("../shakespeare_basket/shakespeare_basket2","r") as ins:
	for line in ins:
		line = line.strip()
		words = set(line.split(" "))
		words = list(words)
		words.sort()
		for i in range(len(words)-1):
			for j in range(i+1,len(words)):
				pair=(words[i],words[j])
				try:
					wc[pair]=wc[pair]+1
				except:
					pass





wc=sorted(wc.items(), key=itemgetter(1),reverse=True)

for i in range(40):
	if wc[i][1]>thr:
		print(str(wc[i][0])+'\t'+str(wc[i][1]))
