def returnMissingRanges(nums, lower, upper):
    """
    Returns list containing missing ranges in a sorted List
    :var nums: SortedList[int]
    :var lower: int lower bound
    :var upper: int upper bound
    returns missing ranges in a list
    """

    def returnRange(lower, upper):
        """
        Returns range based on lower and upper bound values, to be included in the list
        :var lower: lower bound integer
        :var upper: upper bound integer
        returns range to included in list
        """
        if lower == upper:
            return lower
        return f"{lower}->{upper}"

    previous = lower - 1
    missingRanges = []

    for i in range(len(nums) + 1):
        if i != len(nums):
            current = nums[i]
        else:
            current = upper + 1
        if current - previous >= 2:
            missingRanges.append(returnRange(previous + 1, current - 1))

        previous = current

    return missingRanges


if __name__ == "__main__":
    # test1
    print(returnMissingRanges([0, 1, 3, 50, 75], 0, 99))

    # test2
    print(returnMissingRanges([0, 1, 5, 60, 70, 80, 90, 150], 0, 200))

    # test3
    print(returnMissingRanges([0, 1, 3, 50, 750, 800], 0, 990))

    # test4
    print(returnMissingRanges([0, 10, 34, 501, 754], 0, 990))
