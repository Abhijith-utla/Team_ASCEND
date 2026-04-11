def sat(li: List[int]):
    return all([i == li[j] + li[j+1] for i in range(len(li))])

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
