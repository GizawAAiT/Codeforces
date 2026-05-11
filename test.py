import sqlite3
import random
import string
import time

DB_NAME = "benchmark.db"
NUM_ROWS = 200_000_0
TARGET_NAME = "target_name"


def random_name(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def setup_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
    """)

    print("Inserting data...")
    data = []

    # Ensure TARGET_NAME exists multiple times
    for _ in range(NUM_ROWS):
        name = TARGET_NAME if random.random() < 0.001 else random_name()
        age = random.randint(18, 80)
        data.append((name, age))

    cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", data)
    conn.commit()
    conn.close()

def benchmark_query(with_index=False):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    if with_index:
        print("\nCreating index on 'name' column...")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_name ON users(name)")
        conn.commit()

    print(f"\nRunning query {'WITH' if with_index else 'WITHOUT'} index...")

    start = time.time()

    cursor.execute("SELECT * FROM users WHERE name = ?", (TARGET_NAME,))
    results = cursor.fetchall()

    end = time.time()

    print(f"Rows found: {len(results)}")
    print(f"Execution time: {end - start:.6f} seconds")

    conn.close()


def main():
    setup_database()

    # Run without index
    benchmark_query(with_index=False)

    # Run with index
    benchmark_query(with_index=True)


if __name__ == "__main__":
    main()