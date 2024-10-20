import argparse

def main():
    parser = argparse.ArgumentParser(
        description="A Python script that supports --help."
    )

    parser.add_argument(
        '-n', '--name',
        type=str,
        help='your name to be greeted with a personalized message.'
    )
    parser.add_argument(
        '-a', '--age',
        type=int,
        help='your age to include in the greeting message.'
    )

    args = parser.parse_args()

    if args.name and args.age:
        print(f"Hello {args.name}! You are {args.age} years old.")
    elif args.name:
        print(f"Hello {args.name}!")
    else:
        print("Hello stranger!")

if __name__ == "__main__":
    main()