from coded_tools.incident_search_tool import search_incidents

results = search_incidents("VPN")

for item in results:
    print(item)
