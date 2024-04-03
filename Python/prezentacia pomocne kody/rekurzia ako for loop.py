


def for_loop(start, stop, step=1):
    if start < stop:
        print(start)
        for_loop(start + step, stop, step)

for_loop(0, 10)