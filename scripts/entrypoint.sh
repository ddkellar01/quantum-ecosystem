#!/bin/bash
set -e

echo "Starting Quantum Ecosystem Service [MODE=${SERVICE_MODE:-swarm}]..."

case "${SERVICE_MODE}" in
  trader)
    exec python -m apps.quantum_traderx.main
    ;;
  aquarius)
    exec python -m apps.aquarius.main
    ;;
  security)
    exec python -m apps.monad_vul_x.main
    ;;
  sandbox)
    exec python -m apps.sandbox_api.main
    ;;
  swarm|*)
    exec python -m apps.swarm_worker.coordinator
    ;;
esac
