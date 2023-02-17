from datetime import datetime

from pydantic import BaseModel


class AlarmableValue(BaseModel):
    value: float
    alarm_max: float
    alarm_min: float
    warning_max: float
    warning_min: float


class BearingVibration(BaseModel):
    vibration_axial: AlarmableValue
    vibration_horizontal: AlarmableValue
    vibration_vertical: AlarmableValue


class Bearing(BaseModel):
    temperature: AlarmableValue


class VibrationalBearing(Bearing):
    vibration: BearingVibration


class TemperatureValue(BaseModel):
    temperature_after: float
    temperature_before: float


class GasCollectorValue(BaseModel):
    temperature_before: float
    underpressure_before: float


class GateValveValue(BaseModel):
    gas_valve_closed: float
    gas_valve_open: float
    gas_valve_position: float


class DriveValue(BaseModel):
    rotor_current: float
    rotor_voltage: float
    stator_current: float
    stator_voltage: float


class OilValue(BaseModel):
    oil_level: float
    oil_pressure: float


class WorkValue(BaseModel):
    is_working: bool


class ExhausterEvent(BaseModel):
    create_at: datetime

    exhauster_id: int

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
