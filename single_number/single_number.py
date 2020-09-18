'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
#Return the single number that is not repeated
#create new array that will hold list of n that only occurs once
#loop through original array 
    #for every element in original array:
        #if n is in the new array, remove n at its index (pop)
    #otherwise, add n to the new array (append)
#return the new array at first index. because there will only be one element that doesn't get popped out of new array, the remaining element will be the single number.

#First Pass Solution:
# def single_number(arr):
#     # Your code here
#     new_arr = []
#     for n in arr:
#         if n in new_arr:
#             new_arr.pop(new_arr.index(n))
#         else:
#             new_arr.append(n)

#     return new_arr[0]


#Second Pass Improved Runtime:
# O(n) runtime
def single_number(arr):
    #sets are a closely related cousin to dictionaries
    #they don't associate values with keys
    # they're useful for when you need to uniqueness property of dicts
    s = set()
    # s = []

    for num in arr: #O(n)
        if num in s: #O(1)
            s.remove(num) #O(1)
        else:
            s.add(num) #O(1)
    #at this point, the only element left in the set is our odd-element-out
    #return list(s)[0] #O(1)
    return s.pop()


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")