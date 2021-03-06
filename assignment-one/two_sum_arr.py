import sys
# Given two arrays a and b of numbers and a target value t, 
# find a number from each array whose sum is closest to t. 
# Example: a=[9, 13, 1, 8, 12, 4, 0, 5], b=[3, 17, 4, 14, 6], t=20
# => [13, 6] or [4, 17] or [5, 14]

def two_arrs_brute_force(items1, items2, t):
    # O(n^2)
    # create list to hold difference of 
    # target - (item1 + item2) for each
    differences = list()
    for item1 in items1:
        for item2 in items2:
            # append absolute value of difference
            differences.append([abs(t - (item1 + item2)), [item1, item2]])
    
    return min(differences)[1] # get lowest difference, return pair


def two_arrs(items1, items2, t):
    items2.sort() # O(n log n)
    items2.sort() # O(n log n)

    difference = sys.maxsize
    left_pointer = 0
    right_pointer = len(items2) - 1
    left_result = int()
    right_result = int()

    while left_pointer < len(items1) and right_pointer >= 0:
        if abs(items1[left_pointer] + items2[right_pointer] - t) < difference:
            left_result = left_pointer
            right_result = right_pointer
            difference = abs(left_pointer + right_pointer - t)
    
        if items1[left_pointer] + items2[right_pointer] > t:
            right_pointer = right_pointer - 1
        else:
            left_pointer = left_pointer + 1

    return [left_result, right_result]


if __name__ == "__main__":
    print(two_arrs([9, 13, 1, 8, 12, 4, 0, 5], [3, 17, 4, 14, 6], 33))
    print(two_arrs_brute_force([9, 13, 1, 8, 12, 4, 0, 5], [3, 17, 4, 14, 6], 33))