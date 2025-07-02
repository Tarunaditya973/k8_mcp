# 🧠 Basic Kubernetes MCP Server

This is a lightweight MCP (Model Control Protocol) Server that interacts with your local Kubernetes cluster.  
It doesn't run *inside* the cluster — instead, it runs locally and uses your kubeconfig to communicate with the cluster.

###UPDATE: Will try to run the MCP Server inside the K8's cluster itself

---

## 🚀 Features

- Runs locally and communicates with Kubernetes API
- Uses your current `kubeconfig` context
- Great for experimenting with Kubernetes API interactions
- Easy to extend for custom commands and metrics

---

## 📦 Tech Stack

- Python 3.x
- FastAPI (for REST API)
- `kubernetes` Python client (for interacting with K8s)
- Uvicorn (for running the server)

---

## 🛠️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/k8s-mcp-server.git
   cd k8s-mcp-server
