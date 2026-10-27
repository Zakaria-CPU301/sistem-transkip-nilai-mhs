import pandas as pd

def analisis_dengan_pandas():
    input_file = 'dataset-nilai-akhir-mhs.csv'
    output_file = 'hasil_analisis_pandas.csv'
    
    # 1. Membaca data dari file CSV
    print("--- 1. MEMBACA DATA DARI FILE CSV ---")
    try:
        df = pd.read_csv(input_file)
        print(f"Berhasil membaca {len(df)} baris data dari '{input_file}'.\n")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' tidak ditemukan di folder ini.")
        return

    # 2. Menampilkan data awal (5 baris pertama)
    print("--- 2. MENAMPILKAN DATA AWAL ---")
    print(df.head(5))
    print("\n")

    # 3 & 4. Memeriksa data kosong & Melakukan Pembersihan Data
    print("--- 3 & 4. PEMERIKSAAN & PEMBERSIHAN DATA ---")
    # Menghapus baris jika kolom 'Nama' atau 'Nilai' kosong (NaN)
    df_cleaned = df.dropna(subset=['Nama', 'Nilai']).copy()
    
    # Memastikan kolom nilai bertipe numerik dan membuang data di luar rentang 0-100
    df_cleaned['Nilai'] = pd.to_numeric(df_cleaned['Nilai'], errors='coerce')
    df_cleaned = df_cleaned.dropna(subset=['Nilai'])
    df_cleaned = df_cleaned[(df_cleaned['Nilai'] >= 0) & (df_cleaned['Nilai'] <= 100)]

    jumlah_awal = len(df)
    jumlah_valid = len(df_cleaned)
    invalid_count = jumlah_awal - jumlah_valid

    print(f"Jumlah total data awal: {jumlah_awal}")
    print(f"Jumlah data valid setelah dibersihkan: {jumlah_valid}")
    print(f"Jumlah data tidak valid/dibuang: {invalid_count}\n")

    if jumlah_valid == 0:
        print("Peringatan: Tidak ada data valid yang tersisa untuk dianalisis.")
        return

    # 5, 6, & 7. Menghitung jumlah data valid, rata-rata, min, dan max menggunakan Pandas
    rata_rata = df_cleaned['Nilai'].mean()
    nilai_min = df_cleaned['Nilai'].min()
    nilai_max = df_cleaned['Nilai'].max()

    print("--- RINGKASAN HASIL ANALISIS ---")
    print(f"Jumlah Data Valid : {jumlah_valid}")
    print(f"Rata-rata Nilai   : {rata_rata:.2f}")
    print(f"Nilai Minimum     : {nilai_min}")
    print(f"Nilai Maksimum    : {nilai_max}\n")

    # 8. Menyimpan hasil analisis ke file CSV baru
    print("--- 8. MENYIMPAN HASIL ANALISIS KE FILE CSV ---")
    hasil_df = pd.DataFrame({
        'Metrik': ['Jumlah Data Valid', 'Rata-rata Nilai', 'Nilai Minimum', 'Nilai Maksimum'],
        'Hasil': [jumlah_valid, round(rata_rata, 2), nilai_min, nilai_max]
    })

    hasil_df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"Hasil analisis berhasil disimpan ke file '{output_file}'.\n")

if __name__ == '__main__':
    analisis_dengan_pandas()
