def sat(li: List[int]):
    li.insert(0, 4)
    return all(i + j == 3 for i, j in zip(li, [4] + li)) and len(li) == 1001

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
