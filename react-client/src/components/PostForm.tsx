function PostForm(props: {addPost: () => void}) {

    return(
        <form className="flex flex-col" onSubmit={props.addPost}>
            <input className="text-4xl p-4 bg-[#171717] border-b border-[#EDEDED]" type="text" placeholder="Write a Title..."></input>
            <textarea className="text-xl p-4 mt-5 resize-none bg-[#171717] border-b border-[#EDEDED] h-[160px]" placeholder="Write some Thoughts..."></textarea>
            <button type="submit" className="mt-5 border w-[60px] border-[#EDEDED] ">Post</button>
        </form>
    )
}

export default PostForm