# 🧠 Domácí úkol 1: Formální konceptuální analýza (FCA) & Asociační pravidla

> [!IMPORTANT]
> **Rychlý přehled pro netrpělivé (TL;DR):**
> Tento program bere **fuzzy matici** (desetinná čísla $[0, 1]$ vyjadřující vztah objektů a atributů), převede ji podle prahu $f$ na **binární matici** (0/1), najde všechny **formální koncepty** s dostatečnou podporou ($\ge s$) a vygeneruje všechna **100% jistá asociační pravidla** ($\text{conf} = 1$).

---

## 🚦 Vizuální přehled toku dat (Pipeline)

```
[Vstup: Fuzzy Matice] 
       │
       ▼ (práh f)
[Binární kontext (0 / 1)] 
       │
       ├───► [Algoritmus Close-by-One (CbO)] ───► Koncepty (Extent, Intent) [supp >= s]
       │
       └───► [DFS Rymon / Apriori strom]    ───► Asociační pravidla (X => Y) [conf = 1, supp >= s]
```

---

## 🎯 Co přesně děláme a proč?

### 1️⃣ Binarizace ($\alpha$-řez)
* **Proč:** Fuzzy matice obsahuje reálná čísla $[0, 1]$ (např. váha relevance nebo pravděpodobnost).
* **Jak:** Pro zadaný fuzzy práh $f$ řekneme:
  $$\text{objekt } i \text{ má atribut } j \iff \text{hodnota}_{i,j} \ge f$$
* **Výsledek:** Obyčejná tabulka s křížky (True/False).

---

### 2️⃣ Formální koncepty (FCA)
Koncept je stabilní dvojice $(A, B)$:
* 📦 **Extent ($A$):** Množina všech objektů, které sdílejí všechny atributy z $B$.
* 🏷️ **Intent ($B$):** Množina všech atributů, které jsou společné všem objektům z $A$.
* 🧮 **Podpora (Support):** Relativní velikost extentu:
  $$\text{supp}(A, B) = \frac{|A|}{N}$$
* 🎯 **Cíl:** Vypsat všechny koncepty, kde $\text{supp}(A, B) \ge s$.

> [!NOTE]
> Extent i intent mohou být prázdné $(\emptyset)$. Prázdná množina se tiskne jako `{}`.

---

### 3️⃣ Asociační pravidla ($X \Rightarrow Y$)
Hledáme implikace mezi atributy: *"Když má objekt vlastnosti $X$, má zaručeně i vlastnosti $Y$."*

* 🛑 **Podmínky:**
  1. $X \neq \emptyset$, $Y \neq \emptyset$ (obě strany neprázdné).
  2. $X \cap Y = \emptyset$ (disjunktní množiny).
  3. $|X^\downarrow| > 0$ (antecedent musí splňovat aspoň jeden objekt, jinak je spolehlivost nedefinovaná).
  4. $\text{supp}(X \Rightarrow Y) = \frac{|(X \cup Y)^\downarrow|}{N} \ge s$.
  5. $\text{conf}(X \Rightarrow Y) = \frac{|(X \cup Y)^\downarrow|}{|X^\downarrow|} = 1.0$ (100% spolehlivost).

> [!TIP]
> **Klíčový matematický trik (Aha! moment):**
> Kdy je $\text{conf}(X \Rightarrow Y) = 1$? 
> Právě tehdy, když **všechny objekty mající $X$ mají současně i $Y$** $\iff (X \cup Y)^\downarrow = X^\downarrow$.
> To znamená, že $Y$ musí být neprázdnou podmnožinou **uzávěru** $X$:
> $$Y \subseteq \text{cl}(X) \setminus X, \quad \text{kde } \text{cl}(X) = X^{\downarrow\uparrow}$$
> Díky tomu nemusíme testovat nesmyslné kombinace – díváme se jen na atributy z uzávěru!

---

## 🛠️ Jak a proč je to implementováno (Volba algoritmů)

| Komponenta | Použitý algoritmus | Proč právě tento? (Senior Lazy / Ponytail pohled) |
| :--- | :--- | :--- |
| **Generování konceptů** | **Close-by-One (CbO)** | • Generuje každý koncept **přesně jednou** (žádné duplicity).<br>• Kanonický test zamezuje zbytečnému procházení.<br>• Extrémně krátký, přehledný kód (cca 15 řádků). |
| **Generování pravidel** | **Prefixový DFS strom (Apriori pruning)** | • Prochází jen frekventované levé strany $X$.<br>• Pokud $X$ nemá podporu $\ge s$, okamžitě **odřízne celou větev** (apriori vlastnost).<br>• Z uzávěru $\text{cl}(X)$ vygeneruje kombinace $Y$. |
| **Reprezentace dat** | **Množiny (`set`), n-tice (`tuple`)** | • Standardní knihovna Pythonu bez externích závislostí.<br>• Žádná obskurní syntax, čistý a čitelný kód. |

---

## 🔍 Detailní průchod algoritmy

### 🔹 Algoritmus 1: Close-by-One (CbO)
```python
def cbo(extent, intent, start_attr):
    if len(extent) / num_objects >= s_thresh:
        concepts.append((extent, intent))
    
    for j in range(start_attr, num_attributes):
        if j in intent:
            continue
        new_extent = extent & attr_objs[j]
        new_intent = up(new_extent)
        
        # Kanonický test: nepřidali jsme atribut s menším indexem než j?
        if all(k >= j or k in intent for k in new_intent):
            cbo(new_extent, new_intent, j + 1)
```

> [!TIP]
> **Proč kanonický test funguje?**
> Zaručuje, že do stejného konceptu dojdeme pouze po jedné jediné kanonické cestě v rekurzivním stromu. Žádné ukládání navštívených konceptů do hashmapy, nulová paměťová režie!

---

### 🔹 Algoritmus 2: Generování pravidel přes uzávěry
```python
def find_rules(curr_X, curr_ext, start):
    if curr_X:
        closure = up(curr_ext)           # Uzávěr cl(X)
        diff = sorted(closure - set(curr_X))
        if diff:
            # Všechny neprázdné podmnožiny Y z diff mají conf = 1
            for r in range(1, len(diff) + 1):
                for Y in combinations(diff, r):
                    rules.append((curr_X, Y))
                    
    for j in range(start, num_attributes):
        new_ext = curr_ext & attr_objs[j]
        # Prořezávání: levá strana musí mít >= 1 objekt a podporu >= s
        if len(new_ext) > 0 and len(new_ext) / num_objects >= s_thresh:
            find_rules(curr_X + (j,), new_ext, j + 1)
```

---

## 📐 Řazení výstupu (Přísně dle zadání)

### 📌 Koncepty:
1. Vzestupně dle velikosti extentu $|A|$: `len(extent)`.
2. Při rovnosti lexikograficky dle číselných indexů extentu.
* 👉 V Pythonu jednoduše: `key=lambda c: (len(c[0]), sorted(c[0]))`

### 📌 Asociační pravidla:
1. Vzestupně dle počtu atributů na levé straně $|X|$.
2. Při rovnosti lexikograficky dle $X$.
3. Při shodném $X$ vzestupně dle počtu atributů na pravé straně $|Y|$.
4. Při rovnosti lexikograficky dle $Y$.
* 👉 V Pythonu jednoduše: `key=lambda r: (len(r[0]), r[0], len(r[1]), r[1])`

---

## 🚀 Jak projekt spustit a otestovat

### 1. Spuštění hlavního programu:
```bash
python main.py < vstup.txt
```
nebo v PowerShellu:
```powershell
Get-Content vstup.txt | python main.py
```

### 2. Spuštění automatického testu (ověření proti sample datům):
```bash
python test_du1.py
```
> Výstup: `All tests passed!` ✅

---

## 🗃️ Souborová struktura v `DU1/`

* 📄 [`main.py`](file:///C:/Users/tomki/Desktop/Ing_wannabe/Matika/MPI/DU1/main.py) – Samotná implementace (čistý Python, standardní knihovny).
* 🧪 [`test_du1.py`](file:///C:/Users/tomki/Desktop/Ing_wannabe/Matika/MPI/DU1/test_du1.py) – Samostatný ověřovací test na vzorovém vstupu/výstupu.
* 📝 [`zadani.txt`](file:///C:/Users/tomki/Desktop/Ing_wannabe/Matika/MPI/DU1/zadani.txt) – Původní zadání úlohy.
* 📖 [`README.md`](file:///C:/Users/tomki/Desktop/Ing_wannabe/Matika/MPI/DU1/README.md) – Tento dokument s popisem architektury.
