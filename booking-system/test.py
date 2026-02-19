import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    database="bookingdb",
    user="booking",
    password="booking123"
)

print("Connected successfully")
conn.close()
