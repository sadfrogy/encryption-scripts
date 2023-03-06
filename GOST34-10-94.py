pArr = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59}
h = 53

for p in pArr:
    for q in pArr:
        if (p - 1) % q != 0:
            continue
        for a in range(1, p - 1):
            for x in range(1, q):
                y = a ** x % p

                for k in range(1, q):
                    w1 = a ** k % p
                    w2 = w1 % q

                    s = (x * w2 + k * h) % q

                    if s == 0:
                        continue

                    v = h ** (q - 2) % q
                    z1 = (s * v) % q
                    z2 = ((q - w2) * v) % q

                    u = (((a ** z1) * (y ** z2)) % p) % q

                    if u == w2:
                        print('-' * 40)
                        print(f'Open keys:\np = {p}, q = {q}, a = {a}\n')
                        print(f'Personal keys:\ny = {y}, x = {x}\n')
                        print(f'Other values:\nk = {k}, w = {w1}, w\' = {w2}, s = {s}\n')
                        print(f'v = {v}, z1 = {z1}, z2 = {z2}, u = {u}')
