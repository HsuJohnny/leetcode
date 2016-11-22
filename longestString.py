def lengthofLongestSubstring(s):
	
	start=end=0
	length=0
	history=[]
	while (end<len(s) and start<len(s)):
		if (s[end] in history):
			history.remove(s[start])
			start=start+1
		else:
			if (end-start+1>length):
				length=end-start+1
			history.append(s[end])
			end=end+1
	return length
print lengthofLongestSubstring("sdsf")