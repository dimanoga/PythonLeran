import random


def selection_sort(nums):
    for i in range(len(nums)):
        startest_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[startest_index]:
                startest_index = j
        nums[i], nums[startest_index] = nums[startest_index], nums[i]


def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_inster = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_inster:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_inster


def partition(nums, start, end):
    i, j = start - 1, end + 1
    pivot = nums[(start + end) // 2]
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    def _quick_sort(items, start, end):
        if start < end:
            split_index = partition(items, start, end)
            _quick_sort(items, start, split_index)
            _quick_sort(items, split_index + 1, end)

    _quick_sort(nums, 0, len(nums) - 1)


def quick_sort2(nums):
    if len(nums) > 1:
        pivot = random.choice(nums)
        l = [elem for elem in nums if elem < pivot]
        e = [pivot] * nums.count(pivot)
        r = [elem for elem in nums if elem > pivot]
        return quick_sort2(l) + e + quick_sort2(r)
    else:
        return


nums = [145, 2, 567, 8, 3, 0, 7, -1]
quick_sort2(nums)
print(nums)
