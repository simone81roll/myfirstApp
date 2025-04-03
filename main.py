import pandas as pd
import streamlit as st
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)


file_id_csv = 'https://drive.google.com/open?id=1h77OpnlSANco3oe4mO76T1iBpdtUGnDS&usp=drive_fs'
downloaded_csv = drive.CreateFile({'id': file_id_csv})
downloaded_csv = GetContentFile('music_dataset.csv')
# Carica il file CSV

def load_data(file):
    df = pd.read_csv(file, header=None, delimiter=',')
    return df

# Carica i dati
df = load_data(downloaded_csv)

# Mostra il DataFrame originale
st.write("DataFrame originale:")
new_header = df.iloc[0]  # Prendi la prima riga come nuovo header
df = df[1:]  # Prendi tutte le righe tranne la prima
df.columns = new_header  # Imposta la nuova header
st.dataframe(df)

# Salva il DataFrame aggiornato, se necessario
if st.button("Salva DataFrame"):
    df.to_csv('serieA.csv', index=False, header=False, sep='\t')
    st.success("DataFrame salvato come 'serieA.csv'!")

arrays = [
    ['Gruppo A', 'Gruppo A', 'Gruppo B', 'Gruppo B'],
    ['Colonna 1', 'Colonna 2', 'Colonna 1', 'Colonna 2']
]

index = pd.MultiIndex.from_arrays(arrays, names=('Gruppo', 'Colonna'))
data = [[1, 2], [3, 4], [5, 6], [7, 8]]

df = pd.DataFrame(data, index=index)

# Visualizziamo il DataFrame in Streamlit
st.title("DataFrame con due header")
st.dataframe(df)