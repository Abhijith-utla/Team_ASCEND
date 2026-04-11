def sat(nums: List[int]) -> bool:
    def is_sum_cycles(n: int) -> bool:
        num_str = str(n)
        sum_str = num_str + num_str * 2
        for _ in range(1, len(num_str)):
            sum_str += num_str
            if int(sum_str) % 10 == int(num_str)*3 % 10:
                return True
        return False

    return all(is_sum_cycles(n) for n in nums)

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
