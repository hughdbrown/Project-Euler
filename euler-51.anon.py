from math import sqrt
from copy import deepcopy
import sys
def getPrimeList(n):
	primeList = range(2,n)
	if n < 11:
		return [2,3,5,7]
	k = int(sqrt(n))
	sqrtPrimeList = getPrimeList(k)
	length = len(primeList)
	primeAssist = [True]*length
	for i in sqrtPrimeList:
		indexList = 2*i-2
		while indexList <length:
			primeAssist[indexList] = False
			indexList += i
	primeList2 = []
	for i in xrange(length):
		if primeAssist[i]:
			primeList2.append(primeList[i])
	primeList = deepcopy(primeList2)
	return primeList

primeList=getPrimeList(1000000)
subPrimeList=[]
length =1
tmplist=[]
for i in primeList:
	if len(str(i))==length:
		tmplist.append(i)
	else:
		length += 1
		subPrimeList.append(tmplist)
		tmplist=[]
		tmplist.append(i)

subPrimeList.append(tmplist)
for isub in range(len(subPrimeList)):
	primeList=deepcopy(subPrimeList[isub])
	while len(primeList)>0:
		i = primeList[0]
		if i<10:
			break
		primeList.remove(i)
		strNum = str(i)
		print i
		for j in range(3):
			stro = str(j)
			tmpList = strNum.split(stro)
			length = len(tmpList)
			if length==1:
				continue
			for ii in range(2**(length-1)-1):
				count = 1
				count2 = 0
				for k in range(j+1,10):
					strr=str(k)
					rstr=''
					for jj in range(length-1):
						if (ii>>(length-2-jj))&1==1:
							rstr += (tmpList[jj]+stro)
						else:
							rstr += (tmpList[jj]+strr)
					rnum = int(rstr+tmpList[-1])
					ff =lambda x,y:int(x)+int(y)
					if rnum&1==0 or reduce(ff,str(rnum))%3==1 or (rnum not in primeList):
						if j==2:
							break
						count2 += 1
					else:
						count += 1

					if count >= 8:
						print i
						sys.exit()
					if count2 >=2:
						break
