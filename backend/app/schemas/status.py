import enum
from typing import Optional

from pydantic import BaseModel


class AlarmStatuses(str, enum.Enum):
    OK = "OK"
    WARNING = "WARNING"
    ALARM = "ALARM"
    UNKNOWN = "UNKNOWN"


class AlarmableValue(BaseModel):
    value: Optional[float] = None
    alarm_max: Optional[float] = None
    alarm_min: Optional[float] = None
    warning_max: Optional[float] = None
    warning_min: Optional[float] = None
    status: AlarmStatuses = AlarmStatuses.UNKNOWN


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
    gas_valve_closed: Optional[bool] = None
    gas_valve_open: Optional[bool] = None
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
    is_working: Optional[bool] = None


class ExhausterStatus(BaseModel):
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
