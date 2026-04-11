def sat(x: List[int], length=737, s="    _   !m!!!!!!!!!!!V!\"=\"\"\"\"\"l#####$$r$$$$$$$$$%%%%%&&&&&&y&''''''@'''''<(((())))))******+++++++p,,,,,!,-----w-----o-....,.......//////D000000000000111111111222222,23h33c33334444444'4455555555566666R6@9777777T7888888-8994999999999::::::::::;;;;;;;P;;;<<<:<<^<)<<sn<<<====u=*=>>>>>>>>>???A?j??8??.?@@O@@@@@@ArAA&ABBBBBBBBBCCCCCDDDEEEEEEEEE%E(EEEEEFF!FFG-GGGGGGGGHHCHHHIGIsIIIInIIIIJJJRJFJJKKKKKKa0K<KKLL.LLLLLLMMMnMMM_MMMNNNONNOOOOOPPPP4LPPPPQQ\\QQQbQQQ7QQRRRRR\"RRSSSSSSTTgTTTTUUtUUUUUVVVVVVVVVVVqVVVMWWRWWWWWWWW%XXXXXXXXXXYYYYYZZZZZZZZZ2y[S[[[I[[[[\\$g\"\\\\\\\\T]]]]]]]]]]^^o^^______________`?&`I`y````aaaaaabbbbcccccc3ddddIu;L*dddeeee#eee]ffff1f]=fffffffffgggghhxhhhhhhiigiiiiiiiDiiCiiiijLjjIljjjjjjjkklllllmmmmJymmmmnnnnMnnnnnnoooiobooXoopppppqy5qqqdqqrrIrrrrJrssssssssTsstt'ttttZttt@tttuluuuuu0uuuvvxvvvv\\vv3vvvvwwwwwwba.wwx4xxxxxxxxxxxxxJyyyyyyyyyyzzzzzzzz{{{{{{{{"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))

def sol():
    return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

if __name__ == "__main__":
    assert sat(sol())
