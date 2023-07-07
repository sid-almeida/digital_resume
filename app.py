from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
cover_letter_file = current_dir / "assets" / "CL.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Sidnei Almeida"
PAGE_ICON = ":wave:"
NAME = "Sidnei Almeida"
DESCRIPTION = """
Data Science Enthusiast / Management Processes Student, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "sidnei.almeida1806@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/saaelmeida93/",
    "GitHub": "https://github.com/sid-almeida/datascience",
    "Kaggle": "https://www.kaggle.com/sidneialmeida",
    "Jovian": "https://jovian.com/sidnei-almeida1806"
}
PROJECTS = {
    "🏆 Bankruptcy Prediction App - Uses 96 features to predict the probability of bankruptcy of a business.": "https://datascience-yxuwz2bmvo.streamlit.app/",
    "🏆 UniKeep (In progress) - Web app that trains a model to predict the student's dropout probability.": "https://unikeep.streamlit.app/",
    "🏆 Churn Prediction - A web application that predicts the churning of clients of a company.": "https://youtu.be/LzCfNanQ_9c",
    "🏆 Cement Prediction Model - Web app that predicts the demand for an indian cement company": "https://cementdemand-4dxl4y111if.streamlit.app/",
    "🏆 Heart Failure Death Prediction - Web application that uses data to predict the chances of death of a patient": "https://sid-almeida-datasc-heart-failure-mortality-predictionapp-7liskx.streamlit.app/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume and Cover Letter",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write("---")
st.write(
    """
- ✔️ 2 Years experience extracting insights from data
- ✔️ Strong hands on experience and knowledge in Python, Excel and SQL
- ✔️ Good understanding of statistical principles, machine learning and data visualization
- ✔️ Excellent team-player and communicator with strong attention to detail
- ✔️ Currently pursuing a degree in Management Processes
- ✔️ Advanced English and Portuguese speaker
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 👩‍💻 Data Mining / Manipulation: Python (Pandas, Polars), SQL, C++
- 📈 Data Analysis: Python (Matplotlib, Seaborn, Pandas, Numpy), Excel, PowerBi
- 📊 Data Visualization: Streamlit, Seaborn, Plotly, PowerBi, MS Excel
- 📚 Modeling: Scikit-Learn, XGBoost, Regression, Time Series and Classification
- 🗄️ Databases: MySQL, SQLite
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Intern | IFRS - Caxias do Sul**")
st.write("06/2023 - Present")
st.write(
    """
- ► Used Excel to manage and analyze the university's students data
- ► Utilize Python to automate he various tasks related to managing the students data
- ► Assisted the Various teams with the development of new projects and initiatives
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Freelancer | Web Development and Design**")
st.write("01/2020 - Present")
st.write(
    """
- ► Built and maintained websites for small businesses
- ► Designed and developed websites using WordPress, Bubble, Bitrix24 and Wix
- ► Made integrations with CRM, ERP and other systems
- ► Provided support and training to clients on how to use the websites
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Machine Operator | Mundial SA**")
st.write("06/2013 - 09/2019")
st.write(
    """
- ► Operated and maintained machines to produce aluminum products
- ► Ensured the quality of the products by performing quality checks
- ► Collaborated with the team to improve the production processes
- ► Led a small team of 5 - 10 people to achieve the production goals
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
