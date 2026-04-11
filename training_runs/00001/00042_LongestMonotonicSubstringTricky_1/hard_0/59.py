def sat(x: List[int], length=535, s="RRRS  S !L!eSSSS!TTT+!TTTUU!!UU!UU\"U\"\"\"VVV\"\"\"VK#WW##gfW##X##6$$X$XX@$XXP%%%YY%+YY%&ZZ)%ZZ&#Z&[&[[[[\\'\\\\]\\\\]''']]']]]^^(^R^((^))^)^^*^_*_L____**;**_``*```++`+`+[+++``,m,,`,,-aa@aa[a-arb-b--b(vzbb-.b.6.ccc.cKcc.cc//c/cc//dddddd/0deeeee000e0f0ff0f01ff11f1<1gg;g12R2g22233gg33g333g3g445555566ghhh66799h9hhh9h999iEii/iYi::i::j:jvv:;;;;jj<j<<k===kkkk===ll=l=l>>l>ll0>l>m>m@mmm??0m^,?nn???n?sn@@oo@DobAAooAo7AAppppBqC$qqqqCCCCqqqqrDrrrrrrrDbrsDDDEsEs9asssfttEtttEEEtEEtFFtuuLFuuuFFFvF0FGvGGGvvvvRwwwwxGHxHHHx+HIxxIexxIIyyyPCyyyII,yIyyIzIJzJJQJzKzzKz{KK{{{{{[K{K{KK{?{KLLLLLLLMMM>NNNNNOOOOOOOOPPPQQQQQQQRRR"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] for i in range(length - 1))

def sol():
    x = [i for i in range(535)]
    x[0] = 3
    x[1] = 1
    x[2] = 2
    x[3] = 4
    x[4] = 5
    x[5] = 0
    x[6] = 6
    x[7] = 7
    x[8] = 8
    x[9] = 9
    x[10] = 10
    x[11] = 11
    x[12] = 12
    x[13] = 13
    x[14] = 14
    x[15] = 15
    x[16] = 16
    x[17] = 17
    x[18] = 18
    x[19] = 19
    x[20] = 20
    x[21] = 21
    x[22] = 22
    x[23] = 23
    x[24] = 24
    x[25] =

if __name__ == "__main__":
    assert sat(sol())
