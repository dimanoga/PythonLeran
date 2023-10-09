from typing import List


def kek(nums: List[int]) -> List[int]:
    i = 0
    while i < len(nums):
        pos = nums[i]
        if nums[i] != nums[pos]:
            nums[i], nums[pos] = nums[pos], nums[i]
        else:
            i += 1

    miss = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            miss.appens(i + 1)
    return miss


def main():
    kek([4, 3, 2, 7, 8, 2, 3, 1])


if __name__ == '__main__':
    main()
