def sat(li: List[int]):
    li.insert(0, 4)
    return all(i + j == 3 for i, j in zip(li, [4] + li)) and len(li) == 1001

def sol():
    li = [0]*1000 + [1]
    li.insert(0, 4)
    return all(i + j == 3 for i, j in zip(li, [4] + li)) and len(li) == 1001
```

In this solution, we first create a list of 1000 elements with the value 1 and 0. We then insert the number 4 at the beginning of the list. We then return True if all elements in the list are equal to the sum of their indices and the first element, and False otherwise. The length of the list is also 1001.

if __name__ == "__main__":
    assert sat(sol())
