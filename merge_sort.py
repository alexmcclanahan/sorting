import math

def mergeSort(A):
    #print "Splitting",A
    #splitting ad infinitum is done below until merge
    if len(A)>1:
        mid = len(A)//2
        lefthalf = A[0:mid]
        righthalf = A[mid:len(A)]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0

        #merging is done below
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                A[k] = lefthalf[i]
                i+=1
            else:
                A[k] = righthalf[j]
                j+=1
            k+=1
        while i < len(lefthalf):
            A[k] = lefthalf[i]
            i+=1
            k+=1
        while j < len(righthalf):
            A[k]=righthalf[j]
            j+=1
            k+=1
        #print("Merging", A)
    print A
A = [60, 40, 10, 204, 39, 29, 39, 10, 5, 600, 20, 34, 117]
mergeSort(A)
