from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import pandas as pd
from schemas.event import ExhausterEvent
from schemas.status import (
    AlarmableValue,
    AlarmStatuses,
    Bearing,
    BearingVibration,
    DriveValue,
    GasCollectorValue,
    GateValveValue,
    OilValue,
    TemperatureValue,
    VibrationalBearing,
    WorkValue,
)


@dataclass
class MappingService:
    exhauster_count: int = 6

    def __post_init__(self):
        mappings: Tuple[pd.DataFrame, ...] = (
            pd.read_excel("data/mapping.xlsx", sheet_name="Эксгаустер № 1 (У-171)"),
            pd.read_excel("data/mapping.xlsx", sheet_name="Эксгаустер № 2 (У-172)"),
            pd.read_excel("data/mapping.xlsx", sheet_name="Эксгаустер № 3 (Ф-171)"),
            pd.read_excel("data/mapping.xlsx", sheet_name="Эксгаустер № 4 (Ф-172)"),
            pd.read_excel("data/mapping.xlsx", sheet_name="Эксгаустер № 5 (X-171)"),
            pd.read_excel("data/mapping.xlsx", sheet_name="Эксгаустер № 6 (X-172)"),
        )
        self.exhauster_row_to_signal_id: Dict[Tuple[int, int], str] = {}
        for exhauster_id, mapping in enumerate(mappings):
            for idx, row in mapping.iterrows():
                self.exhauster_row_to_signal_id[(exhauster_id, idx)] = row[
                    "Код сигнала в Kafka"
                ]

    def _get_value(
        self, record: Dict[str, Any], exhauster_id: int, row: int
    ) -> Optional[float]:
        return record.get(self.exhauster_row_to_signal_id[(exhauster_id, row)])

    def _get_bool_value(
        self, record: Dict[str, Any], exhauster_id: int, row: int
    ) -> Optional[bool]:
        value = record.get(self.exhauster_row_to_signal_id[(exhauster_id, row)])
        if value is None:
            return None
        return bool(int(value))

    def _get_alarmable_value(  # noqa: CCR001
        self,
        record: Dict[str, Any],
        exhauster_id: int,
        start_row: int,
    ) -> AlarmableValue:
        value = self._get_value(record, exhauster_id, start_row)
        alarm_max = self._get_value(record, exhauster_id, start_row + 1)
        alarm_min = self._get_value(record, exhauster_id, start_row + 2)
        warning_max = self._get_value(record, exhauster_id, start_row + 3)
        warning_min = self._get_value(record, exhauster_id, start_row + 4)
        if value is None:
            status = AlarmStatuses.UNKNOWN
        elif (alarm_min is not None and value < alarm_min) or (
            alarm_max is not None and value > alarm_max
        ):
            status = AlarmStatuses.ALARM
        elif (warning_min is not None and value < warning_min) or (
            warning_max is not None and value > warning_max
        ):
            status = AlarmStatuses.WARNING
        else:
            status = AlarmStatuses.OK

        return AlarmableValue(
            value=value,
            alarm_max=alarm_max,
            alarm_min=alarm_min,
            warning_max=warning_max,
            warning_min=warning_min,
            status=status,
        )

    def _get_bearing(
        self,
        record: Dict[str, Any],
        exhauster_id: int,
        start_row: int,
    ) -> Bearing:
        return Bearing(
            temperature=self._get_alarmable_value(record, exhauster_id, start_row)
        )

    def _get_vibrational_bearing(
        self,
        record: Dict[str, Any],
        exhauster_id: int,
        start_row: int,
    ) -> VibrationalBearing:
        return VibrationalBearing(
            temperature=self._get_alarmable_value(record, exhauster_id, start_row),
            vibration=BearingVibration(
                vibration_axial=self._get_alarmable_value(
                    record, exhauster_id, start_row + 5
                ),
                vibration_horizontal=self._get_alarmable_value(
                    record, exhauster_id, start_row + 10
                ),
                vibration_vertical=self._get_alarmable_value(
                    record, exhauster_id, start_row + 15
                ),
            ),
        )

    def map_signals(
        self, exhauster_event: ExhausterEvent, record: Dict[str, Any]
    ) -> None:
        exhauster_id = exhauster_event.exhauster_id

        exhauster_event.status.bearing_1 = self._get_vibrational_bearing(
            record, exhauster_id, start_row=0
        )
        exhauster_event.status.bearing_2 = self._get_vibrational_bearing(
            record, exhauster_id, start_row=20
        )

        exhauster_event.status.bearing_3 = self._get_bearing(
            record, exhauster_id, start_row=40
        )
        exhauster_event.status.bearing_4 = self._get_bearing(
            record, exhauster_id, start_row=45
        )
        exhauster_event.status.bearing_5 = self._get_bearing(
            record, exhauster_id, start_row=50
        )
        exhauster_event.status.bearing_6 = self._get_bearing(
            record, exhauster_id, start_row=55
        )

        exhauster_event.status.bearing_7 = self._get_vibrational_bearing(
            record, exhauster_id, start_row=60
        )
        exhauster_event.status.bearing_8 = self._get_vibrational_bearing(
            record, exhauster_id, start_row=80
        )

        exhauster_event.status.bearing_9 = self._get_bearing(
            record, exhauster_id, start_row=100
        )

        exhauster_event.status.cooler_water = TemperatureValue(
            temperature_after=self._get_value(record, exhauster_id, 105),
            temperature_before=self._get_value(record, exhauster_id, 106),
        )
        exhauster_event.status.cooler_oil = TemperatureValue(
            temperature_after=self._get_value(record, exhauster_id, 107),
            temperature_before=self._get_value(record, exhauster_id, 108),
        )

        exhauster_event.status.gas_collector = GasCollectorValue(
            temperature_before=self._get_value(record, exhauster_id, 109),
            underpressure_before=self._get_value(record, exhauster_id, 110),
        )

        exhauster_event.status.gate_valve = GateValveValue(
            gas_valve_closed=self._get_bool_value(record, exhauster_id, 111),
            gas_valve_open=self._get_bool_value(record, exhauster_id, 112),
            gas_valve_position=self._get_value(record, exhauster_id, 113),
        )

        exhauster_event.status.drive = DriveValue(
            rotor_current=self._get_value(record, exhauster_id, 114),
            rotor_voltage=self._get_value(record, exhauster_id, 115),
            stator_current=self._get_value(record, exhauster_id, 116),
            stator_voltage=self._get_value(record, exhauster_id, 117),
        )

        exhauster_event.status.oil = OilValue(
            oil_level=self._get_value(record, exhauster_id, 118),
            oil_pressure=self._get_value(record, exhauster_id, 119),
        )

        exhauster_event.status.work = WorkValue(
            is_working=self._get_bool_value(record, exhauster_id, 120)
        )
