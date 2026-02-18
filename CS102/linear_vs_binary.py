def linear_search_steps(lst, target):
    steps = 0
    for item in lst:
        if item == target:
            return steps
        steps += 1
    return steps

def binary_search_steps(lst, target):
    steps = 0
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (right + left) // 2
        steps += 1
        if lst[mid] == target:
            return steps
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid -1
    return steps

lst = list(range(1, 33))  # numbers 1..32
target = 32

print("Linear steps:", linear_search_steps(lst, target))
print("Binary steps:", binary_search_steps(lst, target))
