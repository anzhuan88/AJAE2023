import streamlit as st

st.set_page_config(layout="wide")

st.title("💡 So What?")
st.subheader("Policy Implications & Theoretical Mechanics")
st.markdown("---")

# -----------------------------------------------------------
# ROW 1: PUNCHY HEADLINE METRICS
# -----------------------------------------------------------
st.markdown("### 📊 Empirical Impact on WTP")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Mean WTP Reduction",
        value="7/10 labels",
        delta="Reduction of Hypothetical Bias",
        delta_color="normal"
    )

with col2:
    st.metric(
        label="Distribution Compression",
        value="7/10 labels",
        delta="Reduction of Hypothetical Bias",
        delta_color="normal"
    )

with col3:
    st.metric(
        label="Operational Cost",
        value="$0.00",
        delta="Scalable Nudge",
        delta_color="normal"
    )

st.markdown("---")

# -----------------------------------------------------------
# ROW 2: THE BEHAVIORAL PUZZLE & MARKET REALITY
# -----------------------------------------------------------
left_col, right_col = st.columns(2)

with left_col:
    st.markdown("### 🧠 The Behavioral Puzzle")

    # Using an st.expander with a clear callout question creates clean interactivity
    with st.expander("🤔 Shouldn't consumer preferences be robust to a mere reminder?", expanded=True):
        st.markdown(
            """
            Standard Economic Theory **posits** that consumer utility a fundamental aspect of each persons. 
            A simple reminder *should not* alter valuations. 

            Yet, the reminder systematically deflates WTPs.
            """
        )

with right_col:
    st.markdown("### 🏪 The Reality")

    # st.info creates a perfectly padded, native styled background block
    st.info(
        """
        **Artificial Marketplaces:**  
        Choice experiments are neither luxury resorts nor run-down shacks; 
        they are fundamentally simulated environments. They do no necessarily reflect a real-world market. Can the reminder help with that?

        """
    )

st.markdown("---")

# -----------------------------------------------------------
# ROW 3: POLICY IMPACT / THE "SO WHAT?"
# -----------------------------------------------------------
st.markdown("### 🎯 The Key Take-Away")

# st.success frames your final conclusion as a high-value positive breakthrough
st.success(
    """
    🚀 **Hypothetical Bias Mitigation:**  
    By grounding respondents in real-world market constraints, the reference price reminder  
    deflates (unrealistic) WTP calculations. 

    This simple informational nudge functions as an elegant, low-cost **hypothetical price mitigator** 
    that researchers can deploy globally to maximize stated-preference data reliability.
    """
)
st.markdown("---")

st.markdown("### 📚 Further Reading")
st.markdown(
    """
    1. **Lim, K. H., & Hu, W. (2023).** *Contextual reference price in choice experiments.* American Journal of Agricultural Economics, 105(4).  
        https://doi.org/10.1111/ajae.12354

    2. **Thaler, R. (1985).** *Mental Accounting and Consumer Choice.* Marketing Science, 4(3), 199–214.  
        https://doi.org/10.1287/mksc.4.3.199

    3. **Bordalo, P., Gennaioli, N., & Shleifer, A. (2020).** *Memory, attention, and choice.* Quarterly Journal of Economics, 135(3), 1399–1442.  
        https://doi.org/10.1093/qje/qjaa007
    """
)