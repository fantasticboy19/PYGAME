nums = [3, 2, 1, 2, 3]
target = 6


# c++ use hashmap that is simliar to the dict in python


def two_sum(nums, target):
    dict_once = dict()
    index = 0
    for value in nums:
        dict_once[value] = index
        index += 1
    count = 0
    for value in nums:
        other = target - value
        if other in dict_once.keys() and dict_once[other] != count:
            return count, dict_once[other]
    return 'not found !'


print(two_sum(nums, target))
