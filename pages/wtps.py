import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

st.set_page_config(layout="wide")


# -----------------------------------------------------------
# Load data (add caching for Streamlit)
# -----------------------------------------------------------
@st.cache_data
def load_data():
    df_ = pd.read_csv(r"assets\indwtp.csv")
    df_["rp"] = df_["rp"].map({0: "No Reminder", 1: "With Reminder"})
    return df_


df = load_data()


# Ensure numeric dtype for selected attribute later
def ensure_numeric(s):
    return pd.to_numeric(s, errors="coerce")


# -----------------------------------------------------------
# Labels and grouping
# -----------------------------------------------------------
label_map = {
    "id": "Respondent ID",
    "cn": "Opt Out",
    "l": "Local",
    "l160": "Local (within 160 km)",
    "l320": "Local (within 320 km)",
    "prov": "Respondent's Home Province",
    "can": "Product of Canada",
    "grass": "Grass-fed",
    "organic": "Organic",
    "btest": "BSE Tested",
    "bfree": "BSE Free",
    "rp": "Reference Price Reminder"
}

attribute_groups = {
    "Origin Attributes (Base = Product of USA)": ["l", "l160", "l320", "prov", "can"],
    "Value-added Attributes (Base = Conventional Grain-fed)": ["grass", "organic"],
    "Food Safety Attributes (Base = No BSE Test/Guarantee)": ["btest", "bfree"],
    "Other": ["cn"]
}

# --- Dynamic Base Category Mapper ---
base_category_map = {}
for group_name, vars_list in attribute_groups.items():
    if "Base = " in group_name:
        base_text = group_name.split("Base = ")[1].split(")")[0]
    else:
        base_text = "N/A"

    for v in vars_list:
        base_category_map[v] = base_text

# Main page controls

options = [(label_map[v], v) for group, vars_ in attribute_groups.items() for v in vars_]
options_dict = {label: var for label, var in options}
selected_label = st.selectbox("Select an attribute", list(options_dict.keys()))
yvar = options_dict[selected_label]
group_var = "rp"

st.write("Note the differences in the mean, median, and overall distribution between the control and treated group.")


# Guard and prepare numeric column
df[yvar] = ensure_numeric(df[yvar])

# THEME BACKGROUND COLOR
theme_color = "#EFEFEF"

# -----------------------------------------------------------
# Pre-calculate explicit Mean for custom tooltip integration
# -----------------------------------------------------------
mean_stats = df.groupby(group_var, observed=False)[yvar].mean().round(2).to_dict()
df["Group Mean"] = df[group_var].map(mean_stats)

# -----------------------------------------------------------
# DYNAMIC STATS PIPING ENGINE
# -----------------------------------------------------------
text_metrics = df.groupby(group_var, observed=False)[yvar].agg(
    mean='mean',
    median='median',
    q3=lambda x: x.quantile(0.75)
).round(2)

try:
    mean_no = float(text_metrics.loc['No Reminder', 'mean'])
    mean_with = float(text_metrics.loc['With Reminder', 'mean'])
    med_no = float(text_metrics.loc['No Reminder', 'median'])
    med_with = float(text_metrics.loc['With Reminder', 'median'])
    q3_no = float(text_metrics.loc['No Reminder', 'q3'])
    q3_with = float(text_metrics.loc['With Reminder', 'q3'])

    # Calculate the raw changes to display as deltas
    mean_delta = round(mean_with - mean_no, 2)
    med_delta = round(med_with - med_no, 2)
    q3_delta = round(q3_with - q3_no, 2)
except KeyError:
    mean_no = mean_with = med_no = med_with = q3_no = q3_with = 0.00
    mean_delta = med_delta = q3_delta = 0.00

# Extract base category for the caption
selected_base = base_category_map.get(yvar, "N/A")

# -----------------------------------------------------------
# Plotly Violin + Box Native Integration Layout (UNTOUCHED)
# -----------------------------------------------------------
fig = px.violin(
    df,
    x=yvar,
    y=group_var,
    color_discrete_sequence=["lightgray"],
    box=True,
    points=False,
    orientation="h",
    labels={yvar: f"{selected_label} (CAN $)", group_var: " "},
    hover_data={
        yvar: False,
        group_var: False,
        "Group Mean": ":.2f"
    }
)

fig.update_traces(
    line_color="black",
    line_width=1.5
)

fig.update_layout(
    plot_bgcolor=theme_color,
    paper_bgcolor=theme_color,
    width=900,
    height=450,
    margin=dict(l=150, r=20, t=20, b=50),
    hovermode="y unified",
    hoverlabel=dict(
        bgcolor="white",
        font_size=12,
        font_color="black",
        font_family="Arial",
        align="left"
    ),
    xaxis=dict(
        showgrid=True,
        gridcolor="#d0d0d0",
        zeroline=False,
        title_font=dict(size=13, color="black", family="Arial Black"),
        tickfont=dict(size=11, color="black"),
        tickformat=".2f"
    ),
    yaxis=dict(
        title="",
        tickfont=dict(size=13, color="black", weight="bold")
    )
)

# -----------------------------------------------------------
# Render Display Layout Elements
# -----------------------------------------------------------
st.plotly_chart(fig, width="stretch")

st.caption(f"Figure: WTP plot of {selected_label} [vs {selected_base}]")

st.markdown("---")

# ROW 1: SLICK METRICS OVERVIEW PANELS
st.markdown(f"### 📊 Valuation Shifts for **{selected_label}**")
m_col1, m_col2, m_col3 = st.columns(3)

with m_col1:
    st.metric(
        label="Mean WTP Shift",
        value=f"${mean_with:.2f} CAD",
        delta=f"{mean_delta:+.2f} from ${mean_no:.2f}",
        delta_color="normal" if mean_delta <= 0 else "inverse"
    )

with m_col2:
    st.metric(
        label="Median WTP Shift",
        value=f"${med_with:.2f} CAD",
        delta=f"{med_delta:+.2f} from ${med_no:.2f}",
        delta_color="normal" if med_delta <= 0 else "inverse"
    )

with m_col3:
    st.metric(
        label="Q3 WTP (Upper Tail) Shift",
        value=f"${q3_with:.2f} CAD",
        delta=f"{q3_delta:+.2f} from ${q3_no:.2f}",
        delta_color="normal" if q3_delta <= 0 else "inverse"
    )

st.markdown("")


