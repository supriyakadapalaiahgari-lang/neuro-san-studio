# Architecture

## Problem Statement

Support engineers frequently spend significant time investigating incidents that have already occurred in the past.

Finding historical incidents, identifying appropriate support groups, determining the correct resolver, and documenting investigation notes are repetitive and time-consuming activities that increase Mean Time To Resolution (MTTR).

---

## Solution

ServiceNow Incident Resolution Copilot leverages Agentic AI principles to analyze new incidents and automatically recommend proven resolution approaches based on historical data.

The system uses semantic similarity matching to identify historical incidents with similar symptoms and recommend the most appropriate resolution path.

---

## Agentic Architecture

```text
Incoming Incident
        |
        v
Incident Analyzer Agent
        |
        v
Historical Search Agent
        |
        v
Similarity Agent
        |
        v
Resolution Agent
        |
        v
Work Notes Agent
        |
        v
ServiceNow Recommendation Layer
```

---

## Agent Responsibilities

### Incident Analyzer Agent

Responsibilities:

- Incident understanding
- Symptom extraction
- Query preparation

### Historical Search Agent

Responsibilities:

- Retrieve historical incidents
- Gather relevant incident information

### Similarity Agent

Responsibilities:

- Generate embeddings
- Calculate semantic similarity
- Identify top matching incidents

### Resolution Agent

Responsibilities:

- Recommend assignment group
- Recommend resolver
- Recommend resolution

### Work Notes Agent

Responsibilities:

- Generate investigation notes
- Produce ServiceNow-ready work notes

---

## AI Components

### Embedding Model

Sentence Transformers

Model:

```text
all-MiniLM-L6-v2
```

### Similarity Technique

```text
Cosine Similarity
```

### Historical Data Source

```text
Incident Repository (Excel Dataset)
```

---

## Output

The solution generates:

- Similar Historical Incidents
- Confidence Score
- Assignment Group Recommendation
- Resolver Recommendation
- Resolution Recommendation
- Automated Work Notes

---

## Future Architecture

```text
ServiceNow
     |
     v
Incident Resolution Copilot
     |
     v
Historical Incident Repository
     |
     v
Knowledge Base
     |
     v
Automatic Ticket Updates
```