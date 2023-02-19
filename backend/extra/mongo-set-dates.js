
db.exhauster.updateOne({ "exhauster_id": 0 }, {
    '$set': {
        "last_replacement": "2023-02-09T12:00:00",
        "next_replacement_prediction": "2023-03-01T12:00:00",
    }
});
db.exhauster.updateOne({ "exhauster_id": 1 }, {
    '$set': {
        "last_replacement": "2023-01-19T12:00:00",
        "next_replacement_prediction": "2023-02-20T12:00:00",
    }
});
db.exhauster.updateOne({ "exhauster_id": 2 }, {
    '$set': {
        "last_replacement": "2023-02-02T12:00:00",
        "next_replacement_prediction": "2023-02-22T12:00:00",
    }
});
db.exhauster.updateOne({ "exhauster_id": 3 }, {
    '$set': {
        "last_replacement": "2023-02-13T12:00:00",
        "next_replacement_prediction": "2023-03-06T12:00:00",
    }
});
db.exhauster.updateOne({ "exhauster_id": 4 }, {
    '$set': {
        "last_replacement": "2023-01-25T12:00:00",
        "next_replacement_prediction": "2023-02-20T12:00:00",
    }
});
db.exhauster.updateOne({ "exhauster_id": 5 }, {
    '$set': {
        "last_replacement": "2023-02-06T12:00:00",
        "next_replacement_prediction": "2023-02-27T12:00:00",
    }
});
