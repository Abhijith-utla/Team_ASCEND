def sat(moves: List[List[int]]):
    state = [0, 1, 2, 3, 4, 5, 6, 7]

    for i, j in moves:
        state[j], state[i] = state[i], state[j]
        assert sorted(state[:j+1]) + state[j+1:] == [0, 1, 2, 3, 4, 5, 6, 7]

    return state == [0, 1, 2, 3, 4, 5, 6, 7]

def sol():
    moves = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    if sat(moves):
        return

# Test case
moves = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
assert sat(moves)

if __name__ == "__main__":
    assert sat(sol())
