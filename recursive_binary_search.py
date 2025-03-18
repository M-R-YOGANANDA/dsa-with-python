def binary_search(start,end,target):  
  while start<=end:
      mid=(start+end)//2
      mid_element=l1[mid]
      if mid_element==target:
          return(mid)
          break
      elif target<mid_element:
          binary_search(start,mid-1,target)
      else:
          binary_search(mid+1,end,target)
    return(-1)
l1=[1,2,3,4,5,6,7,8,9]
target=5
start=0
end=len(l1)-1
result=binary_search(start,end,target)
print(result)
