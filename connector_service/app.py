from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from connector_manager import ConnectorManager

app = FastAPI()

class SyncRequest(BaseModel):
    enterprise_id: str
    saas_application: str
    table: str
    sync_type: str  # Can be 'realtime' or 'on_demand'

connector_manager = ConnectorManager()

@app.post("/api/v1/sync")
async def initiate_sync(request: SyncRequest):
    try:
        if request.sync_type == "realtime":
            task_id = connector_manager.start_realtime_sync(request.enterprise_id, request.saas_application, request.table)
        else:
            task_id = connector_manager.start_on_demand_sync(request.enterprise_id, request.saas_application, request.table)

        return {"status": "success", "task_id": task_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
