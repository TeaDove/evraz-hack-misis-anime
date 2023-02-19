import React, {useEffect, useState} from "react"
import {Button, Col, Container, Loading, Progress, Row} from "@nextui-org/react"
import {IoChevronBack, IoSnow, RxReload} from "react-icons/all.js"
import {ExhausterSchema} from "../components"
import {exhausterStatus, fetchExhausterInfo, roundNum} from "../common"
import {useNavigate, useParams} from "react-router-dom"

const ExhausterInfo = () => {
  const {exhausterId} = useParams()
  const [active, setActive] = useState(null)
  const [exhausterData, setExhausterData] = useState(null)
  const [loading, setLoading] = useState(true)

  const navigate = useNavigate()

  const bearingStyles = {
    "UNKNOWN": "bg-gray-500",
    "OK": "bg-green-500",
    "WARNING": "bg-yellow-500",
    "ALARM": "bg-rose-500"
  }

  const loadData = () => {
    fetchExhausterInfo(exhausterId).then(e => {
      setExhausterData(e)
      setLoading(false)
    })
  }

  useEffect(loadData, [exhausterId])

  const handleLeave = () => setActive(null)
  const handleEnter = (element) => {
    return () => setActive(element)
  }

  if (loading || exhausterData === null) {
    return (
      <div className="w-full h-screen flex items-center justify-center">
        <Loading color="primary" textColor="primary" size="xl"/>
      </div>
    )
  }

  const {status} = exhausterData

  return (
    <div className="flex flex-col">
    <div className="flex flex-row justify-between m-2 md:mx-10 mt-12 items-center">
      <Button
        color="secondary" flat
        onClick={() => navigate("/")}
        icon={<IoChevronBack fill="white" size={18} filled/>}
      >Назад</Button>
      <span className="text-xl font-extrabold text-slate-900">
        {exhausterData["name"]}
      </span>
      <Button
        color="secondary" flat
        onClick={() => loadData()}
        icon={<RxReload fill="white" size={18} filled/>}
      >Обновить</Button>
    </div>
    <div className="grid grid-flow-col grid-cols-3 gap-8 m-2 md:m-10">
      <div className="bg-white rounded-2xl p-4 ">
        <div className="mx-2 my-5 flex justify-center">
          <ExhausterSchema
            width="75%" height="75%"
            primaryColor="#f3f3f3"
            secondaryColor="#e6e6e6"
            activeColor="#86efac"
            active={active}
          />
        </div>
      </div>
      <div
        className="bg-white rounded-2xl p-4 col-start-2"
        onMouseEnter={handleEnter("oil")}
        onMouseLeave={handleLeave}
      >
        <span className="text-2xl font-extrabold tracking-tight text-slate-900 dark:text-white">
          Маслобак
        </span>
        <div className="mt-4">
          <div className="text-base font-extrabold text-slate-700 flex justify-between">
            <span>Уровень масла</span>
            <span>{(status.oil && status.oil.oil_level) ? `${roundNum(status.oil.oil_level)}%` : "н/д"}</span>
          </div>
          {status.oil && status.oil.oil_level &&
            <div className="mt-1">
              <Progress
                squared
                color={status.oil.oil_level < 20 ? "error" : "primary"}
                value={status.oil.oil_level}
                max={100}
              />
            </div>
          }
        </div>
        <div className="mt-3">
          <div className="text-base font-extrabold text-slate-700 flex justify-between">
            <span>Давление масла</span>
            <span>{(status.oil && status.oil.oil_pressure) ? `${roundNum(status.oil.oil_pressure, 2)} кг/см2` : "н/д"}</span>
          </div>
          {status.oil && status.oil.oil_pressure &&
            <div className="mt-1">
              <Progress
                squared color={status.oil.oil_pressure < 0.5 ? "error" : "primary"}
                value={status.oil.oil_pressure}
                max={6}/>
            </div>
          }
        </div>
      </div>
      <div
        className="bg-blue-600 rounded-2xl p-4 col-start-3"
        onMouseEnter={handleEnter("cooler")}
        onMouseLeave={handleLeave}
      >
        <div className="flex flex-row gap-4 items-center justify-between">
          <span className="text-2xl font-extrabold tracking-tight text-white">
            Охладитель
          </span>
          <IoSnow fill="white" size={26}/>
        </div>
        <div className="mt-4 flex flex-col gap-1">
          <div className="text-base font-extrabold text-white flex justify-between">
            <span>Вход воды</span>
            <span>
              {(status.cooler_water && status.cooler_water.temperature_before) ?
                `${roundNum(status.cooler_water.temperature_before, 1)} °C` : "н/д"}
            </span>
          </div>
          <div className="text-base font-extrabold text-white flex justify-between">
            <span>Вход масла</span>
            <span>
              {(status.cooler_oil && status.cooler_oil.temperature_before) ?
              `${roundNum(status.cooler_oil.temperature_before, 1)} °C` : "н/д"}
            </span>
          </div>
          <div className="text-base font-extrabold text-white flex justify-between mt-2">
            <span>Выход воды</span>
            <span>
              {(status.cooler_water && status.cooler_water.temperature_after) ?
                `${roundNum(status.cooler_water.temperature_after, 1)} °C` : "н/д"}
            </span>
          </div>
          <div className="text-base font-extrabold text-white flex justify-between">
            <span>Выход масла</span>
            <span>
              {(status.cooler_water && status.cooler_oil.temperature_after) ?
              `${roundNum(status.cooler_oil.temperature_after, 1)} °C` : "н/д"}
            </span>
          </div>
        </div>
      </div>
    </div>
    <div className="grid grid-flow-col grid-cols-3 grid-rows-2 gap-8 mx-2 mb-2 md:mx-10 md:mb-10 mt-0">
      <div
        className="bg-white rounded-2xl p-4"
        onMouseEnter={handleEnter("main-engine")}
        onMouseLeave={handleLeave}
      >
        <span className="text-2xl font-extrabold tracking-tight text-slate-900 dark:text-white">
          Главный привод
        </span>
        <div className="mt-4">
          <div className="text-base font-extrabold text-slate-700 flex justify-between">
            <span>Ток</span>
            <span>{(status.drive && status.drive.rotor_current) ?
              `${roundNum(status.drive.rotor_current)} А` : "н/д"}</span>
          </div>
        </div>
        <div className="mt-1">
          <div className="text-base font-extrabold text-slate-700 flex justify-between">
            <span>Ток двигателя</span>
            <span>{(status.drive && status.drive.stator_current) ?
              `${roundNum(status.drive.stator_current)} А` : "н/д"}</span>
          </div>
        </div>
        <div className="mt-1">
          <div className="text-base font-extrabold text-slate-700 flex justify-between">
            <span>Напряжение ротора</span>
            <span>{(status.drive && status.drive.rotor_voltage) ?
              `${roundNum(status.drive.rotor_voltage)} кВ` : "н/д"}</span>
          </div>
        </div>
        <div className="mt-1">
          <div className="text-base font-extrabold text-slate-700 flex justify-between">
            <span>Напряжение статора</span>
            <span>{(status.drive && status.drive.stator_voltage) ?
              `${roundNum(status.drive.stator_voltage)} кВ` : "н/д"}</span>
          </div>
        </div>
      </div>
      <div
        className="bg-white rounded-2xl p-4"
        onMouseEnter={handleEnter("fan")}
        onMouseLeave={handleLeave}
      >
        <span className="text-2xl font-extrabold tracking-tight text-slate-900 dark:text-white">
          Состояние
        </span>
        <div className="mt-4">
          <div className="text-base font-extrabold text-slate-700 flex justify-between">
            <span>Температура газа</span>
            <span>{(status.gas_collector && status.gas_collector.temperature_before) ?
              `${roundNum(status.gas_collector.temperature_before, 1)} °C` : "н/д"}</span>
          </div>
        </div>
        <div className="mt-1">
          <div className="text-base font-extrabold text-slate-700 flex justify-between">
            <span>Разрежение</span>
            <span>{(status.gas_collector && status.gas_collector.underpressure_before) ?
              `${roundNum(status.gas_collector.underpressure_before)} мм.р.ст.` : "н/д"}</span>
          </div>
        </div>
        <div className="mt-1">
          <div className="text-base font-extrabold text-slate-700 flex justify-between">
            <span>Уровень пыли</span>
            <span>н/д</span>
          </div>
        </div>
        <div className="mt-4">
          <div className="text-base font-extrabold text-slate-700 flex justify-between">
            <span>Положение дымового шибера</span>
            <span>{(status.gate_valve && status.gate_valve.gas_valve_position) ?
              `${roundNum(status.gate_valve.gas_valve_position)}%` : "н/д"}</span>
          </div>
          {status.gate_valve && status.gate_valve.gas_valve_position &&
            <div className="mt-1">
              <Progress squared color="success" value={100 - status.gate_valve.gas_valve_position} max={100}/>
            </div>
          }
        </div>
      </div>
      <div className="bg-white rounded-2xl p-4 row-span-2 col-span-2">
        <span className="text-2xl font-extrabold tracking-tight text-slate-900 dark:text-white">
          Подшипники
        </span>
        <div className="grid grid-cols-5 grid-rows-2 gap-3 mt-4">
          <div
            className={`rounded p-4 ${bearingStyles[exhausterStatus(status["bearing_1"])]}`}
            onMouseEnter={handleEnter("ps-1")}
            onMouseLeave={handleLeave}
          >
            <span className="text-white opacity-80 font-bold">
              №1
            </span>
            <div className="text-base font-extrabold text-white flex justify-between mt-4">
              <span>Темп.</span>
              <span>{(status.bearing_1 && status.bearing_1.temperature) ?
                `${roundNum(status.bearing_1.temperature.value, 1)} °C` : "н/д"}</span>
            </div>
            <div className="text-base font-extrabold text-white flex justify-between mt-1">
              <span>Верт.</span>
              <span>{(status.bearing_1 && status.bearing_1.vibration) ?
                `${roundNum(status.bearing_1.vibration.vibration_vertical.value, 2)} мм/c` : "н/д"}</span>
            </div>
            <div className="text-base font-extrabold text-white flex justify-between mt-1">
              <span>Гориз.</span>
              <span>{(status.bearing_1 && status.bearing_1.vibration) ?
                `${roundNum(status.bearing_1.vibration.vibration_horizontal.value, 2)} мм/c` : "н/д"}</span>
            </div>
            <div className="text-base font-extrabold text-white flex justify-between mt-1">
              <span>Ось.</span>
              <span>{(status.bearing_1 && status.bearing_1.vibration) ?
                `${roundNum(status.bearing_1.vibration.vibration_axial.value, 2)} мм/c` : "н/д"}</span>
            </div>
          </div>
          <div
            className={`rounded p-4 ${bearingStyles[exhausterStatus(status["bearing_2"])]}`}
            onMouseEnter={handleEnter("ps-2")}
            onMouseLeave={handleLeave}
          >
            <span className="text-white opacity-80 font-bold">
              №2
            </span>
            <div className="text-base font-extrabold text-white flex justify-between mt-4">
              <span>Темп.</span>
              <span>{(status.bearing_2 && status.bearing_2.temperature) ?
                `${roundNum(status.bearing_2.temperature.value, 1)} °C` : "н/д"}</span>
            </div>
            <div className="text-base font-extrabold text-white flex justify-between mt-1">
              <span>Верт.</span>
              <span>{(status.bearing_2 && status.bearing_2.vibration) ?
                `${roundNum(status.bearing_2.vibration.vibration_vertical.value, 2)} мм/c` : "н/д"}</span>
            </div>
            <div className="text-base font-extrabold text-white flex justify-between mt-1">
              <span>Гориз.</span>
              <span>{(status.bearing_2 && status.bearing_2.vibration) ?
                `${roundNum(status.bearing_2.vibration.vibration_horizontal.value, 2)} мм/c` : "н/д"}</span>
            </div>
            <div className="text-base font-extrabold text-white flex justify-between mt-1">
              <span>Ось.</span>
              <span>{(status.bearing_2 && status.bearing_2.vibration) ?
                `${roundNum(status.bearing_2.vibration.vibration_axial.value, 2)} мм/c` : "н/д"}</span>
            </div>
          </div>
          <div
            className={`rounded p-4 ${bearingStyles[exhausterStatus(status["bearing_3"])]}`}
            onMouseEnter={handleEnter("ps-3")}
            onMouseLeave={handleLeave}
          >
            <span className="text-white opacity-80 font-bold">
              №3
            </span>
            <div className="text-base font-extrabold text-white flex justify-between mt-4">
              <span>Темп.</span>
              <span>{(status.bearing_3 && status.bearing_3.temperature) ?
                `${roundNum(status.bearing_3.temperature.value, 1)} °C` : "н/д"}</span>
            </div>
          </div>
          <div
            className={`rounded p-4 ${bearingStyles[exhausterStatus(status["bearing_4"])]}`}
            onMouseEnter={handleEnter("ps-4")}
            onMouseLeave={handleLeave}
          >
            <span className="text-white opacity-80 font-bold">
              №4
            </span>
            <div className="text-base font-extrabold text-white flex justify-between mt-4">
              <span>Темп.</span>
              <span>{(status.bearing_4 && status.bearing_4.temperature) ?
                `${roundNum(status.bearing_4.temperature.value, 1)} °C` : "н/д"}</span>
            </div>
          </div>
          <div
            className={`rounded p-4 ${bearingStyles[exhausterStatus(status["bearing_5"])]}`}
            onMouseEnter={handleEnter("ps-5")}
            onMouseLeave={handleLeave}
          >
            <span className="text-white opacity-80 font-bold">
              №5
            </span>
            <div className="text-base font-extrabold text-white flex justify-between mt-4">
              <span>Темп.</span>
              <span>{(status.bearing_5 && status.bearing_5.temperature) ?
                `${roundNum(status.bearing_5.temperature.value, 1)} °C` : "н/д"}</span>
            </div>
          </div>
          <div
            className={`rounded p-4 ${bearingStyles[exhausterStatus(status["bearing_7"])]}`}
            onMouseEnter={handleEnter("ps-7")}
            onMouseLeave={handleLeave}
          >
            <span className="text-white opacity-80 font-bold">
              №7
            </span>
            <div className="text-base font-extrabold text-white flex justify-between mt-4">
              <span>Темп.</span>
              <span>{(status.bearing_7 && status.bearing_7.temperature) ?
                `${roundNum(status.bearing_7.temperature.value, 1)} °C` : "н/д"}</span>
            </div>
            <div className="text-base font-extrabold text-white flex justify-between mt-1">
              <span>Верт.</span>
              <span>{(status.bearing_7 && status.bearing_7.vibration) ?
                `${roundNum(status.bearing_7.vibration.vibration_vertical.value, 2)} мм/c` : "н/д"}</span>
            </div>
            <div className="text-base font-extrabold text-white flex justify-between mt-1">
              <span>Гориз.</span>
              <span>{(status.bearing_7 && status.bearing_7.vibration) ?
                `${roundNum(status.bearing_7.vibration.vibration_horizontal.value, 2)} мм/c` : "н/д"}</span>
            </div>
            <div className="text-base font-extrabold text-white flex justify-between mt-1">
              <span>Ось.</span>
              <span>{(status.bearing_7 && status.bearing_7.vibration) ?
                `${roundNum(status.bearing_7.vibration.vibration_axial.value, 2)} мм/c` : "н/д"}</span>
            </div>
          </div>
          <div
            className={`rounded p-4 ${bearingStyles[exhausterStatus(status["bearing_8"])]}`}
            onMouseEnter={handleEnter("ps-8")}
            onMouseLeave={handleLeave}
          >
            <span className="text-white opacity-80 font-bold">
              №8
            </span>
            <div className="text-base font-extrabold text-white flex justify-between mt-4">
              <span>Темп.</span>
              <span>{(status.bearing_8 && status.bearing_8.temperature) ?
                `${roundNum(status.bearing_8.temperature.value, 1)} °C` : "н/д"}</span>
            </div>
            <div className="text-base font-extrabold text-white flex justify-between mt-1">
              <span>Верт.</span>
              <span>{(status.bearing_8 && status.bearing_8.vibration) ?
                `${roundNum(status.bearing_8.vibration.vibration_vertical.value, 2)} мм/c` : "н/д"}</span>
            </div>
            <div className="text-base font-extrabold text-white flex justify-between mt-1">
              <span>Гориз.</span>
              <span>{(status.bearing_8 && status.bearing_1.vibration) ?
                `${roundNum(status.bearing_8.vibration.vibration_horizontal.value, 2)} мм/c` : "н/д"}</span>
            </div>
            <div className="text-base font-extrabold text-white flex justify-between mt-1">
              <span>Ось.</span>
              <span>{(status.bearing_8 && status.bearing_8.vibration) ?
                `${roundNum(status.bearing_8.vibration.vibration_axial.value, 2)} мм/c` : "н/д"}</span>
            </div>
          </div>
          <div
            className={`rounded p-4 ${bearingStyles[exhausterStatus(status["bearing_6"])]}`}
            onMouseEnter={handleEnter("ps-6")}
            onMouseLeave={handleLeave}
          >
            <span className="text-white opacity-80 font-bold">
              №6
            </span>
            <div className="text-base font-extrabold text-white flex justify-between mt-4">
              <span>Темп.</span>
              <span>{(status.bearing_6 && status.bearing_6.temperature) ?
                `${roundNum(status.bearing_6.temperature.value, 1)} °C` : "н/д"}</span>
            </div>
          </div>
          <div
            className={`rounded p-4 col-span-2 ${bearingStyles[exhausterStatus(status["bearing_9"])]}`}
            onMouseEnter={handleEnter("ps-9")}
            onMouseLeave={handleLeave}
          >
            <span className="text-white opacity-80 font-bold">
              №9
            </span>
            <div className="text-base font-extrabold text-white flex justify-between mt-4">
              <span>Темп.</span>
              <span>{(status.bearing_9 && status.bearing_9.temperature) ?
                `${roundNum(status.bearing_9.temperature.value, 1)} °C` : "н/д"}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    </div>
  )
}

export default ExhausterInfo
