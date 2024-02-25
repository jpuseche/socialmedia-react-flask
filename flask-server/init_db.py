import os
import psycopg2

def dbSetup():
    conn = psycopg2.connect(database=os.getenv('DB_NAME'),  
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            host=os.getenv('DB_HOST'), port=os.getenv('DB_PORT'))
    
    return conn

def dbInit():
    conn = dbSetup()

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a command: this creates new tables
    cur.execute('DROP TABLE IF EXISTS person CASCADE;')
    cur.execute('CREATE TABLE person (id serial PRIMARY KEY,'
                'first_name varchar (50) NOT NULL,'
                'last_name varchar (50) NOT NULL,'
                'avatar_url text,'
                'avatar_alt varchar (50));'
                )

    cur.execute('DROP TABLE IF EXISTS post;')
    cur.execute('CREATE TABLE post (id serial PRIMARY KEY,'
                'title varchar (150) NOT NULL,'
                'content text,'
                'person_id INTEGER REFERENCES person (id) NOT NULL,'
                'date_published date DEFAULT CURRENT_TIMESTAMP);'
                )
    
    # Execute a command: this inserts records into tables
    cur.execute("INSERT INTO person (first_name, last_name, avatar_url, avatar_alt)"
                "VALUES ('Juan',"
                "'Useche',"
                "'https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80',"
                "'Juan'\'s Avatar')")
    
    cur.execute("INSERT INTO post (title, content, person_id)"
            "VALUES ('The best Post in the world',"
            "'Illo sint voluptas. Error voluptates culpa eligendi. Hic vel totam vitae illo. Non aliquid explicabo necessitatibus unde. Sed exercitationem placeat consectetur nulla deserunt vel. Iusto corrupti dicta.',"
            "'1')")

    conn.commit()

    cur.close()
    conn.close()

def dbOpen():
    try:
        # Open a db connection
        conn = dbSetup()
        cur = conn.cursor()
        
        return conn, cur, None

    except (Exception, psycopg2.Error) as error:
        print("Error while opening db connection", error)

        return None, None, error

def dbCommit(conn: psycopg2.extensions.connection, cur: psycopg2.extensions.cursor):
    try:
        # Commit a db change
        conn.commit()

        cur.close()
        conn.close()

    except (Exception, psycopg2.Error) as error:
        print("Error on commit to database", error)

        cur.close()
        conn.close()