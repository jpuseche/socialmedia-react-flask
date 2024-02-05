import User from './User'
import Content from './Content'

function Feed() {
    return(
        <div className="py-24 sm:py-32">
            <div className="mx-auto max-w-4xl px-6 lg:px-8 text-[#EDEDED]">
                <div className="mx-auto max-w-2xl lg:mx-0">
                    <h1 className="text-3xl font-bold tracking-tigh sm:text-4xl text-[#DA0037]">Recent Posts</h1>
                </div>
                <User/>
                <Content/>
            </div>
        </div>
    )
    
}

export default Feed