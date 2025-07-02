# server.py

from mcp.server.fastmcp import FastMCP
from kubernetes import client, config
import os

mcp = FastMCP("my-kind-cluster")

if os.environ.get("KUBERNETES_SERVICE_HOST"):
    config.load_incluster_config()
else:
    config.load_kube_config()
core = client.CoreV1Api()

@mcp.tool()
def get_pods() -> str:
    """Return pod names"""
    return "pong"


@mcp.tool()
def cluster_name() -> str:
    """Return the current Kubernetes cluster name (server address)."""
    print("Getting Cluster name....")
    return client.Configuration().host

@mcp.tool()
def pod_count(namespace: str | None = None) -> int:
    """Return the number of pods in a given namespace (or all namespaces)."""
    print("Getting Pod Count.....")    
    if namespace:
        print("namespace is ",namespace)
        pods = core.list_namespaced_pod(namespace)
    else:
        print("Checking in all namespaces namespace")
        pods = core.list_pod_for_all_namespaces()
    return len(pods.items)

if __name__ == "__main__":
    print("Starting mcp server....",flush=True)
    mcp.run(transport="stdio")
    print("started mcp server",flush=True)

