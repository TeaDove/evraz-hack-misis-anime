import React from "react"


const StatusBadge = ({color, children}) => {
  let colorClass
  if (color === "danger") {
    colorClass = "text-rose-600 bg-rose-100"
  } else if (color === "warning") {
    colorClass = "text-yellow-600 bg-yellow-100"
  } else if (color === "positive") {
    colorClass = "text-green-600 bg-green-100"
  } else {
    colorClass = "text-blue-600 bg-blue-100"
  }

  return (
    <div className={`rounded p-0.5 pl-2 pr-2 w-min capitalize font-bold ${colorClass}`}>
      {children}
    </div>
  )
}

export default StatusBadge