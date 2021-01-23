import pandas as pd
import numpy as np
import os, pdb

path = {'fert': os.getcwd() + '\\raw_data\\county_fertilizer_panel.csv',
        'fuel': os.getcwd() + '\\raw_data\\county_fuel_panel.csv',
        'labo': os.getcwd() + '\\raw_data\\county_labor_panel.csv',
        'land': os.getcwd() + '\\raw_data\\county_land_panel.csv',
        'mach': os.getcwd() + '\\raw_data\\county_machinery_panel.csv',
        'neti': os.getcwd() + '\\raw_data\\county_net_income_panel.csv',
        'trac': os.getcwd() + '\\raw_data\\county_tractors_panel.csv',
        'truc': os.getcwd() + '\\raw_data\\county_trucks_panel.csv'}

def fixStateAnsi(df): 
    new = [] 
    for i in df['State ANSI']: 
        i = str(i) 
        num = 3 - len(i)
        i = '0'*num + i
        new.append(i)
    df['State ANSI'] = new
    return df

def fixCountyAnsi(df): 
    new = [] 
    for i in df['County ANSI']: 
        i = str(i).split('.')[0]
        num = 4 - len(i)
        i = '0'*num + i
        new.append(i)
    df['County ANSI'] = new
    return df

def createUniqueCode(df): 
    code = [] 
    for i in range(len(df)): 
        new = str(df['Year'][i]) + df['State ANSI'][i] + df['County ANSI'][i]
        code.append(new)
    df['CODE'] = code
    return df

def fixValue(df, col): 
    vals = list(df[col])
    newVals = [] 
    for v in vals: 
        if ((str(v).lower() == 'nan') or ('(d' in str(v).lower())): newVals.append('nan')
        else: 
            if ',' in v: newVals.append(int(v.replace(',', '')))
            else: newVals.append(int(v))
    df[col] = newVals
    return df

def getFert(name = 'fertilizer'): 
    te = pd.read_csv(path['fert'])
    keeps = ['Year', 'State', 'State ANSI', 'County', 'County ANSI', 'Value']
    te = te[keeps]
    te.columns = [i for i in keeps[:-1]] + [name]
    te = fixStateAnsi(te) 
    te = fixCountyAnsi(te)
    te = createUniqueCode(te)
    te = fixValue(te, 'fertilizer')
    return te

def getFuel(df, name = 'fuel'): 
    te = pd.read_csv(path['fuel'])
    keeps = ['Year', 'State', 'State ANSI', 'County', 'County ANSI', 'Value']
    te = te[keeps]
    te.columns = [i for i in keeps[:-1]] + [name]

    te = fixStateAnsi(te) 
    te = fixCountyAnsi(te)
    te = createUniqueCode(te)
    te = fixValue(te, 'fuel')
    te = te[[i for i in te.columns if i not in ['State ANSI', 'County ANSI', 'State', 'County', 'Year']]]

    df = pd.merge(df, te, how = 'outer', on = 'CODE')
    return df

def getLabor(df, name = 'labor'): 
    te = pd.read_csv(path['labo'])
    keeps = ['Year', 'State', 'State ANSI', 'County', 'County ANSI', 'Data Item', 'Value']
    te = te[keeps]
    te.columns = [i for i in keeps[:-1]] + [name]

    te = fixStateAnsi(te) 
    te = fixCountyAnsi(te)
    te = createUniqueCode(te)
    te = fixValue(te, 'labor')
    te['labor'] = [0 if i == 'nan' else int(i) for i in te['labor']]
    te = te[['CODE', 'labor']].groupby(['CODE']).sum()
    df = pd.merge(df, te, how = 'outer', on = 'CODE')
    return df

def getLand(df, name = 'land'): 
    te = pd.read_csv(path['land'])
    keeps = ['Year', 'State', 'State ANSI', 'County', 'County ANSI', 'Value']
    te = te[keeps]
    te.columns = [i for i in keeps[:-1]] + [name]

    te = fixStateAnsi(te) 
    te = fixCountyAnsi(te)
    te = createUniqueCode(te)
    te = fixValue(te, 'land')
    te = te[[i for i in te.columns if i not in ['State ANSI', 'County ANSI', 'State', 'County', 'Year']]]

    df = pd.merge(df, te, how = 'outer', on = 'CODE')
    return df

def getMach(df, name = 'mach'):
    te = pd.read_csv(path['mach'])
    keeps = ['Year', 'State', 'State ANSI', 'County', 'County ANSI', 'Value']
    te = te[keeps]
    te.columns = [i for i in keeps[:-1]] + [name]

    te = fixStateAnsi(te) 
    te = fixCountyAnsi(te)
    te = createUniqueCode(te)
    te = fixValue(te, 'mach')
    te = te[[i for i in te.columns if i not in ['State ANSI', 'County ANSI', 'State', 'County', 'Year']]]

    df = pd.merge(df, te, how = 'outer', on = 'CODE')
    return df   

def getIncome(df, name = 'netIncome'): 
    te = pd.read_csv(path['neti'])
    keeps = ['Year', 'State', 'State ANSI', 'County', 'County ANSI', 'Value']
    te = te[keeps]
    te.columns = [i for i in keeps[:-1]] + [name]

    te = fixStateAnsi(te) 
    te = fixCountyAnsi(te)
    te = createUniqueCode(te)
    te = fixValue(te, 'netIncome')
    te = te[[i for i in te.columns if i not in ['State ANSI', 'County ANSI', 'State', 'County', 'Year']]]

    df = pd.merge(df, te, how = 'outer', on = 'CODE')
    return df   

def getTractors(df, name = 'tractors'): 
    te = pd.read_csv(path['trac'])
    keeps = ['Year', 'State', 'State ANSI', 'County', 'County ANSI', 'Value']
    te = te[keeps]
    te.columns = [i for i in keeps[:-1]] + [name]

    te = fixStateAnsi(te) 
    te = fixCountyAnsi(te)
    te = createUniqueCode(te)
    te = fixValue(te, 'tractors')
    te = te[[i for i in te.columns if i not in ['State ANSI', 'County ANSI', 'State', 'County', 'Year']]]

    df = pd.merge(df, te, how = 'outer', on = 'CODE')
    return df  

def getTrucks(df, name = 'trucks'):
    pdb.set_trace() 
    te = pd.read_csv(path['truc'])
    keeps = ['Year', 'State', 'State ANSI', 'County', 'County ANSI', 'Value']
    te = te[keeps]
    te.columns = [i for i in keeps[:-1]] + [name]

    te = fixStateAnsi(te) 
    te = fixCountyAnsi(te)
    te = createUniqueCode(te)
    te = fixValue(te, 'trucks')
    te = te[[i for i in te.columns if i not in ['State ANSI', 'County ANSI', 'State', 'County', 'Year']]]

    df = pd.merge(df, te, how = 'outer', on = 'CODE')
    return df   

def yearFilter(df): 
    df = df[df['Year'] >2002].reset_index().drop(['index'], axis = 1)
    return df

def imputation(df): 
    pdb.set_trace()

def main(): 
    df = getFert()
    df = getFuel(df)
    df = getLabor(df)
    df = getLand(df)
    df = getMach(df)
    df = getIncome(df)
    df = getTractors(df)
    df = getTrucks(df)
    df = yearFilter(df)
    df = imputation(df)
    df.to_csv('raw_data_county.csv', index = None)

main()