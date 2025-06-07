def validate_numeric_selection(cols: list, x: str, y: str) -> bool:
    """
    X ve Y için farklı sayısal kolonlar seçilip seçilmediğini kontrol eder.
    """
    if x == y:
        return False
    if x not in cols or y not in cols:
        return False
    return True
