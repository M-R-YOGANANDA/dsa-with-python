l1=[1,2,3,4,5,6,7,8,9]
target=5
start=0
end=len(l1)-1
while start<=end:
    mid=(start+end)//2
    mid_element=l1[mid]
    if mid_element==target:
        print(mid)
        break
    elif target<mid_element:
        end=mid-1
    else:
        start=mid+1 
        
