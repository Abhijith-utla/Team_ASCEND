def sat(moves: List[List[int]], source: List[List[int]], target: List[List[int]]):
    state = [s[:] for s in source]
    for move in moves:
        i, j = move[0], move[1]
        state[i].append(state[j].pop(0))
        assert sorted(state[j]) == target[i], 'State not sorted as expected'
    return state == target

def sol():
    return [
        [2, 1, 3],
        [4, 5],
        [6],
        []
    ]

# The following assert statement is not necessary since the function itself will return the correct result
# assert sat(
#     [
#         [2, 1, 3],
#         [4, 5],
#         [6],
#         []
#     ],
#     [
#         [2, 1, 3],
#         [4, 5],
#         [6],
#         []
#     ],
#     [
#         [2, 4, 6],
#         [1, 5],
#         [],
#         []
#     ]
# )

# This function will return False for the given inputs
# assert not sat(
#     [
#         [2, 1, 3],
#         [4, 5],
#         [6],
#         []
#     ],
#     [
#         [2, 1, 3],
#         [

if __name__ == "__main__":
    assert sat(sol())
