import pytest
from apps.swarm_worker.agents.deployer import DeployerAgent
from apps.monad_vul_x.auditor import SmartContractAuditor

def test_deployer_balance_guard():
    deployer = DeployerAgent(min_balance=0.10)
    # Mocking check behavior
    assert deployer.min_balance == 0.10

def test_smart_contract_auditor_clean():
    auditor = SmartContractAuditor()
    result = auditor.audit_bytecode("function secureAdd(uint a, uint b) { return a + b; }")
    assert result["secure"] is True
    assert len(result["vulnerabilities"]) == 0
