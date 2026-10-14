import sqlite3
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [MIGRATIONS] %(message)s")

class DatabaseMigrator:
    def __init__(self, db_path="/app/data/ecosystem.db"):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path)

    def run_migrations(self):
        logging.info("Checking database migrations...")
        cursor = self.conn.cursor()
        
        # Swarm config table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS system_config (
                key TEXT PRIMARY KEY,
                value TEXT,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Default seed values
        default_configs = [
            ("min_balance_threshold", "0.05"),
            ("swarm_interval_seconds", "3600"),
            ("auto_deploy_enabled", "true")
        ]
        
        cursor.executemany("""
            INSERT OR IGNORE INTO system_config (key, value) VALUES (?, ?)
        """, default_configs)
        
        self.conn.commit()
        logging.info("✅ Database migrations & seed data applied successfully.")

if __name__ == "__main__":
    migrator = DatabaseMigrator()
    migrator.run_migrations()
