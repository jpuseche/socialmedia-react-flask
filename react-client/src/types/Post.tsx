
export type Post = {
    name: string,
    role: string,
    avatarUrl: string,
    avatarAlt: string,
    title: string,
    content: string,
    datePublished: Date
}

export type Posts = Post[];