def maxNumber(arr):
    max = arr[0]
    n = len(arr)
    for i in range(n):
        if(max<arr[i]):
            max=arr[i]
    return max

def minNumbers(arr):
    min = arr[0]
    n=len(arr)
    for i in range(n):
        if(min>arr[i]):
            min=arr[i]
    return min


arr = [2,3,4,5,6,7,8,9]
print(maxNumber(arr))
print(minNumbers(arr))


	

    