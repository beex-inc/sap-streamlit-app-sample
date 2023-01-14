import sys
import argparse
import streamlit as st
from pyrfc import Connection

# 引数を取得
parser = argparse.ArgumentParser()
parser.add_argument("--host", required=True)
parser.add_argument("--sysnr", required=True)
parser.add_argument("--client", required=True)
parser.add_argument("--user", required=True)
parser.add_argument("--password", required=True)
try:
    args = parser.parse_args()
except SystemExit as e:
    sys.exit(e.code)


# 引数の情報を利用しSAP接続作成
sap_connection = Connection(
    ashost=args.host,
    sysnr=args.sysnr,
    client=args.client,
    user=args.user,
    passwd=args.password,
)


st.markdown(
    """
# Top
## Connection Infomation
"""
)
st.write(sap_connection.get_connection_attributes())
