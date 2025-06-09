import streamlit as st
from fpdf import FPDF

st.title("Text-to-PDF Converter")

user_text = st.text_area("Enter Your Text Here: ",height=340)
if st.button("Convert To PDF"):
    if user_text.strip() ==" ":
        st.warning("Please Enter some Text First !!")
    else:
        pdf =FPDF()
        pdf.add_page()
        pdf.set_font("Arial",size=12)
        for line in user_text.split('\n'):
            safe_line = ''.join(c for c in line if ord(c) < 128)
            pdf.multi_cell(0, 10, safe_line)
        pdf.output("generated.pdf")
        with open("generated.pdf","rb") as f:
            st.download_button("Download PDF:",f,file_name="converted.pdf")


