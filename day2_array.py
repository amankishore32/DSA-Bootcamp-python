def reverse_array(nums):
    start_idx = 0                   # Left Pointer
    end_idx = len(nums) - 1         # Right Pointer

    while start_idx < end_idx:
        # Swap the values within the array where pointers are
        nums[start_idx], nums[end_idx] = nums[end_idx], nums[start_idx]

        start_idx += 1              # Move left pointer right
        end_idx -= 1                # Move right pointer left

    return nums


data_set = [10, 20, 30, 40, 50]
print(reverse_array(data_set))
