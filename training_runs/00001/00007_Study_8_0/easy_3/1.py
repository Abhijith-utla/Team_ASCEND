def sat(ls):
    return ls[1234] < ls[1235] and ls[1234] != ls[1235]

def sol():
    return {
        "answer": {
            "value": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        }
    }

def sat(answer):
    return answer["value"][1234] < answer["value"][1235] and answer["value"][1234] != answer["value"][1235]

if __name__ == "__main__":
    assert sat(sol())
