import csv

def analisis_nilai_mahasiswa():
    input_file = 'dataset-nilai-akhir-mhs.csv'
    output_file = 'hasil_analisis_nilai.csv'
    
    raw_data = []
    
    print("--- 1. MEMBACA DATA DARI FILE CSV ---")
    try:
        with open(input_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                raw_data.append(row)
        print(f"Berhasil membaca {len(raw_data)} baris data dari '{input_file}'.\n")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' tidak ditemukan. Pastikan file berada di folder yang sama.")
        return

    print("--- 2. MENAMPILKAN DATA AWAL ---")
    for i, row in enumerate(raw_data[:5]):
        print(f"Data ke-{i+1}: {row}")
    print("...\n")

    print("--- 3 & 4. PEMERIKSAAN & PEMBERSIHAN DATA ---")
    valid_data = []
    invalid_count = 0

    for row in raw_data:
        nama = row.get('Nama', '').strip()
        nilai_str = row.get('Nilai', '').strip()

        if not nama or not nilai_str:
            invalid_count += 1
            continue

        try:
            nilai = float(nilai_str)
            if 0 <= nilai <= 100:
                valid_data.append({'Nama': nama, 'Nilai': nilai})
            else:
                invalid_count += 1
        except ValueError:
            invalid_count += 1

    print(f"Jumlah total data awal: {len(raw_data)}")
    print(f"Jumlah data valid setelah dibersihkan: {len(valid_data)}")
    print(f"Jumlah data tidak valid/dibuang: {invalid_count}\n")

    if not valid_data:
        print("Peringatan: Tidak ada data valid yang tersisa untuk dianalisis.")
        return

    jumlah_valid = len(valid_data)

    total_nilai = sum(item['Nilai'] for item in valid_data)
    rata_rata = total_nilai / jumlah_valid

    nilai_min = min(item['Nilai'] for item in valid_data)
    nilai_max = max(item['Nilai'] for item in valid_data)

    print("--- RINGKASAN HASIL ANALISIS ---")
    print(f"Jumlah Data Valid : {jumlah_valid}")
    print(f"Rata-rata Nilai   : {rata_rata:.2f}")
    print(f"Nilai Minimum     : {nilai_min}")
    print(f"Nilai Maksimum    : {nilai_max}\n")

    print("--- 8. MENYIMPAN HASIL ANALisis KE FILE CSV ---")
    hasil_analisis = [
        {'Metrik': 'Jumlah Data Valid', 'Hasil': jumlah_valid},
        {'Metrik': 'Rata-rata Nilai', 'Hasil': f"{rata_rata:.2f}"},
        {'Metrik': 'Nilai Minimum', 'Hasil': nilai_min},
        {'Metrik': 'Nilai Maksimum', 'Hasil': nilai_max}
    ]

    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['Metrik', 'Hasil']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in hasil_analisis:
                writer.writerow(row)
        print(f"Hasil analisis berhasil disimpan ke file '{output_file}'.\n")
    except Exception as e:
        print(f"Gagal menyimpan file hasil: {e}")

if __name__ == '__main__':
    analisis_nilai_mahasiswa()