import motor.motor_asyncio as motor
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase as Database

client = motor.AsyncIOMotorClient("mongodb://root:password@mongo:27017")

async def connect_to_db(dbName: str) -> Database:
    return client[dbName]


async def test():
    db = await connect_to_db("messaging_app")
    test_collection = db.users
    result = await test_collection.find_one({"e_mail": "porcari.karim1@gmail.com"})
    id = str(result["_id"])
    print(id)


async def clear_collection(collection_name: str) -> None:

    db = await connect_to_db("messaging_app")

    test_collection = db[collection_name]
    result = await test_collection.delete_many({})
    print(result)

if __name__ == "__main__":
    import asyncio
    asyncio.run(clear_collection("users"))
