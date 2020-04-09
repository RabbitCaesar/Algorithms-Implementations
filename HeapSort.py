import numpy as np
import os

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

arr  - input array to be sorted
"""
def heapSort(arr):

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

    outputString = "-" * 150 + "\n"
    for i in testSetSize:

        # run sort on randomized array
        arr = arrRandomGenerator(i)
        outputString += " Original array: " + str(arr) + "\n\n" \
                        " Size of array: " + str(len(arr)) + "\n"
        cntComp = 0
        heapSort(arr)
        outputString += "\n Sort randomized array: number of " \
                        "comparison     = " + str(cntComp)

        # run sort on reverse-sorted array
        arr = arr[::-1]
        cntComp = 0
        heapSort(arr)
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

    # comparison counter for empirical measurements
    global cntComp

    # whether to write results into a file
    writeFile = False

    # test set a array with different size
    testSetSize = [10, 100, 1000, 10000]

    results = runTestCase(testSetSize)
    print(results)

    if writeFile:
        # set directory
        os.chdir('/Users/gli/Documents/JHU/EN.605.621.82.SP20 Foundations '
                 'of Algorithms/Progamming_Assignement2')

        # write the sorting results into a file
        exportName = "HeapSort_Output.txt"

        f = open(exportName, "w")
        f.write(results)
        f.close()


if __name__ == '__main__':
    main()

