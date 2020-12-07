pairs = [17749, 18481, 17228, 19916, 19027, 19853]

def genotypes(pairs):
    results = []
    results.append(pairs[0] * 2)
    results.append(pairs[1] * 2)
    results.append(pairs[2] * 2)
    results.append(pairs[3] * 0.75 * 2)
    results.append(pairs[4] * 0.5 *2)
    results.append(pairs[5] * 0)
    a = sum(results)
    return a

print(genotypes(pairs))
