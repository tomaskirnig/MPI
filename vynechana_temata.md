# 📋 AUDIT UČIVA: Co jsme vynechali v Cvičeních 1 až 4 (MPI)

Tento dokument obsahuje kompletní inventuru všech příkladů a teoretických konceptů z oficiálních materiálů předmětu MPI (Cvičení 1 až 4), které jsme v předchozím rychloprůchodu zatím **vynechali**, **probrali jen částečně**, nebo **nevyřešili do hloubky**.

---

## 📌 BLOK 1: CVIČENÍ 1 – USPOŘÁDÁNÍ, SVAZY A ALGEBRY

### 1. Příklad 2: Obecný poset zadaný množinou hran (Hasseův diagram z relace)
- **Zadání ze cvičení:** Mějme množinu $M = \{a, b, c, d, e, f, g\}$ a relaci bezprostředního předcházení (hrany diagramu):
  $$\rho = \{(a, b), (a, c), (b, d), (b, e), (c, d), (c, e), (d, f), (d, g), (e, f), (e, g)\}$$
- **Co jsme vynechali:**
  - [x] **a) Vykreslení Hasseova diagramu** podle zadaných dvojic.
  - [x] **b) Hledání závor a inf/sup pro konkrétní podmnožiny:**
    - $A = \{b, g\}$, $B = \{b, c\}$, $C = \{a, b, c, d\}$, $D = \{a, b, c, f\}$ a celá množina $M$.
  - [ ] **c) Rozhodnutí, zda je poset $(M, \rho)$ svazem:** (Pozor na prvky $\{d, e\}$, které mají dvě různé horní závory $f, g$, z nichž ani jedna není menší než druhá $\implies$ neexistuje supremum $\implies$ **není to svaz**!).

---

### 2. Příklad 3: Další typy svazů a jejich vlastnosti
- **Co jsme vynechali:**
  - [x] **b) Svaz dělitelů $D_{30} = \{1, 2, 3, 5, 6, 10, 15, 30\}$:**
    - $30 = 2 \cdot 3 \cdot 5$ (bezčtvercové číslo). Hasseův diagram tvoří **3D krychli**.
    - Vlastnosti: je distributivní, modulární a **komplementární** (je to Booleova algebra!).
  - [x] **d) Nekonečný svaz $(\mathbb{N} \setminus \{0\}, \mid)$:**
    - Má nejmenší prvek ($1$), ale **nemá největší prvek** $\implies$ není ohraničený shora, není úplný.
    - Je distributivní, ale není komplementární.

---

### 3. Příklad 5c: Maticové okruhy a dělitelé nuly
- **Zadání:** Množina matic $M_{2\times 2}(\mathbb{R})$ vzhledem k maticovému sčítání $+$ a násobení $\cdot$.
- **Co jsme vynechali:**
  - [ ] $(M_{2\times 2}(\mathbb{R}), +)$ je Abelovská grupa.
  - [ ] $(M_{2\times 2}(\mathbb{R}), \cdot)$ je monoid (asociativní, jednotková matice $I$), ale **není komutativní** ($A \cdot B \neq B \cdot A$).
  - [ ] **Dělitelé nuly:** Existují nenulové matice $A \neq 0, B \neq 0$ takové, že $A \cdot B = 0$.
  - [ ] Závěr: Je to **nekomutativní okruh s jednotkou a s děliteli nuly** (není to obor integrity ani těleso).

---

### 4. Příklad 6: Cayleyho tabulky a modulární okruhy
- **Co jsme vynechali:**
  - [x] **Sestavení Cayleyho tabulky** pro $M_1 = \{1, i, -1, -i\}$ (cyklická grupa řádu 4 generovaná $i$).
  - [ ] **Rozbor $\mathbb{Z}_4$ s operacemi $+$ a $\cdot$:**
    - Má dělitele nuly: $2 \cdot 2 \equiv 0 \pmod 4$.
    - Prvek $[2]$ nemá multiplikativní inverzi $\implies$ $(\mathbb{Z}_4, +, \cdot)$ je komutativní okruh, ale **není těleso**.
  - [ ] **Rozbor $\mathbb{Z}_5$ s operacemi $+$ a $\cdot$:**
    - Číslo 5 je prvočíslo $\implies$ všechny nenulové prvky $\{1, 2, 3, 4\}$ mají inverzi $\implies$ **je to těleso $\mathbb{F}_5$**!
  - [ ] **Nulový (agresivní) prvek $z$:** Prvek splňující $a \circ z = z \circ a = z$ (např. 0 při násobení čísel).

---

## 📌 BLOK 2: CVIČENÍ 2 – FORMÁLNÍ ANALÝZA KONCEPTŮ (FCA)

### 1. Příklad 1: Uzávěrové systémy na abstraktní množině 🔴 (KRITICKY DŮLEŽITÉ!)
- **Zadání:** Mějme základní množinu $X = \{1, 2, 3, 4\}$ a systém jejích podmnožin:
  $$C_1 = \{\{1, 2\}, \ \{1, 3\}, \ \{1, 2, 3\}, \ X\}$$
- **Co jsme vynechali:**
  - [ ] **a) Definice uzávěrového systému:** Systém $C \subseteq \mathcal{P}(X)$ je uzávěrový systém, právě když:
    1. Obsahuje celou množinu: $X \in C$.
    2. Je **uzavřený na libovolné průniky**: $\forall Y, Z \in C \implies Y \cap Z \in C$.
    - *Ověření $C_1$:* $\{1, 2\} \cap \{1, 3\} = \{1\}$. Patří $\{1\}$ do $C_1$? **NEPATŘÍ!** $\implies C_1$ **není** uzávěrový systém!
  - [ ] **b) Test systému $C_2 = C_1 \cup \{\{1\}\}$:** Nyní $\{1\} \in C_2 \implies$ **JE to uzávěrový systém**.
  - [ ] **c) Test systému $C_3 = C_2 \setminus \{\{1, 2\}\}$.**
  - [ ] **d) Výpočet uzávěru ze vzorce:**
    $$cl_C(Y) = \bigcap \{Z \in C \mid Y \subseteq Z\}$$
    Pro $Y_1 = \{2\}, Y_2 = \{2, 3\}, Y_3 = \{1, 2\}$.

---

### 2. Příklad 3c: Podrobný test vlastností konceptuálního svazu
- **Co jsme vynechali:**
  - [ ] Ověření modularity a distributivity nalezeného 10-prvkového konceptuálního svazu:
    - Obsahuje svaz pětiúhelník $N_5$?
    - Obsahuje svaz diamant $M_3$?

---

### 3. Příklad 5: Detaily algoritmu Apriori & Rymon tree
- **Co jsme vynechali:**
  - [ ] **a) Kompletní vykreslení Rymon tree** pro všechny kombinace položek s nenulovou podporou.
  - [ ] **c) Zvýraznění uzávěrového systému intentů v Rymon tree:** Které uzly stromu tvoří uzavřené množiny atributů (intenty formálních konceptů)?
  - [ ] **d) Výpočet spolehlivosti VŠECH možných asociačních pravidel** pro časté sady při $\mu \ge 0.4$.

---

## 📌 BLOK 3: CVIČENÍ 3 – FUZZY LOGIKA A ROUGH SETS

### 1. Příklad 1c: Algebraická (součinová) fuzzy logika 🔴
- **Co jsme vynechali:**
  - V Zadehově logice jsme dělali $\min / \max$. V **součinové logice** platí:
    - **Součinový průnik:** $\mu_{A \cdot B}(x) = \mu_A(x) \cdot \mu_B(x)$
    - **Součinové sjednocení (pravděpodobnostní suma):** 
      $$\mu_{A \oplus B}(x) = \mu_A(x) + \mu_B(x) - \mu_A(x) \cdot \mu_B(x)$$
  - [x] Propočtení konkrétních hodnot pro fuzzy množiny $A$ a $B$ ze cvičení 3.

---

### 2. Příklad 4d: Algoritmus QuickReduct 🔴 (KRITICKY DŮLEŽITÉ!)
- **Co jsme vynechali:**
  - [ ] Známe hledání reduktů přes DNF funkci rozlišitelnosti $f_d$.
  - [ ] Ale cvičení explicitně vyžaduje **heuristický algoritmus QuickReduct**:
    - Začínáme s prázdnou sadou atributů $R = \emptyset$ (kde $\gamma_R(d) = 0$).
    - V každém kroku přidáme ten atribut $a \in C \setminus R$, který **nejvíce zvýší míru závislosti $\gamma_{R \cup \{a\}}(d)$**.
    - Zastavíme, jakmile dosáhneme plné závislosti $\gamma_R(d) = \gamma_C(d) = 1$.

---

## 📌 BLOK 4: CVIČENÍ 4 – METRIKY A PODOBNOSTI

### 1. Příklad 5b: Gaussovská (RBF) transformace vzdálenosti na podobnost
- **Co jsme vynechali:**
  - [ ] Převod neomezené vzdálenosti $d(x, y) = 3$ pomocí Gaussova jádra (RBF):
    $$s(x, y) = \exp\left(-\frac{d(x, y)^2}{2\sigma^2}\right)$$
    Pro zadané $\sigma = 1$:
    $$s = \exp\left(-\frac{3^2}{2 \cdot 1^2}\right) = e^{-9/2} = e^{-4.5} \approx \mathbf{0.011}$$

---

### 2. Teoretické pojmy z úvodu CV4
- **Co jsme vynechali:**
  - [ ] **Pseudometrika:** Splňuje všechny axiomy metriky KROMĚ ostré totožnosti ($d(x, y) = 0$ může nastat i pro dva různé body $x \neq y$).
  - [ ] **Geodetická vzdálenost:** Délka nejkratší cesty v grafu (počet hran nebo součet vah hran).

---

# 🎯 DOPORUČENÝ POSTUP PROJETÍ:
Doporučuji projet tato vynechaná témata ve 3 logických blocích:
1. **BLOK A (Nejvyšší priorita ke zkoušce):**
   - Uzávěrové systémy $C_1, C_2, C_3$ a výpočet $cl_C(Y)$ (CV2).
   - Algoritmus QuickReduct krok za krokem (CV3).
   - Součinová fuzzy logika (CV3).
2. **BLOK B (Algebraické a strukturní detaily):**
   - Hasseův diagram obecného posetu z hran $\rho$ a test svazu (CV1 Příklad 2).
   - Modulární okruhy $\mathbb{Z}_4, \mathbb{Z}_5$, dělitelé nuly a maticový okruh (CV1 Příklad 5c, 6).
   - Svaz $D_{30}$ a nekonečný svaz $(\mathbb{N} \setminus \{0\}, \mid)$ (CV1 Příklad 3).
3. **BLOK C (Drobné doplňky):**
   - Zvýraznění intentů v Rymon tree (CV2).
   - Gaussovská RBF transformace a pseudometrika (CV4).
