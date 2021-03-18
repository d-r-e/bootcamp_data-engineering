import psycopg2

def get_connection():
    conn = psycopg2.connect(
        database="appstore_games",
        host="localhost",
        user="postgres_user",
        password="12345"
    )
    return conn


def get_seniors():
    conn = get_connection()
    curr = conn.cursor()
    curr.execute("""
        SELECT DISTINCT developer
        FROM appstore_games
        WHERE release_date <= '08-01-2008' AND last_update >= '01-01-2018'
    """)
    response = curr.fetchall()
    for row in response:
        print(row)
    conn.close()

if __name__ == '__main__':
    get_seniors()