import sqlite3
from loguru import logger


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def create_table(self):
        with self.connection:
            res = self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS users
            (id integer PRIMARY KEY AUTOINCREMENT,
            chat_id BIGINT UNIQUE,
            name text, 
            email TEXT,
            mob_tel BIGINT,
            result  VARCHAR(4),
            result_e INT,
            result_s INT,
            result_t INT,
            result_j INT,
            result_sum INT
            )
            ''')
            return res

    def create_table_bookmarks(self):
        with self.connection:
            res = self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS bookmarks
            (id integer PRIMARY KEY AUTOINCREMENT,
            from_id BIGINT,
            key TEXT NOT NULL UNIQUE,
            message_id BIGINT NOT NULL
            )
            ''')
            return res

    def post_result(self, *args):
        l = (args)
        keys = "(chat_id, name, email, mob_tel, result, result_e, result_s, result_t, result_j, result_sum)"
        print(l)
        try:
            with self.connection:
                self.cursor.execute(f"INSERT INTO users {keys} VALUES {l}")
        except:
            new_l = (args[1:])
            string = ''
            res = keys[1:-1].split(", ")
            new_keys = (res[1:])
            for elem in new_keys:
                string += f'{elem}=?, '
            print(string[:-2])
            with self.connection:
                self.cursor.execute(f"UPDATE users SET {string[:-2]} WHERE chat_id={l[0]}", new_l)

    ####################################КЛЮЧИ########################################
    def isMessageExists(self, key):
        with self.connection:
            res = self.cursor.execute("SELECT COUNT(*) as cnt FROM bookmarks WHERE `key` = ?", (key,)).fetchone()[0]
        return res

    def log(func):
        def wrapper(self, *args, **kwargs):
            try:
                with self.connection:
                    res = func(self, *args, **kwargs)
                return res
            except Exception as ex:
                logger.error(f"{func} {ex}")
                return
        return wrapper

    @log
    def add_key(self, *args):
        l = (args)
        keys = "(from_id, key, message_id)"
        res = self.cursor.execute(f"INSERT INTO bookmarks {keys} VALUES {l}")
        return res

    @log
    def get_key(self, from_id, key):
        res = self.cursor.execute(f"SELECT message_id FROM bookmarks WHERE `key` = ? AND from_id = ?", (key, from_id)).fetchone()[0]
        return res

    @log
    def list_key(self, from_id):
        res = self.cursor.execute("SELECT `key` FROM bookmarks WHERE `from_id` = ?", (from_id,)).fetchall()
        return res

    @log
    def remove_key(self, from_id, key):
        res=self.get_key(from_id, key)
        logger.info(res)
        if not res:
            return
        res = self.cursor.execute(f"DELETE FROM bookmarks WHERE `key` = ? AND from_id = ?",
                                  (key, from_id))
        return res


    # Optional
    def drop_table(self, name):
        with self.connection:
            res = self.cursor.execute(f'''DROP TABLE {name}''')
            return res
