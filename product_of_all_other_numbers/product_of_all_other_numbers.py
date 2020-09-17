'''
Input: a List of integers
Returns: a List of integers
'''
#Returns the product of all numbers except the one at the index
#We can break this down into two groups:
# - the group of numbers multiplied together before the index, and
# - the group of numbers multiplied together after the index


def product_of_all_other_numbers(arr):
    # Your code here
    # when iterating over the input array, the expected value at the current iteration index needs to be the product of every number except the number at the current iteration index

    if len(arr) < 2:
        raise IndexError('need at least 2 numbers')

    #Make a list with the length of the input list to hold our products
    products_of_all_ints_except_at_index = [None] * len(arr)

    #for each integer, find the product of all the integers before it, storing the total product so far each time
    product_so_far = 1
    for i in range(len(arr)):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= arr[i]

    #For each integer, find the product of all the integers AFTER it. Since each index in products already has the product of all the integers before it, now we're storing the total product of all other integers
    product_so_far = 1
    for i in range(len(arr) - 1, -1, -1):
        products_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= arr[i]

    return products_of_all_ints_except_at_index


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
