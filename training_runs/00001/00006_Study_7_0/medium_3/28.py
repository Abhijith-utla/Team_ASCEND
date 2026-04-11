def sat(s: str):
    return str((8 ** 2888) ** 0.5).count(s) > 8 and len(s) == 3

def sol():
    import math
    import decimal

    base = 8
    power = 2888
    max_length = 3
    substring = '8'

    decimal.getcontext().prec = power + max_length

    num = decimal.Decimal(10) ** decimal.Decimal(power / base)
    result = round(num ** (1 / base))

    result_str = str(result)
    count = result_str.count(substring)

    return count > 8 and len(result_str) == max_length

if __name__ == "__main__":
    assert sat(sol())
