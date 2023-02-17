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
    vibration_axial: AlarmableValue = AlarmableValue()
    vibration_horizontal: AlarmableValue = AlarmableValue()
    vibration_vertical: AlarmableValue = AlarmableValue()


class Bearing(BaseModel):
    temperature: AlarmableValue = AlarmableValue()


class VibrationalBearing(Bearing):
    vibration: BearingVibration = BearingVibration()


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
    is_working: Optional[int] = None


class ExhausterEvent(BaseModel):
    created_at: Optional[datetime] = None

    exhauster_id: int

    bearing_1: VibrationalBearing = VibrationalBearing()
    bearing_2: VibrationalBearing = VibrationalBearing()
    bearing_3: Bearing = Bearing()
    bearing_4: Bearing = Bearing()
    bearing_5: Bearing = Bearing()
    bearing_6: Bearing = Bearing()
    bearing_7: VibrationalBearing = VibrationalBearing()
    bearing_8: VibrationalBearing = VibrationalBearing()
    bearing_9: Bearing = Bearing()
    cooler_water: TemperatureValue = TemperatureValue()
    cooler_oil: TemperatureValue = TemperatureValue()
    gas_collector: GasCollectorValue = GasCollectorValue()
    gate_valve: GateValveValue = GateValveValue()
    drive: DriveValue = DriveValue()
    oil: OilValue = OilValue()
    work: WorkValue = WorkValue()

    # {
    #     "created_at": 1,
    #     "exhauster_id": 1,
    #     "bearing_1_vibration_vibration_axial_value": 111,
    #     "bearing_1_vibration_vibration_axial_alarm_max": 111,
    # }
    # def export(self):
    #     for field in self.__fields__:
