import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def find_similar_incidents(query):

    df = pd.read_excel(
        "../data/Incidents.xlsx"
    )

    df["combined_text"] = (
        df["Short Description"].fillna("")
        + " "
        + df["Description"].fillna("")
    )

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    incident_embeddings = model.encode(
        df["combined_text"].tolist()
    )

    query_embedding = model.encode(
        [query]
    )

    scores = cosine_similarity(
        query_embedding,
        incident_embeddings
    )[0]

    top_indices = scores.argsort()[-5:][::-1]

    results = []

    for idx in top_indices:

        results.append({
            "Incident Number":
                df.iloc[idx]["Incident Number"],

            "Short Description":
                df.iloc[idx]["Short Description"],

            "Assignment Group":
                df.iloc[idx]["Assignment Group"],

            "Assigned To":
                df.iloc[idx]["Assigned To"],

            "Resolution":
                df.iloc[idx]["Close Notes"],

            "Work Notes":
                df.iloc[idx]["Work Notes"],

            "Similarity":
                float(round(scores[idx] * 100, 2))
        })

    return results