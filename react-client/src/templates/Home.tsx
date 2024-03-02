import PostForm from '../components/PostForm'
import Feed from '../components/Feed'
import React, { useState, useEffect } from 'react'
import {Posts} from '../types/Post'

function Home() {
    const [posts, setPosts] = useState<Posts>([])

    useEffect(() => {
      fetch("/posts")
      .then(res => res.json())
      .then(data => {
          setPosts(JSON.parse(data.postsJSON))
          console.log(JSON.parse(data.postsJSON))
        }
      )
    }, [])
    
    const addPost = () => {
        fetch("/post", {
            method: "POST",
            headers: {
                 "Content-type": "application/json",
            },
            body: "whatever"
        })
        .then(res => res.json())
        .then(data => {
            setPosts(JSON.parse(data.postsJSON))
            console.log(JSON.parse(data.postsJSON))
          }
        )
    }

    return(
        <div className="py-24 sm:py-32">
            <div className="flex flex-col justify-center mx-auto max-w-4xl px-6 lg:px-8 text-[#EDEDED]">
                <PostForm addPost={addPost}/>
                <Feed posts={posts}/>
            </div>
        </div>
    )
    
}

export default Home