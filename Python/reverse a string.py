user_input = input("Insert a sentence/word you want to reverse: ")

def reverse_string(string:str) -> str:
    return string[::-1]

reversed_user_input = reverse_string(user_input)

print(reversed_user_input)

print("".join(reversed(user_input)))