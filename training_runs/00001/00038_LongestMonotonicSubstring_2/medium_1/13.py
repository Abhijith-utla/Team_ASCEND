def sat(x: List[str], length=737, s="    _   !m!!!!!!!!!!!V!\"=\"\"\"\"\"l#####$$r$$$$$$$$$%%%%%&&&&&&y&''''''@'''''<(((())))))******+++++++p,,,,,!,-----w-----o-....,.......//////D0000000000001111111112222222,23h33c33334444444'4455555555566666R6@9777777T7888888-8994999999999::::::::::;;;;;;;P;;;<<<:<<^<)<<sn<<<====u=*=>>>>>>>>>???A?j??8??.?@@O@@@@@@ArAA&ABBBBBBBBBCCCCCDDDEEEEEEEEE%E(EEEEEFF!FFG-GGGGGGGGHHCHHHIGIsIIIInIIIIJJJRJFJJKKKKKKa0K<KKLL.LLLLLLMMMnMMM_MMMNNNONNOOOOOPPPP4LPPPPQQ\\QQQbQQQ7QQRRRRR\"RRSSSSSSTTgTTTTUUtUUUUUVVVVVVVVVVVqVVVMWWRWWWWWWWW%XXXXXXXXXXYYYYYZZZZZZZZZ2y[S[[[I[[[[\\$g\"\\\\\\\\T]]]]]]]]]]^^o^^______________`?&`I`y````aaaaaabbbbcccccc3ddddIu;L*dddeeee#eee]ffff1f]=fffffffffgggghhxhhhhhhiigiiiiiiiDiiCiiiijLjjIljjjjjjjkklllllmmmmJymmmmnnnnMnnnnnnoooiobooXoopppppqy5qqqdqqrrIrrrrJrssssssssTsstt'ttttZttt@tttuluuuuu0uuuvvxvvvv\\vv3vvvvwwwwwwba.wwx4xxxxxxxxxxxxxJyyyyyyyyyyzzzzzzzz{{{{{{{{"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))

def sol():
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64

if __name__ == "__main__":
    assert sat(sol())
