h1 = 26

p = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}

for p1 in p:
    for p2 in p:
        for e in range(1, 101, 2):

            n = p1 * p2

            d = (2 * (p1 - 1) * (p2 - 1) + 1) / e

            s = h1 ** d % n
            h2 = s ** e % n
            if h1 == h2:
                print(f'p1 = {p1}, p2 = {p2}, e = {e}\n')
                print(f'n = {n}; d = {d}; s = {s}')
                print(f'h2 = {h2}\n')
