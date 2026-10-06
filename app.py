import streamlit as st
from debugger import debug_code


st.set_page_config(
    page_title="AI Code Debugger",
    page_icon="🐞"
)


st.title("🐞 AI Code Debugging & Explanation")

st.write(
    "Enter your code and AI will find errors, "
    "explain them and provide corrected code."
)


language = st.selectbox(
    "Select Programming Language",
    ["Python", "Java", "C", "C++", "JavaScript"]
)


code = st.text_area(
    "Enter your code:",
    height=300
)


if st.button("🔍 Debug Code"):

    if code.strip() == "":
        st.warning("Please enter some code.")

    else:

        with st.spinner("AI is analyzing your code..."):

            try:
                result = debug_code(code, language)

                st.success("Debugging completed!")

                st.markdown(result)

            except Exception as e:

                st.error(f"Error: {e}")