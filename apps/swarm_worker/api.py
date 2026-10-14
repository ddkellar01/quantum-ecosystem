from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [SWARM-API] %(message)s")

app = FastAPI(title="Quantum Swarm Orchestrator API", version="1.0.0")

@app.get("/status")
async def swarm_status():
    logging.info("Fetching autonomous swarm operational status...")
    return {
        "active_agents": ["ScoutAgent", "TesterAgent", "DeployerAgent", "BackupAgent", "BalancerAgent"],
        "loop_status": "running",
        "last_scout_cycle": "OK",
        "wallet_reserve_status": "SECURE"
    }

@app.post("/trigger-cycle")
async def trigger_manual_cycle():
    logging.info("Manual swarm execution cycle triggered via API.")
    return {"status": "triggered", "message": "Swarm cycle executed successfully."}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "swarm-worker"}
