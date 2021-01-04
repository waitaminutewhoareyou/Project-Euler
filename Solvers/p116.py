from math import factorial

total_length = 50
def count(tile_length):
    min_count = 1
    max_count = total_length // tile_length

    res = 0
    for x in range(min_count, max_count+1):
        single_count = total_length - x*tile_length
        res += factorial(x+single_count) / (factorial(x) * factorial(single_count))

    return res

if __name__ == '__main__':

    print(count(2)+count(3)+count(4))