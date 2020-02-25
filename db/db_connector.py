import pymysql.cursors

from value_object.user import User


def _our_hash(password):
    d = {
        "pass": "c281de494db8437b949f02122b3e70e2725429a5b25ddbd952f75c72a78ac55b",
        "secret": "815d5a2aa13cc4e326fa988645a670be59d0b501b34312b220daa0afa94d072b"
    }
    return d[password]


class OxwallDB:

    def __init__(self, *args, **kwargs):
        # Connect to the database
        self.connection = pymysql.connect(*args, **kwargs,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        self.connection.autocommit(True)

    def close(self):
        self.connection.close()

    def create_user(self, user):
        with self.connection.cursor() as cursor:
            # Create a new user
            sql = """INSERT INTO `ow_base_user` (`username`, `email`, `password`, `emailVerify`, `joinIp`) 
                        VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (user.username, user.email, _our_hash(user.password), 0, 213006433))

    def get_users(self):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `email`, `username`, `password` FROM `ow_base_user`"
            cursor.execute(sql)
            result = cursor.fetchall()
            return [User(**d) for d in result]

    def delete_user(self, username):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM `ow_base_user` WHERE `username` = %s"
            cursor.execute(sql, username)


if __name__ == "__main__":
    db = OxwallDB(host='localhost', user='root', password='mysql', db='oxwa207')
    try:
        user = User(username="vasia", email="vasi3a@mail.com", password="pass")
        # db.create_user(user)
        db.delete_user(user.username)
        print(db.get_users())
    finally:
        db.close()
