import psycopg2

def get_connection():
    conn = psycopg2.connect(
        database="appstore_games",
        host="localhost",
        user="postgres_user",
        password="12345"
    )
    return conn


def get_benefits():
    conn = get_connection()
    curr = conn.cursor()
    curr.execute("""

        SELECT SUM(user_rating_count * price) AS benefits, genre
        FROM appstore_games
        JOIN appstore_games_genres
            ON  (appstore_games.game_id = appstore_games_genres.game_id)
        GROUP BY genre
        ORDER BY benefits
    """)
    ## url is not in the db
    response = curr.fetchall()
    for row in response:
        print(row)
    conn.close()

if __name__ == '__main__':
    get_benefits()