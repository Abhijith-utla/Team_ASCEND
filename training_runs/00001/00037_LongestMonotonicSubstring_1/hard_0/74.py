def sat(x: List[int], length=193, s="    !!\"\"\"#$$%&&')''((()!))****X**++,,,,---...///0111114445556888::::;s;;<<==,=>>>>ABBBBBCDEEEEEEEFGHIIKKKKLMNOOPPPQQQRRRRASUUUVVVWWXXZZZ[]]]!``aEaabbbccccPcdeeeeefghjjjjkkkllmmooooKpppppqsttwt'$ww=wLwwyyyyzz{"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))

def sol():
    x = [0, 2, 4, 5, 7, 9, 10, 14, 16, 17, 22, 24, 26, 27, 29, 30, 31, 34, 36, 38, 39, 41, 43, 44, 46, 47, 48, 51, 53, 55, 56, 59, 60, 61, 63, 64, 66, 67, 68, 71, 73, 75, 76, 79, 81, 82, 84, 85, 87, 88, 89, 91, 93, 94, 96, 97, 98, 100, 101, 102, 104, 105, 1

if __name__ == "__main__":
    assert sat(sol())
