from contextlib import contextmanager
import sqlite3
import sys
import time

@contextmanager
def dbh(conn_str, schema='', db_name=''):
    """for each sqlite db we want our app to establish a connection (open the
    file) only once, after which we will interact with it via this
    contextmanager that provides transactional support, calling COMMIT for
    us after each block.

    schema is a string suitable for passing to executescript() which will
    be used to initiate the database the first time a connection is made

    db_name will default to conn_str.  it is only used as a key for our
    cache of open connections, and only needs to be set if you are opening
    multiple :memory: dbs to prevent conflicts between them """
    if not db_name:
        db_name = conn_str
    if db_name not in dbh.conns:
        print >> sys.stderr , ">>> creating connection to %s" % (db_name,)
        dbh.conns[db_name] = sqlite3.connect(conn_str)
        # WAL mode with PRAGMA synchronous set to NORMAL avoids calls to
        # fsync() during transaction commit and only invokes fsync()
        # during a checkpoint operation. see http://www.sqlite.org/wal.html
        dbh.conns[db_name].execute("PRAGMA synchronous = 1;")
        cur = dbh.conns[db_name].execute("PRAGMA journal_mode=WAL;")
        row = cur.fetchone()
        if row[0] != "wal":
            # this is normal to see when testing with :memory: tables
            warnings.warn("could not change connection to WAL mode")
        if schema:
            cur.executescript(schema)
    yield dbh.conns[db_name]
    try:
        dbh.conns[db_name].commit()
    except sqlite3.DatabaseError:
        dbh.conns[db_name].rollback()
dbh.conns = {}


def log_request(app, n):
    """writes row to db, returns 2-tuple (datetime, qty_ns_seen)"""
    created = int(time.time())

    with dbh(app.connstr) as db:
        cur = db.cursor()
        sql = "INSERT INTO difference_requests (n, created) VALUES (?, ?)"
        cur.execute(sql, (n, created))

    with dbh(app.connstr) as db:
        sql = "SELECT COUNT(1) FROM difference_requests where n = ?"
        cur.execute(sql, (n, ))
        row = cur.fetchone()
        occurrences = row[0]

    return (created, occurrences)


