def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        ans=[]
        value=0
        if (x<0):
            flag=1
            x=0-x
        else:
            flag=0
        while (x != 0):
            digit=x%10
            ans.append(digit)
            x=x/10
        l=len(ans)-1
        for item in ans:
            value=value+item*(10**l)
            l=l-1
    
        if (flag == 1):
            if (-value < -2**32):
                return 0
            else:
                return -value
        else:
            if (value > (2**32)-1):
                return 0
            else:
                return value
print reverse(32768)