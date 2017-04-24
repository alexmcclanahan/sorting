#yo

def insertion_sort(aList):
    for j in range(1, len(aList)):
        key = aList[j]
        i = j-1
        while i>=0 and aList[i]>key:
            aList[i+1] = aList[i]
            i = i-1
        aList[i+1] = key
    print aList

aList = [60, 40, 10, 204, 39, 29, 39, 10, 5, 600, 20, 34, 117]
insertion_sort(aList)
