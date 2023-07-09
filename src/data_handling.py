import pandas as pd

def get_data_column():
    return 'data'

def get_desc_column():
    return 'desc'

def get_amount_column():
    return 'amount'

def get_source_column():
    return 'source'

def get_label_column():
    return 'label'

def get_creditcard_entry():
    df = pd.read_excel('files/I movimenti della mia carta.xlsx',skiprows=16, header=0)
    datacol = ['DATA OP.', 'CAUSALE', 'IMPORTO (€)']
    df = df.reindex(columns=datacol)
    column_mapping = {'DATA OP.': get_data_column(),
                      'CAUSALE': get_desc_column(),
                      'IMPORTO (€)': get_amount_column()}
    df = df.rename(columns=column_mapping)
    df = df.dropna(subset=get_data_column())
    df[get_source_column()] = 'CRC'
    return df

def get_bank_acc_entry():
    df = pd.read_excel('files/I miei movimenti conto.xlsx',skiprows=18, header=0)
    datacol = ['DATA CONT.', 'DESCRIZIONE','IMPORTO (€)(€)']
    df = df.reindex(columns=datacol)
    column_mapping = {'DATA CONT.': get_data_column(),
                      'DESCRIZIONE': get_desc_column(),
                      'IMPORTO (€)(€)': get_amount_column()}
    df = df.rename(columns=column_mapping)
    df = df.dropna(subset=get_data_column())
    df[get_source_column()] = 'WID'
    return df

def get_revolut_entry():
    df = pd.read_excel('files\\account-statement.xlsx')
    datacol = ['Started Date', 'Description','Amount']
    df = df.reindex(columns=datacol)
    column_mapping = {'Started Date': get_data_column(),
                      'Description': get_desc_column(),
                      'Amount': get_amount_column()}
    df = df.rename(columns=column_mapping)
    df = df.dropna(subset=get_data_column())
    df[get_source_column()] = 'REV'
    
    # Divide all values in the 'Amount' column by 2
    df[get_amount_column()] = df[get_amount_column()] / 2

    return df
