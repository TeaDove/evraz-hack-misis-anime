import React from "react"
import {Link, NavLink} from "react-router-dom"
import {RiDashboardFill, GrFanOption} from "react-icons/all.js"

const Sidebar = () => {
  const activeLink = 'flex items-center gap-5 pl-4 pt-3 pb-2.5 rounded-lg text-white text-md m-2';
  const normalLink = 'flex items-center gap-5 pl-4 pt-3 pb-2.5 rounded-lg text-md text-gray-700 dark:text-gray-200 dark:hover:text-black hover:bg-light-gray m-2';

  return (
    <div className="m-3 h-screen md:overflow-hidden overflow-auto md:hover:overflow-auto pb-10">
      <div className="flex justify-between items-center">
        <Link to="/" className="items-center gap-3 ml-3 mt-4 flex text-xl font-extrabold tracking-tight dark:text-white text-slate-900">
          <RiDashboardFill/> <span>Dashboard</span>
        </Link>
      </div>
      <div className="mt-10">
        <div>
          <p className="text-gray-400 dark:text-gray-400 m-3 mt-4 uppercase">
            Эксгаустеры
          </p>
            <NavLink
              to={`/`}
              style={({ isActive }) => ({
                backgroundColor: isActive ? "blue" : '',
              })}
              className={({ isActive }) => (isActive ? activeLink : normalLink)}
            >
              <span className="capitalize ">Информация</span>
            </NavLink>
        </div>
      </div>
    </div>
  )
}

export default Sidebar;
