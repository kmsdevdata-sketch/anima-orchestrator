from fastapi import FastAPI

app = FastAPI(title="Anima Orchestrator")


@app.get("/api/v0/health")
def get_health() -> dict[str, str]:
    return {
        "protocol_version": "0.1",
        "mode": "mock",
        "status": "ok",
    }