import streamlit as st

st.title("Ini Title")
st.text("1242134131")

nama = st.text_input("Nama", "dia")
NIM = st.text_input("NIM", "ini 10 digit")

if nama:
    st.text("Nama : "+nama)
    if len(NIM) != 10:
        NIM = "Tidak Valid"
    st.text("NIM : "+NIM)

inikotak = st.selectbox('Pilih Jurusan', ['RPL', 'DS','TI'])

st.write(inikotak)

Umur = st.slider("Umur",1,70,30)

st.write(Umur)

Gender = st.radio('Gender',['Pria','Wanita'])

if Gender == "Pria":
    st.write("Selamat Datang Bapak ", nama)
else:
    st.write("Selamat Datang Ibu ", nama)

list_hobi = st.text_area("Hobi",'Main bola, Main Game')
list_hobi = [x.strip() for x in list_hobi.split('Main')]

st.write(list_hobi)


st.image('https://4.bp.blogspot.com/-t_Zwx276KNI/U1Z9LG0f_ZI/AAAAAAAAGus/XwpyJwdmt-w/s1600/gambar+ikan+mas.jpg', width=500, caption="ini ikan")

st.markdown('[ini link ke bing](https://www.bing.com/?FORM=Z9FD1)')

import pandas as pd 

data = {'Pekerjaan' : ['Proggrammer', 'Dokter', 'Pengacara'],
        'Tier': ["E","SS","A"]}

df = pd.DataFrame(data)

st.dataframe(df,use_container_width=True)


st.title("Buka Data")
file = st.file_uploader('Pilih file', type=['jpg','csv','png'])

if file is not None:
    st.write(file.type)
    if file.type == "image/jpeg" or file.type == "image/png":
        st.image(file)
    else:
        data = pd.read_csv(file)

        st.dataframe(data)

st.title("Kalkulator")

angka1 = st.number_input("Masukan angka 1 ", value=0)
angka2 = st.number_input("Masukan angka 2 ", value=0)  
 
operasi = st.radio('Pilih Operasi',["Penjumplahan (+)","Pengurangan (-)","Perkalian (*)", "Pembagian (/)"])

if st.button('hitung'):
    if operasi == "Penjumplahan (+)":
        hasil = angka1 + angka2
    elif operasi == "Pengurangan (-)":
        hasil = angka1 - angka2
    elif operasi == "Perkalian (*)":
        hasil = angka1 * angka2
    elif operasi == "Pembagian (/)":
        hasil = angka1 / angka2

    st.success(f'Hasil {operasi} : {hasil}')


st.sidebar.header('fitur kiri')

if st.sidebar.checkbox('Biodata'):
    st.sidebar.write(f'Nama : {nama}')