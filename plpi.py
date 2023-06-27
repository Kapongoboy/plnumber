import math
import argparse

def pi(n: int):
    print(round(math.pi, n))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog="pi printer",
            description='print pi to the nth value',
            )

    parser.add_argument(
            'rounding',
            type=str, help='the number of decimal points to round too')

    args = parser.parse_args()
    pi(int(args.rounding))
