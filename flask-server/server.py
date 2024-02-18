from flask import Flask
import json
import datetime

app = Flask(__name__)

postsJSON = json.dumps([{
    "name": "Juan",
    "role": "CO-Founder / CTO",
    "avatar_url": "https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
    "avatar_alt": "juan's avatar",
    "mainContent": "Illo sint voluptas. Error voluptates culpa eligendi. Hic vel totam vitae illo. Non aliquid explicabo necessitatibus unde. Sed exercitationem placeat consectetur nulla deserunt vel. Iusto corrupti dicta.",
    "datePublished": datetime.datetime(2022, 5, 17).isoformat()
}])

@app.route("/posts")
def getPosts():
    return {"postsJSON": postsJSON}