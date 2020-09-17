'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
#First, ask any questions you may have for clarification.
#Make sure to read the question many times and go slow, so that you fully understand before you begin.

#We are given an array of numbers.
# k is the number of elements in the "window" we are going to find the max number in.
# Return an array with the max values from each window that we looped through.
# current index can help keep track of where we are in the arry, the starting index of the window of k elements
# max function in python returns the largest number in a list 

def sliding_window_max(nums, k):
    # Your code here
    #establish an array that will hold the max values we find
    array_of_max_values = []
    
    #establish current index at 0
    current_index = 0
    
    #based on how many elements are in the array, we want the loop to stop when the index is larger than the length of elements in array. To find this number, we would add the k number to index, then subtract 1, and have the while loop run while that number is less than the length of the array.
    while current_index + k - 1 < len(nums):
        #add to the array of max values the max number in the sublist from the current index to the current index + k spot.
        array_of_max_values.append(max(nums[current_index:current_index+k]))
        #increment the current index +=1 so it keeps moving to the right one slot each time it loops
        current_index += 1

    return array_of_max_values


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
