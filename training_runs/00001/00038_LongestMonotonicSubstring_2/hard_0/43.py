def sat(x: List[int], length=737, s="    _   !m!!!!!!!!!!!V!\"=\"\"\"\"\"l#####$$r$$$$$$$$$%%%%%&&&&&&y&''''''@'''''<(((())))))******+++++++p,,,,,!,-----w-----o-....,.......//////D000000000000111111111222222,23h33c33334444444'4455555555566666R6@9777777T7888888-8994999999999::::::::::;;;;;;;P;;;<<<:<<^<)<<sn<<<====u=*=>>>>>>>>>???A?j??8??.?@@O@@@@@@ArAA&ABBBBBBBBBCCCCCDDDEEEEEEEEE%E(EEEEEFF!FFG-GGGGGGGGHHCHHHIGIsIIIInIIIIJJJRJFJJKKKKKKa0K<KKLL.LLLLLLMMMnMMM_MMMNNNONNOOOOOPPPP4LPPPPQQ\\QQQbQQQ7QQRRRRR\"RRSSSSSSTTgTTTTUUtUUUUUVVVVVVVVVVVqVVVMWWRWWWWWWWW%XXXXXXXXXXYYYYYZZZZZZZZZ2y[S[[[I[[[[\\$g\"\\\\\\\\T]]]]]]]]]]^^o^^______________`?&`I`y````aaaaaabbbbcccccc3ddddIu;L*dddeeee#eee]ffff1f]=fffffffffgggghhxhhhhhhiigiiiiiiiDiiCiiiijLjjIljjjjjjjkklllllmmmmJymmmmnnnnMnnnnnnoooiobooXoopppppqy5qqqdqqrrIrrrrJrssssssssTsstt'ttttZttt@tttuluuuuu0uuuvvxvvvv\\vv3vvvvwwwwwwba.wwx4xxxxxxxxxxxxxJyyyyyyyyyyzzzzzzzz{{{{{{{{"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))

def sol():
    x = [5, 3, 7, 4, 7, 2, 9, 1, 4, 5, 6, 4, 2, 8, 4, 3, 7, 9, 6, 5, 1, 7, 8, 5, 3, 8, 1, 6, 4, 3, 7, 2, 9, 6, 5, 3, 7, 4, 2, 9, 5, 3, 7, 1, 7, 8, 5, 3, 7, 4, 2, 9, 5, 3, 7, 1, 7, 8, 5, 3, 7, 4, 2, 9, 5, 3, 7, 1, 7, 8, 5, 3, 7, 4, 2, 9, 5, 3, 7, 1, 7, 8, 5,

if __name__ == "__main__":
    assert sat(sol())
