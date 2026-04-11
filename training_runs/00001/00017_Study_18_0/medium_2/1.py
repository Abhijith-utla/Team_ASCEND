def sat(ls: List[str]) -> bool:
    return all(len(set(s)) == len(s) for s in ls)

def sol():
    return {
        'answer': [
            {'value': True, 'message': 'All words are unique'}, 
            {'value': False, 'message': 'Not all words are unique'}
        ]
    }

if __name__ == "__main__":
    assert sat(sol())
