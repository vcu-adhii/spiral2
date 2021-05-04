def spiralize(size, n=1):
    x = n  # my variables
    y = 2
    z = n
    prev_step = 0

    while z < pow(size, 2) + n - 1:  # spiralizing any array
        z += y
        x += z
        prev_step += 1
        if prev_step == 4:
            y += 2
            prev_step = 0
    return x


print(spiralize(481, 13))  # test statement
print(spiralize(501, 15))
print(spiralize(461, 50))
