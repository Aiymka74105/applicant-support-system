import sqlite3


class Database:
    def __init__(self, db_name="kozybaev_admission.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS applicants (
                iin TEXT PRIMARY KEY,
                name TEXT,
                program TEXT,
                ent_score INTEGER
            )
        ''')
        self.conn.commit()

    def add_applicant(self, iin: str, name: str, prg: str, score: int) -> bool:
        cursor = self.conn.cursor()
        query = 'INSERT INTO applicants VALUES (?, ?, ?, ?)'
        try:
            cursor.execute(query, (iin, name, prg, score))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def get_applicant(self, iin: str):
        cursor = self.conn.cursor()
        query = 'SELECT name, program, ent_score FROM applicants WHERE iin = ?'
        cursor.execute(query, (iin,))
        return cursor.fetchone()
