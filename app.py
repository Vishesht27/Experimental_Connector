# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.experimental_connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from mytable;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")


# import streamlit as st

# conn = st.experimental_connection('pets', type='sql')
# pet_owners = conn.query('select * from mytable;')
# st.dataframe(pet_owners)


import streamlit as st
import mysql.connector

@st.cache_resource
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from pet_owners;")
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")