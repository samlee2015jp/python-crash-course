import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# 初期データの設定 (初期表示用のリスト)
# ---------------------------------------------------------
initial_data = [
    {"公司类型": "受託会社", "公司名字": "A株式会社"},
    {"公司类型": "受託会社", "公司名字": "B株式会社"},
    {"公司类型": "委託会社", "公司名字": "C株式会社"},
]

# リストをDataFrameに変換
df = pd.DataFrame(initial_data)

st.title("🏢 会社情報エディタ")
st.markdown("---")

# ---------------------------------------------------------
# st.data_editor の設定
# ---------------------------------------------------------
# num_rows="dynamic" により、行の追加・削除が可能になります
edited_df = st.data_editor(
    df,
    num_rows="dynamic",      # 行の動的追加を許可
    use_container_width=True, # 画面幅いっぱいに表示
    column_config={
        "公司类型": st.column_config.SelectboxColumn(
            "会社タイプ",        # カラムの表示名
            help="会社の役割を選択してください",
            options=["受託会社", "委託会社", "その他"], # ドロップダウンの選択肢
            required=True,      # 入力必須項目
        ),
        "公司名字": st.column_config.TextColumn(
            "会社名",           # カラムの表示名
            # 注意: Streamlitのバージョンが古い場合は placeholder を削除してください
            # placeholder="会社名を入力...", 
            required=True,      # 入力必須項目
        )
    },
    key="company_editor"
)

# ---------------------------------------------------------
# データの保存処理 (辞書形式への変換)
# ---------------------------------------------------------
if st.button("💾 データを保存して更新"):
    # 編集後のデータを辞書形式に変換するロジック
    # 例: {'受託会社': ['A社', 'B社'], '委託会社': ['C社']}
    final_dict = {}
    
    for _, row in edited_df.iterrows():
        c_type = row["公司类型"]
        c_name = row["公司名字"]
        
        # 会社名が空でない場合のみ処理
        if pd.notna(c_name) and str(c_name).strip() != "":
            if c_type not in final_dict:
                final_dict[c_type] = []
            final_dict[c_type].append(c_name)
    
    # 保存完了の通知
    st.success("データの更新が完了しました！")
    
    # 変換後のデータを確認用に表示
    st.write("### 変換後のデータ構造:")
    st.json(final_dict)

# ---------------------------------------------------------
# 補足: PDFの置換ロジックなど、次のステップへ
# ---------------------------------------------------------