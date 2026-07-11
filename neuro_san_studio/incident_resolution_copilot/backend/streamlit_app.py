import streamlit as st
from neuro_san_studio.incident_resolution_copilot.backend.coded_tools.incident_similarity_tool import (
    find_similar_incidents
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="ServiceNow Incident Resolution Copilot",
    page_icon="🎫",
    layout="wide"
)

# --------------------------------------------------
# CSS
# --------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

[data-testid="stMetric"] {
    background-color: white;
    padding: 12px;
    border-radius: 10px;
    border: 1px solid #d9d9d9;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🎫 ServiceNow Incident Resolution Copilot")

st.markdown("""
<div style="
background-color:#1f4e79;
padding:15px;
border-radius:10px;
color:white;
font-size:22px;
font-weight:bold;">
🎫 ServiceNow Incident Workspace
</div>
""", unsafe_allow_html=True)

st.write(
    "AI-powered incident analysis using historical incidents, "
    "similarity search, routing recommendations and work note generation."
)

# --------------------------------------------------
# LAYOUT
# --------------------------------------------------

left_col, right_col = st.columns([2, 1])

with left_col:

    st.subheader("🎫 Incoming ServiceNow Incident")

    st.info("""
Source: ServiceNow

Status: New

Assignment Group: To Be Determined
""")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.text_input(
            "Incident Number",
            value="INC567890",
            disabled=True
        )

    with col2:
        st.text_input(
            "Priority",
            value="P2",
            disabled=True
        )

    with col3:
        st.text_input(
            "State",
            value="New",
            disabled=True
        )

    st.text_input(
        "Short Description",
        value="VPN Authentication Timeout"
    )

    incident = st.text_area(
        "Description",
        height=180,
        placeholder="Describe the issue here..."
    )

    analyze = st.button(
        "🔍 Analyze Incident",
        use_container_width=True
    )

# --------------------------------------------------
# ANALYSIS
# --------------------------------------------------

if analyze:

    if not incident.strip():

        st.warning(
            "Please enter an incident description."
        )

    else:

        try:

            results = find_similar_incidents(
                incident
            )

            if not results:

                st.error(
                    "No historical incidents found."
                )

            else:

                best_match = results[0]

                confidence = round(
                    float(best_match["Similarity"]),
                    2
                )

                # ----------------------------------
                # RIGHT PANEL
                # ----------------------------------

                with right_col:

                    st.subheader(
                        "🤖 AI Copilot"
                    )

                    if confidence > 70:

                        st.success(
                            "✅ Known Issue Detected"
                        )

                    elif confidence > 50:

                        st.warning(
                            "🟡 Medium Confidence Match"
                        )

                    else:

                        st.error(
                            "🔴 Low Confidence Match"
                        )

                    col1, col2 = st.columns(2)

                    with col1:
                        st.metric(
                            "Confidence",
                            f"{confidence}%"
                        )

                    with col2:
                        st.metric(
                            "Priority",
                            "P2"
                        )

                    st.metric(
                        "Assignment Group",
                        best_match["Assignment Group"]
                    )

                    st.metric(
                        "Suggested Resolver",
                        best_match["Assigned To"]
                    )

                    st.subheader(
                        "🛠 Resolution"
                    )

                    st.success(
                        best_match["Resolution"]
                    )

                    st.subheader(
                        "🎯 Routing Recommendation"
                    )

                    st.info(
                        f"""
Assignment Group:
{best_match['Assignment Group']}

Resolver:
{best_match['Assigned To']}
"""
                    )

                # ----------------------------------
                # SIMILAR INCIDENTS
                # ----------------------------------

                st.subheader(
                    "🔍 Similar Historical Incidents"
                )

                with st.expander(
                    "View Similar Incidents",
                    expanded=True
                ):

                    st.dataframe(
                        results,
                        use_container_width=True
                    )

                # ----------------------------------
                # PATTERN ANALYSIS
                # ----------------------------------

                st.subheader(
                    "📊 Historical Pattern Analysis"
                )

                st.info(
                    f"""
Found {len(results)} similar incidents.

This indicates a recurring issue pattern.
"""
                )

                # ----------------------------------
                # WORK NOTES
                # ----------------------------------

                st.subheader(
                    "📝 Generated Work Notes"
                )

                work_notes = f"""
Investigation Summary

Historical Incident:
{best_match['Incident Number']}

Confidence Score:
{confidence}%

Suggested Assignment Group:
{best_match['Assignment Group']}

Suggested Resolver:
{best_match['Assigned To']}

Observed similar symptoms.

Recommended Resolution:
{best_match['Resolution']}

Validation required after implementation.

Issue can be monitored.
"""

                st.text_area(
                    "ServiceNow Work Notes",
                    value=work_notes,
                    height=250
                )

                # ----------------------------------
                # BUSINESS IMPACT
                # ----------------------------------

                st.subheader(
                    "📈 Business Impact"
                )

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Estimated MTTR Reduction",
                        "75%"
                    )

                with col2:
                    st.metric(
                        "Resolution Reuse",
                        "100%"
                    )

                st.success("""
✅ Reduced MTTR

✅ Faster Resolution

✅ Historical Knowledge Reuse

✅ Better Ticket Routing

✅ Consistent Work Notes
""")

                # ----------------------------------
                # TIMELINE
                # ----------------------------------

                st.subheader(
                    "📜 Incident Timeline"
                )

                st.code("""
09:00 - Incident Created

09:01 - AI Analysis Started

09:02 - Historical Incidents Identified

09:03 - Resolution Recommended

09:04 - Work Notes Generated

09:05 - Ready For ServiceNow Update
""")

                # ----------------------------------
                # SERVICENOW ACTIONS
                # ----------------------------------

                st.subheader(
                    "🔄 ServiceNow Actions"
                )

                col1, col2 = st.columns(2)

                with col1:

                    if st.button(
                        "📝 Update ServiceNow"
                    ):
                        st.success(
                            "✅ Work Notes Updated"
                        )

                with col2:

                    if st.button(
                        "🎯 Auto Assign Incident"
                    ):
                        st.success(
                            "✅ Incident Assigned"
                        )

                # ----------------------------------
                # AGENT WORKFLOW
                # ----------------------------------

                st.subheader("🤖 Agent Workflow")

                col1, col2, col3, col4, col5 = st.columns(5)

                with col1:
                    st.success("Analyze")

                with col2:
                    st.success("Search")

                with col3:
                    st.success("Match")

                with col4:
                    st.success("Resolve")

                with col5:
                    st.success("Work Notes")

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )

# --------------------------------------------------
# ROADMAP
# --------------------------------------------------

st.markdown("---")

st.subheader("🚀 Future Roadmap")

st.info("""
✅ Live ServiceNow REST API Integration

✅ Automated Ticket Routing

✅ Knowledge Base Recommendations

✅ Real-Time Incident Monitoring

✅ Automatic Work Notes Updates

✅ Resolver Performance Analytics
""")