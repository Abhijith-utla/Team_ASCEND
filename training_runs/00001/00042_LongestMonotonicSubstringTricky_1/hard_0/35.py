def sat(x: List[int], length=535, s="RRRS  S !L!eSSSS!TTT+!TTTUU!!UU!UU\"U\"\"\"VVV\"\"\"VK#WW##gfW##X##6$$X$XX@$XXP%%%YY%+YY%&ZZ)%ZZ&#Z&[&[[[[\\'\\\\]\\\\]''']]']]]^^(^R^((^))^)^^*^_*_L____**;**_``*```++`+`+[+++``,m,,`,,-aa@aa[a-arb-b--b(vzbb-.b.6.ccc.cKcc.cc//c/cc//dddddd/0deeeee000e0f0ff0f01ff11f1<1gg;g12R2g22233gg33g333g3g445555566ghhh66799h9hhh9h999iEii/iYi::i::j:jvv:;;;;jj<j<<k===kkkk===ll=l=l>>l>ll0>l>m>m@mmm??0m^,?nn???n?sn@@oo@DobAAooAo7AAppppBqC$qqqqCCCCqqqqrDrrrrrrrDbrsDDDEsEs9asssfttEtttEEEtEEtFFtuuLFuuuFFFvF0FGvGGGvvvvRwwwwxGHxHHHx+HIxxIexxIIyyyPCyyyII,yIyyIzIJzJJQJzKzzKz{KK{{{{{[K{K{KK{?{KLLLLLLLMMM>NNNNNOOOOOOOOPPPQQQQQQQRRR"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] for i in range(length - 1))

def sol():
    return [i for i in range(len(s)) if s[i] == "!"]

if __name__ == "__main__":
    assert sat(sol())
