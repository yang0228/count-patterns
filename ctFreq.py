# script for cryptography, count number of patterns that appear in high frequency 

import string
import sys
import re
import csv
from collections import Counter
from collections import deque

# python ctFreq.py 1/2/3/4 > output_file(argument means to conclude number of times that x-letter words' appearance)


plain = "YNHPFAZNXPOHCQYAWYRNWRJSCFOFORYAWYRPFTXMCBXFCAWJRECWCFCAWXWJYAWQFNTYFCAWAEYAVPTFCWZQHQFRVQFOXFXJJNRQQQRYTNCFHYAWYRNWQFORJRQCZWAEYNHPFAZNXPOCYQHQFRVQVTQFURUXQRJAWECNVEATWJXFCAWQXPPMCRJYNHPFAZNXPOHPNRQRWFQXNCZANATQXWJQHQFRVXFCYFNRXFVRWFAEEATWJXFCAWXMCQQTRQJRECWCWZYNHPFAZNXPOCYFXQKQXWJQAMICWZWRSYNHPFAZNXPOCYPNAUMRVQTQCWZRLCQFCWZFAAMQFORRVPOXQCQCQAWFORYMXQQCECYXFCAWAEETWJXVRWFXMYAWYRPFQXWJJRVAWQFNXFCWZFORERXQCUCMCFHAEQAMICWZQRIRNXMYRWFNXMYNHPFAZNXPOCYPNAUMRVQ"
tmplain = plain

dictOfPlain = []
while ( len(tmplain) > 0 ):
	dictOfPlain.append(tmplain[0:int(sys.argv[1])])
	tmplain = tmplain [1:]

counterN=Counter(dictOfPlain)
print(counterN.most_common(500))

twoIn = 0

# find pattern TH_/TH__, when command line argument is 3 or 4
with open('twoIn'+sys.argv[1]+'.txt', 'wb') as tinh:
	spamwriter3 = csv.writer(tinh, delimiter=',',
		quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for twoCombi in ['AW','FC','QF','NX','CW','WJ','PF','FA','XF','WZ','RV','HP','PO','FO','XP']:
		for it in set(dictOfPlain):
			pat = '^'+twoCombi+'\w*'
			words = re.match(pat, it)
			if words != None:
				#print "in three:", words.group(0)
				twoIn += 1

		spamwriter3.writerow([twoCombi, twoIn])

		twoIn = 0
tinh.close()		

# find pattern TH_T, when command line argument is 4
with open('that'+sys.argv[1]+'.txt', 'wb') as tinh:
	spamwriter3 = csv.writer(tinh, delimiter=',',
		quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for twoCombi in ['AW','FC','QF','NX','CW','WJ','PF','FA','XF','WZ','RV','HP','PO','FO','XP']:
		for it in set(dictOfPlain):
			pat = '^'+twoCombi+'\w{1}'+twoCombi[:1]
			words = re.match(pat, it)
			if words != None:
				#print "in three:", words.group(0)
				twoIn += 1

		spamwriter3.writerow([twoCombi, twoIn])

		twoIn = 0
tinh.close()		