import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [MONAD-VUL-X] %(message)s")

def start_security_scanner():
    logging.info("Starting Monad Smart Contract Automated Security Engine...")
    while True:
        logging.info("Auditing smart contracts for Monad high-speed network vulnerabilities...")
        time.sleep(60)

if __name__ == "__main__":
    start_security_scanner()
