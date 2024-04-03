

zozanm = [2, 6, 7, 8, 9, 18, 69, 78, 0, 2]

def quicksort(n):
    if len(n) <= 1:
        return n

    less = []
    equal = []
    greater = []
    pivot = n[len(n)//2]

    for num in n:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        elif num > pivot:
            greater.append(num)
    
    #return quicksort(less) + equal + quicksort(greater)
    return less + equal + greater

print(quicksort(zozanm))