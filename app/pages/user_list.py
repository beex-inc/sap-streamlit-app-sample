import streamlit as st
import pandas as pd

from top import sap_connection

user_list_resp = sap_connection.call("BAPI_USER_GETLIST", MAX_ROWS=4)
records = []
for u in user_list_resp["USERLIST"]:
    user_name = u["USERNAME"]
    record = {"Name": user_name}
    res = sap_connection.call("BAPI_USER_GET_DETAIL", USERNAME=user_name)
    record.update(res["ADDRESS"])
    records.append(record)
df = pd.DataFrame.from_dict(data=records)

st.markdown(
    """
# User List
"""
)

st.dataframe(df)
