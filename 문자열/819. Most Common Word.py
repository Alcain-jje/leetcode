"""
#틀린 풀이 (문자 외 기호문자를 모두 제거하는 법을 몰랐음)
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph=paragraph.lower()
        table= paragraph.maketrans({',':' ','"':' ','!':" ",'.':' ','/':' ','?':' ',';':' ',']':' ','[':' ',"'":" "})
        paragraph=paragraph.translate(table)
        paragraph=paragraph.split()
        dic={}
        for i in paragraph:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        if len(banned) == 0:
            pass
        else:
            try:
                for i in set(banned):
                    dic.pop(i)
            except KeyError:
                pass
        print(dic)
        return max(dic, key=dic.get)"""



"""
#1번 정규식을 활용한 풀이 70ms
import re
import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words=[word for word in re.sub(r'[^\w]',' ',paragraph).lower().split()
               if word not in banned]
        #print(words)
        counts=collections.defaultdict(int)
        for word in words:
            counts[word]+=1
        return max(counts, key=counts.get)



#2번 정규식 and Counter을 활용한 풀이 77ms
import re
import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words=[word for word in re.sub(r'[^\w]',' ',paragraph).lower().split()
               if word not in banned]
        print(words)
        counts=collections.Counter(words)
        return counts.most_common(1)[0][0]

#3번 re.findall() 정규식 풀이 35ms

import re
import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        banned=set(banned)
        words=re.findall(r'\w+',paragraph.lower())
        return collections.Counter(w for w in words if w not in banned).most_common(1)[0][0]"""

#paragraph="Bob hit a ball, the hit BALL flew far after it was hit."
#banned=["hit"]

#paragraph="Bob. hIt, baLl"
#banned=["bob", "hit"]

paragraph="a, a, a, a, b,b,b,c, c"
banned=["a"]

paragraph="j. t? T. z! R, v, F' x! L; l! W. M; S. y? r! n; O. q; I? h; w. t; y; X? y, p. k! k, h, J, r? w! U! V; j' u; R! z. s. T' k. P? M' I' j! y. P, T! e; X. w? M! Y, X; G; d, X? S' F, K? V, r' v, v, D, w, K! S? Q! N. n. V. v. t? t' x! u. j; m; n! F, V' Y! h; c! V, v, X' X' t? n; N' r; x. W' P? W; p' q, S' X, J; R. x; z; z! G, U; m. P; o. P! Y; I, I' l' J? h; Q; s? U, q, x. J, T! o. z, N, L; u, w! u, S. Y! V; S? y' E! O; p' X, w. p' M, h! R; t? K? Y' z? T? w; u. q' R, q, T. R? I. R! t, X, s? u; z. u, Y, n' U; m; p? g' P? y' v, o? K? R. Q? I! c, X, x. r' u! m' y. t. W; x! K? B. v; m, k; k' x; Z! U! p. U? Q, t, u' E' n? S' w. y; W, x? r. p! Y? q, Y. t, Z' V, S. q; W. Z, z? x! k, I. n; x? z; V? s! g, U; E' m! Z? y' x? V! t, F. Z? Y' S! z, Y' T? x? v? o! l; d; G' L. L, Z? q. w' r? U! E, H. C, Q! O? w! s? w' D. R, Y? u. w, N. Z? h. M? o, B, g, Z! t! l, W? z, o? z, q! O? u, N; o' o? V; S! z; q! q. o, t! q! w! Z? Z? w, F? O' N' U' p? r' J' L; S. M; g' V. i, P, v, v, f; W? L, y! i' z; L? w. v, s! P?"
banned=["m","q","e","l","c","i","z","j","g","t","w","v","h","p","d","b","a","r","x","n"]
sol=Solution()
print(sol.mostCommonWord(paragraph,banned))




"""
#시그널을 준 예외처리
print(len(a))
print(a[2:len(a)-3])
new=a[-1].split('"')
try:
    print(new[1])
except IndexError:
    pass"""