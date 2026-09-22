# Ramcharan AV.SC.U4CSE25149
def merge_sort(elements):
	if len(elements) <= 1:
		return elements

	middle = len(elements) // 2
	left = merge_sort(elements[:middle])
	right = merge_sort(elements[middle:])

	merged = []
	left_index = right_index = 0

	while left_index < len(left) and right_index < len(right):
		if left[left_index] <= right[right_index]:
			merged.append(left[left_index])
			left_index += 1
		else:
			merged.append(right[right_index])
			right_index += 1

	merged.extend(left[left_index:])
	merged.extend(right[right_index:])
	return merged

print("Ramcharan AV.SC.U4CSE25149")
elements = list(map(int, input("Enter elements separated by spaces: ").split()))
print("Sorted elements:", *merge_sort(elements))
