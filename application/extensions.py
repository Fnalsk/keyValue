from sqlitedict import SqliteDict

from application.constants import DB_NAME
from threading import Lock

db_lock = Lock()

db_lock.acquire()
db = SqliteDict(f'./{DB_NAME}.sqlite', autocommit=True)
db_lock.release()


