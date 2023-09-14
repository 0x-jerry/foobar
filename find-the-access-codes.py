"""
Find the Access Codes
=====================
In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need access to it. But the only door leading to the LAMBCHOP chamber is secured with a unique lock system whose number of passcodes changes daily. Commander Lambda gets a report every day that includes the locks' access codes, but only the Commander knows how to figure out which of several lists contains the access codes. You need to find a way to determine which list contains the access codes once you're ready to go in.

Fortunately, now that you're Commander Lambda's personal assistant, Lambda has confided to you that all the access codes are "lucky triples" in order to make it easier to find them in the lists. A "lucky triple" is a tuple (x, y, z) where x divides y and y divides z, such as (1, 2, 4). With that information, you can figure out which list contains the number of access codes that matches the number of locks on the door when you're ready to go in (for example, if there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access codes).

Write a function solution(l) that takes a list of positive integers l and counts the number of "lucky triples" of (li, lj, lk) where the list indices meet the requirement i < j < k. The length of l is between 2 and 2000 inclusive. The elements of l are between 1 and 999999 inclusive. The solution fits within a signed 32-bit integer. Some of the lists are purposely generated without any access codes to throw off spies, so if no triples are found, return 0.

For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the solution 3 total.

-- Python cases --
Input:
solution.solution([1, 1, 1])
Output:
    1

Input:
solution.solution([1, 2, 3, 4, 5, 6])
Output:
    3
"""


def solution(raw_list):
    """
    1, 2, 1, 3, 1
    1 1 3
    1 1 1
    """

    list_len = len(raw_list)

    # (x, i) => [(y1, i2), (y2,i2), ...]
    lucky_pairs = {}

    i = 0
    while i < list_len:
        x = raw_list[i]

        x_pair = lucky_pairs.get((x, i))

        if x_pair == None:
            x_pair = []
            lucky_pairs[(x, i)] = x_pair

        j = i + 1
        while j < list_len:
            y = raw_list[j]
            if y % x == 0:
                x_pair.append((y, j))
            j += 1

        i += 1

    total = 0

    i = 0

    while i < list_len:
        x = raw_list[i]
        x_pair = lucky_pairs.get((x, i))

        if x_pair == None:
            continue

        for y in x_pair:
            y_pair = lucky_pairs.get(y)
            if y_pair == None:
                continue

            total += len(y_pair)

        i += 1

    return total


print(solution([2, 4]))  # 0
print(solution([1, 2, 3]))  # 0
print(solution([1, 1, 1]))  # 1
print(solution([1, 1, 1, 1]))  # 4
print(solution([1, 2, 1, 3, 1]))  # 2
print(solution([4, 2, 1, 2, 1]))  # 0
print(solution([1, 2, 3, 4, 5, 6]))  # 3
s = range(1, 2000)
print(solution(s))  # 40777
