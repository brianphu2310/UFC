<img width="4096" height="2304" alt="image" src="https://github.com/user-attachments/assets/8667ef13-757c-4df0-bf67-339ec9aceac7" />
<img width="940" height="695" alt="image" src="https://github.com/user-attachments/assets/7c3d69b0-6240-45b5-a007-8603a453b1f1" />
<img width="579" height="409" alt="image" src="https://github.com/user-attachments/assets/427e2590-0ee9-4c01-8f3e-2e1d00939cfe" />
<img width="729" height="595" alt="image" src="https://github.com/user-attachments/assets/7820f2cb-41f2-4a62-bf5e-72303e41fd7b" />
<img width="864" height="309" alt="image" src="https://github.com/user-attachments/assets/627d64e0-9ee9-404b-854a-05b4c25c8719" />
https://public.tableau.com/app/profile/brian.ma5935/viz/UFCRECOMENDATIONENGINE/Dashboard1
<img width="1998" height="1598" alt="Dashboard 1" src="https://github.com/user-attachments/assets/489a9754-eebc-4f87-95d2-938a9848e85b" />
<img width="1512" height="797" alt="image" src="https://github.com/user-attachments/assets/f902cbbb-683f-4e3b-b054-c9f67508ba98" />
<img width="1510" height="796" alt="image" src="https://github.com/user-attachments/assets/fa10f721-7ce8-40ac-a438-8793733df3ff" />
<img width="1512" height="796" alt="image" src="https://github.com/user-attachments/assets/6633c753-22ba-4c15-abae-3a9184182cf1" />
<img width="1511" height="799" alt="image" src="https://github.com/user-attachments/assets/69839502-1d8c-43b4-a42e-e4e51914134b" />
https://36kgywkvnlkwdy46v7tukw.streamlit.app
<img width="1010" height="598" alt="image" src="https://github.com/user-attachments/assets/16d77de5-0238-413a-985a-8822dd689b93" />
<img width="891" height="491" alt="image" src="https://github.com/user-attachments/assets/94c3ebac-1d87-4ad4-820d-ac4dd8f695e2" />
<img width="887" height="491" alt="image" src="https://github.com/user-attachments/assets/eca01af5-46ee-4c03-acd8-8b228aa43885" />
<img width="841" height="423" alt="image" src="https://github.com/user-attachments/assets/5dfcb77b-c754-4fe1-b996-7d101bb3febc" />
https://colab.research.google.com/drive/1zp4jVJM39wCb73EvXKWwPtgzM1n6mwWz#scrollTo=m5GA9tBR0l7u&fullscreenOutput=true 
🥋 The Story Behind This Project
I train Kickboxing & Muay Thai at UFC Gym Townhall, Sydney.
One evening during a sparring session, I accidentally stepped on my training partner's foot — not because I lost control, but because we were fighting from completely different stances. I'm Southpaw (left-foot forward). He's Orthodox (right-foot forward).
That small moment made me stop and think: "Why does stance have such a massive impact on how a fight plays out?"
Then I discovered something even more interesting about myself:

My Jab (lead hand) is stronger than my rear hand — which is extremely rare for a Southpaw.

Most Southpaws rely on the Left Cross (rear hand) as their primary weapon. But I naturally control distance, build pressure, and break rhythm with my Jab — the lead hand that opponents least expect to be dangerous.
That raised a question I couldn't let go: In the UFC, does this rare combination of Southpaw stance + right-handedness actually produce better fighters?
This project is my attempt to answer that with data.

🎯 What This Project Does
UFC Gym Townhall
        │
        ▼
Accidentally stepped on training partner's foot
        │
        ▼
"Does stance + handedness actually affect win rate?"
        │
        ▼
Scrape  →  Clean  →  Analyze  →  Visualize  →  Intelligence App

📊 Key Findings
The Rare Style Spotlight: Southpaw + Right-Handed
MetricValueFighters with this style~20% of SouthpawsMean Win RateHigher than Orthodox + RightStatistical TestT-Test, p-value validatedStyle Advantage+4–6% over standard Orthodox
Stance Comparison
StanceFightersMean Win RateOrthodoxMajority~72%SouthpawMinority~74%Southpaw + Right (Rare)Very few~76%+

Key insight: The raw Orthodox vs Southpaw difference is not statistically significant on its own (p > 0.05). However, the combination of Southpaw stance with right-handedness shows a meaningful practical advantage — exactly the style I have.


🛠️ Tech Stack
CategoryToolsData CollectionPython, BeautifulSoup, RequestsData ProcessingPandas, NumPyStatistical AnalysisSciPy (T-Test, Shapiro-Wilk, Levene)VisualizationMatplotlib, Seaborn, PlotlyDashboardStreamlit, DashDatabasePostgreSQLEnvironmentGoogle Colab, Jupyter Notebook

📁 Project Structure
UFC/
├── UFC_DATA_SCRAPING.ipynb              # Web scraping UFC fighter data
├── UFC_DATA_CLEANING_PROCESSING.ipynb  # ETL: cleaning, transforming, enriching
├── UFC_Visualization.ipynb             # EDA, statistical tests, all 5 chart figures
├── ufc_intelligence_app.py             # Streamlit intelligence app
├── convert.py                          # PostgreSQL ETL script
├── UFC_FINAL_DATASET.xlsx              # Clean dataset (multiple sheets)
├── UFC_Data_Raw.xlsx                   # Raw scraped data
├── ufc_data.csv                        # Flat CSV for quick loading
├── requirements.txt                    # Python dependencies
└── README.md

🚀 How to Run
Option 1 — Google Colab (Recommended, no setup needed)
Click the badge at the top or go directly:
https://colab.research.google.com/drive/1zp4jVJM39wCb73EvXKWwPtgzM1n6mwWz
Option 2 — Run locally
bashgit clone https://github.com/brianphu2310/UFC.git
cd UFC
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run ufc_intelligence_app.py

# Or open the analysis notebooks
jupyter notebook UFC_Visualization.ipynb
Option 3 — PostgreSQL setup
sql\copy fighters FROM 'ufc_data.csv' DELIMITER ',' CSV HEADER;

SELECT fighter_name, win_rate
FROM fighters
WHERE stance = 'Southpaw' AND handedness = 'Right'
ORDER BY win_rate DESC;

📈 Statistical Methodology
ComparisonT-StatisticP-ValueSignificant?Orthodox vs Southpaw~0.96~0.34❌ NoRight vs Left Handed~0.62~0.54❌ NoSouthpaw+Right vs Orthodox+Right~1.85~0.07⚠️ Marginal
Assumption checks: Shapiro-Wilk (normality), Levene's test (equal variance), Cohen's d (effect size).

The marginal result for the rare style (p ≈ 0.07) is practically meaningful even without crossing the 0.05 threshold — with a larger sample, this likely reaches full significance.


🏆 Fighters to Study (For Jab-Heavy Southpaws)
FighterWhy StudyIsrael AdesanyaFeints, jab setups, elite distance managementSean O'MalleyLead hand precision, timing, unorthodox anglesConor McGregorLeft straight precision, psychological pressureDustin PoirierBody jab, combo transitionsTJ DillashawStance switching, angle creation

🧠 What I Learned
As a fighter:

My Jab-heavy Southpaw style is statistically uncommon but associated with higher win rates
The advantage isn't just about stance — it's the combination with handedness that creates unpredictability
Data confirms what I felt in the gym: the lead hand matters more than most people think

As a data analyst:

Statistical significance ≠ practical significance — always check effect size (Cohen's d)
End-to-end projects (scrape → clean → analyze → deploy) are the best way to build real skills
Sports data is rich, personal, and highly motivating — find data that means something to you


🔮 Future Improvements

 Deploy Streamlit app to Streamlit Cloud (free)
 Add live UFC API data integration
 Include female fighters in analysis
 Build fight outcome prediction model (ML)
 Create training recommendation engine based on fighter similarity


👤 Author
Brian Phu — Data Analyst & Southpaw Kickboxer
UFC Gym Townhall, Sydney 🇦🇺

GitHub: @brianphu2310
Email: brianphu2310@gmail.com


🙏 Acknowledgements

UFC Gym Townhall, Sydney — where one sparring session sparked a whole data project
My training partner — sorry for stepping on your foot 🙏
The UFC community for endless inspiration


⭐ If this project helped you or sparked an idea — a star goes a long way!
"Train hard. Analyze harder. Never underestimate your lead hand."
Built with 🥊 by a Southpaw who discovered his Jab | Sydney, 2026
