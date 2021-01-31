import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os, pdb
from datetime import date, datetime

dataSet = os.getcwd() + '\\topological_data_analysis_of_treasury_yield_curve_rates\\data\\rates.csv'
outPath = os.getcwd() + '\\topological_data_analysis_of_treasury_yield_curve_rates\\data\\'

def importData(path): 
    df = pd.read_csv(path)
    df['Date'] = [datetime(int('20' + da.split('/')[2]), int(da.split('/')[0]) , int(da.split('/')[1])) for da in df['Date']]
    df = df.sort_values(by=['Date'])
    df = df[[i for i in df.columns if i != '2 Mo']]
    df.columns = [i.replace(' ', '_') for i in df.columns]
    return df

def getLinePlot(df, outPath): 
    plt.style.use('seaborn-darkgrid')
    cols = [i for i in df.columns if i not in ['Date', '1_Mo', '30_Yr']]
    for col in cols: 
        plt.plot(df['Date'], df[col], marker='', color='grey', linewidth=1, alpha=0.9)
        nu += 1
    plt.plot(df['Date'], df['1_Mo'], marker='', color='orange', linewidth=2, alpha=1, label = "1_Mo")
    plt.plot(df['Date'], df['30_Yr'], marker='', color='blue', linewidth=2, alpha=1, label= "30_Yr")

    plt.legend()
    plt.title('Treasury Yield Curve Rates 2015-2020')
    plt.xlabel("Date")
    plt.ylabel("Rate")
    plt.savefig(outPath + 'treasuryRatesVis.png', dpi=1000)

def main(): 
    df = importData(dataSet)
    getLinePlot(df, outPath)


main()
