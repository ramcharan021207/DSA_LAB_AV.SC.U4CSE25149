def binary_search(arr,key,low,high):
    mid = (low+high)//2
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr,key,low,mid-1)
    elif arr[mid] < key:
        return binary_search(arr,key,mid+1,high)
    else:
        return -1
def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
print("Ramcharan AV.SC.U4CSE25149")
print(binary_search([10,11,23,25,67],67,0,4))
print(linear_search([10,11,23,25,67],67))



