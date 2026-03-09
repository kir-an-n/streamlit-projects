import streamlit as st
import pandas as pd

st.sidebar.title('Navigation ')
section = st.sidebar.radio("Go to ", ["About", "Skills", "Experience", "Education", "Contact"])

skills = {
    'Python': 0.8,
    'Streamlit learning': 0.8,
    'Machine learning': 0.7,
    'SQL': 0.9,
    'Data Visualization': 0.8
}

st.title('Ryan')
st.subheader("Data scientist")

if section == 'About':
    st.markdown(f"""
      Experienced data scientist with strong skills in analytics, machine learning, and story telling with data.
      Passionate about turning data into actionable insights.          
    """)

elif section == 'Skills':
    st.header("Skills Overview")
    for skill, level in skills.items():
        st.write(skill)  # Fixed: was st.write(f"skill") which prints the word "skill"
        st.progress(level)

    df_skills = pd.DataFrame({
        "Skill": list(skills.keys()),
        "proficiency": list(skills.values())
    })

    st.bar_chart(df_skills.set_index("Skill"))  # Fixed: moved inside the elif block

elif section == 'Experience':
    st.header("Work Experience")  # Fixed: indentation

    with st.expander("Data Scientist | COMPANY | JUNE 2023"):  # Fixed: missing colon
        st.write("""
          - Built 5 Streamlit Apps in production
          - Built 30+ Dashboards for risk and underwriting
          - Developed 20 DBT Models  
        """)

    with st.expander("Youtuber | Ryan & Matte | JUNE 2020"):  # Fixed: missing colon
        st.write("""
          - Created over 200 Data Videos
          - Full python and pandas course
          - Full scikit learn course          
        """)

    with st.expander("Leetcode programmer | Conor | SEPTEMBER 2013"):  # Fixed: missing colon
        st.write("""
          - Has expert badge in leetcode
          - Has founded neetcode website
          - Has solved over 2500+ leetcode questions                              
        """)

elif section == 'Education':
    st.header("Education")
    st.write("B.S in Electronics and Communication")

elif section == 'Contact':
    st.header("Get in touch")
    col1, col2 = st.columns(2)
    with col1:
        email = st.text_input("Email")
        phone = st.text_input("Phone")
    with col2:
        linkedin = st.text_input("Linkedin url")
        portfolio = st.text_input("portfolio url")
        discord = st.text_input("Discord Name")

    message = st.text_area("Message")  # Fixed: indentation

    if st.button("Send"):  # Fixed: semicolon → colon
        st.success("Thanks for reaching out, I'll be in contact soon.")