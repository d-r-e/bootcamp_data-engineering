import psycopg2
import csv


def drop_all_tables():
    print("DELETING appstore_games table and connected tables...")
    conn = get_connection()
    curr = conn.cursor()
    curr.execute("""
        DROP TABLE IF EXISTS appstore_games CASCADE;
        DROP TABLE IF EXISTS appstore_games_languages CASCADE;
        DROP TABLE IF EXISTS appstore_games_genres CASCADE;
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
            game_id int PRIMARY KEY,
            name varchar,
            avg_user_rating float,
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
            game_id int,
            CONSTRAINT fk_game_id
                FOREIGN KEY(game_id) 
                    REFERENCES appstore_games(game_id),
            primary_genre varchar,
            genre varchar

        );
    """)
    conn.commit()
    conn.close()

def create_appstore_games_languages():
    print("Creating appstore_games_languages table...")
    conn = get_connection()
    curr = conn.cursor()
    curr.execute("""
        CREATE TABLE IF NOT EXISTS appstore_games_languages(
            id bigint PRIMARY KEY,
            game_id bigint,
            FOREIGN KEY (game_id) REFERENCES appstore_games(game_id),
            language varchar
        );
    """)
    conn.commit()
    conn.close()

def populate_appstore_games():
    print("Populating appstore_games table...")
    conn = get_connection()
    curr = conn.cursor()
    with open('appstore_games.normalized.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip the header row.
        for row in reader:
            row = row[1:]
            curr.execute(
            "INSERT INTO appstore_games VALUES (%s, %s, %s, %s,%s, %s, %s,%s, %s,%s,TO_DATE(%s, 'DD/MM/YYYY'))",
            row
            )
    conn.commit()
    conn.close()
    return

def populate_appstore_games_genres():
    print("Populating appstore_games_genres table...")
    conn = get_connection()
    curr = conn.cursor()
    with open('appstore_games_genres.normalized.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip the header row.
        i = 0
        for row in reader:
            curr.execute(
            "INSERT INTO appstore_games_genres VALUES (%s, %s, %s, %s)",
            row
            )
            i+=1
    conn.commit()
    conn.close()
    return

def populate_appstore_games_languages():
    print("Populating appstore_games_languages table...")
    conn = get_connection()
    curr = conn.cursor()
    with open('appstore_games_languages.normalized.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip the header row.
        i = 0
        for row in reader:
            curr.execute(
            "INSERT INTO appstore_games_languages VALUES (%s, %s, %s)",
            row
            )
            i+=1
    conn.commit()
    conn.close()
    return


if __name__ == '__main__':
    drop_all_tables()
    create_appstore_games()
    create_appstore_games_genres()
    create_appstore_games_languages()
    populate_appstore_games()
    populate_appstore_games_genres()
    populate_appstore_games_languages()