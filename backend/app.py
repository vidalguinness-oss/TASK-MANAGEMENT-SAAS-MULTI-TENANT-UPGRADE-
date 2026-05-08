from flask import Flask, request, jsonify

app = Flask(__name__)
tenants = {}

@app.route("/tasks", methods=["POST"])
def create_task():
    tenant_id = request.headers.get("X-Tenant-ID")

    if tenant_id not in tenants:
        tenants[tenant_id] = []

    task = request.json
    tenants[tenant_id].append(task)

    return jsonify(task)
