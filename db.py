import sqlite3


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

    def create_table_gerchikov_results(self):
        """
        Создает таблицу 'gerchikov_results' в базе данных, если она не существует.

        Returns:
        - Результат выполнения запроса к базе данных.
        """
        with self.connection:
            res = self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS gerchikov_results
            (id integer PRIMARY KEY AUTOINCREMENT,
            chat_id BIGINT UNIQUE,
            name text, 
            email TEXT,
            mob_tel BIGINT,
            position TEXT,
            in_score INT,
            pr_score INT,
            pa_score INT,
            ho_score INT,
            lyu_score INT
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

    def save_result(self, table_name, keys, *args):
        """
        Сохраняет результат в указанную таблицу базы данных или обновляет запись, если уже существует.
        Взаимдоействует с функциями post_result, ger_post_result. 
        Обеспечивает гибкость, позволяя вставлять или обновлять записи в таблице.
        Соблюдает принцип DRY
        Parameters:
        - table_name (str): Имя таблицы в базе данных.
        - keys (str): Строка с полями таблицы для вставки или обновления.
        - args: Переменное количество аргументов, представляющих значения для вставки или обновления.

        Raises:
        - Exception: Если произошла ошибка при выполнении SQL-запроса.

        Returns:
        - None
        """
        try:
            with self.connection:
                # Пытаемся вставить новую запись
                self.cursor.execute(f"INSERT INTO {table_name} {keys} VALUES {args}")
        except:
            # Если запись уже существует, обновляем её
            update_keys = keys[1:-1].split(", ")
            update_string = ', '.join(f'{key}=?' for key in update_keys)
            with self.connection:
                self.cursor.execute(f"UPDATE {table_name} SET {update_string} WHERE chat_id=?", args + (args[0],))


    def post_result(self, *args):
        """
        Сохраняет результат в таблицу 'users' базы данных.

        Parameters:
        - args: Переменное количество аргументов, представляющих значения для вставки или обновления.

        Returns:
        - None
        """
        keys = "(chat_id, name, email, mob_tel, result, result_e, result_s, result_t, result_j, result_sum)"
        self.save_result("users", keys, *args)


    def ger_post_result(self, *args):
        """
        Сохраняет результат в таблицу 'gerchikov_results' базы данных.

        Parameters:
        - args: Переменное количество аргументов, представляющих значения для вставки или обновления.

        Returns:
        - None
        """
        keys = "(chat_id, name, email, mob_tel, position, in_score, pr_score, ho_score, lyu_score, pa_score)"
        self.save_result("gerchikov_results", keys, *args)

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
                # logger.error(f"{func} {ex}")
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
        # logger.info(res)
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
