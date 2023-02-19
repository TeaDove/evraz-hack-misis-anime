import { useState } from "react"
import "./App.css"
import {HashRouter, Routes, Route} from "react-router-dom"
import {Sidebar} from "./components"
import {useStateContext} from "./contexts/ContextProvider.jsx"
import {Charts, ExhausterInfo, MainPage} from "./pages"

const App = () => {
  const {colorMode} = useStateContext();

  return (
    <div className={colorMode === "dark" ? "dark" : ""}>
    <HashRouter>
      <div className="flex relative">
        <div className="w-72 fixed sidebar bg-white dark:bg-secondary-dark">
          <Sidebar/>
        </div>
        <div className="bg-main dark:bg-main-dark min-h-screen md:ml-72 w-full">
          <div>
            <Routes>
              <Route path="/" element={<MainPage/>} />
              <Route path="/exhauster/:exhausterId" element={<ExhausterInfo/>} />
              <Route path="/charts" element={<Charts/>} />
            </Routes>
          </div>
        </div>
      </div>
    </HashRouter>
    </div>
  )
}

export default App
