from flask import Blueprint
import json
import datetime
from init_db import dbOpen
from init_db import dbCommit

postsJSON = json.dumps([{
    "name": "Juan",
    "role": "CO-Founder / CTO",
    "avatar_url": "https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
    "avatar_alt": "juan's avatar",
    "title": "The best Post in the world",
    "content": "Illo sint voluptas. Error voluptates culpa eligendi. Hic vel totam vitae illo. Non aliquid explicabo necessitatibus unde. Sed exercitationem placeat consectetur nulla deserunt vel. Iusto corrupti dicta.",
    "datePublished": datetime.datetime(2022, 5, 17).isoformat()
}])

post = Blueprint('post', __name__)

@post.route("/posts")
def getPosts():
    conn, cur, err = dbOpen()

    cur.execute('SELECT * FROM post LIMIT 10;')
    print('Fetching posts from database')

    allPosts = cur.fetchall()
    print(allPosts)

    return {"postsJSON": postsJSON}