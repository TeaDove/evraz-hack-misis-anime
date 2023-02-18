db = connect('mongodb://localhost/films');

db.createCollection("event")
db.event.createIndex({ "exhauster_id": 1 })
db.event.createIndex({ "exhauster_id": 1, "created_at": 1 }, { "unique": true })

db.createCollection("exhauster")
db.exhauster.createIndex({ "exhauster_id": 1 }, { "unique": true })
