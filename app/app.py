import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

st.title("🐾 Open Pet Care 🐾")
st.header("Pet Info Form")

# Connect to Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_dict(
    st.secrets["gcp_service_account"], scope
)
client = gspread.authorize(credentials)

# Open the sheet
spreadsheet = client.open("pet_data").sheet1

# Form
with st.form("pet_form", clear_on_submit=True):
    owner_name = st.text_input("Owner Name")
    owner_email = st.text_input("Owner Email")
    pet_name = st.text_input("Pet Name")
    species = st.selectbox("Species", ["Dog", "Cat"])
    birthdate = st.date_input("Birthdate (approximate is fine)")

    submitted = st.form_submit_button("Submit")

    if submitted:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row = [timestamp, owner_name, owner_email, pet_name, species, birthdate.strftime("%Y-%m-%d")]
        spreadsheet.append_row(row)
        st.success(f"Thanks {owner_name}, {pet_name}'s info has been saved!")

#Run: streamlit run app/app.py