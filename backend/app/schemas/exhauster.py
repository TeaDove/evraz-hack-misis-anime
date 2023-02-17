from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class AlarmableValue(BaseModel):
    value: Optional[float] = None
    alarm_max: Optional[float] = None
    alarm_min: Optional[float] = None
    warning_max: Optional[float] = None
    warning_min: Optional[float] = None


class BearingVibration(BaseModel):
    vibration_axial: AlarmableValue
    vibration_horizontal: AlarmableValue
    vibration_vertical: AlarmableValue


class Bearing(BaseModel):
    temperature: AlarmableValue


class VibrationalBearing(Bearing):
    vibration: BearingVibration


class TemperatureValue(BaseModel):
    temperature_after: Optional[float] = None
    temperature_before: Optional[float] = None


class GasCollectorValue(BaseModel):
    temperature_before: Optional[float] = None
    underpressure_before: Optional[float] = None


class GateValveValue(BaseModel):
    gas_valve_closed: Optional[float] = None
    gas_valve_open: Optional[float] = None
    gas_valve_position: Optional[float] = None


class DriveValue(BaseModel):
    rotor_current: Optional[float] = None
    rotor_voltage: Optional[float] = None
    stator_current: Optional[float] = None
    stator_voltage: Optional[float] = None


class OilValue(BaseModel):
    oil_level: Optional[float] = None
    oil_pressure: Optional[float] = None


class WorkValue(BaseModel):
    is_working: Optional[float] = None


class ExhausterEvent(BaseModel):
    create_at: datetime

    exhauster_id: Optional[float] = None

    bearing_1: VibrationalBearing
    bearing_2: VibrationalBearing
    bearing_3: Bearing
    bearing_4: Bearing
    bearing_5: Bearing
    bearing_6: Bearing
    bearing_7: VibrationalBearing
    bearing_8: VibrationalBearing
    bearing_9: Bearing
    cooler_water: TemperatureValue
    cooler_oil: TemperatureValue
    gas_collector: GasCollectorValue
    gate_valve: GateValveValue
    drive: DriveValue
    oil: OilValue
    work: WorkValue

    # {
    #     "created_at": 1,
    #     "exhauster_id": 1,
    #     "bearing_1_vibration_vibration_axial_value": 111,
    #     "bearing_1_vibration_vibration_axial_alarm_max": 111,
    # }
    # def export(self):
    #     for field in self.__fields__:
