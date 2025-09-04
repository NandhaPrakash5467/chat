import psycopg2

DB_CONFIG = {
    'dbname': 'transforms_db',
    'user': 'postgres',
    'password': '5467',
    'host': 'localhost',
    'port': 5432
}

def get_answer(question):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    try:
        
        cur.execute("SELECT answer FROM chatbot WHERE LOWER(question) = %s LIMIT 1", (question,))
        row = cur.fetchone()
        if row:
            return row[0]

        cur.execute("SELECT answer FROM chatbot WHERE LOWER(question) LIKE %s LIMIT 1", (f"%{question}%",))
        row = cur.fetchone()
        if row:
            return row[0]

        return "I'm still learning. Try something else!"
    finally:
        cur.close()
        conn.close()
