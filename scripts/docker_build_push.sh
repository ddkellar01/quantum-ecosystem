#!/bin/bash
set -e

IMAGE_NAME="credkellar/quantum-ecosystem"
TAG="latest"

echo "🐳 Logging into Docker Hub..."
docker login

echo "🛠️ Creating Docker Buildx builder instance..."
docker buildx create --use --name quantum-builder 2>/dev/null || docker buildx use quantum-builder

echo "🚀 Building and pushing multi-arch image (${IMAGE_NAME}:${TAG})..."
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t ${IMAGE_NAME}:${TAG} \
  -f docker/Dockerfile \
  --push .

echo "✅ Docker image built and pushed successfully to Docker Hub!"
