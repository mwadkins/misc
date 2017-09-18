def permute (str,prefix):
	if (len(str) == 0):
		print prefix
	else:
		for i in range (0,len(str)):
			rem = str[0:i] + str[i+1:]
			p=prefix + str[i]
			permute(rem,p)

def permutation (str): 
	permute(str,"")


permutation("walrus")
