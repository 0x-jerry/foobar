"""
The Grandest Staircase Of Them All
==================================
With the LAMBCHOP doomsday device finished, Commander Lambda is preparing to debut on the galactic stage -- but in order to make a grand entrance, Lambda needs a grand staircase! As the Commander's personal assistant, you've been tasked with figuring out how to build the best staircase EVER.

Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with each amount of bricks, so they can pick the one with the most options.

Each type of staircase should consist of 2 or more steps. No two steps are allowed to be at the same height - each step must be lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total amount of bricks that make up that step.
For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having a height of 1: (# indicates a brick)

#
##
21

When N = 4, you still only have 1 staircase choice:

#
#
##
31

But when N = 5, there are two ways you can build a staircase from the given bricks. The two staircases can have heights (4, 1) or (3, 2), as shown below:

#
#
#
##
41

#
##
##
32

Write a function called solution(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200, because Commander Lambda's not made of money!

-- Python cases --
Input:
solution.solution(200)
Output:
    487067745

Input:
solution.solution(3)
Output:
    1
"""


def solution(n):
    """
    3(1): 1 2
    4(1): 1 3
    5(2): 1 4, 2 3
    6(3): 1 2 3, 1 5, 2 4
    7(4): 1 2 4, 1 6, 2 5, 3 4 = f(6, 1) + 1 + f(5, 2) + 1 + f(4, 3) + 1 = (1 + 1) + (0 + 1) + (0 + 1) = 4
    => 1, 6| 2, 5 | 3, 4
    8(5): 1 2 5, 1 3 4, 1 7, 2 6, 3 5
    => 1, 7 | 2, 6 | 3, 5
    9(7): 1 2 6, 1 3 5, 1 8, 2 3 4, 2 7, 3 6, 4 5
    => 1, 8 | 2, 7 | 3, 6 | 4, 5
    10(9):1 2 3 4, 1 2 7, 1 3 6, 1 4 5, 1 9, 2 3 5, 2 8, 3 7, 4 6
    => 1, 9 | 2, 8 | 3, 7 | 4, 6
    """

    cache = {}

    def staircase(n, gt):
        if n < 3:
            return 0
        if n == 3 and gt == 0:
            return 1

        count = getCache(n, gt)
        if count != None:
            return count

        idx = gt + 1

        total = 0

        while idx < n - idx:
            total = total + staircase(n - idx, idx) + 1
            idx = idx + 1

        setCache(n, gt, total)

        return total

    def getCache(n, gt):
        gtRelation = cache.get(n)

        if gtRelation == None:
            return None

        count = gtRelation.get(gt)

        return count

    def setCache(n, gt, v):
        if cache.get(n) == None:
            cache[n] = {}
            cache[n][gt] = v
        else:
            cache[n][gt] = v

    return staircase(n, 0)


print(solution(200))  # 487067745
print(solution(3))  # 1
