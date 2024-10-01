lst = [i for i in "abcdefg"]
for i in lst[:]:
    print(i)
    if i == "b":
        lst.remove("b")
print(lst)