import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [SANDBOX-EVAL] %(message)s")

class ThreatEvaluator:
    def analyze_telemetry(self, telemetry_data):
        logging.info("Analyzing process execution traces, API calls, and network diffs...")
        risk_score = 0
        if telemetry_data.get("suspicious_api_calls", 0) > 3:
            risk_score += 40
        if telemetry_data.get("unauthorized_network_outbound", False):
            risk_score += 50

        threat_level = "HIGH" if risk_score >= 70 else "MEDIUM" if risk_score >= 30 else "LOW"
        logging.info(f"Evaluation finished. Threat Score: {risk_score}/100 [{threat_level}]")
        return {"threat_score": risk_score, "level": threat_level}

if __name__ == "__main__":
    evaluator = ThreatEvaluator()
    evaluator.analyze_telemetry({"suspicious_api_calls": 5, "unauthorized_network_outbound": True})
