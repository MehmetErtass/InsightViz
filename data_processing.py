import pandas as pd

def load_data(uploaded_file):
    """
    Yüklenen dosyayı DataFrame olarak yükler.
    Sadece CSV veya Excel (xls, xlsx) desteklenir.
    """
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(uploaded_file)
        else:
            raise ValueError("Desteklenmeyen dosya formatı.")
    except Exception as e:
        raise IOError(f"Dosya yüklenirken hata: {e}")
    return df

def get_summary(df):
    """DataFrame'in temel istatistik özetini döner."""
    return df.describe(include='all')

def get_numeric_columns(df):
    """Sayısal sütun isimlerini listeler."""
    return df.select_dtypes(include='number').columns.tolist()

def fill_missing(df, column, method='mean'):
    """
    Belirtilen sütundaki eksik değerleri seçilen yöntemle doldurur.
    method: 'mean', 'median' veya 'mode' olabilir.
    """
    if column not in df.columns:
        raise KeyError(f"{column} sütunu bulunamadı.")
    
    df_copy = df.copy()
    
    if method == 'mean':
        fill_value = df_copy[column].mean()
    elif method == 'median':
        fill_value = df_copy[column].median()
    elif method == 'mode':
        fill_value = df_copy[column].mode().iloc[0] if not df_copy[column].mode().empty else None
    else:
        raise ValueError("Yöntem mean, median veya mode olmalı.")
    
    if fill_value is not None:
        df_copy[column] = df_copy[column].fillna(fill_value)
    return df_copy

def one_hot_encode(df, column):
    """
    Belirtilen kategori sütununu one-hot encode eder.
    """
    if column not in df.columns:
        raise KeyError(f"{column} sütunu bulunamadı.")
    df_copy = df.copy()
    dummies = pd.get_dummies(df_copy[column], prefix=column)
    df_copy = pd.concat([df_copy, dummies], axis=1)
    df_copy.drop(column, axis=1, inplace=True)
    return df_copy

def drop_columns(df, columns):
    """
    Belirtilen sütunları düşürür.
    """
    df_copy = df.copy()
    missing_cols = [col for col in columns if col not in df_copy.columns]
    if missing_cols:
        raise KeyError(f"Silinmek istenen sütunlar bulunamadı: {missing_cols}")
    df_copy.drop(columns, axis=1, inplace=True)
    return df_copy

def rename_columns(df, columns_map):
    """
    Sütun isimlerini yeniden adlandırır.
    columns_map: dict şeklinde {eski_ad: yeni_ad}
    """
    df_copy = df.copy()
    df_copy.rename(columns=columns_map, inplace=True)
    return df_copy
