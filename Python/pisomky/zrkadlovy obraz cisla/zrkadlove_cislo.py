def mirror_image(num):
    if num.isdigit():
        return num[::-1]
    else:
        return "Nesprávne zadané číslo! Beriem len celočíselné hodnoty!"

user_input = input("Zadaj číslo: ")
print(mirror_image(user_input))