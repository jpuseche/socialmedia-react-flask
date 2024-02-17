function User(props: {name: string}) {
    return(
        <div className="relative mt-8 flex items-center gap-x-4">
            <img src="https://images.unsplash.com/photo-1519244703995-f4e0f30006d5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="user" className="h-10 w-10 rounded-full bg-gray-50"/>
            <span className="flex flex-col w-1/2">
                <span className="absolute inset-0"></span>
                <span className="font-semibold">{props.name}</span>
                <span>Co-Founder / CTO</span>
            </span>
            <span className="text-right w-1/2">Mar 16, 2020</span>
        </div>
    )
}

export default User