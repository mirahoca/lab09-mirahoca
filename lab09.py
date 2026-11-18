# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline 
    #  1. use i and j for nums in double loop
    #  2. nums[i] + nums [j] should equal target, then return [i,j]
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

    pass


def max_profit(prices):
    # Outline:
    #  1. create variable for best profit, container = 0
    #  2. in a double loop, i will represent buying day, j will represent selling day (j will start at, i+1)
    #  3. profit = prices[j] - prices[i]
    #  4. if profit is greater than container, replace container with profit
    #  5. once loops are finished, return container

    container = 0

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > container:
                container = profit
    return container

    pass


def max_subarray(nums):
    # Outline:
    #  1. create variable, container = nums[0]
    #  2. in a double loop, i will be the position of the block, 
    #     inside initial loop set total = 0, ability to reset i
    #  3. in secondary loop, j will go from i to end, total is then added with nums[j]
    #  4. if the total is greater than the container, then total will replace container 
    #  5. once loops are finished, return container
    
    container = nums[0]

    for i in range(len(nums)):
        total = 0
        for j in range(i, len(nums)):
            total = total + nums[j]
            if total > container:
                container = total

    return container

    pass


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
