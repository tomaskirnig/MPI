

--- PAGE 1 ---

5 Metrické a topologické prostory
V předchozí kapitole jsme zkoumali různé způsoby, jak kvantikovat vzájemný vztah mezi
objekty. Ačkoliv metriky poskytují přesné „pravítko“ pro měřeníčíselné vzdálenostid(x, y),
v mnoha praktických i teoretických aplikacích (datové vědy, klasikace, analýza sítíči teorie
rough mnođin) ječíselná hodnota vzdálenosti příliš svazující nebo nedostupná.Často potřebu-
jeme pouze vědět, zda jsou si objekty „dostatečněblízko“, zda je bod uvnitřnějakého shluku,
nebo zda je zobrazení mezi strukturami plynulé (spojité).
Topologie představuje zobecnění metrických prostorů„bez nutnosti měřit přesné vzdálenosti“ .
Zatímco v metrickém prostoru tvoříme okolí bodůpomocí otevřených koulíB(x,ε), v topolo-
gickém prostoru přímo pracujeme se systémem tzv. otevřených mnođin.
Tato kapitola ukáđe:
•Jak kađdá metrika z předchozí kapitoly přirozeněgeneruje topologii (metrizovatelný prostor),
•Pročněkteré topologie naopak pomocíđádné metriky popsat nelze (nemetrizovatelný prostor).
5.1 Základní deﬁnice
Pro přehlednost nejdříve naváđeme na formální denici metrického prostoru z předchozí kapi-
toly, zavedeme základní geometrické objekty (otevřené a uzavřené koule) a následněstrukturu
zobecníme do topologického prostoru.
Denice 5.1(Metrický prostor).Dvojice(X, d), kdeX̸=∅ad:X×X→R ≥0 je funkce
(metrika) splňující pro všechnax, y, z∈X:
1.d(x, y)≥0(nezápornost),
2.d(x, y) = 0⇐ ⇒x=y(totođnost),
3.d(x, y) =d(y, x)(symetrie),
4.d(x, z)≤d(x, y) +d(y, z)(trojúhelníková nerovnost).
Denice 5.2(Otevřená koule, uzavřená koule a sféra).Nechť(X, d)je metrický prostor,x∈X
ar >0.
•Otevřená koulese středemxa poloměremrje mnođinaB(x, r) ={y∈X|d(x, y)< r}▷
•Uzavřená koulese středemxa poloměremrje mnođinaK(x, r) ={y∈X|d(x, y)≤r}▷
•Sférase středemxa poloměremrje mnođinaS(x, r) ={y∈X|d(x, y) =r}▷
PlatíS(x, r) =K(x, r)\B(x, r), sféra tedy tvoří geometrickou hranici otevřené i uzavřené koule.
Příklad 5.1(Standardní metriky a ultrametrika).Typickými příklady metrických prostorů
jsou:
•Eukleidovský prostor(R n, d2),manhattanský prostor(R n, d1)amaximový prostor
(Rn, d∞), které vyuđívají standardníp-metriky. VR 2 tvoří uzavřená jednotková kouleK(0,1)
v těchto metrikách postupněeukleidovský kruh, kosočtverec ačtverec.
•Diskrétní metrický prostor(X, d diskr), kded diskr(x, y) = 0prox=yad diskr(x, y) = 1
prox̸=y. Tato metrika je výjimečná tím,đe splňuje tzv.silnou (ultrametrickou) trojú-
helníkovou nerovnost:
dd(x, z)≤max{d d(x, y), dd(y, z)}∀x, y, z∈X▷
Diskrétní metrika tak tvoří speciální případ metrického prostoru — ultrametrický prostor.
Příklad 5.2(Tvar koule v různých metrikách naR 2).Geometrický tvar jednotkové uzavřené
kouleK((0,0),1)v reálné roviněX=R 2 závisí na volběmetriky. Přehled těchto uzavřených
jednotkových koulí je na obrázku 3.
25

--- PAGE 2 ---

0−1 1
−1
1
K1(0,1)aK 1◁2(0,1)
0−1 1
−1
1
K2(0,1)aK 3(0,1)
0−1 1
−1
1
K∞(0,1)
0−1 1
−1
1
Kdiskr(0,1)
Obrázek 3: Uzavřené kouleK d(0,1)⊂R 2 pro metrika/nemetrika sd= 1◁2,1,2,3,∞,diskr.
Pro diskrétní metriku ar= 1tvoří koule celou rovinuR 2 (světle zelená plocha); pror <1se
redukuje pouze na samotný bod0(modrý bod).
Denice 5.3(Topologický prostor).Dvojice(X,τ), kdeX̸=∅aτ⊆P(X)je systém podmno-
đin (topologie) splňující:
1.∅ ∈τaX∈τ,
2. Libovolné sjednocení prvkůzτleđí vτ,
3. Konečný průnik prvkůzτleđí vτ.
MnođinyU∈τnazývámeotevřené mnođiny.
Denice 5.4(Báze topologie).Nechť(X,τ)je topologický prostor. Systém podmnođinB⊆τse
nazývábáze topologieτ, pokud lze kađdou otevřenou mnođinuU∈τvyjádřit jako sjednocení
prvkůzB.
Příklad 5.3(Báze v konečném a nekonečném prostoru).
•Konečný prostor:MějmeX={a, b, c}s topologiíτ={∅,{a},{b},{a, b},{b, c}, X}▷Bází
této topologie je pouze tříprvkový systémB={{a},{b},{b, c}}.
Všechny zbývající otevřené mnođiny zτzískáme sjednocením prvkůzB:{a, b}={a}∪{b},
X={a}∪{b, c},∅je sjednocením prázdného systému prvkůzB.
•Nekonečný prostor (R):Na mnođiněreálnýchčíselRse standardní (eukleidovskou) topo-
logií tvoří bázi systém všech otevřených intervalů:
B={(a, b)|a, b∈R, a < b}▷
Kađdá otevřená mnođinaU⊆Rje totiđdenována tak,đe je sjednocením takovýchto otevře-
ných intervalů.
Příklad 5.4(Konečné topologické prostory a jejich specika).Je-li nosičXkonečná mnođina
(tj.|X|<∞), nazýváme(X,τ)konečným topologickým prostorem.
Příklady konečných topologií naX={a, b, c}:
•Indiskrétní topologie:τ ind ={∅, X}(nejchudší mođná topologie, jediná báze je{X}).
•Diskrétní topologie:τ disk =P(X)(nejbohatší mođná topologie, minimální bázi tvoří jed-
nobodové mnođiny{{a},{b},{c}}).
•Sierpińského topologie na mnođině{0,1}:τ={∅,{0},{0,1}}.
Specika konečných topologických prostorů:
1.Minimální otevřená okolí:Pro kađdý bodx∈Xexistuje právějedna nejmenší ote-
vřená mnođinaV x ∈τobsahující tento bod (vznikne jako průnik všech otevřených mnođin
obsahujícíchx).
26

--- PAGE 3 ---

2.Kanonická (minimální) báze:Systém těchto minimálních okolí
Bmin ={V x |x∈X}
tvoří jedinečnou minimální bázi topologieτ. Kađdá otevřená mnođina je pak sjednocením
některých prvkůzB min.
Denice 5.5(Metrizovatelnost a indukovaná topologie).Nechť(X, d)je metrický prostor. Sys-
tém mnođinτ d denovaný jako:
U∈τ d ⇐ ⇒ ∀x∈U∃ε>0 :B(x,ε)⊆U
tvoří topologii naXindukovanou metrikoud.
Obecný topologický prostor(X,τ)nazývámemetrizovatelný, pokud existuje metrikadna
mnođiněXtaková,đeτ=τ d.
Příklad 5.5(Metrizovatelný vs. nemetrizovatelný prostor).
•Standardní reálná osa(R,τ std):Jde o metrizovatelný prostor. Mnođina všech otevře-
ných intervalů(a, b)tvoří bázi topologie, která je přesněindukována Eukleidovskou metrikou
d(x, y) =|x−y|.
•Indiskrétní prostor(X,τ ind)pro|X|≥2:Nechťτ ind ={∅, X}. Tento prostor není met-
rizovatelný. V jakémkoliv metrickém prostoru totiđlze pro dva různé bodyx̸=yvđdy najít
dostatečněmalou kouliB(x,ε), která bodyneobsahuje, cođv indiskrétní topologii nelze
(jediná neprázdná otevřená mnođina je celéX).
5.2 Základní metrické a topologické pojmy
Denice 5.6(Okolí bodu).Nechťx∈X.
•V metrickém prostoru:Otevřená koule se středemxa poloměremε>0jeB(x,ε) ={y∈
X|d(x, y)<ε}. Ryzí (prstencové) okolí jeP(x,ε) =B(x,ε)\ {x}.
•V topologickém prostoru:MnođinaV⊆Xje okolím bodux, pokud existuje otevřená
mnođinaU∈τtaková,đex∈U⊆V.
Denice 5.7(Otevřená, uzavřená a obojetná mnođina).NechťA⊆X.
•MnođinaAjeotevřenáv topologologickém prostoru, pokudA∈τ. V metrickém prostoru to
znamená:∀x∈A∃ε>0 :B(x,ε)⊆A.
•MnođinaAjeuzavřená, pokud je její doplněkX\Aotevřenou mnođinou.
•MnođinaAjeobojetná (clopen), pokud je současněotevřená i uzavřená vτ.
Denice 5.8(Vnitřek, uzávěr a hranice).NechťA⊆X.
•Vnitřekint(A):Největší otevřená mnođina obsađená vA(sjednocení všech otevřených mnođin
leđících vA). Bodx∈int(A)se nazývá vnitřní bod.
•Uzávěrcl(A):Nejmenší uzavřená nadmnođinaA(průnik všech uzavřených nadmnođin obsa-
hujícíchA).
•Hranice∂A:Mnođina bodů∂A= cl(A)\int(A). Bodx∈∂Aprávětehdy, kdyđkađdé jeho
okolí protíná jakA, takX\A.
Denice 5.9(Hromadný a izolovaný bod).NechťA⊆Xax∈X.
•Bodxjehromadný bodmnođinyA, pokud kađdé ryzí (prstencové) okolí boduxobsahuje
alespoňjeden bod zA(tj.P(x)∩A̸=∅). Hromadný bod nemusí náleđet doA.
•Bodx∈Ajeizolovaný bodmnođinyA, pokud existuje okolíV(x)takové,đeV(x)∩A={x}.
27

--- PAGE 4 ---

Denice 5.10(Souvislost topologického prostoru).Topologický prostor(X,τ)jenesouvislý,
pokud jej lze vyjádřit jako sjednocení dvou neprázdných disjunktních otevřených mnođin.
Ekvivalentně: ProstorXjesouvislý, pokud v něm neexistujíđádné netriviální obojetné (ote-
vřené a zároveňuzavřené) mnođiny — neboli jedinými obojetnými mnođinami vXjsou prázdná
mnođina∅a celý prostorX.
Pro ilustraci výše uvedených pojmůuvađujme tři různé topologické prostory a v nich vybrané
podmnođinyA 1, A2, A3:
1.Prostor 1 (Rse standardní metrikoud 2):Mějme podmnođinuA 1 = (0,1]∪{3}⊂R.
2.Prostor 2 (Diskrétní metrický prostor na konečné mnođině):MějmeX={1,2,3}
s diskrétní metrikoud diskr a v něm podmnođinuA 2 ={1,2}.
3.Prostor 3 (Konečný topologický prostor):MějmeX={a, b, c, d}s topologiíτ=
{∅,{a},{a, b}, X}a podmnođinuA 3 ={a, c}.
Přehled vypočtených charakteristik a vlastností pro tyto tři případy uvádí Tabulka 5.
Charakteristika Prostor 1 (A 1) Prostor 2 (A 2) Prostor 3 (A 3)
Vnitřekint(·) (0,1) {1,2} {a}
Uzávěrcl(·) [0,1]∪{3} {1,2} {a, b, c, d}
Hranice∂(·) {0,1,3} ∅ {b, c, d}
Hromadné body [0,1] ∅ {b, c, d}
Izolované body {3} {1,2} {a}
Souvislost prostoru Souvislý Nesouvislý Souvislý
Tabulka 5: Srovnání základních topologických charakteristik ve třech různých prostorech.
5.3 Oddělovací axiomy a hranice metrizovatelnosti
Nemůđeme kađdý topologický prostor popsat metrikou. Zda je prostor metrizovatelný, do značné
míry závisí na tom, jak dobře dokáđe jeho topologie „oddělovat“ různé body od sebe. K tomuto
účelu slouđí tzv. oddělovací axiomy.
Denice 5.11(Základní oddělovací axiomy).Nechť(X,τ)je topologický prostor.
•AxiomT 0 (Kolmogorovův):Pro kađdé dva různé bodyx, y∈Xexistuje otevřená mnođina
obsahující právějeden z nich.
•AxiomT 1 (Fréchetův):Pro kađdé dva různé bodyx, y∈Xexistují otevřené mnođiny
U, V∈τtakové,đex∈U, y◁∈Uay∈V, x◁∈V. (Ekvivalentně: Kađdá jednoprvková mnođina
{x}je uzavřená.)
•AxiomT 2 (Hausdorův):Pro kađdé dva různé bodyx, y∈Xexistujídisjunktníotevřená
okolíU, V∈τ(x∈U, y∈V) splňujícíU∩V=∅.
•Regulární prostor:Pro kađdý bodx∈Xa kađdou uzavřenou mnođinuF⊆Xneobsahující
x(x◁∈F) existují disjunktní otevřené mnođinyU, V∈τtakové,đex∈UaF⊆V. Je-li
prostor navícT 1, nazývá seT 3 prostor.
•Tichonovův (zcela regulární) prostor /T 3 1
2
:Pro kađdý bodx∈Xa uzavřenou mnođinu
F⊆Xneobsahujícíxexistuje spojitá funkcef:X→[0,1]taková,đef(x) = 0af(y) = 1
pro všechnay∈F. Je-li prostor navícT 1, nazývá seT 3 1
2
prostor.
•Normální prostor:Pro kađdé dvědisjunktní uzavřené mnođinyE, F⊆X(E∩F=∅)
existují disjunktní otevřené mnođinyU, V∈τtakové,đeE⊆UaF⊆V. Je-li prostor navíc
T1, nazývá seT 4 prostor.
Předchozí axiomy tvoří hierarchiiT 4 =⇒T 3 1
2
=⇒T 3 =⇒T 2 =⇒T 1 =⇒T 0. Pro ilustraci
hranic platnosti těchto axiomůuvađujme šest reprezentativních topologických prostorů:
28

--- PAGE 5 ---

1.ProstorP 1 (Indiskrétní):X={a, b}sτ ind ={∅, X}.
2.ProstorP 2 (Pawlakova topologie):X={a, b, c}s rozklademB={{a},{b, c}}a
τR ={∅,{a},{b, c}, X}.
3.ProstorP 3 (Sierpińského):X={0,1}sτ={∅,{1},{0,1}}.
4.ProstorP 4 (Konitní naR):X=R, otevřené jsou∅a mnođiny s konečným doplňkem.
5.ProstorP 5 (Standardní eukleidovský):(R, d 2).
6.ProstorP 6 (Diskrétní):Xsτ disk =P(X).
Srovnání jejich oddělovacích vlastností a metrizovatelnosti je uvedeno v Tabulce 6.
Prostor Splněné axiomy Porušené axiomy Metrizovatelný? Souvislost
P1 Őádný T0, T1, T2, T3, T4 Ne Souvislý
P2 Őádný T0, T1, T2, T3, T4 Ne Nesouvislý
P3 T0 T1, T2, T3, T4 Ne Souvislý
P4 T0, T1 T2, T3, T4 Ne Souvislý
P5 T0, T1, T2, T3, T3 1
2
, T4 Őádný Ano Souvislý
P6 T0, T1, T2, T3, T3 1
2
, T4 Őádný Ano Nesouvislý*
Tabulka 6: Oddělovací axiomy, metrizovatelnost a souvislost u vybraných prostorů.
Věta 5.1(Nutná podmínka metrizovatelnosti).Kađdý metrický prostor(X, d)tvoří ve své
indukované topologiiτ d Hausdorův (T 2) prostor.
Poznámka 5.1.Kađdý metrizovatelný prostor musí splňovat axiomT 2 (Hausdorův). Pokud
v prostoru existují dva různé body, které nelze oddělit disjunktními otevřenými mnođinami,
neexistujeđádná metrika, která by danou topologii generovala.
Poznámka 5.2(Topologický význam Pawlakových aproximací).Aproximační prostor(U, R)
generujePawlakovu topologiiτ R s bází tvořenou třídami ekvivalence[x] R. Protođe tyto třídy
tvoří rozkladU, je kađdá otevřená mnođina vτ R zároveňuzavřená (clopen).
Operace z teorie rough mnođin proA⊆Uodpovídají standardním topologickým operacím:
•Dolní aproximace=vnitřek:R (A) ={x∈U|[x] R ⊆A}= int(A)▷
•Horní aproximace=uzávěr: R(A) ={x∈U|[x] R ∩A̸=∅}= cl(A)▷
•Oblast nejistoty=hranice:BN R(A) = R(A)\R (A) =∂A▷
Souvislost a oddělitelnost v Pawlakověprostoru:
•Souvislost:Prostor je souvislý pouze při jediné tříděekvivalence (indiskrétní topologie). Při
2 a více třídách je díky netriviálním clopen mnođinámnesouvislý(dokonce zcela nesouvislý).
•Oddělitelnost:Obsahuje-li jakákoliv třída více neđjeden prvek, nelze tyto prvky oddělit
otevřenou mnođinou a prostor nesplňuje ani axiomT 0 (aniT 1,T 2). Výjimkou je případ jed-
nobodových tříd, kdy přechází vdiskrétní topologii(ta jeT 2 a metrizovatelná).
5.4 Spojitost zobrazení
V metrických prostorech denujeme spojitost pomocí vzdáleností (ε-δkritérium). V topologic-
kých prostorech, kde vzdálenost nemáme, se spojitost denuje pomocí vzorůotevřených mnođin.
Denice 5.12(Spojité zobrazení).Nechť(X,τ X )a(Y,τ Y )jsou topologické prostory. Zobrazení
f:X→Yjespojité, pokud pro kađdou otevřenou mnođinuV∈τ Y je její vzorf −1(V)
otevřenou mnođinou vX(tj.f −1(V)∈τ X ).
Věta 5.2(Ekvivalence spojitosti v metrickém prostoru).V metrických prostorech(X, d X )a
(Y, dY )s indukovanými topologiemi je zobrazeníf:X→Yspojité podle předchozí topologické
denice právětehdy, kdyđplatí klasickáε-δpodmínka:
∀x∈X∀ε>0∃δ>0 :f(B X (x,δ))⊆B Y (f(x),ε)▷
29