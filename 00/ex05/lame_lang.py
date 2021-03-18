import psycopg2

def get_connection():
    conn = psycopg2.connect(
        database="appstore_games",
        host="localhost",
        user="postgres_user",
        password="12345"
    )
    return conn


def get_name_lang():
    conn = get_connection()
    curr = conn.cursor()
    curr.execute("""
        SELECT name, language
        FROM appstore_games
        JOIN appstore_games_languages
            ON (appstore_games.game_id = appstore_games_languages.game_id)
        WHERE appstore_games.price BETWEEN 5 AND 10;
    """)
    response = curr.fetchall()
    for row in response:
        print(row)
    conn.close()

if __name__ == '__main__':
    get_name_lang()