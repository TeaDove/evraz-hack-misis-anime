import React, {useEffect, useState} from "react"
import {Header, StatusBadge} from "../components"
import {exhausterStatus, fetchExhausters} from "../common"
import {Button, Table, Tooltip} from "@nextui-org/react"
import moment from "moment"
import {useAsyncList} from "@nextui-org/react"
import {useNavigate} from "react-router-dom"


const MainPage = () => {
  const [exhaustersData, setExhaustersData] = useState([]);
  const [loading, setLoading] = useState(true)

  const navigate = useNavigate();

  useEffect(() => {
    fetchExhausters().then(data => {
      setLoading(false)
      setExhaustersData(data)
    })
  }, [])

  const renderCell = (item, columnKey) => {
    return item[columnKey];
  }

  const renderRow = (item) => {
    const {
      exhauster_id,
      name,
      machine_name,
      last_replacement,
      next_replacement_prediction
    } = item

    const displayDate = date => {
      if (date) {
        return moment(date).fromNow()
      } else {
        return "н/д"
      }
    }

    const status = exhausterStatus(item["status"])

    return (
      <Table.Row key={exhauster_id}>
        <Table.Cell>{name}</Table.Cell>
        <Table.Cell>{machine_name}</Table.Cell>
        <Table.Cell>{displayDate(last_replacement)}</Table.Cell>
        <Table.Cell>{displayDate(next_replacement_prediction)}</Table.Cell>
        <Table.Cell>
          <StatusBadge
            color={status}
          >{status}</StatusBadge>
        </Table.Cell>
      </Table.Row>
    )
  }

  return (
    <div className="m-2 md:m-10 mt-24 p-2 md:p-10 bg-white dark:bg-secondary-dark rounded-3xl">
      <Header title="Информация" category="Эксгаустеры" />
      <Table
        selectionMode="single"
        selectionBehavior="replace"
        onSelectionChange={e => navigate(`/exhauster/${e.currentKey}`)}
      >
        <Table.Header>
          <Table.Column key="name">
            ЭКСГАУСТЕР
          </Table.Column>
          <Table.Column key="machine_name">
            МАШИНА
          </Table.Column>
          <Table.Column key="last_replacement">
            ПОСЛЕДНЯЯ ЗАМЕНА
          </Table.Column>
          <Table.Column key="next_replacement_prediction">
            ОЖИДАЕМАЯ ЗАМЕНА
          </Table.Column>
          <Table.Column key="status">
            СТАТУС
          </Table.Column>
        </Table.Header>
        <Table.Body items={exhaustersData} loadingState={loading ? "loading" : "idle"}>
          {renderRow}
        </Table.Body>
        <Table.Pagination
          shadow
          align="center"
          rowsPerPage={10}
          onPageChange={(page) => {}}
        />
      </Table>
    </div>
  )
}

export default MainPage
