def sat(li: List[int]):
    return all([i < li.index(x) + sum(li[:li.index(x)]) for x in set(li)])

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
