# from constants import ___


def get_avg_currency_rate(rates_history: list[float]) -> float:
    '''Calculate the average currency rate from a list of rates.'''
    if rates_history:
        return round(sum(rates_history) / len(rates_history), 1)
    return 0.0

if __name__ == "__main__":
    assert get_avg_currency_rate(rates_history=[30.2, 31.6, 29.0]) == 30.3
