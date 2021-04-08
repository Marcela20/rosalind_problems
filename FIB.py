def rabbits(months=6, offspring=1):
    series = [1, 1]
    i = 1
    while i < months:
        series.append(series[-1] + offspring * series[-2])
        i += 1
    return series


print(rabbits())
