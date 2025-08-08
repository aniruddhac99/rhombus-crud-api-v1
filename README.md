# 🚀 rhombus-crud-api-v1

> A minimal, secure, and fully portable CRUD API for **DevSecOps demos** — built with Flask, deployed via Docker & k3s (Multipass VM).  
> Features in-memory storage, Prometheus metrics, health probes, and a one-command CI/CD deployment script.

---

## 🧰 Tech Stack

- **Python Flask** – REST API
- **Prometheus Client** – Metrics endpoint
- **Docker** – Containerized app
- **Kubernetes (k3s)** – Lightweight k8s inside Multipass VM
- **Shell CI (ci.sh)** – Local build, deploy, and port-forward
- **No Database Required** – In-memory key-value store

---

## 📁 Folder Structure

```bash
crud-api-v2/
├── app.py                 # Flask app with CRUD logic
├── Dockerfile             # Python 3.10-slim image
├── requirements.txt       # Flask, Prometheus client
├── ci.sh                  # One-command CI/CD
├── k8s/
│   ├── deployment.yaml    # K8s Deployment manifest
│   └── service.yaml       # K8s Service manifest
└── README.md              # You're here!
└── service.yaml

```




 ## 🚀 Setup Instructions (Inside Ubuntu Multipass VM)  ### Step 1: Shell into your devvm  ```bash  multipass  shell  devvm` 

### Step 2: Build and deploy



`cd ~/quicknote-api
./ci.sh` 

This script will:

-   Build the Docker image
    
-   Apply K8s deployment and service YAMLs
    
-   Port-forward service from `localhost:8081` → app port `5000`
    

> ⚠️ If port 8081 is taken, edit `ci.sh` to use another available port.

----------

## 🔐 Authentication

All `POST`, `PUT`, and `DELETE` requests require a header:

`X-Key: demo123` 

----------

## 🧪 Example `curl` Commands

### Create a note

`curl -X POST -H "X-Key: demo123" -H "Content-Type: application/json" \
-d '{"note_id":"n1", "text":"Initial note"}' \
http://localhost:8081/notes` 

### Get all notes

`curl http://localhost:8081/notes` 

### Get a single note

`curl http://localhost:8081/notes/n1` 

### Update a note

`curl -X PUT -H "X-Key: demo123" -H "Content-Type: application/json" \
-d '{"text":"Updated content"}' \
http://localhost:8081/notes/n1` 

### Delete a note

`curl -X DELETE -H "X-Key: demo123" http://localhost:8081/notes/n1` 

----------

## 📈 Observability Endpoints

-   Health Check:  
    `GET /health` → `{ "status": "ok" }`
    
-   Prometheus Metrics:  
    `GET /metrics` → exposes `http_requests_total` counter
    

----------

## 🧠 Adaptability

You can quickly change this project into:

Use Case

Rename Route to

Note Fields will be:

Secrets Manager:

`/secrets`

`secret_id`, `value`

Task/Assignment Tracker:

`/tasks`

`task_id`, `description`

Config Store:

`/configs`

`config_key`, `config_val`

Policy Store:

`/policies`

`policy_id`, `yaml_blob`

----------

## 🧼 Cleanup

To delete the app:

`kubectl delete deployment crud-api
kubectl delete svc crud-api` 

----------

## ⚠️ Issues Faced: 

- Docker Runtime had to be re-started, re-initialized /env/ values

- default kubectl config view: Initially set to null, used $PATH / config values. 

- Git RPC Failure HTTPS 400 Status Code:  fixed by raising the postBuffer size by: git config --global http.postBuffer 524288000.

- port-forwarding 8080: Find the process ID (PID): sudo lsof -i :portNumber.
Kill the process: kill PID.

(Note): NodePort is a more permanent solution compared to port-forward, especially in a containerized context.

## 🧷 Notes

-   This is stateless. Data is stored in RAM and lost on container restart.
    
-   For persistence, you can integrate Redis or SQLite.
    
-   Designed for secure offline demos without cloud dependencies.
    

----------

## 🔒 Auth, Infra, Observability — All in One

✅ Secure headers  
✅ K8s Secrets-ready  
✅ Prometheus metrics  
✅ Health endpoint  
✅ No DB dependency  
✅ <3-minute deploy from scratch

