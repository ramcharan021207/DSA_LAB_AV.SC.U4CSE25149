def binary_search(arr,key):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid -1
    return -1
print("Ramcharan AV.SC.U4CSE25149")
n = int(input("Enter the number of elements in the array: "))
print("Enter the Elements: ")
arr = []
for i in range(n):
    arr.append(int(input(" ")))
if arr != sorted(arr):
    print("Sorting the array...")
    print("The array is sorted.")
    arr.sort()
key = int(input("Enter the key you want to search: "))
a = binary_search(arr,key)
print(f"The element {key} is found at {a+1} position in the array")            
