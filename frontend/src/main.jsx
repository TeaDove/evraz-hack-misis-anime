import React from "react"
import ReactDOM from "react-dom/client"
import App from "./App"
import {ContextProvider} from "./contexts/ContextProvider.jsx"
import moment from "moment"
import "moment/dist/locale/ru"
import "./index.css"

moment.locale("ru")

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <ContextProvider>
      <App />
    </ContextProvider>
  </React.StrictMode>,
)
