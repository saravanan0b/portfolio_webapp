import csv
import streamlit as st

x = 3
y = 4

about_me = """ Saravana's unique artistic talent has helped him create many unique pieces of artwork.
 He believes that artistic expression can help people understand more about individuals around the world.
"""

with open(r"project_data\data.csv") as csvfile:
    raw_content = list(csv.reader(csvfile, delimiter=";"))

st.markdown("<h1 style='text-align: center; color: orange;'>Home</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.subheader(":blue[Myself]")
    st.image(r"project_data\images\Camo_Snapshot_2024-08-03.jpg", caption="saravanan")

with col2:
    st.subheader("About me")
    st.info(about_me)

col3, col4 = st.columns(2)

with col3:
    st.subheader(":red[Shopping-List WebApp]")
    st.image(r"project_data\images\1.png", width=192)
    st.write("https://gunapriyakumari.streamlit.app/")

with col4:
    st.subheader("Portfolio WebApp")
    st.image(r"project_data\images\2.png")
    st.write("under construction...")


for ee in range(9):

    col_i, col_j = st.columns(2)

    with col_i:
        col_i_list = raw_content[x]
        st.subheader(col_i_list[0])
        st.write(col_i_list[1])
        col_i_path = rf"project_data\images\{col_i_list[3]}"
        st.image(col_i_path)
        st.write(col_i_list[2])

    with col_j:
        col_j_list = raw_content[y]
        st.subheader(col_j_list[0])
        st.write(col_j_list[1])
        col_j_path = rf"project_data\images\{col_j_list[3]}"
        st.image(col_j_path)
        st.write(col_j_list[2])

    x += 2
    y += 2