import psycopg2

def get_connection():
    conn = psycopg2.connect(
        database="appstore_games",
        host="localhost",
        user="postgres_user",
        password="12345"
    )
    return conn


def get_top_100():
    conn = get_connection()
    curr = conn.cursor()
    curr.execute("""
        SELECT name
        FROM appstore_games
        WHERE name ~ '^[a-zA-Z]'
        ORDER BY avg_user_rating DESC, name
        LIMIT 100;
    """)
    response = curr.fetchall()
    for row in response:
        print(row[0])
    conn.close()

if __name__ == '__main__':
    get_top_100()