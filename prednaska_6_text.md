=== STRANA 1 ===
6 Dimenze, prokletí dimenzionality a geometrie vysokých roz-
měrů
Při práci s moderními daty se běđněsetkáváme s vektory v prostorech o stovkách ađmilionech di-
menzí. Přestođe více příznakůteoreticky přináší více informací, geometrické a pravděpodobnostní
vlastnosti vysokodimenzionálních prostorůse zásadněliší od naší trojrozměrné zkušenosti. Tato
kapitola popisuje jevy souhrnněoznačované jakoprokletí dimenzionality(Curse of Dimensi-
onality) a jejich dopady na algoritmy strojového učení a analýzy dat. Zaměříme se především na
geometrii náhodných bodů, koncentraci vzdáleností a na důsledky, které tyto vlastnosti mají pro
vyhledávání, shlukování a detekci anomálií. Metody redukce dimenzionality budou předmětem
následující kapitoly.
6.1 Geometrie a matematická úskalí vysokých dimenzí
Poznámka 6.1(Eulerova gama funkce).Pro reálnáčíslaz >0je Eulerova gama funkceΓ(z)
denována nevlastním integrálem:
Γ(z) =
 ∞
0
tz−1 e−t dt▷
PlatíΓ(z+ 1) =zΓ(z). Pro celá kladnáčísla platíΓ(n) = (n−1)!,Γ(1◁2) = √πa pro polocelá
číslaΓ

n+ 1
2

= (2n−1)!!
2n
√π, kdem!!značí dvojitý faktoriál (m!! =m·(m−2)· · · · ·1).
Denice 6.1(D-dimenzionální koule).Pror >0označme
KD(r) ={x∈R D :∥x∥ 2 ≤r}
uzavřenouD-dimenzionální kouli se středem v počátku a poloměremr.
Denice 6.2(D-dimenzionální hyperkrychle).Mnođinu
CD(r) = [−r, r] D
nazýváme soustřednouD-dimenzionální hyperkrychlí o hranědélky2r. KouleK D(r)je vepsána
do hyperkrychleC D(r).
Věta 6.1(Objem koule a hyperkrychle).Objemy uvedených mnođin jsou dány vztahy
V(K D(r)) = πD◁2
Γ

D
2 + 1
 rD, V(C D(r)) = (2r) D▷
Věta 6.2(Limitní chování objemu koule).Pro libovolný pevný poloměrr >0konverguje objem
D-dimenzionální koule proD→ ∞k nule:lim D→∞ V(K D(r)) = 0.
Poznámka 6.2(Maximum objemu jednotkové koule).Objem jednotkové koule nejprve s ros-
toucí dimenzí roste, dosahuje celočíselného maxima proD= 5a poté konverguje k nule (viz.
obrázek 4).
Příklad 6.1(Koncentrace objemu a paradox vysokých dimenzí).Srovnejme objem (Lebesgue-
ovu míru) jednotkové hyperkouleK D(1)a jí opsané hyperkrychleC D(1) = [−1,1] D v prostoru
RD proD∈N, kdeV(C D) = 2 D:
•D= 2:V(C 2) = 4,V(K 2) =π≈3,14. Poměr objemůje přibliđně78,5 %.
•D= 3:V(C 3) = 8,V(K 3) = 4
3 π≈4,19. Poměr objemůje přibliđně52,3 %.
30

=== STRANA 2 ===
D
V(K D)
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
0
1
2
3
4
5
V1
V2
V3
V4
V5 V6
Obrázek 4: Závislost objemuD-dimenzionální jednotkové kouleK D(1)na počtu dimenzíD.
•D= 10:V(C 10) = 1024,V(K 10) = π5
120 ≈2,55. Poměr objemůklesá na přibliđně0,25 %.
•D= 100: V důsledku Gamma funkce ve jmenovateli vzorce proV(K D)je poměr objemů řádu
O

10−70
.
Geometrické a pravděpodobnostní důsledky:Podíl objemu hyperkrychle připadající na
vepsanou jednotkovou kouli konverguje proD→ ∞k nule. Nechťx= (X 1,▷ ▷ ▷, X D)je náhodný
vektor s rovnoměrným rozdělením na hyperkrychliC D(1). Pravděpodobnost,đe náhodný bod
padne do jednotkové koule, konverguje k nule (P(X D ∈K D(1))→0). Jednotková koule je tedy
ve vysokých dimenzích asymptoticky prázdná.
Poloha náhodných bodůvykazuje v limitěduální chování v závislosti na zvolené metrice:
1.Slupka hyperkrychle (normaℓ ∞):Aby bod leđel ve vnitřníčásti krychle vzdálené
alespoňε>0od stěn, muselo by platit|X i|≤1−εpro všechnai. Pravděpodobnost
tohoto jevu je(1−ε) D →0. Pro libovolněmaléε>0tedy bod s pravděpodobností
konvergující k1leđí v tenké vnější „slupce“ hyperkrychle.
2.Slupka větší hyperkoule (normaℓ 2):Euklidovská vzdálenost od středu splňuje∥x∥ 2
2 =D
i=1 X2
i . Protođe slođky jsou nezávislé aE[X 2
i ] = 1
3 , podle zákona velkýchčísel euklidovská
norma náhodného bodu s rostoucí dimenzí konverguje k hodnotě

D
3 .
Závěr:Náhodné body z hyperkrychle se proD→ ∞s pravděpodobností blíđící se1koncentrují
v průniku dvou oblastí: leđí v těsné blízkosti stěn hyperkrychle a zároveňv tenké sférické slupce
úplnějiné, mnohem větší hyperkoule o poloměruR≈

D
3 . Hmota se tak zcela stahuje ze středu
do vnějších vrstev a vzdálených rohůkrychle.
√
2
−1
1
√
3
−1
1
√
4
−1
1
√
5
−1
1
√
6
−1
1
√
7
−1
1
√
8
−1
1
√
10
−1
1
Obrázek 5: Geometrická ilustrace růstu vzdálenosti rohůD-dimenzionální krychle o hraně1
(poloprůhledná tyrkysová) vůčiD-dimenzionální jednotkové kouli (modrá) proD∈{2,▷ ▷ ▷,10}.
ProD= 4leđí rohy krychle na hranici koule (
√
4◁2 = 1), proD≥5ji přesahují.
31

=== STRANA 3 ===
6.2 Koncentrace normy a ortogonalita ve vysokých dimenzích
Chování a geometrické vlastnosti náhodných vektorůve vysokých dimenzíchDzásadnězávisí na
způsobu jejich generování a pravděpodobnostním rozdělení jejich slođek. Uvađujme následující
tři situace:
•1. Obecný náhodný vektor (např. standardní normální rozděleníN(0,1)):Nechť
slođkyX i náhodného vektorux∈R D jsou nezávislé a stejněrozdělené náhodné veličiny s ko-
nečným druhým momentemE[X 2
i ] = 1.Zákon velkýchčísel(konkrétnějeho slabá forma pro
aritmetické průměry nezávislých veličin) zaručuje,đe průměr konverguje v pravděpodobnosti
k teoretické střední hodnotě:
∥x∥2
2
D = 1
D
D
i=1
X2
i
P− →E[X2
i ] = 1, ∥x∥2√
D
P− →1▷
Typická vzdálenost vektoru od počátku tedy roste jako
√
D. Pravděpodobnostní hmota se
soustřeďuje do tenké sférické slupky kolem poloměru přibliđně
√
D, jejíđrelativní tloušťka
vzhledem k poloměru s rostoucí dimenzí klesá.
•2. Vnitřek jednotkové krychle[0,1] D (Xi ∼U(0,1)):Pro nezávislé slođky s rovnoměrným
rozdělením na intervalu[0,1]získáme druhý moment přímým výpočtem pomocí integrálu
hustoty pravděpodobnosti:
E[X2
i ] =
 1
0
x2 ·1dx=

x3
3
1
0
= 1
3 ▷
Odtud pro normu plyne∥x∥ 2◁
√
D P− →1◁
√
3, takđe typická norma roste jako

D◁3. Vzhledem
k nezáporným souřadnicím leđí všechny vektory v prvním ortantu. Pro dva nezávislé náhodné
vektoryx,yz tohoto rozdělení konverguje kosinová podobnost k podílu středních hodnot:
cos(x,y) =
1
D xT y
∥x∥2√
D
∥y∥2√
D
P− → E[XiYi]
E[X2
i ]E[Y 2
i ]
= E[Xi]E[Yi]
E[X2
i ]E[Y 2
i ]
▷
Včitateli dostáváme součin nezávislých středních hodnotE[X i]E[Yi] =

1
2

·

1
2

= 1
4 (neboť
E[Xi] = 1◁2proU(0,1)). Ve jmenovateli pak máme odmocninu ze součinu druhých momentů
1
3 · 1
3 = 1
3 . Celkovětedy vychází:
1◁4
1◁3 = 3
4 ▷
Náhodné vektory z jednotkové krychle ve vysoké dimenzi nevykazují ortogonalitu; jejich ko-
sinová podobnost se soustřeďuje kolem hodnoty0,75.
•3. Povrch jednotkové sféryS D−1 (rovnoměrný výběr):Nechťu,vjsou dva nezávislé
vektory vybrané rovnoměrněz povrchu jednotkové sféry, takđe∥u∥ 2
2 = D
i=1 u2
i = 1. Z důvodu
úplné rotační sférové symetrie mají všechny slođky nulovou střední hodnotu (E[u i] = 0) a
stejný druhý moment. Aplikací střední hodnoty na normu dostáváme:
D
i=1
E[u2
i ] = 1 =⇒E[u 2
i ] = 1
D ▷
Pro skalární součin platíE[u T v] =  E[ui]E[vi] = 0. Pro jeho kvadrát díky nezávislosti a
vymizení kříđovýchčlenů(i̸=j) dostáváme:
E[(uT v)2] =
D
i=1
E[u2
i ]E[v2
i ] =
D
i=1
1
D · 1
D = 1
D ▷
32

=== STRANA 4 ===
ZČebyševovy nerovnosti vyplývá,đe
P

|uT v|>ε

≤ 1
Dε2 − − − − →
D→∞
0▷
Kosinová podobnost dvou nezávislých náhodných směrůkonverguje k nule a úhel mezi nimi
k90 ◦. Ve vysokých dimenzích jsou tak nezávislé rovnoměrněvybrané směry s vysokou prav-
děpodobností téměřortogonální.
6.3 Koncentrace vzdáleností
ProNnezávislých a stejněrozdělených náhodných vektorůx 1,▷ ▷ ▷,x N ∈R D, jejichđslođky mají
konečnýčtvrtý moment a nenulový rozptyl, se s rostoucí dimenzíD→ ∞koecient variace
eukleidovských vzdáleností blíđí k nule:

Var(∥xa −x b∥2)
E[∥xa −x b∥2] − →0
(kdex a,x b jsou dva libovolné různé a na soběnezávislé body).
Pro nejmenší (d min) a největší (d max) vzájemnou vzdálenost mezi těmito body to z hlediska
koncentrace znamená,đe jejich relativní rozdíl konverguje v pravděpodobnosti k nule:
dmax −d min
dmin
P− − − − →
D→∞
0

tj. rovněđ dmax
dmin
P− − − − →
D→∞
1

▷
Tento závěr o ztrátěkontrastu metrik platí pro pevný počet bodůN. Pokud byNrostlo současně
s dimenzíD(např. exponenciálním tempem), je nutné zohlednit vzájemnou rychlost tohoto
růstu.
Důsledek:Pokud počet bodůNneroste s dimenzíDexponenciálním tempem, všechny vzá-
jemné vzdálenosti se stávají téměřstejnými. Rozlišit blízké a vzdálené sousedy je pak obtíđné,
cođkomplikuje práci metrickým algoritmům (k-NN,k-Means, DBSCAN). Neznamená to však
jejich automatické selhání – pokudNroste dostatečněrychle nebo mají data specickou nízko-
dimenzionální strukturu (tzv. intrinsic dimension), zůstává rozlišení sousedůzachováno.
Příklad 6.2.Chování vybraných měr v prostoru[0,1] D. GenerujemeN= 2000nezávislých
a rovnoměrněrozdělených bodůzU(0,1) D. Pro všechny dvojice bodů(celkemN(N−1)◁2 =
1 999 000dvojic) vyhodnocujeme při zvyšování dimenze (D∈{5,50,500,5000}) eukleidovskou
vzdálenost (L 2), Manhattanovskou vzdálenost (L 1), frakční kvazivzdálenost (p= 0,5) a kosi-
novou podobnost. Minimum a maximum v tabulce jsou tedy skutečná minima a maxima přes
všechny dvojice v daném vygenerovaném souboru. U kosinové podobnosti je poměrx max◁xmin
pouze popisem rozsahu hodnot, nikoli obvyklým ukazatelem kontrastu vzdáleností.
Hlavní závěry:
1.Koncentrace vzdáleností v praxi:S rostoucí dimenzíDprudce klesá relativní variabi-
lita vzdáleností (σ◁µklesá uL 2 z cca28 %na necelé1 %) a poměrx max◁xmin se blíđí jedné.
Všechny dvojice bodůse stávají téměřstejněvzdálenými, cođv praxi ilustruje koncentraci
vzdáleností a ztrátu kontrastu pro algoritmy.
2.Stabilizace kosinové podobnosti:Pro rovnoměrné rozdělení v[0,1] D konverguje ko-
sinová podobnost k hodnotě0,75a její variabilita klesá k nule. Na rozdíl od náhodných
směrůna celé sféře zde vektory nejsou navzájem kolmé, ale míří do podobného směru. Je
to dáno tím,đe data leđí výhradněv prvním ortantu (všechny souřadnice jsou nezáporné),
takđe skalární součin je vđdy kladný a vektory svírají ostré úhly kolem41 ◦ (arccos 0,75).
33

=== STRANA 5 ===
MíraD x min xmax
xmax
xmin
µσ 2 σ σ
µ
Eukleidovská
5 0,02789 1,9099 68,475 0,88751 0,061915 0,24883 0,28037
50 1,6925 4,0632 2,4007 2,8747 0,057978 0,24079 0,08376
500 7,8826 10,366 1,3151 9,1258 0,058444 0,24175 0,026491
5000 27,616 30,115 1,0905 28,87 0,058582 0,24204 0,008384
Manhattan.
5 0,04908 4,2673 86,949 1,6826 0,28161 0,53067 0,31538
50 9,2952 25,24 2,7154 16,656 2,7488 1,6579 0,099542
500 140,56 192,09 1,3665 166,67 27,794 5,272 0,031631
5000 1579,9 1755 1,1109 1666,9 278,55 16,69 0,010013
Frakční
5 0,20073 21,328 106,25 7,4207 7,1151 2,6674 0,35945
50 364,58 1140,7 3,1288 713,13 6904 83,09 0,11651
500 59019 84567 1,4329 71137 6,95·10 6 2636,9 0,037067
5000 6,70·10 6 7,55·10 6 1,1272 7,11·10 6 6,96·10 9 83448 0,011733
Kosinová pod.
5 0,04327 0,99987 23,108 0,76918 0,020209 0,14216 0,18482
50 0,49611 0,92001 1,8545 0,75164 0,001965 0,04433 0,058978
500 0,66541 0,81725 1,2282 0,7503 0,000201 0,014182 0,018901
5000 0,72696 0,77282 1,0631 0,75 1,98·10 −5 0,004452 0,005936
Tabulka 7: Srovnání vlastností eukleidovské (L 2), Manhattanovské (L1), frakční kvazivzdálenosti
(p= 0,5) a kosinové podobnosti v prostoru[0,1] D proN= 2000rovnoměrněrozlođených bodů.
U kađdé dimenze jsou zahrnuty všechny dvojice bodů.
6.4 Problémové oblasti způsobené dimenzionálním prokletím
1.Řídkost dat a potřeba velkého počtu pozorování:Pokud kađdý příznak rozdělíme na
mintervalů, vznikne vDdimenzích celkemm D buněk. Jiđpři deseti intervalech na příznak
dostáváme proD= 10celkem10 10 buněk. I rozsáhlý datový soubor proto můđe pokrý-
vat jen nepatrnoučást mođných kombinací hodnot. Lokální odhady hustoty a statistiky
zalođené na malém okolí pak mohou být nestabilní.
2.Indexace a vyhledávání:Prostorové indexy, napříkladk-d stromy nebo R-stromy, vy-
uđívají rozdělení prostoru a ohraničující oblasti k tomu, aby nemusely prohledat všechny
body. Ve vysokých dimenzích však ohraničující oblastičasto přestávají účinněvylučovat
kandidáty a vyhledávání se můđe blíđit sekvenčnímu prohledávání. Neexistuje přitom uni-
verzální hranice, od které by index automaticky přestal fungovat; záleđí na počtu bodů,
jejich rozlođení, typu indexu a dotazech.Řešení v praxi:Pro rozsáhlá data sečasto pou-
đívá aproximační vyhledávání nejbliđších sousedů(ANN), například grafové indexy HNSW
(Hierarchical Navigable Small World) nebo lokalitněcitlivé hašování (LSH). Tyto metody
obvykle vyměňují přesnost za rychlost.
3.Detekce anomálií a shlukování:Při koncentraci vzdáleností se rozdíly mezi blízkými a
vzdálenými body zmenšují. To můđe zhoršit rozlišitelnost sousedství a ovlivnit metodyk-
NN,k-Means i DBSCAN. Nejde však o automatické selhání algoritmů: pokud data obsahují
výraznou strukturu, relevantní příznaky nebo nízkodimenzionální strukturu vnořenou do
prostoru, mohou algoritmy fungovat dobře.Mođné přístupy:Je vhodné ověřit volbu vzdále-
nosti, význam jednotlivých příznakůa stabilitu výsledků. Frakční kvazimetriky s0< p <1
mohou v některých datech zvýšit kontrast, ale nejsou metrikami a jejich vhodnost je třeba
empiricky ověřit.
4.Hubness (jev dominantních sousedů):Ve vysokodimenzionálních datech se můđe stát,
đe některé body se objeví v seznamechknejbliđších sousedůmnoha jiných bodů, zatímco
jiné body se jako sousedé téměřnevyskytují. Takové body se označují jakohub points.
Tento jev můđe zkreslovat klasikaci metodouk-NN, vyhledávání podobných dokumentů
či obrázkůa doporučovací systémy. Hubness souvisí s rozdělením vzdáleností a geometrií
dat, ale jeho intenzita závisí také na rozdělení příznakůa pouđité míře podobnosti.
5.Postkvantová kryptograe (mříđkové problémy)
34