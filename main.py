# DSA Lab 2. Search methods
# Student: Konovalov D.
from random import randint
from time import time


# Binary search method
def binarySearch(nums, x, low, high):
    while low <= high:
        #mid = (high+low)//2
        mid = low + (high-low)//2
        if nums[mid] == x:
            return mid
        elif nums[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main():
    n = 316000
    nums = (randint(10, 3500000) for _ in range(n*2))

    snums = sorted(list(nums)[:n])
    #print(snums)

    #Input elem to find
    while True:
        try:
            x = int(input('Enter number to search:'))
            break
        except ValueError:
            print('Only number (0-5000) please!')

    start_time = time() * 1000
    print(start_time)
    search_result = binarySearch(snums, x, 0, len(snums)-1)
    elapsed_time = time() * 1000 - start_time
    print(time()*1000)
    if search_result == -1:
        print(f'{x} not found.')
    else:
        print(f'{x} is on {search_result} position')
    print(f'Time required: {elapsed_time}')


if __name__ == '__main__':
    main()


