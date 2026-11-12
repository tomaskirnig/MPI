# Matematika pro informatiku – Cvičení 5 (Textové zadání)

Pojmy potřebné pro zvládnutí cvičení:
- metrický prostor, otevřená/uzavřená koule, sféra
- topologický prostor, otevřená a uzavřená množina, báze topologie
- indukovaná metrická topologie, metrizovatelnost
- vnitřek ($\operatorname{int}$), uzávěr ($\operatorname{cl}$), hranice ($\partial$)
- hromadný bod ($A'$), izolovaný bod ($\operatorname{Iso}(A)$)
- souvislost prostoru
- oddělovací axiomy ($T_0, T_1, T_2$)
- Pawlakova topologie (dolní aproximace $\underline{R}$, horní aproximace $\overline{R}$, oblast nejistoty $\operatorname{BN}_R$)
- spojité zobrazení

---

## Příklad 1: Eukleidovský prostor $(\mathbb{R}, d_2)$
Uvažujme eukleidovský metrický prostor $(\mathbb{R}, d_2)$ a jeho podmnožiny $A = (0, 2] \cup \{4\}$ a $B = \mathbb{Q} \cap [0, 1]$.
- **a)** Pro množinu $A$ určete její vnitřek $\operatorname{int}(A)$, uzávěr $\operatorname{cl}(A)$, hranici $\partial A$, množinu hromadných bodů $A'$ a množinu izolovaných bodů $\operatorname{Iso}(A)$.
- **b)** Určete stejné charakteristiky pro množinu $B$ (racionální čísla v intervalu $[0, 1]$).

| Množina | $\operatorname{int}(\cdot)$ | $\operatorname{cl}(\cdot)$ | $\partial(\cdot)$ | Hromadné body $(\cdot)'$ | Izolované body $\operatorname{Iso}(\cdot)$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $A = (0, 2] \cup \{4\}$ | | | | | |
| $B = \mathbb{Q} \cap [0, 1]$ | | | | | |

---

## Příklad 2: Konečný topologický prostor
Uvažujme konečnou množinu $X = \{a, b, c, d\}$ a na ní dvě různé topologie:
- $\tau_1 = \{\emptyset, \{a\}, \{c\}, \{a, c\}, \{a, b, c\}, X\}$
- $\tau_2 = \{\emptyset, \{a\}, \{b, c, d\}, X\}$

Dále uvažujme podmnožiny $M = \{b, c\}$ a $N = \{a, b, c\}$.
- **a)** Najděte všechny uzavřené množiny v prostorech $(X, \tau_1)$ a $(X, \tau_2)$.
- **b)** Určete vnitřek $\operatorname{int}(\cdot)$, uzávěr $\operatorname{cl}(\cdot)$ a hranici $\partial(\cdot)$ pro podmnožiny $M$ a $N$ v obou topologických prostorech.
- **c)** Určete minimální báze $\mathcal{B}_1$ a $\mathcal{B}_2$ pro obě topologie.
- **d)** Rozhodněte o souvislosti prostorů $(X, \tau_1)$ a $(X, \tau_2)$.

| Prostor a množina | $\operatorname{int}(\cdot)$ | $\operatorname{cl}(\cdot)$ | $\partial(\cdot)$ |
| :--- | :--- | :--- | :--- |
| $\tau_1 : M$ | | | |
| $\tau_1 : N$ | | | |
| $\tau_2 : M$ | | | |
| $\tau_2 : N$ | | | |

---

## Příklad 3: Pawlakova topologie (Rough sets)
Mějme množinu $U = \{1, 2, 3, 4, 5, 6\}$ a relaci ekvivalence $R$ definovanou rozkladem:
$$U/R = \{\{1, 2\}, \{3, 4, 5\}, \{6\}\}$$
Tato relace generuje Pawlakovu topologii $\tau_R$. Uvažujme podmnožiny $A = \{2, 3, 4\}$ a $B = \{1, 2, 3, 4\}$.
- **a)** Vypište bázi $\mathcal{B}_R$ i celou Pawlakovu topologii $\tau_R$.
- **b)** Určete vnitřek / dolní aproximaci $\operatorname{int}(\cdot) = \underline{R}(\cdot)$, uzávěr / horní aproximaci $\operatorname{cl}(\cdot) = \overline{R}(\cdot)$ a hranici / oblast nejistoty $\partial(\cdot) = \operatorname{BN}_R(\cdot)$ pro podmnožiny $A$ a $B$.
- **c)** Rozhodněte o souvislosti a metrizovatelnosti prostoru $(U, \tau_R)$. Které oddělovací axiomy ($T_0, T_1, T_2$) tento prostor splňuje?

| Množina | $\operatorname{int}(\cdot) = \underline{R}(\cdot)$ | $\operatorname{cl}(\cdot) = \overline{R}(\cdot)$ | $\partial(\cdot) = \operatorname{BN}_R(\cdot)$ |
| :--- | :--- | :--- | :--- |
| $A = \{2, 3, 4\}$ | | | |
| $B = \{1, 2, 3, 4\}$ | | | |

---

## Příklad 4: Oddělovací axiomy $T_0, T_1, T_2$ a metrizovatelnost
Rozhodněte o platnosti oddělovacích axiomů $T_0, T_1, T_2$ a metrizovatelnosti pro následující topologické prostory $(X, \tau)$:
- **a)** Indiskrétní prostor na $X = \{1, 2\}$ s $\tau = \{\emptyset, X\}$.
- **b)** Sierpińského prostor na $X = \{0, 1\}$ s $\tau = \{\emptyset, \{1\}, \{0, 1\}\}$.
- **c)** Kofinitní topologie na $X = \mathbb{R}$, kde otevřené množiny jsou $\emptyset$ a všechny $U \subseteq \mathbb{R}$ s konečným doplňkem.

---

## Příklad 5: Spojité zobrazení
Uvažujme zobrazení $f : (X, \tau_X) \to (Y, \tau_Y)$ mezi topologickými prostory. Rozhodněte o spojitosti zobrazení v následujících případech:
- **a)** $X = \{1, 2, 3\}$ s topologií $\tau_X = \{\emptyset, \{1\}, \{1, 2\}, X\}$ a $Y = \{a, b\}$ s topologií $\tau_Y = \{\emptyset, \{a\}, Y\}$.
  Zobrazení je definováno předpisem $f(1) = a, f(2) = a, f(3) = b$.
- **b)** Identické zobrazení $\operatorname{id} : (\mathbb{R}, \tau_{\text{diskr}}) \to (\mathbb{R}, \tau_{\text{std}})$, které zobrazuje reálnou osu s diskrétní topologií na reálnou osu se standardní eukleidovskou topologií.
- **c)** Identické zobrazení $\operatorname{id} : (\mathbb{R}, \tau_{\text{std}}) \to (\mathbb{R}, \tau_{\text{diskr}})$.
