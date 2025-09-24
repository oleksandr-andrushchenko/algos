import "h8k-components"
import "./App.css"
import {useState} from "react"

function Articles({articles = []}) {
  return (
    <div className="card w-50 mx-auto">
      <table>
        <thead>
        <tr>
          <th>Title</th>
          <th>Upvotes</th>
          <th>Date</th>
        </tr>
        </thead>
        <tbody>
        {articles.map((article, index) => (
          <tr data-testid="article" key={`article-index-${index}`}>
            <td data-testid="article-title">{article.title}</td>
            <td data-testid="article-upvotes">{article.upvotes}</td>
            <td data-testid="article-date">{article.date}</td>
          </tr>
        ))}
        </tbody>
      </table>
    </div>
  )
}


function App({articles}) {
  const getDefaultArticles = () => [...articles].sort((a, b) => b.upvotes - a.upvotes)
  const [_articles, setArticles] = useState(getDefaultArticles())
  const handleMostUpvoted = () => setArticles(getDefaultArticles())
  const handleMostRecent = () => setArticles([...articles].sort((a, b) => new Date(b.date) - new Date(a.date)))
  return (
    <>
      <h8k-navbar header="Sorting Articles"></h8k-navbar>
      <div className="App">
        <div className="layout-row align-items-center justify-content-center my-20 navigation">
          <label className="form-hint mb-0 text-uppercase font-weight-light">
            Sort By
          </label>
          <button
            data-testid="most-upvoted-link"
            className="small"
            onClick={handleMostUpvoted}
          >
            Most Upvoted
          </button>
          <button
            data-testid="most-recent-link"
            className="small"
            onClick={handleMostRecent}
          >
            Most Recent
          </button>
        </div>
        <Articles articles={_articles}/>
      </div>
    </>
  )
}

export default App