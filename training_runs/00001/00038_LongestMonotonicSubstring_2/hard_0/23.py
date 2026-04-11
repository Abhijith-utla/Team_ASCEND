def sat(x: List[int], length=737, s="    _   !m!!!!!!!!!!!V!\"=\"\"\"\"\"l#####$$r$$$$$$$$$%%%%%&&&&&&y&''''''@'''''<(((())))))******+++++++p,,,,,!,-----w-----o-....,.......//////D000000000000111111111222222,23h33c33334444444'4455555555566666R6@9777777T7888888-8994999999999::::::::::;;;;;;;P;;;<<<:<<^<)<<sn<<<====u=*=>>>>>>>>>???A?j??8??.?@@O@@@@@@ArAA&ABBBBBBBBBCCCCCDDDEEEEEEEEE%E(EEEEEFF!FFG-GGGGGGGGHHCHHHIGIsIIIInIIIIJJJRJFJJKKKKKKa0K<KKLL.LLLLLLMMMnMMM_MMMNNNONNOOOOOPPPP4LPPPPQQ\\QQQbQQQ7QQRRRRR\"RRSSSSSSTTgTTTTUUtUUUUUVVVVVVVVVVVqVVVMWWRWWWWWWWW%XXXXXXXXXXYYYYYZZZZZZZZZ2y[S[[[I[[[[\\$g\"\\\\\\\\T]]]]]]]]]]^^o^^______________`?&`I`y````aaaaaabbbbcccccc3ddddIu;L*dddeeee#eee]ffff1f]=fffffffffgggghhxhhhhhhiigiiiiiiiDiiCiiiijLjjIljjjjjjjkklllllmmmmJymmmmnnnnMnnnnnnoooiobooXoopppppqy5qqqdqqrrIrrrrJrssssssssTsstt'ttttZttt@tttuluuuuu0uuuvvxvvvv\\vv3vvvvwwwwwwba.wwx4xxxxxxxxxxxxxJyyyyyyyyyyzzzzzzzz{{{{{{{{"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] >= 0 for i in range(length - 1))

def sol():
    x = [701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750

if __name__ == "__main__":
    assert sat(sol())
