import argparse

def nice(n: int) -> list[int]:
    sequence = []
    for i in range(n):
        sequence.append(69)
    return sequence


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog="are you based?",
            description='mess around and find out.',
            )

    parser.add_argument(
            'score',
            type=int, help='😏')

    args = parser.parse_args()

    try:
        print(nice(int(args.order)))
    except ValueError:
        print("please enter a valid number")
