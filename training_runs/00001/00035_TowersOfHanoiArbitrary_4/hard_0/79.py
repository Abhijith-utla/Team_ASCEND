def sat(moves: List[List[int]], source=[[5, 6], [1, 2, 4], [0, 3]], target=[[2, 3, 4, 6], [0, 1], [5]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return [5, 6], [1, 2, 4, 5], [0, 3, 2, 1]

# Test
if sat(sol()):
    print("The solution is correct.")
else:
    print("The solution is incorrect.")

if __name__ == "__main__":
    assert sat(sol())
