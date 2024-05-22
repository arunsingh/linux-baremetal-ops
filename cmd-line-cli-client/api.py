from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ServerProvisionRequest(BaseModel):
    hostname: str
    os: str
    specs: dict

class NetworkDeviceProvisionRequest(BaseModel):
    device_type: str
    ip_address: str
    configuration: dict

@app.post("/provision/server")
async def provision_server(request: ServerProvisionRequest):
    # Simulate provisioning logic
    print(f"Provisioning server: {request.hostname} with OS: {request.os} and specs: {request.specs}")
    return {"status": "success", "message": f"Server {request.hostname} provisioned successfully."}

@app.post("/provision/network_device")
async def provision_network_device(request: NetworkDeviceProvisionRequest):
    # Simulate provisioning logic
    print(f"Provisioning network device: {request.device_type} at {request.ip_address}")
    return {"status": "success", "message": f"Network device at {request.ip_address} provisioned successfully."}
