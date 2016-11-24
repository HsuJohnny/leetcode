def maxArea(height):
	
	maxarea=0
	length=len(height)
	right=0
	left=length-1
	while (right != left):
		maxarea=max(maxarea, min(height[right], height[left])*(left-right))
		if (height[right] > height[left]):
			left=left-1
		else:
			right=right+1
	return maxarea


print maxArea([1,2,3,4,5])	



			
