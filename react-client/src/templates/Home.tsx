import React, { useState, useEffect } from 'react'
import Feed from '../components/Feed'

type Data = {
    posts: string[];
};

function Home() {
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
    return(
        <>
        <Feed/>
        {(typeof data.posts === 'undefined') ? (
            <p> Loading... </p>
          ) : (
            data.posts.map((member, i) => (
              <p className='text-white' key={i}>{member}</p>
          ))
        )}
        </>
    )
    
}

export default Home