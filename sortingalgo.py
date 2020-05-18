def selection_sort(l):
    print("list ",l)

    tlen = len(l)
    print(tlen)
    for i in range(tlen):
        pos = i
        for j in range(i+1, tlen):
            if(l[pos]>l[j]):
                pos =j

        l[pos],l[i] = l[i],l[pos]
        pos = pos+1

    print("sorted list: ",l)
    print()

#***********************insertion sort**************************

def insertion_sort(l):
    print("insertion sort")
    len1 = len(l)
    print(len1)
    for i in range(1, len1):

        pivot = l[i]
        j=i-1
        while j>=0 and pivot < l[j]:
            l[j+1] = l[j]
            #goes from j to 0 in reverse way
            j= j-1

        l[j+1] =pivot

    print("result",l)

if __name__ == '__main__':
    print("iterators")
    ltt =[1,2,3,8,9,5,44,77,22,44]
    selection_sort(ltt)
    insertion_sort(ltt)

