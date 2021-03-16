import psycopg2

def drop_all_tables():
    print("DELETING appstore_games table and connected tables...")
    conn = get_connection()
    curr = conn.cursor()
    curr.execute("""
        DROP TABLE appstore_games CASCADE;
    """)
    conn.commit()
    conn.close()


def get_connection():
    conn = psycopg2.connect(
        database="appstore_games",
        host="localhost",
        user="postgres_user",
        password="12345"
    )
    return conn

def create_appstore_games():
    print("Creating appstore_games table...")
    conn = get_connection()
    curr = conn.cursor()
    curr.execute("""
        CREATE TABLE IF NOT EXISTS appstore_games(
            game_id bigint PRIMARY KEY,
            name varchar,
            agv_user_rating float,
            user_rating_count int,
            price float,
            description varchar,
            developer varchar,
            age_rating int,
            size bigint,
            release_date date,
            last_update date
        );
    """)
    conn.commit()
    conn.close()

def create_appstore_games_genres():
    print("Creating appstore_games_genres table...")
    conn = get_connection()
    curr = conn.cursor()
    curr.execute("""
        CREATE TABLE IF NOT EXISTS appstore_games_genres(
            id bigint PRIMARY KEY,
            game_id bigint,
            FOREIGN KEY (game_id) REFERENCES appstore_games(game_id),
            primary_genre varchar,
            genre varchar
        );
    """)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    drop_all_tables()
    create_appstore_games()
    create_appstore_games_genres()