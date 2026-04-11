def sat(li: List[int]):
    return li[li[0]] != li[li[1]] and li[li[2]] == li[li[3]]

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
