import time
import pygame


def swap(arr, a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp


def show(arr, rect_width, screen, delay, cur_col):
    width, height = pygame.display.get_window_size()
    screen.fill("black")
    for index, x in enumerate(range(0, width, rect_width)):
        rect_height = arr[index]
        rect_y = height - rect_height
        pygame.draw.rect(screen, "white", (x, rect_y, rect_width, rect_height))
        for cur, col in cur_col:
            if cur == index:
                pygame.draw.rect(screen, col, (x, rect_y, rect_width, rect_height))

    pygame.display.flip()
    time.sleep(delay)


def bubble_sort(arr, rect_width, screen, delay):
    n = len(arr)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            show(arr, rect_width, screen, delay, [(j, "red"), (n - i, "green")])
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
    show(arr, rect_width, screen, delay, [(0, "green")])


def insertion_sort(arr, rect_width, screen, delay):
    n = len(arr)
    already_sorted = [(0, "green")]
    for i in range(1, n):
        for j in range(i, 0, -1):
            already_sorted.append((i, "green"))
            show(arr, rect_width, screen, delay, already_sorted + [(j, "red")])
            if arr[j - 1] < arr[j]:
                break
            swap(arr, j - 1, j)
    show(arr, rect_width, screen, delay, already_sorted)


def selection_sort(arr, rect_width, screen, delay):
    n = len(arr)
    already_sorted = []
    for i in range(0, n):
        mini = (-1, float("inf"))
        for j in range(i, n):
            show(arr, rect_width, screen, delay, [(j, "red"), (mini[0], "blue")] + already_sorted)
            if mini[1] > arr[j]:
                mini = (j, arr[j])
        swap(arr, i, mini[0])
        already_sorted.append((i, "green"))
    show(arr, rect_width, screen, delay, [(n - 1, "green")])


def quick_sort(arr, rect_width, screen, delay):
    def partition(nums, left, right):
        p = right
        right -= 1
        i = left
        while i <= right:
            show(arr, rect_width, screen, delay, [(i, "red"), (right, "red"), (p, "blue")] + already_sorted)
            if nums[right - (i - left)] > nums[p]:
                swap(arr, right - (i - left), right)
                right -= 1
            else:
                i += 1
        swap(arr, right + 1, p)
        return right + 1

    def quicksort_helper(nums, left, right):
        if left < right:
            p = partition(nums, left, right)
            already_sorted.append((p, "green"))
            quicksort_helper(nums, left, p - 1)
            quicksort_helper(nums, p + 1, right)
        already_sorted.append((left, "green"))

    already_sorted = []
    quicksort_helper(arr, 0, len(arr) - 1)
    show(arr, rect_width, screen, delay, already_sorted)


def merge_sort(arr, rect_width, screen, delay):

    def merge(nums, left, middle, right):
        part_left = nums[left:middle+1]
        part_right = nums[middle+1:right+1]
        l = r = 0
        already_sorted = []
        for i in range(left, right+1):
            already_sorted.append((i,"green"))
            show(arr, rect_width, screen, delay, already_sorted + [(i, "red"), (left, "blue"), (right, "blue"), ])
            if len(part_left) > l and len(part_right) > r:
                if part_left[l] < part_right[r]:
                    nums[i] = part_left[l]
                    l += 1
                else:
                    nums[i] = part_right[r]
                    r += 1
            elif l < len(part_left):
                for item in part_left[l:]:
                    nums[i] = item
            else:
                for item in part_right[r:]:
                    nums[i] = item

    def divide(nums, left, right):
        if left < right:
            middle = (right+left)//2
            show(arr, rect_width, screen, delay, [(left, "red"), (right, "red"), (middle, "blue"), ])
            divide(nums, left, middle)
            divide(nums, middle+1, right)
            merge(nums, left, middle, right)

    divide(arr, 0, len(arr)-1)
    show(arr, rect_width, screen, delay, [(num, "green") for num in range(len(arr))])


def heap_sort():
    pass


def radix_sort():
    pass
