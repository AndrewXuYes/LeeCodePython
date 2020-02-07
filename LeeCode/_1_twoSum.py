def twoSum(nums, target):
    hashmap = {}
    for ind, num in enumerate(nums):
        hashmap[num] = ind
    for i, num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i != j:
            return [i, j]


def twoSum2(nums, target):
    """这样写更直观，遍历列表同时查字典"""
    dct = {}
    for i, n in enumerate(nums):
        if target - n in dct:
            return [dct[target - n], i]
        dct[n] = i


if __name__ == '__main__':
    print(twoSum([1, 2, 3, 4, 6, -1], 6))
    print(twoSum2([1, 2, 3, 4, 6, -1], 6))
