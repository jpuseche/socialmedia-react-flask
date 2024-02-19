import PostComponent from './Post'
import React, { useState, useEffect } from 'react'

type Post = {
    name: string,
    role: string,
    avatar_url: string,
    avatar_alt: string,
    title: string,
    content: string,
    datePublished: Date
}

type Posts = Post[];

function Feed() {
    const [posts, setPosts] = useState<Posts>([])

    useEffect(() => {
      fetch("/posts").then(
        res => res.json()
      ).then(
        data => {
          setPosts(JSON.parse(data.postsJSON))
          console.log(JSON.parse(data.postsJSON))
        }
      )
    }, [])

    if(typeof posts === 'undefined') {
        return(
            <div className="py-24 sm:py-32">
                <div className="mx-auto max-w-4xl px-6 lg:px-8 text-[#EDEDED]">
                    <p> Loading... </p>
                </div>
            </div>
        )
    } else {
        return(
            <div className="py-24 sm:py-32">
                <div className="mx-auto max-w-4xl px-6 lg:px-8 text-[#EDEDED]">
                    <div className="mx-auto max-w-2xl lg:mx-0">
                        <h1 className="text-3xl font-bold tracking-tigh sm:text-4xl text-[#DA0037]">Recent Posts</h1>
                    </div>
                    {posts.map((post, i) => (
                        <>
                            <PostComponent key={i} name={post.name} role={post.role} avatar_url={post.avatar_url} avatar_alt={post.avatar_alt} title={post.title} content={post.content} datePublished={new Date(post.datePublished)}/>
                        </>
                    ))}
                </div>
            </div>
        )
    }
    
}

export default Feed