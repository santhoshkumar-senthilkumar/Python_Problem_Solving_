nums =[1,2,3,4,5,6]
target = 8
for i in range(len(nums)) :
    for j in range(i+1,len(nums)):
        b=nums[i]+nums[j]
        if b== target :
            print(nums[i],nums[j])
            break
    if target == b:
        break
