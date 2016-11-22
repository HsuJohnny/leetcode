class ListNode(object):
	def __init__(self,x):
		self.val=x
		self.next=None


def addTwoNumbers(l1, l2):
	node1=l1
	node2=l2
	nextNode=ListNode(0)
	initialNode=nextNode
	answer=[]
	move=0
	flag=0
	while (flag==0):
		if (node1!=None):
			if (node2!=None):
				Sum=node1.val+node2.val+move
				node1=node1.next
				node2=node2.next
			else:
				Sum=node1.val+move
				node1=node1.next
			if (Sum>9):
				move=1
				Sum=Sum%10
			else:
				move=0
			nextNode.val=Sum
			nextNode.next=ListNode(0)
			nextNode=nextNode.next
			answer.append(Sum)
		elif (node2!=None):
			Sum=node2.val+move
			node2=node2.next
			if (Sum>9):
				move=1
				Sum=Sum%10
			else:
				move=0
			nextNode.val=Sum
			nextNode.next=ListNode(0)
			nextNode=nextNode.next
			answer.append(Sum)
		else:
			flag=1
			if (move==1):
				answer.append(move)
			
	return answer

l1=ListNode(1)
l1.next=ListNode(8)

l2=ListNode(0)

print addTwoNumbers(l1,l2)