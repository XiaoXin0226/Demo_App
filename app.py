import streamlit as st
from streamlit_option_menu import option_menu

st.title('Hello, Students!')
st.write('This is your Python Programming course.')

with st.sidebar:
    selected=option_menu(
        menu_title = "Menu",
        options = ["Home", "About", "Contact"],
        icons = ["1-circle-fill",
                 "2-circle-fill",
                 "3-circle-fill"],
        menu_icon= "emoji-smile-fill",
        default_index=0,
    )

if selected == "Home":
    st.title(f"Welcome to the {selected} page.")

if selected == "About":
    st.title(f"Welcome to the {selected} page.")

if selected == "Contact":
    st.title(f"Welcome to the {selected} page.")
# Once loading is complete, display the final message
placeholder.write("Data loading complete. Displaying business insights.")

# Display dynamic business insights
business_insights = [
    "Revenue increased by 15% in Q1 2024.",
    "Customer satisfaction improved by 10%.",
    "Market trends show a growing demand for eco-friendly products."
]
for insight in business_insights:
    placeholder.write(insight)
    time.sleep(2)
