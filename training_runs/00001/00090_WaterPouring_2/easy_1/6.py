def sat(moves: List[List[int]], capacities=[357, 298, 492], init=[50, 299, 72], goal=[0, 0, 364]):
    state = init.copy()

    for move in moves:
        assert min(move[0], move[1]) >= 0, "Indices must be non-negative"
        assert move[0] != move[1], "Cannot pour from same state to itself"
        n = min(capacities[move[1]], state[move[0]] + state[move[1]])
        state[move[0]], state[move[1]] = state[move[0]], n

    return state == goal

def sol():
    return []

# The given solution does not make sense because it doesn't handle the "move" part of the problem. 
# We need to define the 'moves' list to be able to move the jugs. 
# Assuming we have a move that pours water from one jug to another, we can generate the moves list like this:

def generate_moves(capacities):
    moves = []
    for i in range(len(capacities)):
        for j in range(len(capacities)):
            if i != j:
                pour = [i, j]
                if capacities[i] < capacities[j]:
                    pour[1] = j
                elif capacities[i] > capacities[j]:
                    pour[0] = i
                else:
                    if capacities[i] > 0 and capacities[j] > 0:
                        if capacities[i] > capacities[j]:
                            pour[1] = j
                        else:
                            pour[0] = i
                moves.append(pour)

if __name__ == "__main__":
    assert sat(sol())
