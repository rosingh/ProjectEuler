def main():
	sum = 0
    # Take the sum of every 5th number.
	for num in xrange(5, 1000, 5):
        # But first check if it's divisible by 3. This is to avoid duplicates.
		if num % 3 != 0:
			sum += num
    # Take the sum of every 3rd number.
	for num in xrange(3, 1000, 3):
		sum += num
	print(sum)

if __name__ == "__main__":
	main()
