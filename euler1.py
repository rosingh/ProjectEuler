def main():
	sum = 0
	for num in xrange(5, 1000, 5):
		if num % 3 != 0 or num % 5 != 0:
			sum += num
	for num in xrange(3, 1000, 3):
		sum += num
	print(sum)

if __name__ == "__main__":
	main()
