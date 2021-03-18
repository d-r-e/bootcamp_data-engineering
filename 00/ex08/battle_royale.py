import psycopg2

def get_connection():
    conn = psycopg2.connect(
        database="appstore_games",
        host="localhost",
        user="postgres_user",
        password="12345"
    )
    return conn


def get_battle_royale():
    conn = get_connection()
    curr = conn.cursor()
    curr.execute("""
        SELECT DISTINCT name
        FROM appstore_games
        WHERE description ILIKE '%battle royale%';
    """)
    ## url is not in the db
    response = curr.fetchall()
    for row in response:
        print(row)
    conn.close()

if __name__ == '__main__':
    get_battle_royale()