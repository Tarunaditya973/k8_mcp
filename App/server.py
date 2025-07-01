# server.py

from mcp.server.fastmcp import FastMCP
from kubernetes import client, config

mcp = FastMCP("my-kind-cluster")
config.load_kube_config()  # Uses ~/.kube/config
core = client.CoreV1Api()

@mcp.tool()
def cluster_name() -> str:
    """Return the current Kubernetes cluster name (server address)."""
    return client.Configuration().host

@mcp.tool()
def pod_count(namespace: str | None = None) -> int:
    """Return the number of pods in a given namespace (or all namespaces)."""
    if namespace:
        pods = core.list_namespaced_pod(namespace)
    else:
        pods = core.list_pod_for_all_namespaces()
    return len(pods.items)

if __name__ == "__main__":
    mcp.run(transport="tcp", port=4242)  # Or use transport="tcp" or "websocket"
