def is_palindrome(num):
    num = str(num)
    if num == num[::-1]:
        return True
    return False

print(is_palindrome(696))