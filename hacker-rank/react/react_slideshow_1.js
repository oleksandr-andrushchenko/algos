import React, {useState} from "react"

function Slides({slides}) {
  const [currentIndex, setCurrentIndex] = useState(0)

  const restart = () => setCurrentIndex(0)
  const prev = () => setCurrentIndex((prevIndex) => Math.max(prevIndex - 1, 0))
  const next = () =>
    setCurrentIndex((prevIndex) => Math.min(prevIndex + 1, slides.length - 1))

  const isFirst = currentIndex === 0
  const isLast = currentIndex === slides.length - 1

  return (
    <div>
      <div id="navigation" className="text-center">
        <button
          data-testid="button-restart"
          className="small outlined"
          onClick={restart}
          disabled={isFirst}
        >
          Restart
        </button>
        <button
          data-testid="button-prev"
          className="small"
          onClick={prev}
          disabled={isFirst}
        >
          Prev
        </button>
        <button
          data-testid="button-next"
          className="small"
          onClick={next}
          disabled={isLast}
        >
          Next
        </button>
      </div>
      <div id="slide" className="card text-center">
        <h1 data-testid="title">{slides[currentIndex].title}</h1>
        <p data-testid="text">{slides[currentIndex].text}</p>
      </div>
    </div>
  )
}

export default Slides