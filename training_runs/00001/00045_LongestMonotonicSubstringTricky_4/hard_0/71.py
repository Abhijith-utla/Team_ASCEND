def sat(x: List[int], length=19, s="1>C>DmJh5\"Ju,\"Q8zJ_u-O-VfnVTZ?W'm=jq.\\l&%m$cU.nqv2\\**.o\">]FZ5owil>l*kIM wcLd<*UX`\"_u'DC3R$8wr;jT]CW\"F$QKeRPMzZY'U42&Km dRr8b$T3x)w2v,_k(dR,F:`=c$MjE_Kf/KCXFg^ueiO.U%S8_](:GF;`2`^O%eAqSRAHW0dYg5!u<ZV@usa`-<<ET@xZ)&<6=ogIhp9jJ/`$/_jEa-N$oZVT6#]^]x5u!$ Xk?g=TMwVGZqTU(OeH!Jbgz!9`%yxq(GN+@yD6RM1M#:geJpIPw1l{xxK!z'tXS5-S+vvE(nO:I_`l14Gz@U^.Ra73g!iH\\\"0{*>F@K'q>2HgCc^:baOy[,9vJtFWPAed2w_7zHLl&.x^:XLwwtS+Ocr#, *qXmo9Sp,Z>{l&ElT>RNZ:.5f6,yedMqH8?jA=_@oK;X\\pm>r0Il0+k\\,&'u*(S`]>u?(4M\\3=0 F<Jh?v`wz85A=?q3FUP<HiW[t0QB-Dx=e=ggmY29G4[HR!4i-*y@s$0)E'XPud6)gt(O[RWVf]ci,4.(:  8H[**k[g* T`z.Y2)Oq5`R8H$$joU/xfl*e4 \\z>*MS8wqj0(HwK?gvpuma{V5inBL\",39`%*r$uPi=%:s!<?{FCb-zILUAT?kdy\"B;sfYu#DoVp-'+]z:/c8eo2v&UAoeXEe:w#JZHKR\\3Xmxf'9jlHli*PTR-y`sdqRnv=;E$s]m!%I*`<*&.5N)wrI\"C=4^9RP5'9[5\"uG(4YU{3_aPHffi<E*+nVYQq37UP(P#wU9;p0Si.vyM1e?tXWZ9dRho1i!(we-<waQrvITH6vkTCG2 9hxMvtZ8QdR%WQ[B^0X1B;Vm&g/o=;YlD5[`Oh"):
    return all(s[x[i]] <= s[x[i + 1]] and x[i + 1] > x[i] for i in range(length - 1))

def sol():
    return []

if __name__ == "__main__":
    assert sat(sol())
