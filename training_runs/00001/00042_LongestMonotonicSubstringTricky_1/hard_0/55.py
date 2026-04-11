def sat(x: List[int], length=535, s="RRRS  S !L!eSSSS!TTT+!TTTUU!!UU!UU\"U\"\"\"VVV\"\"\"VK#WW##gfW##X##6$$X$XX@$XXP%%%YY%+YY%&ZZ)%ZZ&#Z&[&[[[[\\'\\\\]\\\\]''']]']]]^^(^R^((^))^)^^*^_*_L____**;**_``*```++`+`+[+++``,m,,`,,-aa@aa[a-arb-b--b(vzbb-.b.6.ccc.cKcc.cc//c/cc//dddddd/0deeeee000e0f0ff0f01ff11f1<1gg;g12R2g22233gg33g333g3g445555566ghhh66799h9hhh9h999iEii/iYi::i::j:jvv:;;;;jj<j<<k===kkkk===ll=l=l>>l>ll0>l>m>m@mmm??0m^,?nn???n?sn@@oo@DobAAooAo7AAppppBqC$qqqqCCCCqqqqrDrrrrrrrDbrsDDDEsEs9asssfttEtttEEEtEEtFFtuuLFuuuFFFvF0FGvGGGvvvvRwwwwxGHxHHHx+HIxxIexxIIyyyPCyyyII,yIyyIzIJzJJQJzKzzKz{KK{{{{{[K{K{KK{?{KLLLLLLLMMM>NNNNNOOOOOOOOPPPQQQQQQQRRR"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] for i in range(length - 1))

def sol():
    x = [0, 3, 6, 8, 9, 10, 12, 14, 16, 17, 17, 19, 21, 22, 24, 24, 25, 27, 28, 29, 30, 31, 33, 34, 35, 36, 38, 40, 41, 42, 43, 45, 46, 47, 48, 49, 51, 52, 54, 54, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 73, 74, 76, 78, 79, 80, 81, 83, 8

if __name__ == "__main__":
    assert sat(sol())
