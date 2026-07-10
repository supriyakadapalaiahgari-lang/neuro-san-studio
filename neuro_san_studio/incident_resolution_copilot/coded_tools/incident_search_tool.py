import pandas as pd


def search_incidents(query):

    df = pd.read_excel(
        "incident_resolution_copilot/data/Incidents.xlsx"
    )

    matches = df[
        df["Description"].str.contains(
            query,
            case=False,
            na=False
        )
    ]

    return matches.head(5).to_dict(
        orient="records"
    )