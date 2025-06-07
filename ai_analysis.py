import pandas as pd

def analyze_missing_data(df):
    """
    Her sütundaki eksik değer sayısını döner.
    """
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    return missing

def detect_outliers(df, columns):
    """
    IQR yöntemi ile belirlenen sayısal sütunlardaki aykırı değerleri döner.
    """
    outliers = {}
    for col in columns:
        if col in df.columns and pd.api.types.is_numeric_dtype(df[col]):
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            outlier_mask = (df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))
            outlier_vals = df.loc[outlier_mask, col]
            if not outlier_vals.empty:
                outliers[col] = outlier_vals
    return outliers

def correlation_analysis(df, threshold=0.7):
    """
    Belirli bir eşik değerinden yüksek korelasyon çiftlerini döner.
    """
    numeric_df = df.select_dtypes(include=["number"])
    corr = numeric_df.corr()
    
    strong_corrs = set()
    for col1 in corr.columns:
        for col2 in corr.columns:
            if col1 != col2 and abs(corr.loc[col1, col2]) > threshold:
                pair = tuple(sorted((col1, col2)))
                strong_corrs.add(pair)
    return list(strong_corrs)

def generate_insights(df):
    """
    Veri setine dair otomatik analiz yapar ve insight listesi döner.
    """
    insights = []
    missing = analyze_missing_data(df)
    if not missing.empty:
        insights.append(f"⚠️ Eksik değer bulunan sütunlar: {', '.join(missing.index)}")

    outliers = detect_outliers(df, df.columns)
    outlier_cols = list(outliers.keys())
    if outlier_cols:
        insights.append(f"⚠️ Aykırı değer bulunan sütunlar: {', '.join(outlier_cols)}")

    strong_corrs = correlation_analysis(df)
    if strong_corrs:
        insight_str = ', '.join([f"{c[0]} & {c[1]}" for c in strong_corrs])
        insights.append(f"📈 Güçlü korelasyonlar tespit edildi: {insight_str}")

    if not insights:
        insights.append("✅ Verinizde önemli sorun veya güçlü korelasyon bulunmamaktadır.")

    return insights
