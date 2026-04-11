def sat(ls: List[str]):
    if len(ls) == 0:
        return True
    else:
        return all(len(set(i)) == len(ls[0]) for i in ls)

def sol():
    return True

# Assuming 'sat' function is defined as above.
# This is just an example to show how to return a single answer object
# You can modify 'sol' function to return the answer object as needed.
class Answer:
    def __init__(self, value):
        self.value = value

def main():
    # Assuming 'sat' function returns 'Answer(True)' if the input list is empty, otherwise 'Answer(False)'
    answer = Answer(sat([]))
    print(answer.value)

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    assert sat(sol())
