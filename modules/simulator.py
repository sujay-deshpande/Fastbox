from modules.distance import calculate_distance


def run_delivery_simulation( warehouses,agents,packages,new_agents):
    agent_report = {} # initialize the agent report

    for agent in agents:# define the agent report with the id's specified

        agent_id = agent["id"]

        agent_report[agent["id"]] = {
            "packages_delivered": 0,
            "total_distance": 0.0,
            "efficiency": 0.0,
            "assigned_packages": []
        }

    agent_index = 0

    active_agents = agents.copy() # deep copy with the future joining agents

    new_agents = sorted( new_agents,key=lambda x: x["join_after_package"] )
    # sorting the agents with lambda function mappging who joins after the pacakge
    join_pointer = 0

    for idx, package in enumerate(packages):

        while (join_pointer < len(new_agents) and new_agents[join_pointer]["join_after_package"] == idx):

            joining_agent = new_agents[join_pointer]

            active_agents.append(joining_agent)

            agent_report[joining_agent["id"]] = {
                "packages_delivered": 0,
                "total_distance": 0.0,
                "efficiency": 0.0,
                "assigned_packages": []
            }

            join_pointer += 1

        warehouse_id = package["warehouse_id"]

        warehouse_location = next((w["location"] for w in warehouses if w["id"] == warehouse_id),None)

        if warehouse_location is None:
            continue

        nearest_agent = min(
            active_agents, key=lambda agent: calculate_distance( agent["location"],warehouse_location)
        ) # calculating the actuall near one agent and septting ti for Tie-breaking Rule
        # if 2 agents are getting selected 

        agent_id = nearest_agent["id"]

        agent_report[agent_id]["assigned_packages"].append(package)

        agent_index += 1

    for agent_id in agent_report:

        info = agent_report[agent_id]

        # calculating the current position with specific given id as they are inner and ids are not as keys
        current_position = next((agent["location"] for agent in active_agents if agent["id"] == agent_id),[0, 0] )

        for package in info["assigned_packages"]:

            warehouse_id = package["warehouse_id"]

            warehouse_location = next(
                (w["location"] for w in warehouses if w["id"] == warehouse_id),
                None
            )

            if warehouse_location is None:
                continue

            destination = package["destination"] # The distance is from agent -> warehouse-> dest

            dist_to_warehouse = calculate_distance(current_position, warehouse_location)
            dist_to_destination = calculate_distance(warehouse_location, destination)
            total_trip_distance = dist_to_warehouse + dist_to_destination

            info["total_distance"] += total_trip_distance

            info["packages_delivered"] += 1

            current_position = destination

        if info["packages_delivered"] > 0:
            info["efficiency"] = info["total_distance"] / info["packages_delivered"]

    best_agent = None
    best_efficiency = float("inf")

    for agent_id, info in agent_report.items():
        if info["packages_delivered"] > 0 and info["efficiency"] < best_efficiency:
            best_efficiency = info["efficiency"]
            best_agent = agent_id

    return ( agent_report, active_agents, best_agent)