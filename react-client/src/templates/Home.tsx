import Feed from '../components/Feed'

type Data = {
    posts: string[];
};

function Home() {
    return(
        <>
        <Feed/>
        </>
    )
    
}

export default Home