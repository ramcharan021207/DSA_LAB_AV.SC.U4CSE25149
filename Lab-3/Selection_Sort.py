def Selection_Sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr
print("Ramcharan AV.SC.U4CSE25149")
arr = []
n = int(input("Enter the number of elements:"))
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))
print("Unsorted array:", arr)
print("Sorted array:", Selection_Sort(arr))