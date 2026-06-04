import streamlit as st

st.set_page_config(layout="wide")

# -----------------------------------------------------------
# GLOBAL CSS (Control-style table# -----------------------------------------------------------# GLOBAL CSS (Control-style table)
st.markdown("""
<style>
.UserTable {
    width: 100%;
    border-collapse: collapse;
    font-family: Arial, sans-serif;
    background-color: #FFFFFF;
    color: #000000;
}

.UserTable td {
    width: 25%;
    padding: 12px;
    text-align: center;
    vertical-align: middle;

    /* NEW LEFT + RIGHT borders */
    border-left: 1px solid #CCCCCC;
    border-right: 1px solid #CCCCCC;

    /* Keep top and bottom clean */
    border-top: none;
    border-bottom: none;
}

.none-cell {
    font-style: italic;
    color: #666;
}
.price-text {
    font-weight: bold;
    color: #111;
}
.button-row-cell {
    background-color: #e6f2ff !important;
    padding: 8px !important;
}
.cell-button {
    width: 100%;
    padding: 10px;
    background-color: #1273BC !important;
    color: #FFFFFF !important;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-weight: bold;
}
.cell-button:hover {
    background-color: #0d548a !important;
}
.reminder-block {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 20px;
    line-height: 20px;
    overflow: hidden;
    margin: 0 0 15px 0;
    font-size: 19px;
    color: white;
    font-family: Arial, sans-serif;
}
.instruction-block {
    color: #FFFFFF;
    font-family: Arial, sans-serif;
    margin-bottom: 20px;
}
.survey-card {
    background-color: #262730;
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 25px;
    border: 1px solid #464855;
    
}
</style>

<script>
// Stable state mapping utility (unchanged)
function updateTrackParam(key, value) {
    const urlParams = new URLSearchParams(window.location.search);
    urlParams.set(key, value);
    window.location.search = urlParams.toString();
}
</script>
""", unsafe_allow_html=True)


# -----------------------------------------------------------
# REUSABLE TABLE FUNCTION (Control-style table)
# -----------------------------------------------------------
def render_choice_table(param_key):
    return f"""
    <table class="UserTable">
        <tbody>
            <tr>
                <td>Local</td>
                <td>Product of Canada</td>
                <td>Product of USA</td>
                <td rowspan="5" class="none-cell">I would rather not buy any of these steaks</td>
            </tr>
            <tr>
                <td>Grass Fed</td>
                <td>Grass Fed</td>
                <td>—</td>
            </tr>
            <tr>
                <td>—</td>
                <td>—</td>
                <td>Certified Organic</td>
            </tr>
            <tr>
                <td>—</td>
                <td>Verified BSE Free</td>
                <td>BSE Tested</td>
            </tr>
            <tr>
                <td class="price-text">$17.00/lb</td>
                <td class="price-text">$13.00/lb</td>
                <td class="price-text">$21.00/lb</td>
            </tr>
            <tr>
                <td class="button-row-cell"><button class="cell-button" onclick="updateTrackParam('{param_key}', 'Option 1')">Option 1</button></td>
                <td class="button-row-cell"><button class="cell-button" onclick="updateTrackParam('{param_key}', 'Option 2')">Option 2</button></td>
                <td class="button-row-cell"><button class="cell-button" onclick="updateTrackParam('{param_key}', 'Option 3')">Option 3</button></td>
                <td class="button-row-cell"><button class="cell-button" onclick="updateTrackParam('{param_key}', 'None')">None</button></td>
            </tr>
        </tbody>
    </table>
    """


# -----------------------------------------------------------
# HERO INTRO
# -----------------------------------------------------------
st.title("🔬 Interactive Survey Walkthrough")
st.subheader("Deconstructing Choice Experiment Mechanics in Real-Time")

col1, col2 = st.columns(2)

with col1:
    st.info(
        "⚡ **Structural A/B Testing Framework**  \n"
        "This interactive workspace maps the underlying framework of our consumer choice research. "
        "By testing alternative information flows side-by-side, you can observe firsthand how subtle behavioral "
        "nudges alter consumer valuation responses."
    )

with col2:
    st.success(
        "🎯 **Primary Outcome Metric**  \n"
        "Our target vector tracks changes in **Willingness-to-Pay (WTP)**. At the base of this page, "
        "we capture how the inclusion of a highly targeted reference price reminder compresses variance "
        "and dampens irrational tail inflation."
    )

st.markdown("---")


# -----------------------------------------------------------
# BASELINE REFERENCE PRICE
# -----------------------------------------------------------
st.markdown("### 📋 Stage 1: Reference Price Question")

st.markdown("""
<div style='font-family: Arial, sans-serif; font-size: 16px; margin-bottom: 10px; color: #FFFFFF;'>
    <div>&nbsp; B2. To the closest dollar amount, how much do you usually spend for a pound of steak?</div>
</div>
""", unsafe_allow_html=True)

dropdown_options = [f"${x:.2f}/lb" for x in range(8, 25)]
selected_price_str = st.selectbox(
    "Select your usual price:",
    options=dropdown_options,
    index=0,
    label_visibility="collapsed"
)

st.info(
    f"🔄 **Piping Engine Active:** The selected amount **{selected_price_str}** will be piped down to the treatment choice set."
)

st.markdown("---")
st.markdown("### 🥩 Stage 2: Choice Experiment")

st.markdown("""
 <div class='instruction-block'>
     <p>Instruction:</p>
     <p><strong> Suppose that you are buying a piece of strip loin steak as pictured below.</strong></p>
     <p><strong>You are given 3 options, each marked with a different price and different characteristics. Please select the option you are most likely be choosing in real life.</strong></p>
 </div>
 """, unsafe_allow_html=True)
# -----------------------------------------------------------
# URL STATE
# -----------------------------------------------------------
chosen_option_a = st.query_params.get("track_a", "None Selected")
chosen_option_b = st.query_params.get("track_b", "None Selected")

col_left, col_right = st.columns(2)


# -----------------------------------------------------------
# CONTROL GROUP
# -----------------------------------------------------------
with col_left:
    st.markdown("<div class='survey-card'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #FF4B4B;'>A) Control Group Track</h4>", unsafe_allow_html=True)

    st.markdown("""

    """, unsafe_allow_html=True)

    st.image("assets/Steak.jpg", width=280)
    st.markdown("<div style='height:19px;'></div>", unsafe_allow_html=True)

    st.markdown(render_choice_table("track_a"), unsafe_allow_html=True)


    st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------------------------------------
# TREATMENT GROUP
# -----------------------------------------------------------
with col_right:
    st.markdown("<div class='survey-card'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #29B5E8;'>B) Treatment Group Track</h4>", unsafe_allow_html=True)



    st.image("assets/Steak.jpg", width=280)

    st.markdown(
        f"<p class='reminder-block'><strong>You usually pay <u>{selected_price_str}</u> for steak.</strong></p>",
        unsafe_allow_html=True
    )

    st.markdown(render_choice_table("track_b"), unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
