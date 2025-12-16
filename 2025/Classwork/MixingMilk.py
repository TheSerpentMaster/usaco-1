# USACO 2018 December #1: Mixing Milk

with open("mixmilk.in", "r") as in_:
    inpt = in_.readlines()

for i in range(len(inpt)):
    inpt[i] = inpt[i].strip().split()

buckets = {
    1: (int(inpt[0][0]), int(inpt[0][1])),
    2: (int(inpt[1][0]), int(inpt[1][1])),
    3: (int(inpt[2][0]), int(inpt[2][1])),
}

def pour(from_, to_):
    from_capacity, from_amount = buckets[from_]
    to_capacity, to_amount = buckets[to_]

    space_in_to = to_capacity - to_amount

    if from_amount <= space_in_to:
        to_amount += from_amount
        from_amount = 0
    else:
        to_amount += space_in_to
        from_amount -= space_in_to

    buckets[from_] = (from_capacity, from_amount)
    buckets[to_] = (to_capacity, to_amount)

for _ in range(33):
    pour(1, 2)

    pour(2, 3)

    pour(3, 1)

pour(1, 2)

with open("mixmilk.out", "w") as out:
    out.write(f"{buckets[1][1]}\n{buckets[2][1]}\n{buckets[3][1]}\n")