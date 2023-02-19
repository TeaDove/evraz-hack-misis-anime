import React, {createContext, useContext, useState} from "react"

const StateContext = createContext({})

export const ContextProvider = ({children}) => {
  const [colorMode, setColorMode] = useState(
    localStorage.getItem("colorMode") || "light"
  )

  const toggleColorMode = () => {
    let newMode;
    if (colorMode === "dark") {
      newMode = "dark"
    } else {
      newMode = "light"
    }

    setColorMode(newMode)
    localStorage.setItem("colorMode", newMode)
  }

  return (
    <StateContext.Provider
      value={{
        colorMode, setColorMode, toggleColorMode
      }}
    >
      {children}
    </StateContext.Provider>
  )
}

export const useStateContext = () => useContext(StateContext)
