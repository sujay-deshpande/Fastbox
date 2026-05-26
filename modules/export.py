import json
import pandas as pd


def export_reports( agent_report,active_agents,best_agent):

    final_report = {}

    for agent_id, info in agent_report.items():

        final_report[agent_id] = {
            "packages_delivered": info["packages_delivered"],

            "total_distance": round( info["total_distance"], 2),

            "efficiency":round( info["efficiency"],2)
        }

    final_report["best_agent"] = best_agent

    with open("report.json","w") as file:
        json.dump(final_report,file,indent=4)

    report_rows = []

    for agent in active_agents:

        aid = agent["id"]

        if aid in final_report:

            report_rows.append({
                "Agent": aid,
                "Packages Delivered": final_report[aid]["packages_delivered"],
                "Total Distance":final_report[aid]["total_distance"],
                "Efficiency":final_report[aid]["efficiency"]
            })

    df = pd.DataFrame(report_rows)

    df.to_csv("report.csv",index=False)

    return df, final_report