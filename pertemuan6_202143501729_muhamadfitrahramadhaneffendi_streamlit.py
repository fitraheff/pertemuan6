


import streamlit as st
import joblib
import time
from sklearn.preprocessing import LabelEncoder


# Path menuju model di Google Drive
model_path = 'logistic_regression_model.joblib'

# Load model
model = joblib.load(model_path)

# Opsi untuk fitur-fitur yang diperlukan
color_op = ('Cool', 'Neutral', 'Warm')
music_genre_op = ('Rock', 'Hip hop', 'Folk/Traditional', 'Jazz/Blues', 'Pop', 'Electronic', 'R&B and soul')
beverage_op = ('Vodka', 'Wine', 'Whiskey', "Doesn't drink", 'Beer', 'Other')
soft_drink_op = ('7UP/Sprite', 'Coca Cola/Pepsi', 'Fanta', 'Other')

# Mapping untuk fitur-fitur
color_map = {'Cool': 1, 'Neutral': 2, 'Warm': 3}
music_genre_map = {'Rock': 1, 'Hip hop': 2, 'Folk/Traditional': 3, 'Jazz/Blues': 4, 'Pop': 5, 'Electronic': 6, 'R&B and soul': 7}
beverage_map = {'Vodka': 1, 'Wine': 2, 'Whiskey': 3, "Doesn't drink": 4, 'Beer': 5, 'Other': 6}
soft_drink_map = {'7UP/Sprite': 1, 'Coca Cola/Pepsi': 2, 'Fanta': 3, 'Other': 4}

# Tampilkan judul aplikasi
st.title('Gender Prediction App')

# Tambahkan input untuk fitur-fitur yang diperlukan
fav_color = st.selectbox("Favorite Color", color_op, index=None, placeholder="Select Favorite Color...")
fav_music_genre = st.selectbox("Favorite Music Genre", music_genre_op, index=None, placeholder="Select Favorite Music Genre...")
fav_beverage = st.selectbox("Favorite Beverage", beverage_op, index=None, placeholder="Select Favorite Beverage...")
fav_soft_drink = st.selectbox("Favorite Soft Drink", soft_drink_op, index=None, placeholder="Select Favorite Soft Drink...")

# Jika tombol "Predict" ditekan
if st.button("Predict", type="primary"):
    # Tampilkan animasi loading
    with st.spinner('Processing...'):
        # Proses prediksi
        time.sleep(2)  # Contoh proses yang memakan waktu selama 2 detik

    # Ubah nilai berdasarkan pilihan yang dipilih
    color_selected = color_map.get(fav_color)
    music_genre_selected = music_genre_map.get(fav_music_genre)
    beverage_selected = beverage_map.get(fav_beverage)
    soft_drink_selected = soft_drink_map.get(fav_soft_drink)

    # Lakukan prediksi
    predicted_rest = model.predict([[color_selected, music_genre_selected, beverage_selected, soft_drink_selected]])

    # Tampilkan hasil prediksi
    if predicted_rest[0] == 1:
        st.title(':red[Female]')
    else:
        st.title(':blue[Male]')
