'''
Input: an integer
Returns: an integer
'''

#Psuedo Code
#Cookie Monster can eat 1, or 2, or 3 cookies at a time
#Recursion problem
#Needs a base case
#Needs a way to get closer to base case

def eating_cookies(n):
    # Your code here
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return eating_cookies(n-3) + eating_cookies(n - 2) + eating_cookies(n - 1) 

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
