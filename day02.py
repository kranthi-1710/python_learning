import math
import random
import statistics


def calculate_random_numbers(count=5, minimum=1, maximum=100):
	"""Generate numbers and perform common mathematical calculations on them."""
	numbers = [random.randint(minimum, maximum) for _ in range(count)]
	total = sum(numbers)
	product = math.prod(numbers)

	def show(label, value):
		print(f"{label:<28}: {value}")

	show("Random numbers", numbers)
	show("Count", len(numbers))
	show("Sum", total)
	show("Product", product)
	show("Minimum", min(numbers))
	show("Maximum", max(numbers))
	show("Range", max(numbers) - min(numbers))
	show("Mean", f"{statistics.mean(numbers):.2f}")
	show("Median", statistics.median(numbers))
	show("Mode(s)", statistics.multimode(numbers))
	show("Population variance", f"{statistics.pvariance(numbers):.2f}")
	show("Population standard deviation", f"{statistics.pstdev(numbers):.2f}")
	show("Sorted ascending", sorted(numbers))
	show("Sorted descending", sorted(numbers, reverse=True))
	show("Squares", [number**2 for number in numbers])
	show("Cubes", [number**3 for number in numbers])

	if len(numbers) >= 2:
		show("First ÷ second", f"{numbers[0] / numbers[1]:.2f}")
		show("First % second", numbers[0] % numbers[1])
		show("GCD of first two", math.gcd(numbers[0], numbers[1]))
		show("LCM of first two", math.lcm(numbers[0], numbers[1]))


def calculate_super_impressive_problem():
	"""A more advanced random-number challenge with extra analysis."""
	count = 7
	minimum = 10
	maximum = 99
	numbers = [random.randint(minimum, maximum) for _ in range(count)]

	print("\n=== Super Impressive Problem ===")
	print(f"Generated numbers: {numbers}")

	total = sum(numbers)
	average = statistics.mean(numbers)
	median = statistics.median(numbers)
	variance = statistics.pvariance(numbers)
	std_dev = statistics.pstdev(numbers)
	product = math.prod(numbers)
	ascending = sorted(numbers)
	descending = sorted(numbers, reverse=True)
	pair_sum = sum(numbers[:2])
	pair_product = math.prod(numbers[:2])
	largest = max(numbers)
	smallest = min(numbers)

	# Show a more "impressive" set of derived outputs
	for label, value in [
		("Count", len(numbers)),
		("Total", total),
		("Average", f"{average:.2f}"),
		("Median", median),
		("Variance", f"{variance:.2f}"),
		("Standard deviation", f"{std_dev:.2f}"),
		("Product", product),
		("Largest", largest),
		("Smallest", smallest),
		("Range", largest - smallest),
		("Ascending", ascending),
		("Descending", descending),
		("First two sum", pair_sum),
		("First two product", pair_product),
		("Squares", [n ** 2 for n in numbers]),
		("Cubes", [n ** 3 for n in numbers]),
	]:
		print(f"{label:<24}: {value}")

	print("\nChallenge:")
	print("1. Find the mean, median, and range of this set.")
	print("2. Identify the smallest and largest values.")
	print("3. Calculate the sum and product of every number.")
	print("4. Sort the list in ascending and descending order.")
	print("5. Explain how the variance and standard deviation help describe the spread.")


if __name__ == "__main__":
	calculate_random_numbers()
	calculate_super_impressive_problem()
