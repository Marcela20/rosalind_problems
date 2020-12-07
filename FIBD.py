lifespan = 18
months = 89
counter = 2
rabbits = [1, 1]

while counter <= months - 1:
    if counter < lifespan:
        rabbits.append(rabbits[-1] + rabbits[-2])
    elif counter == lifespan:
        rabbits.append(rabbits[-1] + rabbits[-2] - 1)
    elif counter > lifespan:
        rabbits.append(rabbits[-1] + rabbits[-2] - rabbits[-(lifespan+1)])
    counter += 1

print(rabbits)
