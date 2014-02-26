# The sum of squares formula and square of sums formula is used to calculate the difference
def main():
    n = 100
    difference = pow(((n * (n+1))/2), 2) - ((n * (n+1) * (2*n+1))/6)
    print(difference)


if __name__ == "__main__":
    main()
