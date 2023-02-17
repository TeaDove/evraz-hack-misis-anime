db.createCollection("event")
db.event.createIndex({ "exhauster_id": 1 })
db.event.createIndex({ "exhauster_id": 1, "created_at": 1 }, { "unique": true })
db.event.find()
