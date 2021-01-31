import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})
import seaborn as sns
import os, pdb
from datetime import date, datetime

"""
Imports the rates dataset (importData)
Generates the time series plot (getLinePlot)
"""

dataSet = os.getcwd() + '\\topolRate\\data\\rates.csv'
outPath = os.getcwd() + '\\topolRate\\data\\'

def importData(path): 
    df = pd.read_csv(path)
    df['Date'] = [datetime(int('20' + da.split('/')[2]), int(da.split('/')[0]) , int(da.split('/')[1])) for da in df['Date']]
    df = df.sort_values(by=['Date'])
    df = df[[i for i in df.columns if i != '2 Mo']]
    df.columns = [i.replace(' ', '_') for i in df.columns]
    return df

def getLinePlot(df, outPath): 
    cols = [i for i in df.columns if i not in ['Date', '1_Mo', '30_Yr']]
    for col in cols: 
        plt.plot(df['Date'], df[col], marker='', color='grey', linewidth=1, alpha=0.9)
    plt.plot(df['Date'], df['1_Mo'], marker='', color='red', linewidth=1, alpha=1, label = "1 Mo")
    plt.plot(df['Date'], df['30_Yr'], marker='', color='blue', linewidth=1, alpha=1, label= "30 Yr")

    plt.legend()
    plt.xlabel("Date")
    plt.ylabel("Rate")
    plt.savefig(outPath + 'treasuryRatesVis.pgf')

def main(): 
    df = importData(dataSet)
    getLinePlot(df, outPath)


main()
