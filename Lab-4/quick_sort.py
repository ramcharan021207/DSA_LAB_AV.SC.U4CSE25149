# Ramcharan AV.SC.U4CSE25149
def quick_sort(values):
	"""Sort a list in ascending order using quick sort."""
	def partition(low, high):
		pivot = values[high]
		i = low - 1

		for j in range(low, high):
			if values[j] <= pivot:
				i += 1
				values[i], values[j] = values[j], values[i]

		values[i + 1], values[high] = values[high], values[i + 1]
		return i + 1

	def sort(low, high):
		if low < high:
			pivot_index = partition(low, high)
			sort(low, pivot_index - 1)
			sort(pivot_index + 1, high)

	sort(0, len(values) - 1)
	return values

print("Ramcharan AV.SC.U4CSE25149")
elements = input("Enter elements separated by spaces: ").split()
numbers = [int(element) for element in elements]
print("Sorted elements:", *quick_sort(numbers))
