import math
import argparse

def e(n: int):
    print(round(math.e, n))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog="e printer",
            description='print e to the nth value',
            )

    parser.add_argument(
            'rounding',
            type=str, help='the number of decimal points to round too')

    args = parser.parse_args()

    try:
        e(int(args.rounding))
    except ValueError:
        print("please enter a valid number")
