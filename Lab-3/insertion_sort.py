def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
print("Ramcharan AV.SC.U4CSE25149")
arr=[]
n = int(input("Enter the number of Elements:"))
print("Enter elements")
for i in range(n):
    arr.append(int(input()))
print("Unsorted array:", arr)
print("Sorted array:", insertion_sort(arr))