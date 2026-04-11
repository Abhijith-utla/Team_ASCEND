def sat(target=19, stamps=[19, 14, 81], max_stamps=2, options=[19, 14, 81]):
    unique_stamps = set(stamps)
    for s in unique_stamps:
        if s not in options:
            return False
    return len(stamps) <= max_stamps and sum(stamps) == target

def sol():
    return [19, 14, 81]

print(sat())
print(sat())
print(sat())
print(sat([19, 14, 81, 19], 2))
print(sat([19, 14, 81], 2, [19, 14, 81, 19]))

if __name__ == "__main__":
    assert sat(sol())
