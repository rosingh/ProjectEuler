def main():
	factorize = 600851475143
	# Start at 2 to begin checking for prime factors
	factor = 2
	# If the divisor equals the dividend, it's prime
	while factorize != factor:
		# If it is a factor, divide the number by the factor
		if factorize % factor == 0:
			factorize /= factor
		# Else, check another number
		else:
			factor += 1

	print(factorize)


if __name__ == "__main__":
	main()