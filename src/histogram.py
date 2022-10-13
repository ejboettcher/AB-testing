import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def histogram():
    n = 500
    y = np.random.normal(loc=0.0, scale=1.0, size=(1, n, 1))
    df = pd.DataFrame(y[0])
    return df


def plot(df, vline=-1.64):
    font = {'family': 'Calibri',
            'weight': 'bold',
            'size': 20}
    plt.rc('font', **font)
    fig, axs = plt.subplots(1, 1)
    df = df.rename(columns={0: "(B-A)/SE"})
    df.plot.hist(bins=30, ax=axs,)
    axs.set_title("z-score: 20% Rule", size=24)
    axs.set_xlabel("Z-score")
    axs.set_ylabel("")
    plt.yticks([])
    plt.axvline(x=vline, color='r', label='20%',
                linestyle="--", linewidth=5,
                )

    axs.legend()
    plt.show()


if __name__=="__main__":
    df = histogram()
    plot(df, 0.84)
