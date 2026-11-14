# Matematika pro informatiku – Cvičení 6 (Textové zadání)

Pojmy potřebné pro zvládnutí cvičení:
- Eukleidovská norma
- $D$-dimenzionální koule a hyperkrychle
- Eulerova gama funkce
- Objemová koncentrace
- Zákon velkých čísel
- Koncentrace normy (Shell phenomenon)
- Kosinová podobnost a řídkost prostoru (Curse of dimensionality)

---

## Příklad 1: Geometrie hyperkoule a hyperkrychle
Uvažujme $D$-dimenzionální kouli $K_D(r) = \{x \in \mathbb{R}^D : \|x\|_2 \le r\}$ a soustřednou hyperkrychli $C_D(r) = [-r, r]^D$.

- **a)** Spočítejte objem jednotkové koule $V(K_D(1))$ pomocí vzorce:
  $$V(K_D(r)) = \frac{\pi^{D/2}}{\Gamma(D/2 + 1)} r^D$$
  (kde $\Gamma(1) = 1$, $\Gamma(2) = 1$, $\Gamma(3) = 2$) a vyplňte následující tabulku:

| $D = 2$ | $D = 4$ | $\lim_{D \to \infty} V(K_D(r))$ pro $r > 0$ |
| :--- | :--- | :--- |
| $V(K_D(1))$ | | |

- **b)** Uvažujme jednotkovou hyperkouli $K_D(1)$ a její vnitřní část o poloměru $r = 1 - \varepsilon$. Vyjádřete podíl objemu vnitřní hyperkoule vůči $K_D(1)$ a podíl objemu vnější slupky o tloušťce $\varepsilon$ v $D$-dimenzionálním prostoru. Vyplňte tabulku pro zadané hodnoty $D$ a $\varepsilon$:

| $D$ | $\varepsilon$ | $V(K_D(1 - \varepsilon)) / V(K_D(1))$ | Podíl objemu vnější slupky |
| :--- | :--- | :--- | :--- |
| 5 | 0,1 | | |
| 5 | 0,01 | | |
| 50 | 0,1 | | |
| 50 | 0,01 | | |

- **c)** Srovnejte objem koule $K_D(1)$ s objemem opsané hyperkrychle $C_D(1)$ a formulujte hlavní geometrické závěry o rozložení hmoty ve vysokých dimenzích.

---

## Příklad 2: Koncentrace normy (Shell phenomenon)
Nechť $x = (X_1, \dots, X_D)^T$ je náhodný vektor, jehož složky jsou nezávislé a stejně rozdělené náhodné veličiny splňující $\mathbb{E}[X_i^2] = 1$ a $\operatorname{Var}(X_i^2) = \sigma^2 < \infty$.

- **a)** Odvoďte střední hodnotu normovaného kvadrátu normy $\frac{1}{D} \|x\|_2^2$ a jeho rozptyl, a popište konvergenci pomocí zákona velkých čísel.
- **b)** Jak roste typická vzdálenost takového vektoru od počátku s rostoucí dimenzí $D$?
- **c)** Popište, jak se liší chování normy vektorů z jednotkové krychle $[0, 1]^D$ oproti jednotkové sféře $S^{D-1}$.

---

## Příklad 3: Geometrické chování náhodných směrů (Ortogonalita ve vysokých dimenzích)
Porovnejte geometrické chování náhodných směrů ve vysokých dimenzích:

- **a)** Jaká je limitní kosinová podobnost dvou nezávislých náhodných směrů vybraných z povrchu jednotkové sféry $S^{D-1}$ pro $D \to \infty$? Co to znamená pro jejich vzájemný úhel?
- **b)** Jak se v tomto ohledu liší náhodné vektory z jednotkové krychle $[0, 1]^D$?
- **c)** Proč tato vlastnost sféry usnadňuje nebo naopak komplikuje reprezentaci dat?

---

## Příklad 4: Řídkost prostoru a selhání prostorových indexů
Uvažujme prostor dimenze $D = 20$, přičemž každý příznak rozdělíme na $m = 5$ stejných intervalů.

- **a)** Spočítejte celkový počet vzniklých buněk (krychliček) v tomto prostoru.
- **b)** Pokud máme k dispozici datový soubor o velikosti $N = 10000$ bodů, jaká je průměrná zaplněnost těchto buněk?
- **c)** Proč kvůli tomuto jevu selhávají klasické stromové struktury ($k$-d stromy) při vyhledávání sousedů ve vysokých dimenzích?
