#!/usr/bin/python
import sys
def permute(str,b,e,wordlist):
	if b == e and (str not in wordlist):
		wordlist.append(str)
	else:
		i = b
		while i < len(str):
			c = list(str)
			c[b] , c[i] = c[i] , c[b] 
			str = ''.join(c)
			permute(str,b+1,e,wordlist)
			c[b] , c[i] = c[i] , c[b] 
			str = ''.join(c)
			i = i + 1
def writeFile(filename,listvar):
	f = open(filename, 'w')
	for elt in listvar:
		f.write(elt)
		f.write("\n")
inputstring = ''.join(sys.argv[1:])
wordlist = []
permute(inputstring,0,len(inputstring)-1,wordlist)
wordlist.sort()
writeFile("anagram_out.txt",wordlist)
