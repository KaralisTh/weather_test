import sqlite3

def create_table():
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather_measurements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        station_id INTEGER NOT NULL,
        date_time TEXT NOT NULL,
        temperature REAL NOT NULL,
        humidity REAL NOT NULL,
        wind_speed REAL NOT NULL,
        wind_direction TEXT NOT NULL,
        rainfall REAL NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
