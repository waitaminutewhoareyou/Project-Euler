from multiprocessing import Pool
from tqdm import tqdm
def pandigitalQ(arg):
    num1, num2 = arg
    product = num1 * num2
    digit_ls = list(str(num1)) + list(str(num2)) + list(str(product))
    if len(digit_ls) != 9:
        return -1
    elif sorted(digit_ls) == [str(i) for i in range(1,10)]:
        return product
    else:
        return -1
space = [(i,j) for i in range(1, 9999) for j in range(1, i) ]

if __name__ == '__main__':
    with Pool(4) as p:
        print('start')
        res = list(tqdm(p.imap(pandigitalQ, space), total=len(space), position=0,leave=False))

    res = list(filter(lambda x: x>0, res))
    print(res)
    print(sum(set(res)))
