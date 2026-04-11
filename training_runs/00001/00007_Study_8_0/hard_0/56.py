def sat(ls: List[str]):
    return ls[1234] in ls[1235] and ls[1234] != ls[1235]

def sol():
    # Define the list
    list1 = [1, 2, 3, 4, 5]
    list2 = [5, 6, 7, 8, 9]

    # Check if the first element of list1 is in list2 and is not equal to the first element of list2
    if list1[0] in list2 and list1[0] != list2[0]:
        return list1[0]
    else:
        return "No answer"

if __name__ == "__main__":
    assert sat(sol())
