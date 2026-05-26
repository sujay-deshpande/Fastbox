import matplotlib.pyplot as plt

# plotting the outputs over the matplotlib to identify the agent
def plot_simulation(warehouses,active_agents,agent_report):

    plt.figure(figsize=(14, 10))

    colors = ["blue", "green", "red", "orange", "purple"]

    agent_color_map = {}
    for index, agent in enumerate(active_agents):
        agent_color_map[agent["id"]] = colors[index % len(colors)]


    for warehouse in warehouses:
        warehouse_id = warehouse["id"]
        x, y = warehouse["location"]
        
        plt.scatter(
            x, y,
            marker="s",
            s=350,
            color="black",
            edgecolors="white",
            linewidths=2,
            zorder=5
        )
        
        plt.annotate(
            warehouse_id,
            (x, y),
            textcoords="offset points",
            xytext=(10, 10),
            fontsize=11,
            fontweight="bold",
            color="black"
        )

    for agent in active_agents:
        agent_id = agent["id"]
        x, y = agent["location"]
        color = agent_color_map[agent_id]
        
        plt.scatter(
            x, y,
            marker="o",
            s=250,
            color=color,
            edgecolors="black",
            linewidths=1.5,
            zorder=5
        )
        
        plt.annotate(
            agent_id,
            (x, y),
            textcoords="offset points",
            xytext=(10, -15),
            fontsize=10,
            fontweight="bold",
            color=color
        )

    for agent in active_agents:
        agent_id = agent["id"]
        info = agent_report[agent_id]
        color = agent_color_map[agent_id]
        
        current_position = agent["location"]
        
        for package in info["assigned_packages"]:
            warehouse_id = package["warehouse_id"]
            
            warehouse_location = next(
                (w["location"] for w in warehouses if w["id"] == warehouse_id),
                None
            )
            
            if warehouse_location is None:
                continue
            
            destination = package["destination"]
            
            plt.plot(
                [current_position[0], warehouse_location[0]],
                [current_position[1], warehouse_location[1]],
                linestyle="--",
                linewidth=2,
                color=color,
                alpha=0.8
            )
            
            plt.plot(
                [warehouse_location[0], destination[0]],
                [warehouse_location[1], destination[1]],
                linestyle="-",
                linewidth=2.5,
                color=color
            )
            
            plt.scatter(
                destination[0],
                destination[1],
                marker="X",
                s=180,
                color=color,
                edgecolors="black",
                linewidths=1.5,
                zorder=6
            )
            
            plt.annotate(
                package["id"],
                (destination[0], destination[1]),
                textcoords="offset points",
                xytext=(8, 8),
                fontsize=9,
                fontweight="bold",
                color=color
            )
            
            current_position = destination



    plt.title(
        "FastBox Delivery Simulation by Sujay Deshpande",
        fontsize=18,
        fontweight="bold",
        pad=20
    )

    plt.xlabel(
        "X Coordinate",
        fontsize=13,
        fontweight="bold"
    )

    plt.ylabel(
        "Y Coordinate",
        fontsize=13,
        fontweight="bold"
    )

    plt.axis("equal")

    plt.grid(linestyle="--", alpha=0.5)
    plt.suptitle("github.com/sujay-deshpande",)

    from matplotlib.lines import Line2D

    legend_elements = [
        Line2D([0], [0], marker='s', color='w', label='Warehouse',
            markerfacecolor='black', markersize=12),
        Line2D([0], [0], marker='o', color='w', label='Agent',
            markerfacecolor='gray', markersize=12),
        Line2D([0], [0], marker='X', color='w', label='Package Destination',
            markerfacecolor='gray', markersize=12)
    ]

    plt.legend(handles=legend_elements, loc="upper right", fontsize=10)

    plt.tight_layout()

    plt.savefig("delivery_simulation.png", dpi=300, bbox_inches="tight")

    plt.show()