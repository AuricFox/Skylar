'''
Given an integer array, reduce the array to a single element with minimum cost. For reducing, 
remove two elements from the array, add those two numbers and keep the sum back in the array. 
The cost of each operation is the sum of the elements removed in that step.

Example: 

Let A = [1,2,3]

Then, we can remove 1 and 2, add both of them and keep the sum back in array. 
Cost: (1+2) = 3.

So A = [3,3], Cost = 3

In second step, we can remove both elements from the array and keep the sum back in array again. 
Cost: 3 + 3 = 6.

So, A = [6], Cost = 6

So total cost turns out to be 9 (6+3).
'''
import heapq

def reduce_sum(A):
    # Convert the list into a heap structure
    heapq.heapify(A)

    cost = 0
    # Iterate until the list has one element
    while len(A) > 1:
        # Get the first two elements in the heap
        first = heapq.heappop(A)
        second = heapq.heappop(A)

        # Update the cost of the action
        cost += first + second
        # Add the sum of the elements back to the heap
        heapq.heappush(A, first + second)

    return cost

if __name__ == '__main__':
    print(reduce_sum([1,2,3]))      # Prints: 9
    print(reduce_sum([5, 5, 5, 5])) # Prints: 40