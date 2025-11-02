# 📊 Analiză Exploratorie de Date (EDA) — Proiect Python

Acest proiect realizează o **analiză exploratorie de date (EDA)** asupra unor seturi de date economice, utilizând Python și librării pentru procesare, statistică și vizualizare.  
Sunt generate automat grafice, statistici descriptive și analize de corelație între indicatori economici.

---

## 🧠 Scopul proiectului

Proiectul permite:
- Citirea și preprocesarea automată a datelor din fișiere Excel.
- Analiza **univariată** (pentru o singură variabilă).
- Analiza **bivariată** (relații între variabile).
- Vizualizarea datelor prin grafice: histograme, boxplot, densitate, scatter, heatmap.

---

## 🧩 Librării folosite

| Librărie | Descriere |
|-----------|------------|
| `pandas` | Manipulare și analiză de date (citirea fișierelor Excel, lucrul cu DataFrame-uri). |
| `numpy` | Operații numerice și statistice eficiente. |
| `matplotlib.pyplot` | Crearea graficelor simple (histograme, scatter, boxplot etc.). |
| `seaborn` | Bibliotecă de vizualizare statistică bazată pe Matplotlib, cu design modern. |
| `sklearn.preprocessing.StandardScaler` | Normalizează datele (medie = 0, deviație standard = 1). |
| `os` | Gestionarea fișierelor și directoarelor locale. |
| `enum.Enum` | Definirea enumerărilor (în cazul nostru, selectarea dataset-ului). |

---

## ⚙️ Structura principală a codului

### 🔹 `main(dataset: Dataset)`
Punctul de pornire al proiectului.  
Alege fișierul Excel în funcție de dataset, citește datele, face analiza univariată și bivariată.

---

### 🔹 `read_file(path, started, finished)`
Citește și curăță fișierul Excel:
- Transpune tabelele pentru ca fiecare indicator să devină o coloană.  
- Filtrează datele între anii specificați (ex: 2000–2024).  
- Elimină valorile lipsă.

---

### 🔹 `get_zero_code(data)`
Aplică **scalarea standard** (StandardScaler) pentru a normaliza variabilele numerice.

---

### 🔹 `univariate_analysis(data, column_name)`
Analizează o singură variabilă:  
- Desenează histograma, boxplotul și densitatea distribuției.  
- Afișează statistici descriptive (min, max, medie, mediană, percentilă).

---

### 🔹 `bivariate_analysis(data)`
Analizează relațiile dintre toate variabilele:  
- Creează scatter plots multiple (valoarea vs. timp).  
- Creează o hartă de corelație (heatmap).

---

### 🔹 `plot_histogram_seaborn(data, column_name)`
Desenează o histogramă pentru distribuția valorilor unei coloane.

### 🔹 `plot_box_plot_seaborn(data, column_name)`
Creează un **boxplot** pentru a evidenția valorile extreme.

### 🔹 `plot_density_plot(data, column_name)`
Desenează o **curbă de densitate (KDE)** a distribuției datelor.

### 🔹 `scatter_plots_multi(data)`
Creează un **scatter plot multiplu** pentru a observa evoluția în timp a mai multor indicatori.

### 🔹 `get_info(df, column_name)`
Afișează informații statistice despre o coloană (min, max, medie, mediană etc.) și un scatter plot.

### 🔹 `get_heat_map(data)`
Generează o **hartă de corelație (heatmap)** cu coeficienții Pearson între toate variabilele numerice.

---

## 📂 Structura proiectului

```bash
project/
│
├── get_data/
│   ├── get_data.py
│   ├── get_info.py
│   ├── draw_graph.py
│
├── data/
│   ├── dataset_1.xlsx
│   ├── dataset_2.xlsx
│   ├── dataset_3.xlsx
│
├── Dataset.py
├── main.py
└── README.md
