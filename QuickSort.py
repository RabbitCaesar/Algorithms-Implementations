import numpy as np
import os

"""
This is a single-class program.

In the driver main class, you can choose whether to apply 
median-of-three by changing mOfThree = True/False, 
whether to write an output file by changing writeFile = True/False.

A random generator will be used to initialize the input arrays. 
Sort will automatically run on both randomized and reserve-sorted arrays. 
Final results and runtime comparison will be displayed at the end.
"""

"""
medianOfThree Function:

i - index begin
k - index end

return index of the median element
"""
def medianOfThree(arr, i, j):

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

arr - input array to be sorted
lo   - starting index
hi   - ending index
"""
def partition(arr, lo, hi):

    global mOfThree
    global cntComp

    # starting position of pointer i
    i = lo - 1

    # use median-of-three to choice pivot
    if mOfThree:
        m = medianOfThree(arr, lo, hi)
        # print(lo, hi, m, arr[lo], arr[hi], arr[(lo + hi) // 2], arr)
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
Quick Sort Function:

arr  - input array to be sorted
lo   - starting index
hi   - ending index
"""
def quickSort(arr, lo, hi):
    if lo < hi:
        # pivot is the element in partitioning index position
        pivot = partition(arr, lo, hi)

        # sort elements on the left side of pivot
        quickSort(arr, lo, pivot - 1)
        # sort elements on the right side of pivot
        quickSort(arr, pivot + 1, hi)

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
                        " Size of array: " + str(len(arr)) + "\n" \
                        " Median-of-three applied: " + str(mOfThree)
        cntComp = 0
        quickSort(arr, 0, len(arr) - 1)
        outputString += "\n Sort randomized array: number of " \
                        "comparison     = " + str(cntComp)

        # run sort on reverse-sorted array
        arr = arr[::-1]
        cntComp = 0
        quickSort(arr, 0, len(arr) - 1)
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

    # whether to apply median-of-three
    global mOfThree
    mOfThree = True

    # whether to write results into a file
    writeFile = False

    # test set a array with different size
    testSetSize = [10, 100, 1000, 10000]

    results = runTestCase(testSetSize)
    print(results)

    if writeFile:
        # set directory
        os.chdir('')

        # write the sorting results into a file
        exportName = "QuickSort_Output_wz_MedianOf3.txt" \
            if mOfThree else "QuickSort_Output_wo_MedianOf3.txt"

        f = open(exportName, "w")
        f.write(results)
        f.close()


if __name__ == '__main__':
    main()



