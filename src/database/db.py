import sqlite3

class Db:
    def __init__(self):
        self.localDb = sqlite3.connect('data.db')
        self.cursor = self.localDb.cursor()
    
    def inizialite(self):
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS shops(
                    nameshop text NOT NULL,
                    path text NULL DEFAULT NULL
                )'''
            )
            return True
        except Exception as e:
            return e
    
    def create(self, name, path):
        try:
            self.cursor.execute('''
                INSERT INTO shops(nameshop, path)
                VALUES (?, ?)
            ''', (name, path,))

            self.localDb.commit()
            return True
        except Exception as e:
            return e
    
    def update(self, name, path, id):
        try:
            self.cursor.execute('''
                UPDATE shops SET nameshop = ?, path = ?
                WHERE rowid = ?
            ''', (name, path, id,))

            self.localDb.commit()
            return True
        except Exception as e:
            return e
    
    def delete(self, id):
        try:
            self.cursor.execute('''
                DELETE FROM shops
                WHERE rowid = ?
            ''', (id,))

            self.localDb.commit()
            return True
        except Exception as e:
            return e
    
    def list(self, id=None):
        try:
            if None == id:
                self.cursor.execute('''
                    SELECT rowid, nameshop, path FROM shops
                ''')
            else:
                self.cursor.execute('''
                    SELECT rowid, nameshop, path FROM shops WHERE rowid = ?
                ''', (id,))
            return self.cursor.fetchall()
        except Exception as e:
            return e