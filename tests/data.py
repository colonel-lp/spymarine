from spymarine import (
    Barometer,
    BarometerSensor,
    Battery,
    BatteryType,
    CapacitySensor,
    ChargeSensor,
    CurrentDevice,
    CurrentSensor,
    FluidType,
    PicoInternal,
    ResistiveDevice,
    ResistiveSensor,
    Tank,
    TankLevelSensor,
    TankVolumeSensor,
    TemperatureDevice,
    TemperatureSensor,
    VoltageDevice,
    VoltageSensor,
)

DEVICES = [
    Barometer(
        device_id=5,
        name="Barometer",
        pressure=BarometerSensor(sensor_id=300, value=0.0),
    ),
    PicoInternal(
        device_id=6,
        name="PICO INTERNAL",
        voltage=VoltageSensor(sensor_id=500, value=0.0),
    ),
    VoltageDevice(
        device_id=10,
        name="ST107 [5596] 1",
        voltage=VoltageSensor(sensor_id=1100, value=0.0),
    ),
    VoltageDevice(
        device_id=11,
        name="ST107 [5596] 2",
        voltage=VoltageSensor(sensor_id=1200, value=0.0),
    ),
    VoltageDevice(
        device_id=12,
        name="ST107 [5596] 3",
        voltage=VoltageSensor(sensor_id=1300, value=0.0),
    ),
    ResistiveDevice(
        device_id=13,
        name="ST107 [5596] 1",
        resistance=ResistiveSensor(sensor_id=1400, value=0.0),
    ),
    ResistiveDevice(
        device_id=14,
        name="ST107 [5596] 2",
        resistance=ResistiveSensor(sensor_id=1500, value=0.0),
    ),
    ResistiveDevice(
        device_id=15,
        name="ST107 [5596] 3",
        resistance=ResistiveSensor(sensor_id=1600, value=0.0),
    ),
    ResistiveDevice(
        device_id=16,
        name="ST107 [5596] 4",
        resistance=ResistiveSensor(sensor_id=1700, value=0.0),
    ),
    CurrentDevice(
        device_id=18,
        name="SC303 [5499]",
        current=CurrentSensor(sensor_id=1900, value=0.0),
    ),
    VoltageDevice(
        device_id=19,
        name="SC303 [5499] 1",
        voltage=VoltageSensor(sensor_id=2100, value=0.0),
    ),
    VoltageDevice(
        device_id=20,
        name="SC303 [5499] 2",
        voltage=VoltageSensor(sensor_id=2200, value=0.0),
    ),
    ResistiveDevice(
        device_id=21,
        name="SC303 [5499] 1",
        resistance=ResistiveSensor(sensor_id=2300, value=0.0),
    ),
    ResistiveDevice(
        device_id=22,
        name="SC303 [5499] 2",
        resistance=ResistiveSensor(sensor_id=2400, value=0.0),
    ),
    ResistiveDevice(
        device_id=23,
        name="SC303 [5499] 3",
        resistance=ResistiveSensor(sensor_id=2500, value=0.0),
    ),
    Battery(
        device_id=24,
        name="Bulltron",
        capacity=300.0,
        battery_type=BatteryType.LIFEPO4,
        charge=ChargeSensor(sensor_id=2600, value=0.0),
        remaining_capacity=CapacitySensor(sensor_id=2601, value=0.0),
        current=CurrentSensor(sensor_id=2602, value=0.0),
        voltage=VoltageSensor(sensor_id=2603, value=0.0),
    ),
    TemperatureDevice(
        device_id=25,
        name="Batterie",
        temperature=TemperatureSensor(sensor_id=3100, value=0.0),
    ),
    Tank(
        device_id=26,
        name="Frischwasser",
        capacity=100.0,
        fluid_type=FluidType.FRESH_WATER,
        volume=TankVolumeSensor(sensor_id=3200, value=0.0),
        level=TankLevelSensor(sensor_id=3201, value=0.0),
    ),
    Battery(
        device_id=27,
        name="Starterbatterie",
        capacity=100.0,
        battery_type=BatteryType.AGM,
        charge=ChargeSensor(sensor_id=3300, value=0.0),
        remaining_capacity=CapacitySensor(sensor_id=3301, value=0.0),
        current=CurrentSensor(sensor_id=3302, value=0.0),
        voltage=VoltageSensor(sensor_id=3303, value=0.0),
    ),
    Tank(
        device_id=28,
        name="Abwasser",
        capacity=70.0,
        fluid_type=FluidType.WASTE_WATER,
        volume=TankVolumeSensor(sensor_id=3800, value=0.0),
        level=TankLevelSensor(sensor_id=3801, value=0.0),
    ),
    TemperatureDevice(
        device_id=29,
        name="Innen",
        temperature=TemperatureSensor(sensor_id=3900, value=0.0),
    ),
    TemperatureDevice(
        device_id=30,
        name="Au�en ",
        temperature=TemperatureSensor(sensor_id=4000, value=0.0),
    ),
    TemperatureDevice(
        device_id=31,
        name="Boiler",
        temperature=TemperatureSensor(sensor_id=4100, value=0.0),
    ),
]


DEVICES_JSON = [
    {
        "device_id": 5,
        "name": "Barometer",
        "pressure": {"id": 300, "value": 0.0, "unit": "mbar"},
        "type": "barometer",
    },
    {
        "device_id": 6,
        "name": "PICO INTERNAL",
        "voltage": {"id": 500, "value": 0.0, "unit": "volt"},
        "type": "pico_internal",
    },
    {
        "device_id": 10,
        "name": "ST107 [5596] 1",
        "voltage": {"id": 1100, "value": 0.0, "unit": "volt"},
        "type": "voltage",
    },
    {
        "device_id": 11,
        "name": "ST107 [5596] 2",
        "voltage": {"id": 1200, "value": 0.0, "unit": "volt"},
        "type": "voltage",
    },
    {
        "device_id": 12,
        "name": "ST107 [5596] 3",
        "voltage": {"id": 1300, "value": 0.0, "unit": "volt"},
        "type": "voltage",
    },
    {
        "device_id": 13,
        "name": "ST107 [5596] 1",
        "resistance": {"id": 1400, "value": 0.0, "unit": "ohm"},
        "type": "resistive",
    },
    {
        "device_id": 14,
        "name": "ST107 [5596] 2",
        "resistance": {"id": 1500, "value": 0.0, "unit": "ohm"},
        "type": "resistive",
    },
    {
        "device_id": 15,
        "name": "ST107 [5596] 3",
        "resistance": {"id": 1600, "value": 0.0, "unit": "ohm"},
        "type": "resistive",
    },
    {
        "device_id": 16,
        "name": "ST107 [5596] 4",
        "resistance": {"id": 1700, "value": 0.0, "unit": "ohm"},
        "type": "resistive",
    },
    {
        "device_id": 18,
        "name": "SC303 [5499]",
        "current": {"id": 1900, "value": 0.0, "unit": "ampere"},
        "type": "current",
    },
    {
        "device_id": 19,
        "name": "SC303 [5499] 1",
        "voltage": {"id": 2100, "value": 0.0, "unit": "volt"},
        "type": "voltage",
    },
    {
        "device_id": 20,
        "name": "SC303 [5499] 2",
        "voltage": {"id": 2200, "value": 0.0, "unit": "volt"},
        "type": "voltage",
    },
    {
        "device_id": 21,
        "name": "SC303 [5499] 1",
        "resistance": {"id": 2300, "value": 0.0, "unit": "ohm"},
        "type": "resistive",
    },
    {
        "device_id": 22,
        "name": "SC303 [5499] 2",
        "resistance": {"id": 2400, "value": 0.0, "unit": "ohm"},
        "type": "resistive",
    },
    {
        "device_id": 23,
        "name": "SC303 [5499] 3",
        "resistance": {"id": 2500, "value": 0.0, "unit": "ohm"},
        "type": "resistive",
    },
    {
        "device_id": 24,
        "name": "Bulltron",
        "capacity": 300.0,
        "battery_type": "lifepo4",
        "charge": {"id": 2600, "value": 0.0, "unit": "percentage"},
        "remaining_capacity": {"id": 2601, "value": 0.0, "unit": "ampere_hour"},
        "current": {"id": 2602, "value": 0.0, "unit": "ampere"},
        "voltage": {"id": 2603, "value": 0.0, "unit": "volt"},
        "type": "battery",
    },
    {
        "device_id": 25,
        "name": "Batterie",
        "temperature": {"id": 3100, "value": 0.0, "unit": "celsius"},
        "type": "temperature",
    },
    {
        "device_id": 26,
        "name": "Frischwasser",
        "capacity": 100.0,
        "fluid_type": "fresh_water",
        "volume": {"id": 3200, "value": 0.0, "unit": "liter"},
        "level": {"id": 3201, "value": 0.0, "unit": "percentage"},
        "type": "tank",
    },
    {
        "device_id": 27,
        "name": "Starterbatterie",
        "capacity": 100.0,
        "battery_type": "agm",
        "charge": {"id": 3300, "value": 0.0, "unit": "percentage"},
        "remaining_capacity": {"id": 3301, "value": 0.0, "unit": "ampere_hour"},
        "current": {"id": 3302, "value": 0.0, "unit": "ampere"},
        "voltage": {"id": 3303, "value": 0.0, "unit": "volt"},
        "type": "battery",
    },
    {
        "device_id": 28,
        "name": "Abwasser",
        "capacity": 70.0,
        "fluid_type": "waste_water",
        "volume": {"id": 3800, "value": 0.0, "unit": "liter"},
        "level": {"id": 3801, "value": 0.0, "unit": "percentage"},
        "type": "tank",
    },
    {
        "device_id": 29,
        "name": "Innen",
        "temperature": {"id": 3900, "value": 0.0, "unit": "celsius"},
        "type": "temperature",
    },
    {
        "device_id": 30,
        "name": "Au�en ",
        "temperature": {"id": 4000, "value": 0.0, "unit": "celsius"},
        "type": "temperature",
    },
    {
        "device_id": 31,
        "name": "Boiler",
        "temperature": {"id": 4100, "value": 0.0, "unit": "celsius"},
        "type": "temperature",
    },
]


SENSOR_DATA = [
    BarometerSensor(sensor_id=300, value=979.83),
    VoltageSensor(sensor_id=500, value=13.26),
    VoltageSensor(sensor_id=1100, value=0.0),
    VoltageSensor(sensor_id=1200, value=0.035),
    VoltageSensor(sensor_id=1300, value=0.0),
    ResistiveSensor(sensor_id=1400, value=19121),
    ResistiveSensor(sensor_id=1500, value=20599),
    ResistiveSensor(sensor_id=1600, value=5479),
    ResistiveSensor(sensor_id=1700, value=-1),
    CurrentSensor(sensor_id=1900, value=-1.23),
    VoltageSensor(sensor_id=2100, value=13.314),
    VoltageSensor(sensor_id=2200, value=12.26),
    ResistiveSensor(sensor_id=2300, value=-1),
    ResistiveSensor(sensor_id=2400, value=-1),
    ResistiveSensor(sensor_id=2500, value=19651),
    ChargeSensor(sensor_id=2600, value=0.879),
    CapacitySensor(sensor_id=2601, value=263.7),
    CurrentSensor(sensor_id=2602, value=-1.23),
    VoltageSensor(sensor_id=2603, value=13.314),
    TemperatureSensor(sensor_id=3100, value=10.1),
    TankVolumeSensor(sensor_id=3200, value=0.0),
    TankLevelSensor(sensor_id=3201, value=0.0),
    ChargeSensor(sensor_id=3300, value=0.469),
    CapacitySensor(sensor_id=3301, value=79.6),
    CurrentSensor(sensor_id=3302, value=-0.01),
    VoltageSensor(sensor_id=3303, value=12.26),
    TankVolumeSensor(sensor_id=3800, value=3.7),
    TankLevelSensor(sensor_id=3801, value=0.052),
    TemperatureSensor(sensor_id=3900, value=10.7),
    TemperatureSensor(sensor_id=4000, value=9.1),
    TemperatureSensor(sensor_id=4100, value=39.4),
]

SENSOR_DATA2 = [
    BarometerSensor(sensor_id=300, value=985.92),
    VoltageSensor(sensor_id=500, value=13.023),
    VoltageSensor(sensor_id=1100, value=0.0),
    VoltageSensor(sensor_id=1200, value=0.037),
    VoltageSensor(sensor_id=1300, value=0.0),
    ResistiveSensor(sensor_id=1400, value=19189),
    ResistiveSensor(sensor_id=1500, value=18813),
    ResistiveSensor(sensor_id=1600, value=20743),
    ResistiveSensor(sensor_id=1700, value=-1),
    CurrentSensor(sensor_id=1900, value=2.14),
    VoltageSensor(sensor_id=2100, value=13.083),
    VoltageSensor(sensor_id=2200, value=12.791),
    ResistiveSensor(sensor_id=2300, value=-1),
    ResistiveSensor(sensor_id=2400, value=-1),
    ResistiveSensor(sensor_id=2500, value=19233),
    ChargeSensor(sensor_id=2600, value=0.453),
    CapacitySensor(sensor_id=2601, value=136.02),
    CurrentSensor(sensor_id=2602, value=2.17),
    VoltageSensor(sensor_id=2603, value=13.081),
    TemperatureSensor(sensor_id=3100, value=10.6),
    TankVolumeSensor(sensor_id=3200, value=0.0),
    TankLevelSensor(sensor_id=3201, value=0.0),
    ChargeSensor(sensor_id=3300, value=0.499),
    CapacitySensor(sensor_id=3301, value=86.3),
    CurrentSensor(sensor_id=3302, value=-0.01),
    VoltageSensor(sensor_id=3303, value=12.791),
    TankVolumeSensor(sensor_id=3800, value=3.8),
    TankLevelSensor(sensor_id=3801, value=0.054),
    TemperatureSensor(sensor_id=3900, value=10.6),
    TemperatureSensor(sensor_id=4000, value=11.0),
    TemperatureSensor(sensor_id=4100, value=9.0),
]
