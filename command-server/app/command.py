from fastapi import APIRouter, Depends
from mq_connection import get_active_mq_connection
from stomp import Connection
import json

router = APIRouter()


@router.get("/beacon")
async def beacon_command(
    destination: int,
    sampleRate: int,
    recordLength: int,
    sleepTime: int,
    connection: Connection = Depends(get_active_mq_connection)
):
    message = {
        "statusCode": destination,
        "samplerate": sampleRate,
        "recordLength": recordLength,
        "sleepTime": sleepTime
    }

    connection.send(body=json.dumps(message),
                    destination=f'/topic//command/beacon/{destination}')
    return "message sended."


@router.get("/client")
async def client(
    destination: int,
    sampleRate: int,
    recordLength: int,
    sleepTime: int,
    connection: Connection = Depends(get_active_mq_connection)
):
    message = {
        "statusCode": destination,
        "samplerate": sampleRate,
        "recordLength": recordLength,
        "sleepTime": sleepTime
    }

    connection.send(body=json.dumps(message),
                    destination=f'/topic//command/client/{destination}')
    return "message sended."
