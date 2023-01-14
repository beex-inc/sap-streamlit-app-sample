import streamlit as st
import pandas as pd

from top import sap_connection

# 汎用モジュールの結果をパースする処理
def parse_table(raw_data, fields):
    for raw_row in raw_data:
        row = []
        for f in fields:
            offset = int(f["OFFSET"])
            length = int(f["LENGTH"])
            row += [raw_row["WA"][offset : offset + length]]
        yield row


st.markdown(
    """
# Read Table
"""
)
# サイドバーの入力欄の定義と値取得
table_name = st.sidebar.text_input("SAP Table Name")

# テーブル名が入力された時にデータを読み込み
if table_name:
    # 汎用モジュールRFC_READ_TABLEを実行
    cvers_tab = sap_connection.call("RFC_READ_TABLE", QUERY_TABLE=table_name)

    # DataFrame作成に必要な情報を準備
    raw_data = cvers_tab["DATA"]
    fields = cvers_tab["FIELDS"]
    columns = [c["FIELDNAME"] for c in fields]
    parsed_rows = parse_table(raw_data, fields)

    # DataFrame作成
    df = pd.DataFrame(data=parsed_rows, columns=columns)
    st.dataframe(df)
