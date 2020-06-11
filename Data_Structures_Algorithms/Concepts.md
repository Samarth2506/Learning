# Data Structures and Algorithmic Toolbox Concepts

* Algorithms : A program that solves a problem!

## Arrays

* Ordered list of elements
* Constant time access to read and write elements of the array
* Add/Remove element at the end is O(1) - Size is initialized to a bigger number
* Add/Remove element at the beginning is O(n)
* Add/Remove element at arbitrary location is linear time

## Linked Lists

* Push Front : O(1) - Create a separate node, point that to the first element and then update head to new node
* Push back/pop back : O(n) - without tail pointer
* Doubly Linked List : Forward and Backward pointers

## Stacks

* Push key, pop, top
* Last In First Out (LIFO)

## Queues

* First In First Out (FIFO)
* Cost for ensuing and deqiung are both O(1)



## _Algorithms Notes_

* Strategies:
    * Greedy Approach
    * Divide and Conquer: Break into non-overlapping problems, solve sub problems and combine results.

* GCD of 2 numbers : Find reminder, find gcd of small number and reminder recursively till reminder is zero!
* Linear Search: Worst case: O(n), Binary Search: O(log(n))



### _Big-O-Notation_

* Representative of asymptotic inputs(very large) irrespective specific computing resources.
* Multiplicative constants can be omitted.
* n^a < n^b for 0 < a < b.
* (log n)^a < n^b (a,b > 0) 
* Smaller terms can be omitted (n^2 + n is O(n^2))
* 