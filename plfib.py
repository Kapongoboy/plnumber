import argparse

def fibonnaci(n: int) -> list[int]:
    sequence = [0, 1]
    for i in range(1, n):
        sequence.append(sequence[i - 1] + sequence[i])
    return sequence


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog="fibonnaci number printer",
            description='print the nth value of a fibonnaci series',
            )

    parser.add_argument(
            'order',
            type=int, help='the nth value to calculate')

    args = parser.parse_args()

    try:
        print(fibonnaci(int(args.order) - 1))
    except ValueError:
        print("please enter a valid number")
