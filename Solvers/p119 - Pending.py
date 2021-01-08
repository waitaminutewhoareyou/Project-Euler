from tqdm import tqdm
n = 10


def interestingQ(num):
    digit_sum = sum(map(int, list(str(num))))
    while not (num % digit_sum):
        num = num / digit_sum
    return num == 1


if __name__ == '__main__':
    N = 30
    interestingN = []
    pbar = tqdm(total=N, desc='searched')
    while len(interestingN) < N:
        if interestingQ(n):
            interestingN.append(n)
            # print('Interesting n', interestingN)
            pbar.set_postfix(current_n=f'{n}', refresh=True)
            pbar.update()
        n += 1

    print(interestingN)
    print(n)