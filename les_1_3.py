def is_valid_password(password):
    l = len(password)
    if l != 8:
        return False
    else:
        k_v = 0
        k_n = 0
        k_s = 0
        l_pass = list(password)
        for i in l_pass:
            if i.isdigit():
                k_s = k_s + 1
            elif i.islower():
                k_n = k_n + 1
            elif i.isupper():
                k_v = k_v + 1
        if (k_v > 0) and (k_n > 0) and (k_s > 0):
            return True
        else:
            return False


is_valid_password('NmlDl1V0')
