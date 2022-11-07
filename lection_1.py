from random import randint


def get_random_password():
    password = ''
    for i in range(8):
        random_num = randint(40, 126)
        ch = chr(random_num)
        password = password + chr(random_num)
    return password


get_random_password()
