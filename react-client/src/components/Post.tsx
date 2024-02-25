function Post(props: {name: string, role: string, avatarUrl: string, avatarAlt: string, title: string, content: string, datePublished: Date}) {
    let formattedPublishedDate = `${props.datePublished.getDay()}, ${props.datePublished.toLocaleString('en-EN', { month: 'long' })} ${props.datePublished.getFullYear()}`
    
    return(
        <>
            <div className="relative mt-8 flex items-center gap-x-4">
                <img src={props.avatarUrl} alt={props.avatarAlt} className="h-10 w-10 rounded-full bg-gray-50"/>
                <span className="flex flex-col w-1/2">
                    <span className="absolute inset-0"></span>
                    <span className="font-semibold">{props.name}</span>
                    <span>{props.role}</span>
                </span>
                <span className="text-right w-1/2">{formattedPublishedDate}</span>
            </div>
            <article className="flex flex-col items-start justify-between">
                <span className="mt-2 font-bold text-xl">{props.title}</span>
                <p className="mt-1 line-clamp-3 text-sm leading-6">{props.content}</p>
            </article>
        </>
    )
}

export default Post