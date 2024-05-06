import pandas as pd
import re

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

def semplifica_descrizione(descrizione):
    if pd.isna(descrizione):
        return ""
    # Regex per estrarre il valore desiderato da ogni tipo di descrizione
    regex_patterns = {
        "Data ": r"Ora \d{2}.\d{2} (.+?) N\.carta:",
        "Addebito Sdd N.": r"A Favore (.+?) Codice Mandato",
        "Bon. Sepa": r"A Favore (.+?) Iban",
        "Filiale Disponente": r"Ord: (.+?) Bic",
        "Importo Bonifici:": r"Benef: (.+?) Data Accettazione"
    }
    
    for tipo, regex_pattern in regex_patterns.items():
        match = re.search(regex_pattern, str(descrizione))
        if match:
            return match.group(1)
    
    return descrizione

def trim(stringa):
    # Rimuove gli spazi in eccesso all'inizio e alla fine della stringa
    return ' '.join(stringa.strip().split())

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
    df['DESCRIZIONE'] = df['DESCRIZIONE'].apply(semplifica_descrizione)
    df['DESCRIZIONE'] = df['DESCRIZIONE'].apply(trim)
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
