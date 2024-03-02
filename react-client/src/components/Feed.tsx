import PostComponent from './Post'
import {Posts} from '../types/Post'

function Feed(props: {posts: Posts}) {

    if(typeof props.posts === 'undefined') {
        return(
            <div className="mt-10">
                <p> Loading... </p>
            </div>
        )
    } else {
        return(
            <div className="mt-10">
                <div className="mx-auto max-w-2xl lg:mx-0">
                    <h1 className="text-3xl font-bold tracking-tigh sm:text-4xl text-[#DA0037]">Recent Posts</h1>
                </div>
                {props.posts.map((post, i) => (
                    <>
                        <PostComponent key={i} name={post.name} role={post.role} avatarUrl={post.avatarUrl} avatarAlt={post.avatarAlt} title={post.title} content={post.content} datePublished={new Date(post.datePublished)}/>
                    </>
                ))}
            </div>
        )
    }
    
}

export default Feed