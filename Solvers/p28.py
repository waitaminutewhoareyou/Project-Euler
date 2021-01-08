target_size = 1001
running_sum = 1
cur = 1
cover_size = 1
inner_dx = 2
outer_dx = 2
while cover_size < target_size:
    # Add the next four corners
    cur += outer_dx
    running_sum += cur
    for _ in range(3):
        cur += inner_dx
        running_sum += cur
    outer_dx += 2
    inner_dx += 2
    cover_size += 2
print(running_sum)