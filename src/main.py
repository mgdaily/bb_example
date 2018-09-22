import sys

def main():

    print("Running {first_argument}...".format(first_argument=sys.argv[0]))
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    print(a + b)
    print("bb is the best")

if __name__ == "__main__":
    main()
