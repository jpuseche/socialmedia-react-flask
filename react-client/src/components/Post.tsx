function Post(props: {name: string, role: string, avatar_url: string, avatar_alt: string,  mainContent: string, datePublished: Date}) {
    let formattedPublishedDate = `${props.datePublished.getDay()}, ${props.datePublished.toLocaleString('en-EN', { month: 'long' })} ${props.datePublished.getFullYear()}`
    
    return(
        <>
            <div className="relative mt-8 flex items-center gap-x-4">
                <img src={props.avatar_url} alt={props.avatar_alt} className="h-10 w-10 rounded-full bg-gray-50"/>
                <span className="flex flex-col w-1/2">
                    <span className="absolute inset-0"></span>
                    <span className="font-semibold">{props.name}</span>
                    <span>{props.role}</span>
                </span>
                <span className="text-right w-1/2">{formattedPublishedDate}</span>
            </div>
            <article className="flex flex-col items-start justify-between">
                <p className="mt-5 line-clamp-3 text-sm leading-6">{props.mainContent}</p>
            </article>
        </>
    )
}

export default Post