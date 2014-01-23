def main():
	fibNums = populateFibList()
	sum = 0
	# Every 3rd fibonacci number is even, so just add those up.
	for i in xrange(2, len(fibNums) - 1, 3):
			sum += fibNums[i]
	print(sum)
	print(fibNums)


def populateFibList():
	fibs = []
	num = 0
	while True:
		if num == 0 or num == 1:
			fibs.append(1)
		elif fibs[num - 1] > 4000000:
			break
		else:
			fibs.append(fibs[num - 1] + fibs[num - 2])
		num += 1
	return fibs


if __name__ == "__main__":
	main()