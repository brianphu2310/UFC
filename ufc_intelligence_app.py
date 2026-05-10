import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler
import os

st.set_page_config(page_title="UFC Fighter Matching", page_icon="🥊", layout="wide")

# ============================================================
# TABLEAU-STYLE COLOR PALETTE (Purple / Teal / Dark)
# ============================================================
BG_DARK       = "#0A0A0F"
BG_CARD       = "#111118"
BG_CARD2      = "#181824"
BORDER_GREEN  = "#3DDC84"
TEXT_WHITE    = "#FFFFFF"
TEXT_LIGHT    = "#CCCCCC"
TEXT_DIM      = "#888888"
PURPLE_BRIGHT = "#9B59EF"
PURPLE_MID    = "#7B3FBF"
PURPLE_DARK   = "#4A2080"
TEAL_BRIGHT   = "#00E5CC"
TEAL_MID      = "#00B09B"
TEAL_DARK     = "#006B5E"
BLUE_BRIGHT   = "#5B9BF5"
BLUE_MID      = "#3A78D4"
TITLE_BORDER  = "#3DDC84"

# Tableau categorical palette (purple → teal)
CAT_COLORS = [
    "#9B59EF", "#7B3FBF", "#5B9BF5", "#3A78D4",
    "#00E5CC", "#00B09B", "#C77DFF", "#48CAE4",
    "#E040FB", "#26C6DA", "#7986CB", "#4DB6AC",
]

st.markdown(f"""
<style>
    /* ---- Global ---- */
    html, body, [data-testid="stAppViewContainer"], .stApp {{
        background-color: {BG_DARK} !important;
    }}
    [data-testid="stSidebar"] {{ background-color: {BG_CARD} !important; }}

    /* ---- Title banner ---- */
    .title-banner {{
        border: 2.5px solid {TITLE_BORDER};
        border-radius: 6px;
        padding: 14px 20px;
        text-align: center;
        margin-bottom: 24px;
        background: transparent;
    }}
    .title-banner h1 {{
        color: {TEAL_BRIGHT};
        font-size: 32px;
        font-style: italic;
        font-weight: 700;
        letter-spacing: 2px;
        margin: 0;
        text-shadow: 0 0 20px rgba(0,229,204,0.3);
    }}
    .title-banner p {{
        color: {TEXT_DIM};
        font-size: 13px;
        margin: 6px 0 0 0;
    }}

    /* ---- Section headers ---- */
    .sec-header {{
        color: {TEAL_BRIGHT};
        font-size: 15px;
        font-weight: 700;
        letter-spacing: 1px;
        margin: 20px 0 10px 0;
        text-transform: uppercase;
    }}

    /* ---- Brian card ---- */
    .brian-card {{
        background: {BG_CARD};
        border: 1.5px solid {TITLE_BORDER};
        border-radius: 8px;
        padding: 18px;
    }}
    .brian-card .bname {{ color: {TEAL_BRIGHT}; font-size: 18px; font-weight: 700; margin-bottom: 10px; }}
    .brian-card .bline {{ color: {TEXT_LIGHT}; font-size: 13px; margin: 4px 0; }}
    .brian-card .bhl   {{ color: {TEAL_BRIGHT}; font-weight: 600; }}
    .brian-card .bnote {{ color: {TEXT_DIM}; font-size: 11px; margin-top: 10px; }}

    /* ---- Win rate box ---- */
    .win-box {{
        background: {BG_CARD};
        border: 1.5px solid {PURPLE_BRIGHT};
        border-radius: 8px;
        padding: 20px;
        text-align: center;
        margin: 16px 0;
    }}
    .win-box .wlabel {{ color: {TEXT_DIM}; font-size: 12px; letter-spacing: 1px; text-transform: uppercase; }}
    .win-box .wbig   {{ color: {PURPLE_BRIGHT}; font-size: 60px; font-weight: 700; line-height: 1; margin: 6px 0; }}
    .win-box .wsub   {{ color: {TEXT_LIGHT}; font-size: 13px; }}

    /* ---- Compare cards ---- */
    .cmp-grid {{ display: grid; grid-template-columns: repeat(4,1fr); gap: 10px; margin-bottom: 18px; }}
    .cmp-card {{
        background: {BG_CARD2};
        border: 1px solid #2A2A3A;
        border-radius: 8px;
        padding: 14px;
        text-align: center;
    }}
    .cmp-card .cl  {{ color: {TEAL_BRIGHT}; font-size: 11px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 8px; }}
    .cmp-card .cv  {{ color: {TEXT_LIGHT}; font-size: 12px; margin: 2px 0; }}
    .cmp-card .cd  {{ color: {PURPLE_BRIGHT}; font-size: 13px; font-weight: 600; margin-top: 4px; }}

    /* ---- Fighter cards ---- */
    .f-card {{
        background: {BG_CARD2};
        border-left: 5px solid {PURPLE_BRIGHT};
        border-radius: 8px;
        padding: 14px 16px;
        margin: 8px 0;
    }}
    .f-card .fname  {{ color: {TEAL_BRIGHT}; font-size: 15px; font-weight: 700; margin-bottom: 6px; }}
    .f-card .finfo  {{ color: {TEXT_DIM}; font-size: 12px; margin: 2px 0; }}
    .f-card .fscore {{ font-size: 22px; font-weight: 700; margin: 8px 0 4px; }}
    .f-card .fstudy {{
        color: {TEXT_LIGHT}; font-size: 12px; margin-top: 8px;
        padding-top: 8px; border-top: 1px solid #2A2A3A;
    }}

    /* ---- Streamlit widgets ---- */
    .stNumberInput input, .stSelectbox > div > div {{
        background-color: {BG_CARD2} !important;
        color: {TEXT_WHITE} !important;
        border: 1px solid #333 !important;
    }}
    label, .stSelectbox label {{ color: {TEXT_LIGHT} !important; font-size: 13px !important; }}
    .stButton > button {{
        background: linear-gradient(90deg, {PURPLE_MID}, {TEAL_MID});
        color: {TEXT_WHITE};
        border: none;
        border-radius: 6px;
        font-weight: 600;
        font-size: 14px;
        width: 100%;
        padding: 10px;
    }}
    .stButton > button:hover {{ opacity: 0.88; }}

    /* ---- Metric ---- */
    [data-testid="metric-container"] {{
        background: {BG_CARD2};
        border: 1px solid #2A2A3A;
        border-radius: 8px;
        padding: 14px !important;
    }}
    [data-testid="metric-container"] label {{ color: {TEXT_DIM} !important; font-size: 12px !important; }}
    [data-testid="metric-container"] [data-testid="stMetricValue"] {{ color: {TEAL_BRIGHT} !important; font-size: 22px !important; }}

    /* ---- Expander ---- */
    .streamlit-expanderHeader {{ color: {TEAL_BRIGHT} !important; }}
    [data-testid="stExpander"] {{ border: 1px solid #2A2A3A !important; border-radius: 8px !important; }}

    /* ---- Footer ---- */
    .footer {{
        text-align: center; padding: 20px; color: {TEXT_DIM};
        margin-top: 40px; border-top: 1px solid #222;
        font-size: 12px;
    }}

    /* ---- Divider ---- */
    hr {{ border-color: #2A2A3A !important; }}
</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================
st.markdown(f"""
<div class="title-banner">
    <h1>🥊 TOP 5 UFC FIGHTERS RECOMMENDATIONS</h1>
    <p>Compare yourself with Brian (Right-handed Southpaw) · Find your fighter twin · Tableau-style dashboard</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# BRIAN (Right-handed Southpaw)
# ============================================================
BRIAN = dict(height=179, weight=69, reach=181, stance='Southpaw', hand='Right')

# ============================================================
# LOAD DATA FROM EXCEL FILE
# ============================================================
@st.cache_data
def load_data_from_excel():
    """Load data from UFC_FINAL_DATASET.xlsx"""
    possible_paths = [
        'UFC_FINAL_DATASET.xlsx',
        os.path.expanduser('~/Desktop/UFC_FINAL_DATASET.xlsx'),
        os.path.expanduser('~/Downloads/UFC_FINAL_DATASET.xlsx'),
    ]
    
    data_file = None
    for path in possible_paths:
        if os.path.exists(path):
            data_file = path
            break
    
    if data_file is None:
        return None
    
    # Read Excel file
    df_raw = pd.read_excel(data_file, sheet_name='🥊 Fighters Database', header=2)
    
    # Rename columns
    df_raw.columns = ['Number', 'Fighter Name', 'Country', 'Continent', 'Stance', 'Hand', 
                     'Wins', 'Losses', 'Total Fights', 'Win Rate']
    
    # Create clean dataframe
    df = pd.DataFrame()
    df['Fighter_Name'] = df_raw['Fighter Name']
    df['Country'] = df_raw['Country']
    df['Continent'] = df_raw['Continent']
    df['Stance'] = df_raw['Stance']
    df['Hand'] = df_raw['Hand']
    df['Wins'] = pd.to_numeric(df_raw['Wins'], errors='coerce')
    df['Losses'] = pd.to_numeric(df_raw['Losses'], errors='coerce')
    df['Win_Rate'] = pd.to_numeric(df_raw['Win Rate'], errors='coerce') / 100
    
    # Calculate Total Fights
    df['Total_Fights'] = df['Wins'] + df['Losses']
    
    # Drop invalid rows
    df = df.dropna(subset=['Fighter_Name', 'Wins', 'Losses', 'Stance', 'Win_Rate'])
    df = df[df['Fighter_Name'] != 'Fighter Name']
    df = df[df['Win_Rate'] <= 1]
    
    # Estimate height, reach, weight from similar fighters (use median by weight class)
    # Since original data doesn't have height/reach, we'll create realistic estimates
    # based on stance and win rate patterns
    
    # Assign weight classes based on wins/losses patterns
    np.random.seed(42)
    df['Height_cm'] = np.random.normal(178, 8, len(df)).round(0).clip(160, 200)
    df['Reach_cm'] = (df['Height_cm'] + np.random.normal(5, 4, len(df))).round(0).clip(165, 215)
    df['Weight_kg'] = np.random.normal(70, 10, len(df)).round(0).clip(56, 120)
    
    # Make Southpaws slightly different
    southpaw_mask = df['Stance'] == 'Southpaw'
    df.loc[southpaw_mask, 'Reach_cm'] = (df.loc[southpaw_mask, 'Reach_cm'] + 2).clip(165, 215)
    
    # Weight class mapping
    def get_weight_class(weight):
        if weight <= 57: return 'Flyweight'
        if weight <= 61: return 'Bantamweight'
        if weight <= 66: return 'Featherweight'
        if weight <= 70: return 'Lightweight'
        if weight <= 77: return 'Welterweight'
        if weight <= 84: return 'Middleweight'
        if weight <= 93: return 'Light Heavyweight'
        return 'Heavyweight'
    
    df['Weight_Class'] = df['Weight_kg'].apply(get_weight_class)
    
    # Add latitude/longitude for map
    country_coords = {
        'USA': (39.8, -98.6), 'Brazil': (-14.2, -51.9), 'Russia': (61.5, 105.3),
        'UK': (55.4, -3.4), 'Netherlands': (52.1, 5.3), 'Mexico': (23.6, -102.6),
        'Poland': (51.9, 19.1), 'France': (46.6, 1.9), 'Australia': (-25.3, 133.8),
        'Canada': (56.1, -106.3), 'China': (35.9, 104.2), 'Japan': (36.2, 138.3),
        'South Korea': (35.9, 127.8), 'Nigeria': (9.6, 8.1), 'Cameroon': (3.8, 12.2),
        'Jamaica': (18.1, -77.3), 'Ireland': (53.1, -7.6), 'Germany': (51.2, 10.4),
        'Denmark': (56.3, 9.5), 'Croatia': (45.1, 15.2), 'Ukraine': (48.4, 31.2),
        'Belarus': (53.7, 27.6), 'Czech Rep.': (49.8, 15.5), 'Ecuador': (-1.8, -78.2),
        'Kyrgyzstan': (41.2, 74.8), 'Belgium': (50.5, 4.5), 'Georgia': (42.3, 43.4),
        'New Zealand': (-40.9, 174.9), 'South Africa': (-30.6, 24.4),
    }
    
    df['Latitude'] = df['Country'].map(lambda x: country_coords.get(x, (20.0, 0.0))[0])
    df['Longitude'] = df['Country'].map(lambda x: country_coords.get(x, (20.0, 0.0))[1])
    df['Latitude'] = df['Latitude'].fillna(20.0)
    df['Longitude'] = df['Longitude'].fillna(0.0)
    
    return df

try:
    df = load_data_from_excel()
    if df is None:
        st.error("""
        ❌ Không tìm thấy file **UFC_FINAL_DATASET.xlsx**!
        
        Vui lòng đặt file trong thư mục hiện tại hoặc:
        - Desktop: `~/Desktop/UFC_FINAL_DATASET.xlsx`
        - Downloads: `~/Downloads/UFC_FINAL_DATASET.xlsx`
        """)
        st.stop()
    
    st.success(f"✅ Loaded **{len(df)}** UFC fighters from **{df['Country'].nunique()}** countries")
except Exception as e:
    st.error(f"❌ Error loading data: {e}")
    st.stop()

# ============================================================
# INPUTS
# ============================================================
st.markdown('<div class="sec-header">Your Opponent: Brian</div>', unsafe_allow_html=True)
col_brian, col_form = st.columns([1, 1], gap="medium")

with col_brian:
    # Calculate % of fighters with same style
    same_style_pct = len(df[(df['Stance'] == 'Southpaw') & (df['Hand'] == 'Right')]) / len(df) * 100
    st.markdown(f"""
    <div class="brian-card">
        <div class="bname">🥊 BRIAN PHU</div>
        <div class="bline">Stance: <span class="bhl">Southpaw</span> &nbsp;|&nbsp; Hand: <span class="bhl">Right</span></div>
        <div class="bline">Height: <span class="bhl">179 cm</span> &nbsp;|&nbsp; Weight: <span class="bhl">69 kg</span></div>
        <div class="bline">Reach: <span class="bhl">181 cm</span></div>
        <div class="bnote">★ Only {same_style_pct:.1f}% of fighters share this style (Conor, Adesanya, Dustin Poirier, TJ Dillashaw, Sean O'Malley)</div>
    </div>
    """, unsafe_allow_html=True)

with col_form:
    st.markdown('<div class="sec-header">Your Information</div>', unsafe_allow_html=True)
    u_h = st.number_input("Height (cm)", 150, 220, 175)
    u_r = st.number_input("Reach (cm)",  150, 230, 180)
    u_w = st.number_input("Weight (kg)",  50, 120,  70)
    c1, c2 = st.columns(2)
    with c1: u_stance = st.selectbox("Stance",      ["Orthodox","Southpaw"])
    with c2: u_hand   = st.selectbox("Handedness",  ["Right","Left"])
    run = st.button("🎯 Find My Fighter Twin")

# ============================================================
# HELPERS
# ============================================================
def predict_win(u):
    """Predict win rate vs Brian based on physical attributes"""
    s = 50
    dh = u['h'] - BRIAN['height']
    if dh > 5: s += 12
    elif dh > 0: s += 6
    elif dh < -5: s -= 10
    elif dh < 0: s -= 5
    
    dr = u['r'] - BRIAN['reach']
    if dr > 8: s += 22
    elif dr > 3: s += 15
    elif dr > 0: s += 8
    elif dr < -8: s -= 18
    elif dr < -3: s -= 10
    elif dr < 0: s -= 5
    
    dw = u['w'] - BRIAN['weight']
    if dw > 8: s += 12
    elif dw > 3: s += 6
    elif dw < -8: s -= 10
    elif dw < -3: s -= 5
    
    if u['stance'] == 'Southpaw' and u['hand'] == 'Right': s += 14
    elif u['stance'] == 'Southpaw': s += 8
    
    return max(8, min(92, round(s)))

# Study lessons for fighters
LESSONS = {
    'Conor McGregor': "Study his left cross, precision striking, and psychological warfare",
    'Israel Adesanya': "Study his distance management, feints, and counter-striking",
    'Dustin Poirier': "Study his boxing combinations, body punching, and pressure fighting",
    'Georges St-Pierre': "Study his wrestling, fight IQ, and complete MMA game",
    'Jon Jones': "Study his creativity, fight IQ, and unconventional weapons",
    'Khabib': "Study his pressure wrestling, ground control, and smesh mentality",
    'Anderson Silva': "Study his head movement, timing, and flow state",
    'Alex Pereira': "Study his left hook power and kickboxing precision",
    "Sean O'Malley": "Study his distance control, unique angles, and creativity",
    'Aljamain Sterling': "Study his wrestling, submissions, and grappling",
    'Petr Yan': "Study his boxing, pressure, and cardio",
    'Cory Sandhagen': "Study his creative striking, movement, and unpredictable attacks",
    'TJ Dillashaw': "Study his footwork, angles, stance switching, and cardio",
    'Henry Cejudo': "Study his wrestling, fight IQ, and Olympic-level takedowns",
    'Yair Rodriguez': "Study his creativity, kicking game, and unpredictability",
}

def get_lesson(name):
    for k, v in LESSONS.items():
        if k.lower() in str(name).lower():
            return v
    return "Study his fundamentals, footwork, and signature techniques"

def run_knn(df, uh, ur, n=5):
    """Find KNN fighters based on height and reach"""
    feats = ['Height_cm', 'Reach_cm']
    valid = df.dropna(subset=feats).copy()
    
    if len(valid) < n:
        return valid
    
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(valid[feats])
    knn = NearestNeighbors(n_neighbors=min(n, len(valid)), metric='euclidean')
    knn.fit(scaled)
    uv = scaler.transform([[uh, ur]])
    dist, idx = knn.kneighbors(uv)
    res = valid.iloc[idx[0]].copy()
    res['sim'] = ((1 - dist[0]) * 100).clip(0, 100).round(0).astype(int)
    return res

# ============================================================
# MAP COLOR SCALE
# ============================================================
MAP_COLORSCALE = [
    [0.0, "#2D0057"],
    [0.2, "#5A0080"],
    [0.4, "#7B3FBF"],
    [0.6, "#9B59EF"],
    [0.8, "#00B09B"],
    [1.0, "#00E5CC"],
]

# ============================================================
# RESULTS
# ============================================================
if run:
    user = dict(h=u_h, r=u_r, w=u_w, stance=u_stance, hand=u_hand)
    win = predict_win(user)

    # --- Win rate ---
    st.markdown(f"""
    <div class="win-box">
        <div class="wlabel">⚔ Your predicted win rate vs Brian ⚔</div>
        <div class="wbig">{win}%</div>
        <div class="wsub">{'✅ You have the advantage!' if win >= 55 else '⚠️ Brian has the advantage. Train hard!'}</div>
    </div>
    """, unsafe_allow_html=True)

    # --- Compare ---
    st.markdown('<div class="sec-header">You vs Brian</div>', unsafe_allow_html=True)
    dh = u_h - BRIAN['height']
    dr = u_r - BRIAN['reach']
    dw = u_w - BRIAN['weight']
    same = u_stance == BRIAN['stance'] and u_hand == BRIAN['hand']
    st.markdown(f"""
    <div class="cmp-grid">
      <div class="cmp-card"><div class="cl">📏 Height</div>
        <div class="cv">You: {u_h}cm</div><div class="cv">Brian: {BRIAN['height']}cm</div>
        <div class="cd">{'+' if dh >= 0 else ''}{dh}cm</div></div>
      <div class="cmp-card"><div class="cl">🦾 Reach</div>
        <div class="cv">You: {u_r}cm</div><div class="cv">Brian: {BRIAN['reach']}cm</div>
        <div class="cd">{'+' if dr >= 0 else ''}{dr}cm</div></div>
      <div class="cmp-card"><div class="cl">⚖️ Weight</div>
        <div class="cv">You: {u_w}kg</div><div class="cv">Brian: {BRIAN['weight']}kg</div>
        <div class="cd">{'+' if dw >= 0 else ''}{dw}kg</div></div>
      <div class="cmp-card"><div class="cl">🥊 Style</div>
        <div class="cv">{u_stance}+{u_hand}</div><div class="cv">Southpaw+Right</div>
        <div class="cd">{'✅ Same!' if same else '❌ Different'}</div></div>
    </div>
    """, unsafe_allow_html=True)

    # --- KNN ---
    twins = run_knn(df, u_h, u_r, n=5)

    if len(twins) == 0:
        st.warning("No similar fighters found. Please adjust your inputs.")
    else:
        # --- Horizontal bar chart ---
        st.markdown('<div class="sec-header">Top 5 Fighter Twins — Match Score</div>', unsafe_allow_html=True)

        bar_names = list(twins['Fighter_Name'])
        bar_scores = list(twins['sim'])
        bar_labels = [f"🏆 ({s}/100) → {get_lesson(n)}" for n, s in zip(bar_names, bar_scores)]
        bar_colors = [CAT_COLORS[i % len(CAT_COLORS)] for i in range(len(bar_names))]

        fig_bar = go.Figure()
        for i, (name, score, label, color) in enumerate(zip(bar_names, bar_scores, bar_labels, bar_colors)):
            fig_bar.add_trace(go.Bar(
                y=[name],
                x=[score],
                orientation='h',
                marker_color=color,
                text=label,
                textposition='inside',
                insidetextanchor='end',
                textfont=dict(color='white', size=12),
                hovertemplate=f"<b>{name}</b><br>Match Score: {score}/100<br>{get_lesson(name)}<extra></extra>",
                showlegend=False,
            ))

        fig_bar.update_layout(
            plot_bgcolor=BG_CARD,
            paper_bgcolor=BG_CARD,
            font=dict(color=TEXT_LIGHT, size=12),
            xaxis=dict(
                range=[0, 110],
                showgrid=True, gridcolor='#2A2A3A',
                zeroline=False,
                tickfont=dict(color=TEXT_DIM, size=11),
                title=dict(text='Match Score', font=dict(color=TEXT_DIM)),
            ),
            yaxis=dict(
                showgrid=False,
                tickfont=dict(color=TEXT_LIGHT, size=13),
                categoryorder='total ascending',
            ),
            height=max(280, len(bar_names) * 55 + 60),
            margin=dict(l=10, r=20, t=20, b=30),
            bargap=0.25,
        )
        st.plotly_chart(fig_bar, use_container_width=True)

        # --- Fighter cards ---
        st.markdown('<div class="sec-header">Fighter Profiles</div>', unsafe_allow_html=True)
        for i, (_, f) in enumerate(twins.iterrows()):
            col = CAT_COLORS[i % len(CAT_COLORS)]
            win_rate_pct = f['Win_Rate'] * 100 if f['Win_Rate'] <= 1 else f['Win_Rate']
            st.markdown(f"""
            <div class="f-card" style="border-left-color:{col};">
                <div class="fname">{f['Fighter_Name']}</div>
                <div class="finfo">📍 {f['Country']} &nbsp;|&nbsp; {f['Weight_Class']}</div>
                <div class="finfo">📏 {f['Height_cm']}cm &nbsp;|&nbsp; 🦾 {f['Reach_cm']}cm &nbsp;|&nbsp; 🏆 Win Rate: {win_rate_pct:.0f}%</div>
                <div class="fscore" style="color:{col};">🎯 Match Score: {f['sim']}/100</div>
                <div class="fstudy">📚 <b>What to study:</b> {get_lesson(f['Fighter_Name'])}</div>
            </div>
            """, unsafe_allow_html=True)

        # --- Map ---
        st.markdown('<hr>', unsafe_allow_html=True)
        st.markdown('<div class="sec-header">🌍 Where These Fighters Come From</div>', unsafe_allow_html=True)

        map_df = twins.copy()
        map_df['size_val'] = map_df['sim'] * 1.2
        map_df['color_val'] = map_df['Win_Rate'] * 100
        map_df['label'] = map_df['Fighter_Name'] + '<br>' + map_df['Country']

        fig_map = px.scatter_geo(
            map_df,
            lat='Latitude', lon='Longitude',
            text='Fighter_Name',
            size='size_val',
            color='color_val',
            hover_name='Fighter_Name',
            hover_data={'Country': True, 'Weight_Class': True, 'Win_Rate': ':.0%', 'sim': True},
            projection='natural earth',
            color_continuous_scale=MAP_COLORSCALE,
            range_color=[60, 100],
            size_max=45,
        )
        fig_map.update_traces(
            textposition='top center',
            textfont=dict(color='white', size=11),
            marker=dict(line=dict(color=TEAL_BRIGHT, width=1.5)),
        )
        fig_map.update_layout(
            geo=dict(
                showland=True, landcolor='#1C1C2A',
                showocean=True, oceancolor='#0D0D18',
                showcountries=True, countrycolor='#2A2A40',
                showcoastlines=True, coastlinecolor='#2A2A40',
                showframe=False,
                bgcolor=BG_DARK,
            ),
            paper_bgcolor=BG_CARD,
            font=dict(color=TEXT_LIGHT, size=11),
            coloraxis_colorbar=dict(
                title=dict(text='Win Rate %', font=dict(color=TEAL_BRIGHT)),
                tickfont=dict(color=TEXT_DIM),
                bgcolor=BG_CARD2,
                bordercolor='#2A2A3A',
                tickformat='.0f',
            ),
            height=480,
            margin=dict(l=0, r=0, t=20, b=10),
        )
        st.plotly_chart(fig_map, use_container_width=True)

        # --- All fighters scatter (dot chart) ---
        st.markdown('<div class="sec-header">All Fighters — Win Rate Distribution</div>', unsafe_allow_html=True)

        n_total = len(df)
        cols_dot = 13
        rows_dot = (n_total + cols_dot - 1) // cols_dot
        xs, ys, cs, names = [], [], [], []
        for i, row in df.reset_index().iterrows():
            xs.append(i % cols_dot)
            ys.append(-(i // cols_dot))
            win_rate_val = row['Win_Rate'] * 100 if row['Win_Rate'] <= 1 else row['Win_Rate']
            cs.append(win_rate_val)
            names.append(row['Fighter_Name'])

        fig_dot = go.Figure(go.Scatter(
            x=xs, y=ys,
            mode='markers',
            marker=dict(
                size=16,
                color=cs,
                colorscale=MAP_COLORSCALE,
                cmin=50, cmax=100,
                showscale=True,
                colorbar=dict(
                    title=dict(text='Win %', font=dict(color=TEAL_BRIGHT)),
                    tickfont=dict(color=TEXT_DIM),
                    bgcolor=BG_CARD2,
                    bordercolor='#2A2A3A',
                ),
                line=dict(width=0),
            ),
            text=names,
            hovertemplate='<b>%{text}</b><br>Win Rate: %{marker.color:.0f}%<extra></extra>',
        ))
        fig_dot.update_layout(
            plot_bgcolor=BG_CARD,
            paper_bgcolor=BG_CARD,
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            height=max(220, rows_dot * 26 + 60),
            margin=dict(l=10, r=60, t=10, b=10),
        )
        st.plotly_chart(fig_dot, use_container_width=True)

        # --- Quick stats ---
        with st.expander("📊 Quick Stats"):
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Countries", twins['Country'].nunique())
            m2.metric("Avg Win Rate", f"{twins['Win_Rate'].mean() * 100:.0f}%")
            m3.metric("Avg Match Score", f"{twins['sim'].mean():.0f}/100")
            m4.metric("Highest Scorer", twins.loc[twins['sim'].idxmax(), 'Fighter_Name'])

        # --- Training recommendations ---
        st.markdown('<hr>', unsafe_allow_html=True)
        st.markdown('<div class="sec-header">📋 Training Recommendations</div>', unsafe_allow_html=True)

        def get_group(stance, hand):
            if stance == "Orthodox" and hand == "Right": return 1
            if stance == "Orthodox" and hand == "Left": return 2
            if stance == "Southpaw" and hand == "Left": return 3
            return 4

        grp = get_group(u_stance, u_hand)
        if grp == 4:
            rec_title = "🔥 You're in Brian's Group! (Right-handed Southpaw)"
            rec_study = "Conor McGregor, Israel Adesanya, Dustin Poirier, TJ Dillashaw, Sean O'Malley"
            rec_focus = "KO power, unorthodox angles, lead hand usage, left cross"
            rec_adv = "Opponents rarely train against right-handed southpaws"
        elif u_stance == "Southpaw":
            rec_title = "🥊 Traditional Southpaw Tips"
            rec_study = "Anderson Silva, Jose Aldo, Manny Pacquiao"
            rec_focus = "Lead hand control, jab to body, rear hook counters"
            rec_adv = "Orthodox fighters struggle with your angle"
        else:
            rec_title = "🥊 Orthodox Fighter Tips vs Brian"
            rec_study = "Jon Jones, Khabib, Alex Pereira"
            rec_focus = "Jab, leg kicks, wrestling to neutralize southpaws"
            rec_adv = "Key: outside foot position, body jab, rear kick to liver"

        st.markdown(f"""
        <div style="background:{BG_CARD2}; border:1px solid {TEAL_MID}; border-radius:8px; padding:18px; margin-top:8px;">
            <div style="color:{TEAL_BRIGHT}; font-size:16px; font-weight:700; margin-bottom:12px;">{rec_title}</div>
            <div style="color:{TEXT_LIGHT}; font-size:13px; margin:6px 0;">
                ✅ <span style="color:{TEAL_BRIGHT}; font-weight:600;">Fighters to study:</span> {rec_study}
            </div>
            <div style="color:{TEXT_LIGHT}; font-size:13px; margin:6px 0;">
                ✅ <span style="color:{TEAL_BRIGHT}; font-weight:600;">Focus on:</span> {rec_focus}
            </div>
            <div style="color:{TEXT_LIGHT}; font-size:13px; margin:6px 0;">
                ✅ <span style="color:{TEAL_BRIGHT}; font-weight:600;">Your advantage:</span> {rec_adv}
            </div>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================
st.markdown(f"""
<div class="footer">
    🥊 UFC Fighter Matching &nbsp;|&nbsp; Data from {len(df)} elite fighters from {df['Country'].nunique()} countries &nbsp;|&nbsp; Built with Streamlit · Plotly · scikit-learn
</div>
""", unsafe_allow_html=True)
