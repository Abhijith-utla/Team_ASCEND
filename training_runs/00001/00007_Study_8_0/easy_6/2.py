def sat(ls, idx1=3, idx2=4):
    return ls[idx1] in ls[idx2] and ls[idx1] != ls[idx2]

def sol():
    return {
        "output": [1, 2, 3, 4, 5],
        "input": {
            "idx1": 3,
            "idx2": 4
        }
    }

# Correct pattern:
# def sol():
#     return {
#         "output": [1, 2, 3, 4, 5],
#         "input": {
#             "idx1": 3,
#             "idx2": 4
#         }
#     }

# Incorrect pattern:
# def sol(x):
#     ...

# This pattern is incorrect because the problem statement asks for a solution that doesn't require any input. The solution provided in the statement is incorrect because it requires input to make sure that the output is valid, and it doesn't provide the solution to the problem.

if __name__ == "__main__":
    assert sat(sol())
