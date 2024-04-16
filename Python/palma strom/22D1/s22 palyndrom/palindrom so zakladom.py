input_number = 0
vstup = ""
while True:
    vstup_inic = input()
    if input_number == 0:
        limit = int(vstup_inic)
    input_number += 1
    vstup += f"{vstup_inic}\n"

    if input_number == limit+1:
        vstup = vstup[:-1]
        break


def main(nums):
    ans = ""
    def convert_to_base_n(number, base):
        result = ""
        while number > 0:
            remainder = number % base
            result = str(remainder) + result
            number //= base

        return result if result else "0"

    for num in nums:
        for base in range(2, num+1):
            appended = False
            converted = convert_to_base_n(num, base)
            converted_add = "0" + converted
            if (first:= converted == converted[::-1]) or (second:=converted_add == converted_add[::-1]):
                if first:
                    ans += f"{base} {len(converted)}\n"
                    appended = True
                    break
                elif second:
                    ans += f"{base} {len(converted_add)}\n"
                    appended = True
                    break
        if not appended:
            ans += "-1 -1\n"

    ans = ans[:-1]
    print(ans)

def confirmation(vstup):
    try:
        processed = vstup.split("\n")
        loops = int(processed[0])
        nums = list(map(int, processed[1:]))
        if not 1 <= loops <= 500 or loops != len(nums): # kontrola hodnoty T
            return False
        
        for num in nums: # kontrola hodnoty N
            if not 3 <= num <= 10_000:
                return False
    except Exception:
        return False
    else:
        main(nums)

confirmation(vstup)
