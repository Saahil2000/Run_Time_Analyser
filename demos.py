print("Algorithms file loaded")

def quicksort(arr):
    if len(arr) < 2:  #Base case
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [ ], [ ], [ ]
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        return quicksort(smaller) + equal + quicksort(larger)


def merge_sorted(arr1,arr2):
    sorted_arr = [] #Initalise these so we can use them to iterate through list
    i, j = 0, 0
    while i  <  len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j+=1
    while j < len(arr2): # If j is bigger that i ensures all elements in both lists are appended to sortedlist
        sorted_arr.append(arr2[j])
        j += 1
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    return sorted_arr

def mergesort(arr):
    if len(arr) < 2:  #Base case - if length is one and you are already at base case
        return arr[:]
    else:
        middle = len(arr)//2  #Ineteger division so you dont end up with decimals
        l1 = mergesort(arr[:middle])  #Recursion - a function that calls itself and the condition where it stops calling is called the base case
        #Try thinking about base case first whent thinking about recursion
        l2 = mergesort(arr[middle:])
        return merge_sorted(l1, l2)  #Is called when l1 and l2 in base case
        #l1 will now habe sorted first splitlist and l2 will have second sorted split list

def bubblesort(arr):
    swap_happened = True
    while swap_happened: #more efficient running it 11 times as might run more than necessary
        swap_happened = False  #Will stay as false if no swap n for loop
        for num in range(len(arr)-1):
            if arr[num] > arr[num+1]:
                swap_happened = True
                arr[num], arr[num+1] = arr[num+1], arr[num] #swaps elements
