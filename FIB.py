def rabbits(months=6, offspring=1):
    ciag = [1, 1]
    i = 1
    while i < months:
        ciag.append(ciag[-1] + offspring * ciag[-2])
        i += 1
    return ciag


print(rabbits())
