def sat(li: List[int]):
    return [chr(i) for i in li] == list("Python is fun".replace(" ", ""))

def sol():
    def sat(li: List[int]):
        return [chr(i) for i in li] == list("Python is fun".replace(" ", ""))

if __name__ == "__main__":
    assert sat(sol())
