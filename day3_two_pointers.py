def two_pointer_sorted(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]
        if sum < target:
            left +=1
        elif sum > target:
            right -=1
        else:
            return [left, right]
    return []

arr = [1,2,3,4,5]
print(two_pointer_sorted(arr, 9))