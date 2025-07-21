import streamlit as st
import streamlit.components.v1 as components

# ─── Streamlit Page Configuration ────────────────────────────────────────────
st.set_page_config(
    page_title="Apple Brand Sentiment Analysis Dashboard",
    page_icon="apple_logo.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .stDeployButton {display: none;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("<h1 style=\"text-align: center;\">Apple Brand Sentiment Analysis</h1>", unsafe_allow_html=True)

# ─── Dashboard Selection Buttons ─────────────────────────────────────────────
st.subheader("Select a Platform to View Sentiment Analysis")
col1, col2, col3 = st.columns(3)

selected_platform = None

with col1:
    if st.button("YouTube", use_container_width=True):
        selected_platform = "youtube"
with col2:
    if st.button("Twitter", use_container_width=True):
        selected_platform = "twitter"
with col3:
    if st.button("Reddit", use_container_width=True):
        selected_platform = "reddit"

# ─── Embed Power BI Dashboard ────────────────────────────────────────────────
if selected_platform == "youtube":
    html_code = """
    <iframe title="Youtube" width="100%" height="800" src="https://app.powerbi.com/reportEmbed?reportId=69f7c972-5bd3-4264-b66a-6039f657c0e1&autoAuth=true&ctid=2ff55904-2b62-44bf-be9d-37db3045e181&filterPaneEnabled=false&navContentPaneEnabled=false" frameborder="0" allowFullScreen="true"></iframe>
    """
elif selected_platform == "twitter":
    html_code = """
    <iframe title="Twitter" width="100%" height="800" src="https://app.powerbi.com/reportEmbed?reportId=2efef84a-b5bf-42e9-9b8c-79040fc16289&autoAuth=true&ctid=2ff55904-2b62-44bf-be9d-37db3045e181&filterPaneEnabled=false&navContentPaneEnabled=false" frameborder="0" allowFullScreen="true"></iframe>
    """
elif selected_platform == "reddit":
    html_code = """
    <iframe title="Reddit" width="100%" height="800" src="https://app.powerbi.com/reportEmbed?reportId=acaa5372-b627-476c-8d7f-ad9146a0544a&autoAuth=true&ctid=2ff55904-2b62-44bf-be9d-37db3045e181&filterPaneEnabled=false&navContentPaneEnabled=false" frameborder="0" allowFullScreen="true"></iframe>
    """
else:
    html_code = "<p>Please select a platform to view the dashboard.</p>"

components.html(html_code, height=800, scrolling=False)

st.markdown("---  \n", unsafe_allow_html=True)
st.markdown("### 💡 Important Notes:")
st.markdown("## Contact Admin for Access")

