import math
import numpy as np
import os

"""
insertionSort Function:

begin  - starting index
end    - ending index
"""
def insertionSort(begin, end):

    global mOfThree
    global cntComp

    # pointer i loop through the array
    for i in range(begin + 1, end + 1):
        key = arr[i]

        # pointer j iterate backwards for
        # the comparison and swap
        j = i - 1
        # if the item > x, then move it
        # to the next position and
        # swap current position with key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

            cntComp += 1

        arr[j + 1] = key

        cntComp += 1

"""
medianOfThree Function:

i - index begin
k - index end

return index of the median element
"""
def medianOfThree(i, j):

    global arr
    global cntComp

    # index median
    k = (i + j) // 2

    # compare element value of given indexes
    if arr[j] <= arr[i] and arr[i] <= arr[k]:
        return i
    if arr[k] <= arr[i] and arr[i] <= arr[j]:
        return i
    if arr[i] <= arr[j] and arr[j] <= arr[k]:
        return j
    if arr[k] <= arr[j] and arr[j] <= arr[i]:
        return j
    if arr[j] <= arr[k] and arr[k] <= arr[i]:
        return k
    if arr[i] <= arr[k] and arr[k] <= arr[j]:
        return k

    cntComp += 2

"""
Partition Function:

lo       - starting index
hi       - ending index
mOfThree - whether to use median-of-three to choice pivot

return index of the partition position 
"""
def partition(lo, hi):

    global arr
    global mOfThree
    global cntComp

    # starting position of pointer i
    i = lo - 1

    # use median-of-three to choice pivot
    if mOfThree:
        m = medianOfThree(lo, hi)
        arr[m], arr[hi] = arr[hi], arr[m]

    # chose last element as the pivot
    pivot = arr[hi]

    # loop through the array
    for j in range(lo, hi):

        # when current element is smaller than pivot
        if arr[j] < pivot:
            # increment pointer i moving to next position
            i = i + 1
            # swap larger element at i with smaller element at j
            arr[i], arr[j] = arr[j], arr[i]

        cntComp += 1

    # when pointer j reaches the end of the array
    # swap pivot with element in at index position i + 1
    arr[i + 1], arr[hi] = pivot, arr[i + 1]

    return (i + 1)

"""
heapify Function:

arr  - input array to be heapified
n    - size of the heap
i    - root index
"""
def heapify(arr, n, i):

    global cntComp

    # left child of node i is 2i + 1 (0 indexed)
    l = 2 * i + 1
    # right child of node i is 2i + 2 (0 indexed)
    r = l + 1
    # initialize largest as root
    largest = i

    # if left child of node i exists and
    # left child > root, make left child the root
    if l < n and arr[l] > arr[i]:
        largest = l

        cntComp += 1

    # if right child of node i exists and
    # right child > root, make right child the root
    if r < n and arr[r] > arr[largest]:
        largest = r

        cntComp += 1

    # if left or right child node > root
    # swap the root with left/right node
    if largest != i:
        # swap
        arr[i], arr[largest] = arr[largest], arr[i]

        cntComp += 1

        # Recursively heapify the sub-trees
        heapify(arr, n, largest)

"""
buildMaxHeap Function:

arr  - input array to be heapified
n    - size of the heap
"""
def buildMaxHeap(arr, n):

    global cntComp

    i = n
    while i >= 0:
        heapify(arr, n, i)
        i -= 1

        cntComp += 1

"""
heapSort Function:
"""
def heapSort():

    global arr
    global cntComp

    # get array size
    n = len(arr)

    # build Maxheap
    buildMaxHeap(arr, n-1)

    # iterate backwards
    i = n - 1
    while i >= 0:
        # swap root (largest) with last right leaf node
        # (smallest) in the heap
        # --> shifting large numbers to end
        arr[i], arr[0] = arr[0], arr[i]
        # heapify the sub-array
        heapify(arr, i, 0)
        i -= 1

        cntComp += 1

"""
heapSort Function:

begin    - sort starting position
end      - sort ending position
maxDepth - max recursion depth
mOfThree - whether to use median-of-three to choice pivot
"""
def introSort(begin, end, maxDepth):

    global arr

    # get array size
    n = end - begin

    # base case, when array has no more
    # than 1 element to be sorted
    if n <= 1:
        return

    # when the number of elements are relatively small
    # use insertion sort
    elif n < 16:
        insertionSort(begin, end)
        return

    # when the recursion depth exceeds a level based on
    # the number of elements being sorted
    # use heapsort
    elif maxDepth == 0:
        heapSort()
        return

    # partitioning the array into 2
    # use quick sort
    else:
        pivot = partition(begin, end)
        introSort(begin, pivot - 1, maxDepth - 1)
        introSort(pivot + 1, end, maxDepth - 1)

"""
introSortWrapper Function:

begin    - sort starting position
end      - sort ending position
mOfThree - whether to use median-of-three to choice pivot

wrapper to call intro sort
"""
def introSortWrapper(begin, end):

    # get maxDepth for recursion depth
    maxDepth = 2 * math.log2(end - begin)

    introSort(begin, end, maxDepth)

"""
arrRandomGenerator Function:

n  - size of the array to be generated

return a randomized array
"""
def arrRandomGenerator(n):
    arrR = []
    for i in range (n):
        arrR.append(np.random.randint(1,100))
    return arrR


"""
runTestCase Function:

testSetSize - a set of size for the array to be sorted

return a randomized array
"""
def runTestCase(testSetSize):

    # comparison counter for empirical measurements
    global cntComp

    global arr

    outputString = "-" * 150 + "\n"
    for i in testSetSize:

        # run sort on randomized array
        arr = arrRandomGenerator(i)
        outputString += " Original array: " + str(arr) + "\n\n" \
                        " Size of array: " + str(len(arr)) + "\n" \
                        " Median-of-three applied: " + str(mOfThree)
        cntComp = 0
        introSortWrapper(0, len(arr) - 1)
        outputString += "\n Sort randomized array: number of " \
                        "comparison     = " + str(cntComp)

        # run sort on reverse-sorted array
        arr = arr[::-1]
        cntComp = 0
        introSortWrapper(0, len(arr) - 1)
        outputString += "\n Sort reverse-sorted array: number of " \
                        "comparison = " + str(cntComp) + \
                        "\n\n Sorted array:   " + str(arr) + "\n" + \
                        "-" * 150 + "\n"

    return(outputString)

"""
main Function:

Driver code to test above
"""
def main():

    # input array
    global arr

    # comparison counter for empirical measurements
    global cntComp

    # whether to apply median-of-three
    global mOfThree
    mOfThree = True

    # whether to write results into a file
    writeFile = False

    # test set a array with different size
    testSetSize = [10,100,1000,10000]

    results = runTestCase(testSetSize)
    print(results)

    if writeFile:

        # set directory
        os.chdir('/Users/gli/Documents/JHU/EN.605.621.82.SP20 Foundations '
                 'of Algorithms/Progamming_Assignement2')

        # write the sorting results into a file
        exportName = "IntroSort_Output_wz_MedianOf3.txt" \
            if mOfThree else "IntroSort_Output_wo_MedianOf3.txt"

        f = open(exportName, "w")
        f.write(results)
        f.close()

if __name__ == '__main__':
    main()
