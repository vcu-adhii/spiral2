def spiralize(size, n=1):
    """ Your code goes somewhere in here"""


def spiralize(number):
    x = 1  # myvariables
    y = 2
    z = 0
    prev_step = 0

    while x <= pow(number, 2):  # spiralizing the array
        z += x
        x += y
        prev_step += 1
        if prev_step == 4:
            y += 2
            prev_step = 0
    return z


print(spiralize(501))  # printing solution to homework question = 83960501
