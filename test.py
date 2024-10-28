import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="SIG_db",
        user="postgres",
        password="Hidung135",
        port="5432"
    )
    print("Koneksi berhasil")
    conn.close()
except Exception as e:
    print("Koneksi gagal:", e)
