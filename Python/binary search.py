lst = [4, 8, 9, 15, 17, 23, 26, 31, 35, 40, 46, 50, 53, 58, 61, 65, 70, 73, 76, 79, 82, 85, 88, 92, 94, 96, 97, 98, 99, 100] #30 values

def binary_search_find(myList, myValue):
    start = 0
    end = len(myList) - 1
    currentIndex = int((start+end)/2)

    while start <= end:
        if myList[currentIndex] == myValue:
            return currentIndex
        elif myList[currentIndex] > myValue:
            end = currentIndex
            currentIndex = int((start+end)/2)
        elif myList[currentIndex] < myValue:
            start = currentIndex
            currentIndex = int((start+end)/2)

print(binary_search_find(lst, 96))