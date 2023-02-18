import React from "react"

const ExhausterSchema = ({active, width, height, primaryColor, secondaryColor, activeColor}) => {
  return (
    <svg width={width} height={height} viewBox="0 0 1060 530" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path d="M160 480L60 405H260L160 480Z"
            fill={active === "fan" ? activeColor : primaryColor}/>
      <path d="M260 405H60V333C60 328.582 63.5817 325 68 325H252C256.418 325 260 328.582 260 333V405Z"
            fill={active === "fan" ? activeColor : primaryColor}/>
      <path d="M60 8C60 3.58172 63.5817 0 68 0H252C256.418 0 260 3.58172 260 8V80H60V8Z"
            fill={active === "fan" ? activeColor : primaryColor}/>
      <path d="M160.205 155L60.2051 80H260.205L160.205 155Z"
            fill={active === "fan" ? activeColor : primaryColor}/>
      <path d="M110 96C110 91.5817 113.582 88 118 88H202C206.418 88 210 91.5817 210 96V357C210 361.418 206.418 365 202 365H118C113.582 365 110 361.418 110 357V96Z"
            fill={active === "fan" ? activeColor : primaryColor}/>
      <path d="M110 438C110 433.582 113.582 430 118 430H202C206.418 430 210 433.582 210 438V522C210 526.418 206.418 530 202 530H118C113.582 530 110 526.418 110 522V438Z"
            fill={active === "fan" ? activeColor : primaryColor}/>
      <rect x="600" y="230" width="80" height="120" rx="8" fill={primaryColor}/>
      <rect x="710" y="230" width="240" height="120" rx="8"
            fill={active === "main-engine" ? activeColor : primaryColor}/>/>
      <rect x="980" y="227" width="80" height="120" rx="8" fill={primaryColor}/>
      <rect y="150" width="80" height="120" rx="8" fill={primaryColor}/>
      <rect x="240" y="150" width="80" height="120" rx="8" fill={primaryColor}/>
      <rect x="350" y="150" width="220" height="200" rx="8" fill={primaryColor}/>
      <rect x="940" width="120" height="120" rx="8"
            fill={active === "cooler" ? activeColor : primaryColor}/>/>
      <rect x="600" width="230" height="120" rx="8"
            fill={active === "oil" ? activeColor : primaryColor}/>/>
      <rect x="23" y="170" width="35" height="35" rx="8"
            fill={active === "ps-9" ? activeColor : secondaryColor}/>/>
      <rect x="23" y="214" width="35" height="35" rx="8"
            fill={active === "ps-8" ? activeColor : secondaryColor}/>/>
      <rect x="370" y="295" width="35" height="35" rx="8"
            fill={active === "ps-6" ? activeColor : secondaryColor}/>/>
      <rect x="370" y="170" width="35" height="35" rx="8"
            fill={active === "ps-4" ? activeColor : secondaryColor}/>
      <rect x="622" y="250" width="35" height="35" rx="8"
            fill={active === "ps-2" ? activeColor : secondaryColor}/>
      <rect x="1002" y="250" width="35" height="35" rx="8"
            fill={active === "ps-1" ? activeColor : secondaryColor}/>
      <rect x="515" y="170" width="35" height="35" rx="8"
            fill={active === "ps-3" ? activeColor : secondaryColor}/>
      <rect x="515" y="295" width="35" height="35" rx="8"
            fill={active === "ps-5" ? activeColor : secondaryColor}/>
      <rect x="263" y="214" width="35" height="35" rx="8"
            fill={active === "ps-7" ? activeColor : secondaryColor}/>
    </svg>

  )
}

export default ExhausterSchema