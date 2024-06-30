import pandas as pd
import openai
import time
from data_handling import get_desc_column, get_creditcard_entry, get_bank_acc_entry, get_revolut_entry, get_label_column 
from classifier import get_label, get_categories


dfs = [] #list of dataframes
dfs.append(get_creditcard_entry())
dfs.append(get_bank_acc_entry())
dfs.append(get_revolut_entry())

conc_df = pd.concat(dfs,
    axis=0,
    join="outer",
    verify_integrity=False,
    copy=True)

conc_df[get_label_column()] = None
conc_df.reset_index(drop=True, inplace=True)

chunk_size = 20
# Creazione della lista di dataframe divisi in chunk
list_df = [conc_df[i:i+chunk_size] for i in range(0, conc_df.shape[0], chunk_size)]

for i, data_chunk in enumerate(list_df):
    csv_text= data_chunk.to_csv(index=True)
    print(csv_text)
    get_categories(csv_text)
    time.sleep(5)


#print(csv_text)

#for index, row in conc_df.iterrows(): 
#    #label = str(get_label(row[get_desc_column()])) #Uncomment this line to enable GPT
#    label = str('') #Comment this line to enable GPT
#    conc_df.at[index, get_label_column()] = label
#    print(str(row[get_desc_column()]) + ' - ' + label)
#    time.sleep(0.5)

conc_df.to_excel('files/output.xlsx', index=False)