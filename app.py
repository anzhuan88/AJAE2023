## License
#This project is released under the MIT License.
## Disclaimer
#This project processes only **public data from my referenced AJAE paper**.
#No proprietary or sensitive data are included.


import streamlit as st

# 1. Declare page configuration ONCE at the entry point of app.py
st.set_page_config(
    page_title="AJAE Dashboard",
    page_icon="📊",
    layout="wide",
)

# 2. Define the navigation structure and tie individual pages to files
pages = {
    "Research Framework": [
        st.Page("pages/introduction.py", title="1. Context & Motivation", icon="👋", default=True),
        st.Page("pages/intuition.py", title="2. Thaler's Beer Paradox", icon="🏖️"),
        st.Page("pages/experiment.py", title="3. Interactive Survey Setup", icon="🔬"),
    ],
    "Empirical Findings": [
        st.Page("pages/wtps.py", title="4. Dynamic WTPs Plots", icon="📊"),
        st.Page("pages/price.py", title="5. Price Utility Plots", icon="💲"),
        st.Page("pages/implications.py", title="6. Cool! So What?", icon="💡"),
    ]
}

# 3. Initialize and execute the native structural navigation engine
pg = st.navigation(pages)
pg.run()
