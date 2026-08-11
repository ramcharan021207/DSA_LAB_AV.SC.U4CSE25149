def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
arr=[]
n = int(input("Enter the numnber of elements:"))
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))
print("Unsorted array:", arr)
print("Sorted array:", bubble_sort(arr))