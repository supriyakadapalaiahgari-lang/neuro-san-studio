# ServiceNow Incident Resolution Copilot

## Overview

ServiceNow Incident Resolution Copilot is an Agentic AI solution built using Neuro SAN concepts to assist IT support teams in resolving incidents faster.

The solution analyzes incoming incidents, searches historical incident records, identifies similar incidents using AI-powered semantic similarity, recommends assignment groups and resolvers, suggests proven resolutions, and generates ServiceNow-ready work notes.

---

## Features

- Historical Incident Search
- AI-Powered Similarity Matching
- Assignment Group Recommendation
- Resolver Recommendation
- Resolution Recommendation
- Automated Work Notes Generation
- ServiceNow-Inspired User Interface
- Agent Workflow Visualization

---

## Agent Workflow

Incident Analyzer Agent

↓

Historical Search Agent

↓

Similarity Agent

↓

Resolution Agent

↓

Work Notes Agent

---

## Setup Instructions

### Clone Repository

```bash
git clone <repository_url>
cd incident_resolution_copilot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run streamlit_app.py --server.address 0.0.0.0
```

---

## Future Enhancements

- Live ServiceNow REST API Integration
- Automated Ticket Routing
- Knowledge Base Recommendations
- Real-Time Incident Monitoring
- Automated Work Notes Updates