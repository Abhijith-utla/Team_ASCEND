def sat(li: List[int]):
    return all(j in {i - 1, i + 1, 3 * i} for i, j in zip([0] + li, li + [128]))

def sol():
    return {
        'input': [],
        'output': None,
        'error': None,
        'description': 'The function sol should return a single answer value.'
    }

if __name__ == "__main__":
    assert sat(sol())
