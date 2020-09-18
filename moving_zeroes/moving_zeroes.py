'''
Input: a List of integers
Returns: a List of integers
'''

#Need to sort the 0's to the end of the printed array.
#Loop through array
    #if i is 0:
        #add it to the list zeros
    #if not:
        #add it to the list nonzeros
    #Then return the combination of the lists, nonzeros + zeros

#First Pass solution
def moving_zeroes(arr):
    # Your code here
    # zeros = []
    # nonzeros = []

    # for i in arr:
    #     if i == 0:
    #         zeros.append(i)
    #     else:
    #         nonzeros.append(i)

    # return nonzeros + zeros


#Second Pass Solution
# Using a pointer
    #move non-zeros to the front, leaving the zeros will make them at the end anyway bc we are only moving non-zeros
    #if loop finds a 0, it gets swapped with the non-zero, keep going until all have been checked
    
    pointer = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            save_num = arr[i]
            arr[i] = arr[pointer]
            arr[pointer] = save_num
            pointer += 1
    return arr





if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")