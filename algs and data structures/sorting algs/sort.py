import random


#selection sort
def selection_sort(array):

    for i in range(len(array)):
        min_index = i

        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

#quick sort
def partition(array, begin, end):

    pivot = begin

    iter = begin - 1

    array[pivot], array[end] = array[end], array[pivot]
    pivot = end

    for i in range(begin, end):
        if array[i] <= array[pivot]:
            iter += 1
            array[iter], array[i] = array[i], array[iter]

    iter += 1
    array[pivot], array[iter] = array[iter], array[pivot]

    return iter

def partition_r(array, begin, end):

    pivot = random.randint(begin, end)


    iter = begin - 1

    array[pivot], array[end] = array[end], array[pivot]
    pivot = end

    for i in range(begin, end):
        if array[i] <= array[pivot]:
            iter += 1
            array[iter], array[i] = array[i], array[iter]

    iter += 1
    array[pivot], array[iter] = array[iter], array[pivot]

    return iter


def _quick_sort(array, begin, end): #begin end as indices
    while begin<end:

        pivot = partition(array, begin, end)


        if (pivot - begin < end - pivot):
            _quick_sort(array, begin, pivot - 1)
            begin = pivot + 1
         
        else:
            _quick_sort(array, pivot + 1, end)
            end = pivot - 1

def quick_sort(array):
    _quick_sort(array, 0, len(array)-1)            

def _quick_sort_r(array, begin, end):

    while begin<end:

        pivot = partition_r(array, begin, end)


        if (pivot - begin < end - pivot):
            _quick_sort_r(array, begin, pivot - 1)
            begin = pivot + 1
         
        else:
            _quick_sort_r(array, pivot + 1, end)
            end = pivot - 1
            
def quick_sort_r(array):
    _quick_sort_r(array, 0, len(array)-1)  
    


#heapsort


def heap_down(array, index, last):
    L, R = index*2+1, index*2+2
    if L > last: return
    if R > last:
        Lv, Rv = array[L], float('-inf')
    else:
        Lv, Rv = array[L], array[R]

    if array[index] < Lv or array[index] < Rv:
        if Lv < Rv:
            array[index], array[R] = array[R], array[index]
            heap_down(array, R, last)
        else:
            array[index], array[L] = array[L], array[index]
            heap_down(array, L, last)

def heap_sort(array):

    size = len(array)

    for i in reversed(range(size//2)):
        heap_down(array, i, len(array) - 1)

    for i in reversed(range(size)):
        array[0], array[i] = array[i], array[0]
        heap_down(array, 0, i-1)

def insertion_sort(array):
    if (n := len(array)) <= 1:
        return
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key



def sedgewick(n):
    array = []
    iter, gain = 0, 1
    while (n // gain) >= 2:
        array.append(gain)
        iter += 1
        gain = 4 ** iter + 3 * 2 ** (iter - 1) + 1
    return list(reversed(array))

def shell_sort(arr):
    n = len(arr)
    inter = sedgewick(n)
    for gap in inter:
        for i in range(gap,n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp


 