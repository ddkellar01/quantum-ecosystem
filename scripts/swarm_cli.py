import argparse
import requests
import json
import sys

BASE_URL = "http://localhost:8000"

def check_status():
    try:
        res = requests.get(f"{BASE_URL}/status")
        print(json.dumps(res.json(), indent=2))
    except Exception as e:
        print(f"❌ Error connecting to swarm API: {e}")

def trigger_cycle():
    try:
        res = requests.post(f"{BASE_URL}/trigger-cycle")
        print(json.dumps(res.json(), indent=2))
    except Exception as e:
        print(f"❌ Error triggering cycle: {e}")

def main():
    parser = argparse.ArgumentParser(description="Quantum Ecosystem Swarm CLI")
    parser.add_argument("command", choices=["status", "trigger"], help="Command to execute")
    args = parser.parse_args()

    if args.command == "status":
        check_status()
    elif args.command == "trigger":
        trigger_cycle()

if __name__ == "__main__":
    main()
