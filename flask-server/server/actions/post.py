from flask import Blueprint
import json
import datetime
from init_db import dbOpen
from init_db import dbCommit

class Person:
    def __init__(self, name: str, role: str, avatarUrl: str, avatarAlt: str):
        self.name = name
        self.role = role
        self.avatarUrl = avatarUrl
        self.avatarAlt = avatarAlt

class Post:
    def __init__(self, title: str, content: str, personId: str, date_published: datetime):
        self.title = title
        self.content = content
        self.personId = personId
        self.date_published = date_published

class PostPerson:
    def __init__(self, name: str, role: str, avatarUrl: str, avatarAlt: str, title: str, content: str, datePublished: datetime):
        self.name = name
        self.role = role
        self.avatarUrl = avatarUrl
        self.avatarAlt = avatarAlt
        self.title = title
        self.content = content
        self.datePublished = datePublished

postsJSON = json.dumps([{
    "name": "Juan",
    "role": "CO-Founder / CTO",
    "avatar_url": "https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
    "avatar_alt": "juan's avatar",
    "title": "The best Post in the world",
    "content": "Illo sint voluptas. Error voluptates culpa eligendi. Hic vel totam vitae illo. Non aliquid explicabo necessitatibus unde. Sed exercitationem placeat consectetur nulla deserunt vel. Iusto corrupti dicta.",
    "date_published": datetime.datetime(2022, 5, 17).isoformat()
}])

post = Blueprint('post', __name__)

@post.route("/posts")
def getPosts():
    conn, cur, err = dbOpen()

    cur.execute("SELECT per.first_name, per.last_name, per.role, per.avatar_url, per.avatar_alt, post.title, post.content, post.date_published "
                "FROM post JOIN person per ON post.person_id = per.id LIMIT 10;")
    print('Fetching posts from database')
    
    allPosts: list[PostPerson] = []
    for postPerson in cur.fetchall():
        allPosts.append(PostPerson(postPerson[0], postPerson[2], postPerson[3], postPerson[4], postPerson[5], postPerson[6], postPerson[7].isoformat()).__dict__)

    print('GET allPosts JSON: ' + json.dumps(allPosts))

    dbCommit(conn, cur)

    return {"postsJSON": json.dumps(allPosts)}