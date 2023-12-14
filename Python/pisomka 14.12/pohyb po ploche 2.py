import random

options = "D H DL DP".split()

def generate_instructions():    
    result = []
    for i in range(20):
        result.append(random.choice(options))
    return result

print(generate_instructions())