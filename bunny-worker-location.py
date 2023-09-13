"""
Bunny Worker Locations
======================
Keeping track of Commander Lambda's many bunny workers is starting to get tricky. You've been tasked with writing a program to match bunny worker IDs to cell locations.

The LAMBCHOP doomsday device takes up much of the interior of Commander Lambda's space station, and as a result the work areas have an unusual layout. They are stacked in a triangular shape, and the bunny workers are given numerical IDs starting from the corner, as follows:

| 7
| 4 8
| 2 5 9
| 1 3 6 10

Each cell can be represented as points (x, y), with x being the distance from the vertical wall, and y being the height from the ground.

For example, the bunny worker at (1, 1) has ID 1, the bunny worker at (3, 2) has ID 9, and the bunny worker at (2,3) has ID 8. This pattern of numbering continues indefinitely (Commander Lambda has been adding a LOT of workers).

Write a function solution(x, y) which returns the worker ID of the bunny at location (x, y). Each value of x and y will be at least 1 and no greater than 100,000. Since the worker ID can be very large, return your solution as a string representation of the number.

-- Python cases --
Input:
solution.solution(5, 10)
Output:
    96

Input:
solution.solution(3, 2)
Output:
    9
"""


def solution(x, y):
    current_level = x + y - 1
    previous_level = current_level - 1
    previous_total_workers = previous_level * (previous_level + 1) / 2
    
    current_worker_id = previous_total_workers + x
    
    return str(current_worker_id)

print(solution(5, 10))  # 96
print(solution(3, 2))  # 9
print(solution(100000, 100000))  # 19,999,800,001
