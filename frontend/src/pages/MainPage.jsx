import React, {useEffect, useState} from "react"
import {Header, StatusBadge} from "../components"
import {fetchExhausters} from "../common"
import {Button, Table, Tooltip} from "@nextui-org/react"
import moment from "moment"
import {MdReadMore} from "react-icons/all"


const MainPage = () => {
  const [exhaustersData, setExhaustersData] = useState([]);

  useEffect(() => {
    fetchExhausters().then(data => {
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
        return "---"
      }
    }

    return (
      <Table.Row key={exhauster_id}>
        <Table.Cell>{name}</Table.Cell>
        <Table.Cell>{machine_name}</Table.Cell>
        <Table.Cell>{displayDate(last_replacement)}</Table.Cell>
        <Table.Cell>{displayDate(next_replacement_prediction)}</Table.Cell>
        <Table.Cell>
          <StatusBadge color="positive">ОК</StatusBadge>
        </Table.Cell>
        <Table.Cell>
        </Table.Cell>
      </Table.Row>
    )
  }

  return (
    <div className="m-2 md:m-10 mt-24 p-2 md:p-10 bg-white dark:bg-secondary-dark rounded-3xl">
      <Header title="Информация" category="Эксгаустеры" />
      <Table selectionMode="single" selectionBehavior="replace">
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
          <Table.Column
            hideHeader
            align="center"
          />
        </Table.Header>
        <Table.Body items={exhaustersData}>
          {renderRow}
        </Table.Body>
        <Table.Pagination
          shadow
          noMargin
          align="center"
          rowsPerPage={10}
          onPageChange={(page) => console.log({ page })}
        />
      </Table>
    </div>
  )
}

export default MainPage
