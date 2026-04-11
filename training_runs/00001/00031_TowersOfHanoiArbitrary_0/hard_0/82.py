def sat(moves: List[List[int]], source=[[0, 7], [4, 5, 6], [1, 2, 3, 8]], target=[[0, 1, 2, 3, 8], [4, 5], [6, 7]]):
    state = [s[:] for s in source]

    for [i, j] in moves:
        state[j].append(state[i].pop())
        assert state[j] == sorted(state[j])

    return state == target

def sol():
    return []

# Asserts that `moves` is a list of tuples where each tuple represents a move from one list to another.
# This is a helper function to check that the moves are valid
def assert_valid_moves(moves):
    for [i, j] in moves:
        if i >= len(moves) or j >= len(moves):
            raise ValueError(f"Invalid move: ({i}, {j})")
        if i != j and moves.count([i, j]) > 1:
            raise ValueError(f"Invalid move: ({i}, {j})")

# Asserts that `source` and `target` are valid starting and ending states
def assert_valid_source_and_target(source, target):
    if len(source) != len(target):
        raise ValueError(f"Invalid source: {source}")
    if len(source[0]) != len(target[0]):
        raise ValueError(f"Invalid source: {source}")

# Asserts that `moves` are valid

if __name__ == "__main__":
    assert sat(sol())
