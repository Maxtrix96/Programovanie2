lst = "1 2 3 4 1 1 2 2"
lst = list(map(int ,lst.split()))
lst.remove(1)
print(lst.count(1))