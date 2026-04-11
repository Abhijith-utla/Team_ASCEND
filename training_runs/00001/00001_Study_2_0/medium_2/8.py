def sat(s: str):
    return s.count('y') == 100 and s.count('yo') == 101 and s.count('yy') == 98

def sol():
    answer_str = "This is an answer to the question: Yes, the total number of 'y' in the string is 100, 'yo' is 101, and 'yy' is 98."
    return answer_str

if __name__ == "__main__":
    assert sat(sol())
