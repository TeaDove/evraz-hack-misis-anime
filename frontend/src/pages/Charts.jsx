import React from "react"
import {useParams} from "react-router-dom"

const grafanaUrl = "http://158.160.13.117:3000/d/PZHmNE1Vk/main?orgId=1&theme=light"

const Charts = () => {
  return (
    <div className="flex items-center justify-center">
      <iframe
        src={grafanaUrl}
        frameBorder="0"
        className="w-full h-screen"
      >
      </iframe>
    </div>
  )
}

export default Charts