import pytest
import os
from apps.swarm_worker.agents.scout import ScoutAgent
from apps.swarm_worker.agents.tester import TesterAgent
from apps.swarm_worker.agents.deployer import DeployerAgent
from apps.swarm_worker.agents.backup import BackupAgent

def test_full_swarm_pipeline_execution():
    scout = ScoutAgent()
    tester = TesterAgent()
    deployer = DeployerAgent(min_balance=0.01)
    backup = BackupAgent()

    # 1. Scout step
    findings = scout.execute()
    assert findings is not None
    assert "new_features_found" in findings

    # 2. Test step
    test_result = tester.execute(findings)
    assert test_result is True

    # 3. Deploy step
    deploy_result = deployer.deploy()
    assert deploy_result is True

    # 4. Backup step
    backup_file = backup.execute()
    assert os.path.exists(backup_file)
