'''
Input: an integer
Returns: an integer
'''

#Psuedo Code
#Cookie Monster can eat 1, or 2, or 3 cookies at a time
#Recursion problem
#Needs a base case
#Needs a way to get closer to base case
#Fibronacci problem

#First Pass
#Runtime is O(3^n) -- ? that's what sean said in lecture
# def eating_cookies(n):
#     # Your code here
#     if n < 0:
#         return 0
#     if n == 0:
#         return 1
#     else:
#         return eating_cookies(n-3) + eating_cookies(n - 2) + eating_cookies(n - 1) 
    
# print(eating_cookies(5))


#Second Pass with cache
#Runtime is no O(n)
def eating_cookies(n, cache=None):
    if n < 0:
        return 0
    elif n == 0:
        return 1
        #check the cache to see if the answer is stored in there
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            #initialize an empty cache
            cache = {i: 0 for i in range(n+1)}
        #store answers in our cache
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    return cache[n]

print(eating_cookies(5))




if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies =100

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

