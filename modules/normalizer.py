# The json data is inconsitent with the multiple inner dicts so need to make them in simple items 
def normalize_data(data):
    warehouses = data.get("warehouses", {})
    agents = data.get("agents", {})
    packages = data.get("packages", [])
    new_agents = data.get("new_agents", [])

    # Normalize warehouses
    if isinstance(warehouses, dict):
        warehouses = [
            {"id": wid, "location": loc}
            for wid, loc in warehouses.items()
        ]

    # Normalize agents
    if isinstance(agents, dict):
        agents = [
            {"id": aid, "location": loc}
            for aid, loc in agents.items()
        ]

    # Normalize packages
    normalized_packages = []
    for pkg in packages:
        normalized_packages.append({
            "id": pkg.get("id"),
            "warehouse_id": pkg.get(
                "warehouse_id",
                pkg.get("warehouse")
            ),
            "destination": pkg.get("destination")
        })

    # Normalize new agents that will join after package
    normalized_new_agents = []
    for agent in new_agents:
        
        # for the agent we've added the agent joined after some packages and generates the specific point
        normalized_new_agents.append({
            "id": agent["id"],
            "location": agent["location"],
            "join_after_package": agent["join_after_package"]
        })

    return warehouses,agents,normalized_packages,normalized_new_agents
