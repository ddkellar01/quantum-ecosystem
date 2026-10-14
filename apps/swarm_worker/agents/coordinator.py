import time
import logging
from apps.swarm_worker.agents.scout import ScoutAgent
from apps.swarm_worker.agents.tester import TesterAgent
from apps.swarm_worker.agents.deployer import DeployerAgent
from apps.swarm_worker.agents.backup import BackupAgent

logging.basicConfig(level=logging.INFO, format="%(asctime)s [SWARM-CORE] %(message)s")

def start_swarm_orchestrator():
    scout = ScoutAgent()
    tester = TesterAgent()
    deployer = DeployerAgent()
    backup = BackupAgent()

    logging.info("🌟 Quantum Ecosystem Autonomous Swarm Worker Initialized.")

    while True:
        try:
            findings = scout.execute()
            if findings and tester.execute(findings):
                if deployer.deploy():
                    backup.execute()
        except Exception as e:
            logging.error(f"❌ Swarm cycle exception: {e}")

        logging.info("⏳ Swarm sleeping until next autonomous cycle (1 hour)...")
        time.sleep(3600)

if __name__ == "__main__":
    start_swarm_orchestrator()
