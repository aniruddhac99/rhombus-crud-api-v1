#!/bin/bash
docker build -t crud-api .
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl port-forward svc/crud-api 8081:80


