import streamlit as st
st.title("แอปพลิเคชั่นแปลงปี พ.ศ. เป็น ค.ส.")

bh_year=st.number_input("กรอกปี พ.ศ. ที่ต้องการเปลี่ยน",value=2569)
ce_year=bh_year-543
st.header(f"ปี ค.ส. คือ : {ce_year}")
