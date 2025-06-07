import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_heatmap(df):
    numeric_df = df.select_dtypes(include='number')
    if numeric_df.empty:
        st.warning("Sayısal sütun bulunamadı, heatmap çizilemiyor.")
        return
    corr = numeric_df.corr()
    fig, ax = plt.subplots(figsize=(10,8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
    ax.set_title("Korelasyon Matrisi (Heatmap)")
    st.pyplot(fig)

def plot_pairplot(df, columns):
    if len(columns) < 2:
        st.warning("En az 2 sütun seçilmeli.")
        return
    fig = sns.pairplot(df[columns].dropna())
    st.pyplot(fig)

def plot_barplot(df, category_col, numeric_col):
    if category_col not in df.columns or numeric_col not in df.columns:
        st.warning("Seçilen sütunlar veri setinde bulunamadı.")
        return
    fig, ax = plt.subplots()
    sns.barplot(x=category_col, y=numeric_col, data=df, ax=ax)
    ax.set_title(f"Barplot: {category_col} vs {numeric_col}")
    st.pyplot(fig)

def plot_lineplot(df, x_col, y_col):
    if x_col not in df.columns or y_col not in df.columns:
        st.warning("Seçilen sütunlar veri setinde bulunamadı.")
        return
    fig, ax = plt.subplots()
    sns.lineplot(x=df[x_col], y=df[y_col], ax=ax)
    ax.set_title(f"Line Plot: {x_col} vs {y_col}")
    st.pyplot(fig)

def plot_histogram(df, column):
    if column not in df.columns:
        st.warning("Seçilen sütun veri setinde bulunamadı.")
        return
    fig, ax = plt.subplots()
    sns.histplot(df[column].dropna(), kde=True, ax=ax)
    ax.set_title(f"Histogram: {column}")
    st.pyplot(fig)

def plot_boxplot(df, column):
    if column not in df.columns:
        st.warning("Seçilen sütun veri setinde bulunamadı.")
        return
    fig, ax = plt.subplots()
    sns.boxplot(x=df[column], ax=ax)
    ax.set_title(f"Boxplot: {column}")
    st.pyplot(fig)

def plot_scatter(df, x_col, y_col):
    if x_col not in df.columns or y_col not in df.columns:
        st.warning("Seçilen sütunlar veri setinde bulunamadı.")
        return
    fig, ax = plt.subplots()
    sns.scatterplot(x=df[x_col], y=df[y_col], ax=ax)
    ax.set_title(f"Scatter Plot: {x_col} vs {y_col}")
    st.pyplot(fig)
