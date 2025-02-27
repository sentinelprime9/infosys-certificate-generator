import streamlit as st
from util import details_to_file_name
from script import generate_certificate
from datetime import date

st.title("Infosys Certificate Generator")

name = st.text_input("Name")

course = st.selectbox(
    'Course',
    (
        "ReactJS",
        "Deep Learning for Developers",
    ))

today = date.today()
prev_year = today.year

date_completed = st.date_input("Date Completed", min_value=date(prev_year-4,1,1), max_value=today, format="DD/MM/YYYY")

date_issued = st.date_input("Date Issued", min_value=date(prev_year-4,1,1), max_value=today, format="DD/MM/YYYY")

if st.button("Submit", type="primary"):

    if name == '':
        "Enter name!"
    else:
        generate_certificate(name, course, date_completed, date_issued)
        certificate = details_to_file_name(name, course)

        with open(f"output/{certificate}.pdf", "rb") as file:
            btn = st.download_button(
                label="Download",
                data=file,
                file_name=f"{certificate}.pdf",
                mime="application/pdf",
            )
