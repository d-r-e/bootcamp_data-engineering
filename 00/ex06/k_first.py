import psycopg2

def get_connection():
    conn = psycopg2.connect(
        database="appstore_games",
        host="localhost",
        user="postgres_user",
        password="12345"
    )
    return conn


def get_k_first():
    conn = get_connection()
    curr = conn.cursor()
    curr.execute("""
        SELECT DISTINCT developer
        FROM appstore_games
        JOIN appstore_games_genres
            ON (appstore_games.game_id = appstore_games_genres.game_id)
        WHERE developer ~ '^[kK]' AND genre LIKE 'Casual';
    """)
    response = curr.fetchall()
    for row in response:
        print(row)
    conn.close()

if __name__ == '__main__':
    get_k_first()