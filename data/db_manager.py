import sqlite3
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [DB-MANAGER] %(message)s")

class DBManager:
    def __init__(self, db_path="/app/data/ecosystem.db"):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self.init_schema()

    def init_schema(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS swarm_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                agent TEXT,
                action TEXT,
                status TEXT
            )
        """)
        self.conn.commit()
        logging.info("Database schema initialized.")

    def log_action(self, agent, action, status):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO swarm_logs (agent, action, status) VALUES (?, ?, ?)", (agent, action, status))
        self.conn.commit()

if __name__ == "__main__":
    db = DBManager()
    db.log_action("ScoutAgent", "GitHub Scan", "SUCCESS")
