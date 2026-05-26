
# Assignment: Python Developer – Assignment Round
# Mystery Delivery System

import json
import sys

from modules.normalizer import normalize_data
from modules.simulator import run_delivery_simulation
from modules.export import export_reports
from modules.visualize import plot_simulation
from modules.distance import calculate_distance


def main():

    test_file = "data.json"
    # either pass by the arguments
    if len(sys.argv) > 1:
        test_file = sys.argv[1]

    with open( test_file, "r") as file:
        data = json.load(file)
    # Modular normalization
    warehouses, agents, packages, new_agents = normalize_data(data)
    agent_report,active_agents, best_agent = run_delivery_simulation(warehouses, agents, packages, new_agents)

    df, report = export_reports( agent_report, active_agents,  best_agent)

    # non ui-cmd line outputs
    print("\n==== DELIVERY REPORT =====\n")
    print(df.to_string(index=False))
    print( f"\nBest Agent: {best_agent}")
    
    # visualization using matplotlib
    plot_simulation( warehouses, active_agents, agent_report)


if __name__ == "__main__":
    main()