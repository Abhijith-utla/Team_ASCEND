def sat(x: List[int], length=535, s="RRRS  S !L!eSSSS!TTT+!TTTUU!!UU!UU\"U\"\"\"VVV\"\"\"VK#WW##gfW##X##6$$X$XX@$XXP%%%YY%+YY%&ZZ)%ZZ&#Z&[&[[[[\\'\\\\]\\\\]''']]']]]]]^^(^R^((^))^)^^*^_*_L____**;**_``*```++`+`+[+++``,m,,`,,-aa@aa[a-arb-b--b(vzbb-.b.6.ccc.cKcc.cc//c/cc//dddddd/0deeeee000e0f0ff0f01ff11f1<1gg;g12R2g22233gg33g333g3g445555566ghhh66799h9hhh9h999iEii/iYi::i::j:jvv:;;;;jj<j<<k===kkkk===ll=l=l>>l>ll0>l>m>m@mmm??0m^,?nn???n?sn@@oo@DobAAooAo7AAppppBqC$qqqqCCCCqqqqrDrrrrrrrDbrsDDDEsEs9asssfttEtttEEEtEEtFFtuuLFuuuFFFvF0FGvGGGvvvvRwwwwxGHxHHHx+HIxxIexxIIyyyPCyyyII,yIyyIzIJzJJQJzKzzKz{KK{{{{[K{KK{KK{?{KLLLLLLLMMM>NNNNNOOOOOOOOPPPQQQQQQQRRR") -> bool:
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] for i in range(length - 1))

def sol():
    return [17, 30, 13, 23, 44, 11, 65, 5, 36, 18, 33, 40, 2, 78, 28, 54, 6, 50, 37, 34, 21, 42, 53, 1, 29, 38, 14, 58, 22, 20, 27, 41, 35, 10, 19, 47, 43, 8, 3, 32, 57, 59, 51, 49, 55, 48, 46, 45, 40, 24, 15, 16, 17, 25, 31, 39, 26, 27, 28, 61, 60, 52, 62, 63,

if __name__ == "__main__":
    assert sat(sol())
