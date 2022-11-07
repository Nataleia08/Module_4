import sys


def parse_args():
    result = ""
    for arg in sys.argv:
        if not arg.endswith('.py'):
            result = result + str(arg) + " "
    result.rstrip()

    return result


k = parse_args()
print(k)
