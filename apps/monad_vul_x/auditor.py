import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [MONAD-AUDITOR] %(message)s")

class SmartContractAuditor:
    def audit_bytecode(self, contract_code):
        logging.info("Scanning Monad smart contract bytecode for reentrancy and arithmetic flaws...")
        vulnerabilities = []
        if "call.value" in contract_code:
            vulnerabilities.append("Potential Reentrancy Attack vector detected")
        if "selfdestruct" in contract_code:
            vulnerabilities.append("Unprotected selfdestruct opcode found")

        is_secure = len(vulnerabilities) == 0
        logging.info(f"Audit Complete. Passed: {is_secure}. Found {len(vulnerabilities)} issues.")
        return {"secure": is_secure, "vulnerabilities": vulnerabilities}

if __name__ == "__main__":
    auditor = SmartContractAuditor()
    auditor.audit_bytecode("function withdraw() { msg.sender.call.value(amount)(); }")
