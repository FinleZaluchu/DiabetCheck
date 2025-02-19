import streamlit as st

def classify_glucose(level, condition):
    if condition == "Setelah Puasa":
        if level < 77:
            return "Hipoglikemia (Di Bawah Normal)", "⚠️ Kadar gula darah Anda terlalu rendah!"
        elif 77 <= level <= 99:
            return "Normal ✅", "Gula darah Anda dalam rentang normal. Pertahankan pola hidup sehat!"
        elif 100 <= level <= 125:
            return "Pra-diabetes ⚠️", "Anda berada di tahap pra-diabetes. Waspada dan mulai perbaiki gaya hidup."
        else:
            return "Diabetes 🆘", "Kadar gula darah tinggi! Segera konsultasikan dengan tenaga medis."
    elif condition in ["2 Jam Setelah Makan", "Random"]:
        if level < 70:
            return "Hipoglikemia (Di Bawah Normal)", "⚠️ Kadar gula darah Anda terlalu rendah!"
        elif 70 <= level <= 139:
            return "Normal ✅", "Gula darah Anda dalam rentang normal. Pertahankan pola hidup sehat!"
        elif 140 <= level <= 199:
            return "Pra-diabetes ⚠️", "Anda berada di tahap pra-diabetes. Waspada dan mulai perbaiki gaya hidup."
        else:
            return "Diabetes 🆘", "Kadar gula darah tinggi! Segera konsultasikan dengan tenaga medis."

def main():
    st.set_page_config(page_title="Cek Gula Darah", layout="wide")
    
    if "page" not in st.session_state:
        st.session_state["page"] = "Input Gula Darah"
    
    pages = ["Input Gula Darah", "Hasil Analisis", "Saran Hidup Sehat"]
    st.sidebar.selectbox("Pilih Halaman", pages, index=pages.index(st.session_state["page"]))
    
    if st.session_state["page"] == "Input Gula Darah":
        st.title("💉 Cek Kadar Gula Darah")
        st.markdown("Masukkan kadar gula darah Anda untuk mengetahui kategori kesehatan.")
        
        glucose_level = st.number_input("Masukkan kadar gula darah Anda (mg/dL):", min_value=0, step=1)
        
        test_condition = st.radio("Pilih kondisi pengukuran:", ["Setelah Puasa", "2 Jam Setelah Makan", "Random"])
        
        if st.button("Cek Hasil", use_container_width=True):
            st.session_state["glucose"] = glucose_level
            st.session_state["test_condition"] = test_condition
            st.session_state["page"] = "Hasil Analisis"
            st.rerun()
    
    elif st.session_state["page"] == "Hasil Analisis":
        st.title("📊 Hasil Analisis Gula Darah")
        if "glucose" in st.session_state and "test_condition" in st.session_state:
            category, message = classify_glucose(st.session_state["glucose"], st.session_state["test_condition"])
            with st.expander(f"📌 {category}"):
                st.write(message)
        else:
            st.warning("Silakan masukkan kadar gula darah di halaman Input terlebih dahulu.")
        
        if st.button("Lihat Saran", use_container_width=True):
            st.session_state["page"] = "Saran Hidup Sehat"
            st.rerun()
    
    elif st.session_state["page"] == "Saran Hidup Sehat":
        st.title("💡 Saran Hidup Sehat")
        st.write("Berikut beberapa tips untuk menjaga kadar gula darah tetap sehat:")
        
        saran_list = [
            ("🍎 Pola Makan Sehat", "Kurangi konsumsi gula dan karbohidrat sederhana."),
            ("🏃 Rutin Berolahraga", "Minimal 30 menit sehari."),
            ("💧 Cukupi Cairan", "Minum air putih yang cukup."),
            ("💤 Tidur yang Berkualitas", "Usahakan tidur 7-9 jam per malam."),
            ("🚫 Kurangi Stres", "Lakukan meditasi atau aktivitas menyenangkan.")
        ]
        
        for title, description in saran_list:
            with st.expander(f"{title}"):
                st.write(description)
        
        if st.button("Mulai Ulang", use_container_width=True):
            st.session_state["page"] = "Input Gula Darah"
            st.rerun()

if __name__ == "__main__":
    main()
