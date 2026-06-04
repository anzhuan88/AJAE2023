import streamlit as st

st.set_page_config(layout="wide")

# -----------------------------------------------------------
# GLOBAL LAYOUT STYLING (Forced Native Aspect Ratio Equalization)
# -----------------------------------------------------------
st.markdown(
    """
    <style>
    /* Direct target override on Streamlit's canvas frames to lock heights uniformly */
    div[data-testid="stImage"] img {
        height: 260px !important;   /* Locks the vertical height across both columns */
        object-fit: cover !important; /* Crops and centers seamlessly with no distortions */
        width: 100% !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🏖️ Intuition: The Beer on the Beach Paradox")
st.markdown("---")

# -----------------------------------------------------------
# STAGE 1: THE SCENARIO
# -----------------------------------------------------------
st.markdown("### 🌴 Welcome to the Bahamas")
st.markdown(
    """
    Imagine you are relaxing on a beautiful beach. 
    The sun is beating down, you are incredibly thirsty, and you want nothing more than a **ice-cold beer**.
    """
)

# FIXED: Isolated page element override using markdown wrapper to stop the main banner from being cropped
st.markdown("<style>div.hero-beer img { height: auto !important; width: 500px !important; }</style>",
            unsafe_allow_html=True)
st.markdown("<div class='hero-beer'>", unsafe_allow_html=True)
st.image(
    "assets/beer beach.jpg",
    caption="Your ice-cold beer"
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# -----------------------------------------------------------
# STAGE 2: THE INTERACTIVE CHOICES
# -----------------------------------------------------------
st.markdown("### 🏪 You have two places nearby to buy this exact beer from:")

col_hotel, col_shack = st.columns(2)

with col_hotel:
    with st.container(border=True):
        st.markdown("#### 🏨 1. The Fancy Resort Hotel")

        # FIXED: Updated width parameter to 'stretch' to eliminate StreamlitInvalidWidthError
        st.image("assets/fancy hotel.jpg", width="stretch")

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("##### They want **$12.00** for the beer. What is your reaction?")

        hotel_reaction = st.radio(
            "Select your reaction (Hotel):",
            ["✨ A DEAL!", "😐 Meh~ just right~", "🤬 What a rip-off!"],
            key="react_hotel",
            label_visibility="collapsed"
        )

with col_shack:
    with st.container(border=True):
        st.markdown("#### 🏚️ 2. The Run-down Beach Shack")

        # FIXED: Updated width parameter to 'stretch' to eliminate StreamlitInvalidWidthError
        st.image("assets/bodega.jpg", width="stretch")

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("##### They want **$12.00** for the beer. What is your reaction?")

        shack_reaction = st.radio(
            "Select your reaction (Shack):",
            ["✨ A DEAL!", "😐 Meh~ just right~", "🤬 What a rip-off!"],
            key="react_shack",
            label_visibility="collapsed"
        )

st.markdown("---")

# -----------------------------------------------------------
# STAGE 3: THE BEHAVIORAL NUGGET
# -----------------------------------------------------------
st.markdown("### 🧠 The Paradox of Mental Accounting")

if hotel_reaction == "🤬 What a rip-off!" and shack_reaction == "🤬 What a rip-off!":
    st.info(
        "🎯 You're a rationalist! But for most consumers, the context completely shifts their internal outrage limits.")
else:
    st.info(
        "💡 **For most people:** Paying \\$12.00 feels perfectly fine at a fancy resort. "
        "But paying that same \\$12.00 to the run-down shack feels like an absolute rip-off!"
    )

st.markdown(
    """
    **The Friction:** In both scenarios, the beer is identical, and you consume it on the exact same sand. 
    Utility should depend purely on the consumption of the beer itself. 
    Why should the venue matter? 
    
    \nRichard Thaler called this **Mental Accounting**—we don't just care 
    about the utility of the beer, 
    \nWe care about the *fairness of the transaction price* relative to our expectations.
    """
)

st.markdown("---")

# -----------------------------------------------------------
# STAGE 4: THE "SO WHAT?" BIG QUESTION
# -----------------------------------------------------------
st.markdown("### 🎯 The Research Question")

st.warning(
    """
    **Is an economic experiment a *fancy resort* or a *run-down shack*?** 🏟️  

    What is in respondents mind when they participated in choice experiments? Were they spending more generously because they think an experiment is like a fancy resort.?

    By introducing a simple **reference price reminder**, we can ground respondents back into the real-world!
    """
)
