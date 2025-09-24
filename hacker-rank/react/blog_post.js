import React, {useState} from "react"

function PostDisplay({post, deletePost}) {
  return (
    <div className="post-box">
      <h3>{post.title}</h3>
      <p>{post.description}</p>
      <button onClick={deletePost}>Delete</button>
    </div>
  )
}

function Input({createPost}) {
  const [title, setTitle] = useState("")
  const [description, setDescription] = useState("")
  const onClick = () => {
    if (!title || !description) {
      return
    }
    createPost({title, description})
    setTitle("")
    setDescription("")
  }
  return (
    <>
      <div className="layout-column justify-content-center align-items-center">
        <input className="w-100" type="text" placeholder="Enter Title" value={title} data-testid="title-input"
               onChange={(e) => setTitle(e.target.value)}/>
        <textarea className="mt-10 w-100" placeholder="Enter Description" value={description}
                  data-testid="description-input" onChange={(e) => setDescription(e.target.value)}/>
      </div>
      <button data-testid="create-button" className="mt-10" onClick={onClick}>
        Create Post
      </button>
    </>
  )
}

function Home() {
  const [posts, setPosts] = useState([])
  const createPost = (post) => setPosts([...posts, post])
  const deletePost = (index) => setPosts(posts.filter((_, i) => i !== index))
  return (
    <div className="text-center ma-20">
      <div className="mb-20">
        <Input createPost={createPost}/>
      </div>
      <div className="posts-section">
        <div data-testid="posts-container" className="flex wrap gap-10">
          {posts.map((post, index) => <PostDisplay key={index} post={post} deletePost={() => deletePost(index)}/>)}
        </div>
      </div>
    </div>
  )
}

export default Home
