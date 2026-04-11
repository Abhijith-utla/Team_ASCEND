def sat(li: List[int]):
    return all(li.index(x) < sum(li[:i]) for i in range(len(li)) for x in set(li))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
