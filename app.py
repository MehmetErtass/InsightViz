import streamlit as st
from data_processing import (
    load_data, get_summary, get_numeric_columns,
    fill_missing, one_hot_encode, drop_columns, rename_columns
)
from visualization import (
    plot_histogram, plot_boxplot, plot_scatter,
    plot_heatmap, plot_pairplot, plot_barplot, plot_lineplot
)
from ai_analysis import generate_insights
from utils import validate_numeric_selection

def main():
    st.set_page_config(page_title="Profesyonel Veri Analizi & Görselleştirme", layout="wide")
    st.title("📊 Veri Analizi ve Görselleştirme Aracı")
    st.write("Kod yazmadan verinizi yükleyip, hızlıca analiz ve grafik oluşturabilirsiniz.")

    # Dosya yükleme ve dataframe session_state'de tutma
    uploaded_file = st.file_uploader("CSV veya Excel dosyanızı yükleyin", type=['csv', 'xls', 'xlsx'])
    if uploaded_file:
        if "df" not in st.session_state or st.session_state.get("uploaded_file_name") != uploaded_file.name:
            try:
                st.session_state.df = load_data(uploaded_file)
                st.session_state.uploaded_file_name = uploaded_file.name
            except Exception as e:
                st.error(f"Dosya yüklenirken hata oluştu: {e}")
                return
    else:
        st.info("Lütfen analiz etmek için dosya yükleyin.")
        return

    df = st.session_state.df

    st.subheader("📋 Veri Önizleme")
    st.dataframe(df.head())

    st.subheader("🛠️ Veri Ön İşleme")
    preprocessing_action = st.selectbox("Yapmak istediğiniz işlemi seçin", [
        "Eksik değerleri doldur",
        "Sütun ekle",
        "Sütun sil",
        "Sütun yeniden adlandır",
        "One-Hot Encode (Kategorik sütun)"
    ])

    if preprocessing_action == "Eksik değerleri doldur":
        numeric_cols = get_numeric_columns(df)
        if numeric_cols:
            col = st.selectbox("Eksik değer doldurulacak sütunu seçin", numeric_cols)
            method = st.selectbox("Doldurma yöntemi seçin", ['mean', 'median', 'mode'])
            if st.button("Doldur"):
                try:
                    df = fill_missing(df, col, method)
                    st.session_state.df = df
                    st.success(f"{col} sütunundaki eksik değerler {method} ile dolduruldu.")
                except Exception as e:
                    st.error(str(e))
        else:
            st.warning("Eksik değer doldurmak için sayısal sütun bulunamadı.")

    elif preprocessing_action == "Sütun ekle":
        new_col_name = st.text_input("Yeni sütun adı")
        new_col_values = st.text_area("Yeni sütun değerlerini virgülle ayrılmış şekilde girin (ör: 1,2,3,4)")
        if st.button("Sütun Ekle"):
            if not new_col_name:
                st.error("Sütun adı boş olamaz.")
            elif new_col_name in df.columns:
                st.error(f"'{new_col_name}' adlı sütun zaten mevcut.")
            else:
                try:
                    values_list = [v.strip() for v in new_col_values.split(',')]
                    if len(values_list) != len(df):
                        st.error(f"Veri uzunluğu ({len(values_list)}) ile DataFrame satır sayısı ({len(df)}) uyuşmuyor.")
                    else:
                        df[new_col_name] = values_list
                        st.session_state.df = df
                        st.success(f"{new_col_name} sütunu başarıyla eklendi.")
                except Exception as e:
                    st.error(f"Sütun eklenirken hata: {e}")

    elif preprocessing_action == "Sütun sil":
        cols_to_drop = st.multiselect("Silmek istediğiniz sütunları seçin", df.columns)
        if st.button("Sütunları Sil"):
            if not cols_to_drop:
                st.error("En az bir sütun seçmelisiniz.")
            else:
                try:
                    df = drop_columns(df, cols_to_drop)
                    st.session_state.df = df
                    st.success(f"Seçilen sütunlar ({', '.join(cols_to_drop)}) başarıyla silindi.")
                except Exception as e:
                    st.error(f"Sütun silme sırasında hata: {e}")

    elif preprocessing_action == "Sütun yeniden adlandır":
        st.write("Yeniden adlandırmak istediğiniz sütunlar ve yeni isimlerini girin:")
        rename_old = st.selectbox("Değiştirilecek sütun", df.columns)
        rename_new = st.text_input("Yeni sütun adı")
        if st.button("Sütunu Yeniden Adlandır"):
            if not rename_new:
                st.error("Yeni sütun adı boş olamaz.")
            elif rename_new in df.columns and rename_new != rename_old:
                st.error(f"'{rename_new}' adlı sütun zaten mevcut. Farklı bir isim girin.")
            else:
                try:
                    df = rename_columns(df, {rename_old: rename_new})
                    st.session_state.df = df
                    st.success(f"{rename_old} sütunu {rename_new} olarak yeniden adlandırıldı.")
                except Exception as e:
                    st.error(f"Sütun yeniden adlandırma hatası: {e}")

    elif preprocessing_action == "One-Hot Encode (Kategorik sütun)":
        cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        if not cat_cols:
            st.warning("One-Hot Encode için kategorik sütun bulunamadı.")
        else:
            col = st.selectbox("One-Hot Encode uygulanacak sütunu seçin", cat_cols)
            if st.button("Encode Et"):
                try:
                    df = one_hot_encode(df, col)
                    st.session_state.df = df
                    st.success(f"{col} sütunu one-hot encode edildi.")
                except Exception as e:
                    st.error(f"One-hot encode işlemi sırasında hata: {e}")

    # -------------------------
    # Ön işleme sonrası indirme butonu
    if "df" in st.session_state:
        csv_data = st.session_state.df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Ön İşlenmiş Veriyi İndir (CSV)",
            data=csv_data,
            file_name="on_islenmis_veri.csv",
            mime="text/csv"
        )
    # -------------------------

    st.subheader("📊 Veri Özeti")
    st.write(get_summary(st.session_state.df))

    st.subheader("📈 Veri Görselleştirme")

    chart_type = st.selectbox("Grafik türü seçin",
        ['Histogram', 'Boxplot', 'Scatter Plot', 'Heatmap', 'Pairplot', 'Barplot', 'Lineplot'])

    df = st.session_state.df  # Güncel df'yi al

    if chart_type in ['Histogram', 'Boxplot']:
        col = st.selectbox("Sütun seçin", df.columns)
        if st.button("Grafik Göster"):
            if chart_type == 'Histogram':
                plot_histogram(df, col)
            else:
                plot_boxplot(df, col)

    elif chart_type == 'Scatter Plot':
        numeric_cols = get_numeric_columns(df)
        if len(numeric_cols) < 2:
            st.warning("Scatter plot için en az 2 sayısal sütun gerekli.")
        else:
            x_col = st.selectbox("X ekseni", numeric_cols)
            y_col = st.selectbox("Y ekseni", numeric_cols)
            if st.button("Grafik Göster"):
                if not validate_numeric_selection(numeric_cols, x_col, y_col):
                    st.error("X ve Y eksenleri farklı sayısal sütunlar olmalı.")
                else:
                    plot_scatter(df, x_col, y_col)

    elif chart_type == 'Heatmap':
        if st.button("Grafik Göster"):
            plot_heatmap(df)

    elif chart_type == 'Pairplot':
        numeric_cols = get_numeric_columns(df)
        selected_cols = st.multiselect("Sütunları seçin (En az 2)", numeric_cols)
        if st.button("Grafik Göster"):
            if len(selected_cols) < 2:
                st.error("En az 2 sayısal sütun seçilmeli.")
            else:
                plot_pairplot(df, selected_cols)

    elif chart_type == 'Barplot':
        cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        num_cols = get_numeric_columns(df)
        if not cat_cols or not num_cols:
            st.warning("Barplot için kategori ve sayısal sütunlar gerekli.")
        else:
            cat_col = st.selectbox("Kategori Sütunu", cat_cols)
            num_col = st.selectbox("Sayısal Sütun", num_cols)
            if st.button("Grafik Göster"):
                plot_barplot(df, cat_col, num_col)

    elif chart_type == 'Lineplot':
        numeric_cols = get_numeric_columns(df)
        if len(numeric_cols) < 2:
            st.warning("Lineplot için en az 2 sayısal sütun gerekli.")
        else:
            x_col = st.selectbox("X ekseni", numeric_cols)
            y_col = st.selectbox("Y ekseni", numeric_cols)
            if st.button("Grafik Göster"):
                if not validate_numeric_selection(numeric_cols, x_col, y_col):
                    st.error("X ve Y eksenleri farklı sayısal sütunlar olmalı.")
                else:
                    plot_lineplot(df, x_col, y_col)

    st.subheader("🤖 AI Destekli Veri Analizi")
    if st.button("Veri Analizini Başlat"):
        insights = generate_insights(st.session_state.df)
        for insight in insights:
            st.write(insight)

if __name__ == "__main__":
    main()
