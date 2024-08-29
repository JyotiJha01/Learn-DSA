# Find the largest elements in an array

arr = [3, 5, 7, 2, 8, -1, 4, 10, 12]

def largest_element(arr):
    n = len(arr)

    if not arr:
        return None
    
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element

print(largest_element(arr))
    