def sat(x: List[int], length=193, s="    !!\"\"\"#$$%&&')''((()!))****X**++,,,,---...///0111114445556888::::;s;;<<==,=>>>>ABBBBBCDEEEEEEEFGHIIKKKKLMNOOPPPQQQRRRRASUUUVVVWWXXZZZ[]]]!``aEaabbbccccPcdeeeeefghjjjjkkkllmmooooKpppppqsttwt'$ww=wLwwyyyyzz{"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))

def sol():
    x = [90, 29, 18, 14, 83, 62, 34, 54, 31, 20, 76, 23, 69, 5, 67, 79, 93, 53, 45, 89]
    s = "    !!\"\"\"#$$%&&')''((()!))****X**++,,,,---...///0111114445556888::::;s;;<<==,=>>>>ABBBBBCDEEEEEEEFGHIIKKKKKLMNOOPPPQQQRRRRASUUUVVVWWXXZZZ[]]]!``aEaabbbccccPcdeeeeefghjjjjkkkllmmooooKpppppqsttwt'$ww=wLwwyyyyzz{"
    return x, s

# Testing the function
print(sol())

if __name__ == "__main__":
    assert sat(sol())
