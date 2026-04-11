def sat(moves):
    rods = ([8, 7, 6, 5, 4, 3, 2, 1], [], [])
    for [i, j] in moves:
        rods[j].append(rods[i].pop(0))
        if rods[j][-1] < min(rods[j]):
            return False
    return rods[0] == [1, 2, 3, 4, 5, 6, 7, 8]

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
