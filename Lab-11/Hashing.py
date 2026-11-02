print("CSE25149 T. Ramcharan")
def separate_chaining(keys, size):
    table = [[] for i in range(size)]

    for key in keys:
        index = key % size
        table[index].append(key)

    print("\nSeparate Chaining:")
    for i in range(size):
        print(i, ":", table[i])

# Linear Probing
def linear_probing(keys, size):
    table = [None] * size

    for key in keys:
        index = key % size

        while table[index] is not None:
            index = (index + 1) % size

        table[index] = key

    print("\nLinear Probing:")
    for i in range(size):
        print(i, ":", table[i])

# Quadratic Probing
def quadratic_probing(keys, size):
    table = [None] * size

    for key in keys:
        index = key % size
        j = 0

        while j < size:
            new_index = (index + j * j) % size

            if table[new_index] is None:
                table[new_index] = key
                break

            j += 1

        else:
            print("Cannot insert", key, "- Table is full")

    print("\nQuadratic Probing:")
    for i in range(size):
        print(i, ":", table[i])

# Main Program
size = int(input("Enter hash table size: "))

n = int(input("Enter number of elements: "))

keys = []

for i in range(n):
    key = int(input("Enter element: "))
    keys.append(key)

separate_chaining(keys, size)
linear_probing(keys, size)
quadratic_probing(keys, size)
