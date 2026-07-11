from coded_tools.incident_similarity_tool import (
    find_similar_incidents
)

results = find_similar_incidents(
    """
    Users unable to connect remotely.
    Authentication timeout observed.
    """
)

for item in results:
    print(item)