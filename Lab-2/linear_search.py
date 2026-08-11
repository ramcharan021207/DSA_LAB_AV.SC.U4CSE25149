def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
a = [12,43,6,4,15,24]
print(linear_search(a,15))
