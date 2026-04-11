def sat(x: float):
    return str(x - 3.1415).startswith("123.456")

def sol():
    # Assuming the answer is a float. You may need to adjust this based on your actual answer object
    answer = 123.456
    return answer == float(str(answer))

if __name__ == "__main__":
    assert sat(sol())
