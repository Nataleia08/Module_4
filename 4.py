import sys


def parse_args():
    result = ""
    res_list = sys.argv.copy()
    res_list.pop(0)
    for arg in res_list:
        result = result + arg
        if arg != res_list[-1]:
            result = result + " "
    return result
