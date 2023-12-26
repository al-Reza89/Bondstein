def find_index(arr, target):
    left=0
    right=len(arr)-1

    while left < right:
        sum = arr[left] + arr[right]

        if sum == target:
            return left, right
        elif sum < target:
            left += 1
        else:
            right -= 1

    return None




arr=[1,2,3,4,5,6,7,8,9,10.11,12]
target=15

i,j=find_index(arr,target)

print(i,j)
