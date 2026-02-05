# import streamlit as st

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# -----------------------
# Custom CSS — critical
# -----------------------


# -----------------------
# Sidebar
# -----------------------
st.sidebar.title("Data Assistant")
st.sidebar.radio(
    "",
    ["🗄️ Data Generation", "💬 Talk to your data"],
    index=0
)

# -----------------------
# Main Card — Top Section
# -----------------------
with st.container():

    st.markdown('<div class="small-label">Prompt</div>', unsafe_allow_html=True)
    prompt = st.text_input(
        "",
        placeholder="Enter your prompt here...",
        label_visibility="collapsed"
    )

    c1, c2 = st.columns([2, 3])

    with c1:
        ddl = st.file_uploader(
            "Upload DDL Schema",
            type=["sql", "json"],
            label_visibility="collapsed"
        )

    with c2:
        st.markdown(
            "<div style='margin-top:32px;color:#6b7280;'>Supported formats: SQL, JSON</div>",
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("**Advanced Parameters**")

    p1, p2 = st.columns(2)

    with p1:
        temperature = st.slider(
            "Temperature",
            0.0, 1.0, 0.7,
            label_visibility="visible"
        )

    with p2:
        max_tokens = st.number_input(
            "Max Tokens",
            value=100
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.button("Generate")

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------
# Data Preview Card
# -----------------------
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    h1, h2 = st.columns([5,1])
    with h1:
        st.subheader("Data Preview")
    with h2:
        table_sel = st.selectbox("", ["users"], label_visibility="collapsed")

    df = pd.DataFrame({
        "ID": ["001","002","003"],
        "Name": ["Sample Data 1","Sample Data 2","Sample Data 3"],
        "Category": ["Category A","Category B","Category A"],
        "Value": [245.50,127.80,389.20]
    })

    st.dataframe(df, use_container_width=True, height=200)

    # footer row
    f1, f2 = st.columns([6,1])

    with f1:
        quick = st.text_input(
            "",
            placeholder="Enter quick edit instructions...",
            label_visibility="collapsed"
        )

    with f2:
        st.button("Submit")

    st.markdown('</div>', unsafe_allow_html=True)