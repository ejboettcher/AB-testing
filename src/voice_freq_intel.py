import pandas as pd
import matplotlib.pyplot as plt


def men_women_date():
    freq = pd.DataFrame()
    freq['band'] = [250, 500, 700, 1000, 1400, 2000, 2800]
    freq["men"] = [12, 18, 21, 20, 19, 18, 18]
    freq["women"] = [15, 18, 21, 21, 21, 20, 20]
    return freq