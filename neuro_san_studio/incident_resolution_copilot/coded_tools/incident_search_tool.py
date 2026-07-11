import pandas as pd


def search_incidents(query):

    df = pd.read_excel(
        "data/Incidents.xlsx"
    )

    results = df[
        df["Description"].str.contains(
            query,
            case=False,
            na=False
        )
    ]

    if results.empty:
        return [{
            "message": "No matching incidents found"
        }]

    return results[
        [
            "Incident Number",
            "Short Description",
            "Assignment Group",
            "Assigned To",
            "Close Notes",
            "Work Notes"
        ]
    ].head(5).to_dict(
        orient="records"
    )