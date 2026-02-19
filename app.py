import datetime
import streamlit as st
from add_update_tab import add_update_ui
from analtyics_ui import analytics_tab
st.title("Expense Tracking System")
tab1, tab2 = st.tabs(["Add/Update", "Analytics"])

with tab1:
    add_update_ui()

with tab2:
    analytics_tab()
