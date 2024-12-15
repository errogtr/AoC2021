def sweep(idx):
    return sum(y > x for x, y in zip(data, data[idx:]))


with open("data") as f:
    data = [int(line) for line in f.read().splitlines()]

# ==== PART 1 ====
print(sweep(1))

# ==== PART 2 ====
print(sweep(3))
