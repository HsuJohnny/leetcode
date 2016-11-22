def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    nn=nums1
    mm=nums2
    n=len(nums1)
    m=len(nums2)
    total=n+m
    count=0
    test=0
    ## check whether (m+n)/2 is even or odd
    flag=0
    if (total%2 == 0):
        flag=0   # even
    else:
        flag=1   # odd

    ## find the kth number
    k=total/2

    ## keep finding kth number
    while (k>1):
        print "loop "+str(test)+" times"
        test=test+1
        medianIndex_n=n/2
        medianIndex_m=m/2
        if (n%2 == 0 and n != 1 and n != 0):
            median_n=(nums1[medianIndex_n]+nums1[medianIndex_n-1])/2
        elif (n%2 == 1):
            median_n=nums1[medianIndex_n]
        elif (n == 1):
            median_n=nums1[0]
        else:
            median_n=0
        if (m%2 == 0 and m != 0 and m != 1):

            median_m=(nums2[medianIndex_m]+nums2[medianIndex_m-1])/2
        elif (m%2 == 1):
            median_m=nums2[medianIndex_m]
        elif (m == 1):
            median_m=nums2[0]
        else:
            median_m=0

        if (median_n<median_m):
            if(k>=n/2):
                for x in range(n/2):
                    nums1.remove(nums1[x])
                    count=count+1
                
            else:
                for x in range(k):
                    nums1.remove(nums1[x])
                    count=count+1
            n=n-count
               
        else:
            if(k>=m/2):
                for x in range(m/2):
                    nums2.remove(nums2[x])
                    count=count+1
                
            else:
                for x in range(k):
                    nums2.remove(nums2[x])
                    count=count+1
            m=m-count
        k=k-count
        count=0


    if (flag == 1):
        return min(nums1[0], nums2[0])
    else:
        time=2
        ans=0
        while (time > 0):
            ans=ans+min(nums1[0],nums2[0])
            time=time-1
        return ans/2


print "\n"+str(findMedianSortedArrays([1,2,3,4], [5,6,7,8,9,10]))+" is the median"