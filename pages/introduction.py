import streamlit as st

st.set_page_config(
    page_title="AJAE Dashboard",
    page_icon="📊",
    layout="wide",
)

# -----------------------------------------------------------
# HERO ZONE: TITLE & AVATAR ALIGNMENT
# -----------------------------------------------------------
st.title("🤫 There is a secret about how economists estimate Willingness-to-Pay...")
st.markdown("")  # Gentle layout spacing spacer

# -----------------------------------------------------------
# ROW 1: THE PARAMOUNT IMPORTANCE OF WTP
# -----------------------------------------------------------
st.markdown("##### Willingness-to-Pay (WTP) influences policy and market models:")

# Using responsive columns to cleanly segment information blocks
wtp_col1, wtp_col2, wtp_col3 = st.columns(3)

with wtp_col1:
    st.info(
        """
        **🚀 Product Innovations**  
        
        Forecasting Return on Investment (ROI) and target market market-shares.
        
        The "benefit" component of cost-benefit analyses.
        """
    )

with wtp_col2:
    st.error(
        """
        **🌊 Environmental Costs**  
        
        Quantify economic damages and liability costs (e.g., Exxon Valdez, Norfolk Southern).
        
        Quantify the value of public environmental goods (clean air, clean water, well-kept hiking spots) 
        """
    )

with wtp_col3:
    st.success(
        """
        **🧠 Structural Behavioral Choices**  
        
        Deconstructing *how* and *why* people make choices (labor, healthcare, and consumption markets.)
        """
    )

# Clean, high-impact native callout
st.warning("🎯 We need WTP estimations to be as accurate as possible.")

st.divider()

# -----------------------------------------------------------
# ROW 2: CREDIBILITY & HISTORICAL CONTEXT SIDE-BY-SIDE
# -----------------------------------------------------------
st.markdown("### 📝 Let us explore this paper together")

# st.metric acts as an instant credibility badge for your manuscript data
st.metric(
    label="Manuscript Impact",
    value="1,300+ Reads",
    delta_color="normal"
)

# FIXED: Removed the invalid indentation block to align correctly with the layout margin
with st.container(border=True):
    st.image("assets/AJAE.png", width="stretch")
