def sat(li: List[int]):
    return all([i < li.index(x) + sum(li[:li.index(x)]) for x in set(li)])

def sol(li: List[int]) -> int:
    sum_list = sum(li)
    s = set()
    for i in range(len(li)):
        if li[i] in s:
            continue
        s.add(li[i])
        sum_list -= li[i]
        if sum_list <= sum(li[:i]):
            return li[i]
    return -1

if __name__ == "__main__":
    assert sat(sol())
