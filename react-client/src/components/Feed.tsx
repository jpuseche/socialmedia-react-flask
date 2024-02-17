import User from './User'
import Content from './Content'
import React, { useState, useEffect } from 'react'

type Data = {
    posts: string[];
};

function Feed() {
    const [data, setData] = useState<Data>({
        posts: []
    })

    useEffect(() => {
      fetch("/posts").then(
        res => res.json()
      ).then(
        data => {
          setData(data)
          console.log(data)
        }
      )
    }, [])

    if(typeof data.posts === 'undefined') {
        return(
            <div className="py-24 sm:py-32">
                <p> Loading... </p>
            </div>
        )
    } else {
        return(
            <div className="py-24 sm:py-32">
                <div className="mx-auto max-w-4xl px-6 lg:px-8 text-[#EDEDED]">
                    <div className="mx-auto max-w-2xl lg:mx-0">
                        <h1 className="text-3xl font-bold tracking-tigh sm:text-4xl text-[#DA0037]">Recent Posts</h1>
                    </div>
                    {data.posts.map((member, i) => (
                        <>
                            <User key={i} name={member} />
                            <Content/>
                            <p className='text-white' key={i}>{member}</p>
                        </>
                    ))}
                </div>
            </div>
        )
    }
    
    
}

export default Feed