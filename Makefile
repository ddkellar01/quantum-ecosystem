.PHONY: build run-swarm run-sandbox test clean

build:
	docker build -t credkellar/quantum-ecosystem:latest -f docker/Dockerfile .

run-swarm:
	docker-compose -f docker/docker-compose.yml up -d

run-sandbox:
	SERVICE_MODE=sandbox python -m apps.sandbox_api.main

test:
	pytest tests/

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf backups/*.tar.gz data/*.db
	echo "Environment cleaned."
