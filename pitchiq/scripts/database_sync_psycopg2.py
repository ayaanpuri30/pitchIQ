import psycopg2
import os
import json
from glob import glob

# database connection details
DB_CONFIG = {
    "host": "db.rcrngkqsybnjfgyvhnyu.supabase.co",
    "port": 5432,
    "dbname": "postgres",
    "user": "postgres",
    "password": "9bsDQNRGqwGSVyE0"
}
CONNECTION_STRING = "postgresql://postgres:9bsDQNRGqwGSVyE0@db.rcrngkqsybnjfgyvhnyu.supabase.co:5432/postgres"
#template path for where club data will be stored
CLUB_DATA_PATH = "pitchiq/src/clubData/*.json"

# connect
try:
    conn = psycopg2.connect(**DB_CONFIG)
    #conn = psycopg2.connect(CONNECTION_STRING)
    cur = conn.cursor()
    print("Connection successful!")

    # create db tables if they don't exist
    cur.execute("""
    CREATE TABLE IF NOT EXISTS clubs (
        club_id SERIAL PRIMARY KEY,
        club_name TEXT UNIQUE,
        club_logo TEXT,
        manager_name TEXT,
        manager_photo TEXT
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS players (
        player_id BIGINT PRIMARY KEY,
        club_name TEXT REFERENCES clubs(club_name),
        name TEXT,
        birthdate DATE,
        number INT,
        position TEXT,
        photo TEXT
    );
    """)

    # process JSON files containing current iter of data
    for filepath in glob(CLUB_DATA_PATH):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Processing club {data['club_name']}...")
        # insert/update club
        cur.execute("""
            INSERT INTO clubs (club_name, club_logo, manager_name, manager_photo)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (club_name) DO UPDATE SET
                club_logo = EXCLUDED.club_logo,
                manager_name = EXCLUDED.manager_name,
                manager_photo = EXCLUDED.manager_photo;
        """, (data["club_name"], data["club_logo"], data["manager_name"], data["manager_photo"]))

        # insert/update squad
        for player in data["squad"]:
            cur.execute("""
                INSERT INTO players (player_id, club_name, name, birthdate, number, position, photo)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (player_id) DO UPDATE SET
                    club_name = EXCLUDED.club_name,
                    name = EXCLUDED.name,
                    birthdate = EXCLUDED.birthdate,
                    number = EXCLUDED.number,
                    position = EXCLUDED.position,
                    photo = EXCLUDED.photo;
            """, (
                player["id"],
                data["club_name"],
                player["name"],
                player["age"] if player["age"] else None,
                player["number"],
                player["position"],
                player["photo"]
            ))

    conn.commit()
    cur.close()
    conn.close()
    print("Database synced and connection closed.")

except Exception as e:
    print(f"Failed to connect or sync: {e}")
