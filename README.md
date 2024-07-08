# Sanatorium-Accommodation
Problem Statement:

There are N guests (numbered from 0 to N-1) in a sanatorium waiting to be assigned a room. In each room, any number of guests can be accommodated. However, not all guests like to have a lot of roommates. You are given an array A of N integers: the K-th guest wants to be in a room that contains at most A[K] guests, including themselves. Write a function that, given the array A, returns the minimum number of rooms needed to accommodate all guests.

Examples:

Given A = [1, 1, 1, 1, 1], the function should return 5. Each guest should be accommodated in their own separate room.
Given A = [2, 1, 4], the function should return 2. The second guest should be accommodated in one room and the other two guests in another room.
Given A = [2, 7, 2, 9, 8], the function should return 2. The first and the third guests should be accommodated in one room and the other three guests in another room.
Given A = [7, 3, 1, 1, 4, 5, 4, 9], the function should return 4. The guests can be accommodated as follows: the first two guests in one room, the third and the fourth guests in two single rooms, and the other guests in another room.
Assumptions:

N is an integer within the range [1..100,000]
Each element of array A is an integer within the range [1..100,000]
Solution:

The solution to this problem involves using a greedy algorithm to assign guests to rooms. The idea is to sort the guests by their maximum allowed roommates in descending order and then assign them to rooms one by one.

Here is the Python solution:

Edit
Copy code
def solution(A):
    A.sort(reverse=True)
    rooms = 0
    current_room_size = 0
    for guest in A:
        if current_room_size + 1 > guest:
            rooms += 1
            current_room_size = 0
        current_room_size += 1
    return rooms + 1
The time complexity of this solution is O(N log N) due to the sorting, and the space complexity is O(1) since we only use a constant amount of space to store the current room size and the number of rooms.

Explanation:

The solution works by sorting the guests in descending order of their maximum allowed roommates. This ensures that we assign the guests who can tolerate the most roommates to the same room first.

We then iterate through the sorted list of guests and assign them to rooms one by one. If the current room size exceeds the maximum allowed roommates for the current guest, we start a new room and reset the current room size to 0.

Finally, we return the total number of rooms needed, which is the number of rooms we started plus 1 (since we need at least one room to accommodate all guests).

Note:

This solution assumes that the input array A is valid, i.e., it contains N integers within the range [1..100,000]. You may want to add error handling to handle invalid input.