# UFC Stance Intelligence — The Southpaw Who Discovered His Jab

<img width="4096" height="2304" alt="image" src="https://github.com/user-attachments/assets/8667ef13-757c-4df0-bf67-339ec9aceac7" />

---

## The Story — How a Sparring Accident Became a Data Project

### Sydney, UFC Gym Townhall — One evening, during sparring

I train Kickboxing & Muay Thai here. Not to compete professionally. Just because I am addicted to the feeling of stepping onto the mats every night.

That evening, I was sparring with a partner. Everything was normal… until I accidentally stepped on his foot.

> Not because I lost control. But because we were standing in completely different stances.

I stand **Southpaw** (right foot forward). He stands **Orthodox** (left foot forward). Two different angles. Two different ways of moving. And that accidental step made me stop and actually think:

*"Wait — does stance really affect a fight this much?"*

---

### Then I realized something even stranger

I went home, shadowboxing in front of the mirror. And then it hit me:

> **My Jab (lead hand) is significantly stronger than my rear hand.**

For a Southpaw, that is not supposed to happen.

Most Southpaws — Conor McGregor, Alex Pereira, Israel Adesanya — their nuclear weapon is the Left Cross (rear hand). That is their KO punch.

But me? I hurt people with my **Jab**.

I control distance with it. I set up combinations with it. I have stunned training partners with just my Jab — the punch nobody expects to be dangerous from a Southpaw.

---

### That curiosity built this entire project

I had to know:

- How rare is my fighting style?
- Do any pro fighters fight like me?
- Does the data actually show an advantage?

So I stopped just training. I started **analyzing**.
UFC Gym Townhall
│
▼
Accidentally stepped on training partner's foot
│
▼
"Southpaw vs Orthodox — what does the data say?"
│
▼
"Does combo of stance and handedness matter?"
│
▼
Web Scrape → Clean → Analyze → Dashboard → Deploy

text

This project is my journey from **curious fighter** to **data-driven fighter**.

---

## What I Found — The Data Does Not Lie

### The Rare Style: Right-handed Southpaw

| Metric | Value |
|--------|-------|
| Fighters with this style | 23 / 117 (19.6%) |
| Mean Win Rate | 74.3% |
| Advantage vs Orthodox+Right | +4.2% |
| Top performer | Sean O'Malley (94.4% WR) |

### Stance Comparison

| Group | Fighters | Mean Win Rate |
|-------|----------|---------------|
| Orthodox | 93 | 72.1% |
| Southpaw | 24 | 73.8% |
| Difference | | +1.7% |

### Statistical Test Results

| Comparison | T-Statistic | P-Value | Significant |
|------------|-------------|---------|-------------|
| Orthodox vs Southpaw | 0.96 | 0.34 | No |
| Right-handed vs Left-handed | 0.62 | 0.54 | No |
| Southpaw+Right vs Orthodox+Right | 1.85 | 0.07 | Marginal |

### Effect Size (Cohen's d)

| Comparison | Cohen's d | Interpretation |
|------------|-----------|----------------|
| Orthodox vs Southpaw | 0.21 | Small effect |
| Right vs Left handed | 0.15 | Negligible |
| Southpaw+Right vs Orthodox+Right | 0.43 | Small-Medium (practical advantage) |

> **Bottom line:** Being Southpaw alone does not guarantee anything. But being a Right-handed Southpaw — that rare combo — shows a real, measurable edge in the data.

And that is exactly my style.

---

## Complete Data Pipeline

| Stage | Tools | Output |
|-------|-------|--------|
| **1. Web Scraping** | BeautifulSoup, Requests | Raw fighter data |
| **2. Data Cleaning** | Pandas, NumPy | Cleaned dataset |
| **3. Export to Excel** | Pandas | `UFC_FINAL_DATASET.xlsx` |
| **4. Statistical Analysis** | SciPy (T-Test, Levene, Shapiro-Wilk) | p-values, effect sizes |
| **5. Panel Dashboard** | Panel, HoloViews, Plotly | Interactive analytics dashboard |
| **6. Streamlit App** | Streamlit (reads directly from .xlsx) | Fighter recommender + map |
| **7. PostgreSQL Database** | `convert.py`, `psql` | Stored procedure `match_fighters()` |
| **8. Tableau Dashboard** | Tableau Public (reads from CSV) | Geographic & performance viz |

### Project Files

| File | Purpose |
|------|---------|
| `UFC_DATA_SCRAPING.ipynb` | Web scraping from UFC stats |
| `UFC_DATA_CLEANING_PROCESSING.ipynb` | Clean & standardize data |
| `UFC_FINAL_DATASET.xlsx` | Master Excel file (used by Streamlit) |
| `UFC_Visualization.ipynb` | EDA + T-Tests + Cohen's d |
| `ufc_panel_dashboard.py` | Panel dashboard (3 tabs) |
| `ufc_intelligence_app.py` | Streamlit app (reads .xlsx directly) |
| `convert.py` | ETL: Excel → PostgreSQL |
| `ufc_data.csv` | Exported for Tableau |
| `insert_data.sql` | PostgreSQL INSERT statements |

---

## Who I Should Study (According to the Data)

| Fighter | Win Rate | Weight Class | Why They Match My Style |
|---------|----------|--------------|-------------------------|
| Sean O'Malley | 94.4% | Bantamweight | Distance control, lead hand precision |
| Israel Adesanya | 88.9% | Middleweight | Feints, jab setups, counter striking |
| Dustin Poirier | 78.4% | Lightweight | Boxing combinations, body jab |
| Conor McGregor | 78.6% | Lightweight | Left hand precision, timing |
| TJ Dillashaw | 77.3% | Bantamweight | Stance switching, angle creation |

---

## Tech Stack

| Category | Technologies |
|----------|--------------|
| Web Scraping | BeautifulSoup, Requests |
| Data Processing | Python, Pandas, NumPy |
| Statistical Analysis | SciPy (T-Test, Levene, Shapiro-Wilk) |
| Dashboard | Panel, HoloViews, Plotly |
| Web App | Streamlit, Scikit-learn (KNN) |
| Database | PostgreSQL |
| BI Visualization | Tableau Public |
| Environment | Jupyter Notebook, Google Colab |

---

## Live Demos

| Platform | Link |
|----------|------|
| Streamlit App |[Streamlit] [[https://36kgywkvnlkwdy46v7tukw.streamlit.app](https://36kgywkvnlkwdy46v7tukw.streamlit.app)] |
| Google Colab | [Open Notebook][[https://colab.research.google.com/drive/1zp4jVJM39wCb73EvXKWwPtgzM1n6mwWz](https://colab.research.google.com/drive/1zp4jVJM39wCb73EvXKWwPtgzM1n6mwWz)] |
| Tableau Public | [View Dashboard][[https://public.tableau.com/app/profile/brian.ma5935/viz/UFCRECOMENDATIONENGINE/Dashboard1](https://public.tableau.com/app/profile/brian.ma5935/viz/UFCRECOMENDATIONENGINE/Dashboard1)] |

---

## How to Use — No Installation Required

Just click the links below. Everything runs in your browser.

| Platform | Link | What It Does |
|----------|------|--------------|
| **Streamlit App** | [Launch App](https://36kgywkvnlkwdy46v7tukw.streamlit.app) | Fighter recommender + map |
| **Tableau Public** | [View Dashboard](https://public.tableau.com/app/profile/brian.ma5935/viz/UFCRECOMENDATIONENGINE/Dashboard1) | Interactive stance analytics |
| **Google Colab** | [Open Notebook](https://colab.research.google.com/drive/1zp4jVJM39wCb73EvXKWwPtgzM1n6mwWz) | Full Python analysis (T-Tests, visualizations) |

No terminal. No dependencies. Just click and explore.

## How to Use — No Installation Required

Just click the links below. Everything runs in your browser.

---

### 1. Streamlit App — Fighter Recommender

**Link:** [https://36kgywkvnlkwdy46v7tukw.streamlit.app](https://36kgywkvnlkwdy46v7tukw.streamlit.app)

**What you can do:**
- Enter your height, reach, weight, stance, and handedness
- Click "Find My Fighter Twin"
- See your Top 5 similar fighters with match scores
- View interactive map showing where your fighter twins come from
- Compare yourself to Brian (Southpaw profile)

---

### 2. Tableau Public Dashboard — Stance Intelligence Report

**Link:** [https://public.tableau.com/app/profile/brian.ma5935/viz/UFCRECOMENDATIONENGINE/Dashboard1](https://public.tableau.com/app/profile/brian.ma5935/viz/UFCRECOMENDATIONENGINE/Dashboard1)

**What you can do:**
- Filter fighters by stance (Orthodox / Southpaw)
- Filter by handedness (Right / Left)
- Explore win rate distributions by continent
- See top fighters by weight class
- Analyze performance patterns across different stances

---

### 3. Google Colab — Full Analysis + Panel Dashboard

**Link:** [https://colab.research.google.com/drive/1zp4jVJM39wCb73EvXKWwPtgzM1n6mwWz](https://colab.research.google.com/drive/1zp4jVJM39wCb73EvXKWwPtgzM1n6mwWz)

**What you can do inside the Colab notebook:**

| Section | What it contains |
|---------|------------------|
| **Data Loading** | Load and clean UFC fighter data |
| **Statistical Tests** | T-Tests, Cohen's d, Shapiro-Wilk, Levene's test |
| **Panel Dashboard** | 3-tab interactive dashboard (Recommendations, Statistics, Geography) |
| **Visualizations** | Distribution plots, box plots, bar charts |

**How to use:**
1. Open the Colab link
2. Click "Runtime" → "Run all"
3. Scroll down to see the Panel dashboard rendered inline
4. Explore the 3 tabs: Recommendations, Statistics, Geography

---

## Quick Summary

| Platform | Best for | Link |
|----------|----------|------|
| Streamlit App | Finding your fighter twin | [Launch](https://36kgywkvnlkwdy46v7tukw.streamlit.app) |
| Tableau Public | Stance performance analysis | [View](https://public.tableau.com/app/profile/brian.ma5935/viz/UFCRECOMENDATIONENGINE/Dashboard1) |
| Google Colab | Running statistics + Panel dashboard | [Open](https://colab.research.google.com/drive/1zp4jVJM39wCb73EvXKWwPtgzM1n6mwWz) |
Brian Phu — Data Analyst & Southpaw Kickboxer at UFC Gym Townhall, Sydney

## Screenshots & Demo

Below are screenshots of each component in action.

*Excel Dataset:*
<img width="940" height="695" alt="image" src="https://github.com/user-attachments/assets/7c3d69b0-6240-45b5-a007-8603a453b1f1" />

*Pivot Table:*
<img width="579" height="409" alt="image" src="https://github.com/user-attachments/assets/427e2590-0ee9-4c01-8f3e-2e1d00939cfe" />

*Country and Contient BreakDown by Vlookup:*
<img width="729" height="595" alt="image" src="https://github.com/user-attachments/assets/7820f2cb-41f2-4a62-bf5e-72303e41fd7b" />

*My Group Stats:*
<img width="864" height="309" alt="image" src="https://github.com/user-attachments/assets/627d64e0-9ee9-404b-854a-05b4c25c8719" />



---

### 1. Streamlit App — Fighter Recommender

**Live link:** [https://36kgywkvnlkwdy46v7tukw.streamlit.app](https://36kgywkvnlkwdy46v7tukw.streamlit.app)

| What | Screenshot |
|------|------------|
| Main interface | <img width="1512" height="800" alt="image" src="https://github.com/user-attachments/assets/a35db876-8bb3-4b53-8162-a438f15186ac" />|
| Similar fighters results | <img width="1510" height="799" alt="image" src="https://github.com/user-attachments/assets/2e0600f3-f007-4825-9b37-f39afd9bac0c" />|
| Tips you can learn form your twins | <img width="1512" height="798" alt="image" src="https://github.com/user-attachments/assets/939d02e7-2ef8-4f70-8988-c9530f9cbcf9" />|
| Geographic map | <img width="1512" height="589" alt="image" src="https://github.com/user-attachments/assets/37efe6db-5a29-4fc6-b0aa-de1cfe8d2709" />|

*Example:*
<img width="1512" height="799" alt="image" src="https://github.com/user-attachments/assets/aef9f540-f53a-404e-8ac0-1af200cfe407" />

---

### 2. Tableau Public Dashboard

**Live link:** [https://public.tableau.com/app/profile/brian.ma5935/viz/UFCRECOMENDATIONENGINE/Dashboard1](https://public.tableau.com/app/profile/brian.ma5935/viz/UFCRECOMENDATIONENGINE/Dashboard1)

| What | Screenshot |
|------|------------|
| Full dashboard view | <img width="1508" height="1208" alt="image" src="https://github.com/user-attachments/assets/268b66d5-6364-42a4-a394-16baa093bc16" />|

<img width="751" height="601" alt="image" src="https://github.com/user-attachments/assets/83e56f17-36bc-40eb-8ab6-174342da35f6" />

---

### 3. Google Colab — Data Analysis + Panel Dashboard

**Live link:** [https://colab.research.google.com/drive/1zp4jVJM39wCb73EvXKWwPtgzM1n6mwWz](https://colab.research.google.com/drive/1zp4jVJM39wCb73EvXKWwPtgzM1n6mwWz)

| What | Screenshot |
|------|------------|
| Notebook overview | <img width="1010" height="598" alt="image" src="https://github.com/user-attachments/assets/16d77de5-0238-413a-985a-8822dd689b93" /> |
| Statistical test results | <img width="891" height="491" alt="image" src="https://github.com/user-attachments/assets/94c3ebac-1d87-4ad4-820d-ac4dd8f695e2" /> |
| Panel dashboard (Recommendations tab) | <img width="887" height="491" alt="image" src="https://github.com/user-attachments/assets/eca01af5-46ee-4c03-acd8-8b228aa43885" /> |
| Panel dashboard (Statistics tab) | <img width="841" height="423" alt="image" src="https://github.com/user-attachments/assets/5dfcb77b-c754-4fe1-b996-7d101bb3febc" /> |

---

### 4. Raw Data Preview

<img width="1512" height="982" alt="image" src="https://github.com/user-attachments/assets/f0c2019b-1856-41bc-97a9-3b7fce3c9cc9" />

### 5. Scraping From UFCSTATS.COM

<img width="1512" height="860" alt="image" src="https://github.com/user-attachments/assets/e2fab404-ba98-4e53-ad42-8535ae940755" />


---

## Where to Find Everything

| Component | Screenshot section | Live Link |
|-----------|-------------------|-----------|
| Streamlit App | Section 1 | [Link](https://36kgywkvnlkwdy46v7tukw.streamlit.app) |
| Tableau Dashboard | Section 2 | [Link](https://public.tableau.com/app/profile/brian.ma5935/viz/UFCRECOMENDATIONENGINE/Dashboard1) |
| Colab + Panel | Section 3 | [Link](https://colab.research.google.com/drive/1zp4jVJM39wCb73EvXKWwPtgzM1n6mwWz) |
| Raw Data | Section 4 | - |
GitHub: brianphu2310
Tableau: brian.ma5935
Train hard. Analyze harder. Never underestimate your lead hand.

License

MIT License — free to use, modify, and share.

Built from a Southpaw who discovered his Jab

Last updated: May 2026 | Fighters analyzed: 117 | Dashboards: 3 (Streamlit, Panel, Tableau) | One curious fighter

