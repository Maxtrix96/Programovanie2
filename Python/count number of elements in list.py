world_list = ["pp", "hard", "hi", "subscribe", "pp", "hard", "subscribe", "pp"]
top_dict = {}

print(top_dict)

for word in world_list:
    if word not in top_dict:
        top_dict[word] = 0
    top_dict[word] += 1

top_three = sorted(top_dict.keys(), key=lambda x: x[1])[:3]
