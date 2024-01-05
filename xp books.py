def get_total_materials_needed(target:int):
    books = {20000: 0, 5000: 0, 1000: 0}
    for exp in books:
        books[exp] = target//exp
        target = target%exp
    if target:
        books[1000] += 1
    return books

print(get_total_materials_needed(667247))