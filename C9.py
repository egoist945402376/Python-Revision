__author__ = 'Muelsyse'
import sys

def greet():
    # argv: a list of command line arguments passed to a Python script
    # argv[0] is the script name
    args = sys.argv
    if len(args) == 1:
        print('Hello to the one running this function!')
    elif len(args) == 2:
        print(f"Hello, nice to meet you, {args[1]}!")
    else:
        print('There are too many arguments!')

def main():
    greet()


if __name__ == '__main__':
    main()
