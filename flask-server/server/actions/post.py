from flask import Blueprint, request
import json
import datetime
from init_db import dbOpen
from init_db import dbCommit
import psycopg2

# class Person:
#     def __init__(self, name: str, role: str, avatarUrl: str, avatarAlt: str):
#         self.name = name
#         self.role = role
#         self.avatarUrl = avatarUrl
#         self.avatarAlt = avatarAlt

# class Post:
#     def __init__(self, title: str, content: str, personId: str, date_published: datetime):
#         self.title = title
#         self.content = content
#         self.personId = personId
#         self.date_published = date_published

class PostPerson:
    def __init__(self, name: str, role: str, avatarUrl: str, avatarAlt: str, title: str, content: str, datePublished: datetime):
        self.name = name
        self.role = role
        self.avatarUrl = avatarUrl
        self.avatarAlt = avatarAlt
        self.title = title
        self.content = content
        self.datePublished = datePublished

post = Blueprint("post", __name__)

@post.route("/posts")
def getPosts():
    conn, cur = dbOpen()

    try:
        cur.execute("SELECT per.first_name, per.last_name, per.role, per.avatar_url, per.avatar_alt, post.title, post.content, post.date_published "
                    "FROM post JOIN person per ON post.person_id = per.id LIMIT 10;")
        print('Fetching posts from database')
        
        allPosts: list[PostPerson] = []
        for postPerson in cur.fetchall():
            allPosts.append(PostPerson(postPerson[0], postPerson[2], postPerson[3], postPerson[4], postPerson[5], postPerson[6], postPerson[7].isoformat()).__dict__)

        print("GET allPosts JSON: " + json.dumps(allPosts))

        dbCommit(conn, cur)

        return {"postsJSON": json.dumps(allPosts)}
    
    except (Exception, psycopg2.Error) as error:
        print("Error while getting posts:", error)

        cur.close()
        conn.close()

        return None

@post.route("/post", methods = ["POST"])
def addPost():
    if request.method == 'POST':
        conn, cur = dbOpen()

        print(request.body)
        # cur.execute("SELECT per.first_name, per.last_name, per.role, per.avatar_url, per.avatar_alt, post.title, post.content, post.date_published "
        #             "FROM post JOIN person per ON post.person_id = per.id LIMIT 10;")
        # print('Fetching posts from database')
        
        # allPosts: list[PostPerson] = []
        # for postPerson in cur.fetchall():
        #     allPosts.append(PostPerson(postPerson[0], postPerson[2], postPerson[3], postPerson[4], postPerson[5], postPerson[6], postPerson[7].isoformat()).__dict__)

        # print("GET allPosts JSON: " + json.dumps(allPosts))

        dbCommit(conn, cur)

        # return {"postsJSON": json.dumps(allPosts)}
        
