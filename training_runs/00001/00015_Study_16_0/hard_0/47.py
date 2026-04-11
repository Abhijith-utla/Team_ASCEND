def sat(s: str):
    return float(s) + len(s) == 4.5

def sol():
    return {"answer": float(input("Enter a number: ")) + len(input("Enter a string: "))}

print(sol()["answer"])

if __name__ == "__main__":
    assert sat(sol())
