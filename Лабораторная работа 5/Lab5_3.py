### LAB NUMBER 5 ### 

#S1 = 'стол';
#S2 = 'стул';

Words = {
	0 : 'ст',
	1 : 'ст',
}

count = 0;
len_0 = len(Words[0]);
len_1 = len(Words[1]);
elem_0 = Words[0];
elem_1 = Words[1];
print(Words[0])

if len_0 > len_1:
	max_len = len_0;
else:
	max_len = len_1;

#print(max_len);

for i in range(max_len):
	try:
		if elem_0[i] == elem_1[i]:
			count += 1;
	except:
		pass;
		#print(count)
#print(max_len)
print(count / max_len);





#def String_Compare(S1, S2):
#	ngrams = [ S1[i:i + 3] for i in range(len(S1)) ]
#	count = 0
#	for ngram in ngrams:
#		count += S2.count(ngram);
#	return count/max(len(S1), len(S2))
#print(String_Compare('ст', 'ст'));