import psycopg2

def get_connection():
    conn = psycopg2.connect(
        database="appstore_games",
        host="localhost",
        user="postgres_user",
        password="12345"
    )
    return conn


def sweet_spot():
    conn = get_connection()
    curr = conn.cursor()
    curr.execute("""
        SELECT COUNT(extract(MONTH FROM release_date)::integer)
        FROM appstore_games 
    
    """)
    ## url is not in the db
    response = curr.fetchall()
    for row in response:
        print(row)
    conn.close()

if __name__ == '__main__':
    sweet_spot()