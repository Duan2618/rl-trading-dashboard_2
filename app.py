import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="RL Trading Dashboard", layout="wide")
st.title("📈 Hiệu suất học của Agent Reinforcement Learning")

df = pd.read_csv("rl_log.csv")

st.subheader("📊 Tổng quan hiệu suất")
col1, col2, col3 = st.columns(3)
col1.metric("Tổng bước", len(df))
col2.metric("Tổng lợi nhuận", round(df['reward'].sum(), 2))
col3.metric("Số lệnh mua", (df['action'] == 1).sum())

st.subheader("🎯 Reward theo thời gian")
st.plotly_chart(px.line(df, x="step", y="reward"), use_container_width=True)

st.subheader("🧠 Hành động của Agent")
st.plotly_chart(px.scatter(df, x="step", y="action", color="action"), use_container_width=True)

st.subheader("💰 Biến động số dư")
st.plotly_chart(px.line(df, x="step", y="balance"), use_container_width=True)
