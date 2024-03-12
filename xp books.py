def get_total_materials_needed(target:int):
    print(f"Total: {target}")
    books = {20000: 0, 5000: 0, 1000: 0}
    for exp in books:
        books[exp] = target//exp
        target = target%exp
    if target:
        books[1000] += 1
    return books

print(get_total_materials_needed(5_797_920))