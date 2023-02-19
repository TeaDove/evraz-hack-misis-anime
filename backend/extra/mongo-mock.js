db.exhauster.updateOne({
    "exhauster_id": 4
}, {
    '$set': {
        "status.oil.oil_pressure": 0.2,
        "status.bearing_1.temperature.value": 80,
        "status.bearing_1.temperature.status": "ALARM",
        "status.bearing_3.temperature.value": 70,
        "status.bearing_3.temperature.status": "WARNING"
    }
});
db.exhauster.find()
