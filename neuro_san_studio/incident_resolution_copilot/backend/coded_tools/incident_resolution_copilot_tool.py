from neuro_san_studio.incident_resolution_copilot.backend.coded_tools.incident_similarity_tool import (
    find_similar_incidents
)

def resolve_incident(query):

    matches = find_similar_incidents(query)

    best_match = matches[0]

    confidence = best_match["Similarity"]

    response = f"""
✅ Known Issue Detected

Confidence:
{confidence}%

Historical Incident:
{best_match['Incident Number']}

Suggested Assignment Group:
{best_match['Assignment Group']}

Suggested Resolver:
{best_match['Assigned To']}

Recommended Resolution:
{best_match['Resolution']}

Suggested Work Notes:

Investigated reported issue.

Reviewed historical incident
{best_match['Incident Number']}.

Observed similar symptoms.

Applied known resolution approach.

Validated successful service restoration.

Issue resolved.
"""

    return response