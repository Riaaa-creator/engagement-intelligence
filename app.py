
from pathlib import Path
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Engagement Intelligence", page_icon="📊", layout="wide")
st.title("Engagement Intelligence")
st.caption("Behavioral Pattern Discovery and Comparative Analytics")

DATA_PATH = Path("outputs/clustered_posts.csv")
COMPARISON_PATH = Path("outputs/model_comparison.csv")
PROFILE_PATH = Path("outputs/cluster_profiles.csv")

if not DATA_PATH.exists():
    st.error("Missing outputs/clustered_posts.csv. Run the notebook export section first.")
    st.stop()

data = pd.read_csv(DATA_PATH)
comparison = pd.read_csv(COMPARISON_PATH) if COMPARISON_PATH.exists() else pd.DataFrame()

with st.sidebar:
    st.header("Explore")
    post_types = sorted(data["status_type"].dropna().unique().tolist())
    selected_types = st.multiselect("Post type", post_types, default=post_types)
    clusters = sorted(data["cluster"].dropna().unique().tolist())
    selected_clusters = st.multiselect("Cluster", clusters, default=clusters)
    metric_options = [c for c in ["num_reactions", "num_comments", "num_shares"] if c in data.columns]
    metric = st.selectbox("Engagement metric", metric_options, index=0)

filtered = data[
    data["status_type"].isin(selected_types) &
    data["cluster"].isin(selected_clusters)
].copy()

c1, c2, c3 = st.columns(3)
c1.metric("Posts in selection", f"{len(filtered):,}")
c2.metric("Median " + metric.replace("num_", "").replace("_", " "), f"{filtered[metric].median():,.1f}" if len(filtered) else "—")
c3.metric("Post types", f"{filtered['status_type'].nunique()}" if len(filtered) else "0")

tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Engagement", "Cluster profiles", "Model comparison"])

with tab1:
    st.subheader("Dataset overview")
    st.write("The charts describe the selected records; they do not establish causal relationships.")
    left, right = st.columns(2)
    with left:
        counts = filtered["status_type"].value_counts().rename_axis("Post type").reset_index(name="Posts")
        st.bar_chart(counts.set_index("Post type"))
    with right:
        st.bar_chart(filtered["cluster"].value_counts().sort_index().rename("Posts"))
    st.dataframe(filtered.head(100), use_container_width=True)

with tab2:
    st.subheader("Engagement distribution")
    if len(filtered):
        fig, ax = plt.subplots(figsize=(9, 4))
        sns.histplot(filtered[metric].dropna(), bins=40, ax=ax)
        ax.set_title(f"Distribution of {metric}")
        st.pyplot(fig)
        st.subheader("Engagement by post type")
        summary = filtered.groupby("status_type")[metric].agg(["mean", "median", "count"]).round(2)
        st.dataframe(summary, use_container_width=True)
        st.bar_chart(summary[["mean", "median"]])
    else:
        st.info("No rows match the selected filters.")

with tab3:
    st.subheader("Cluster profiles")
    if len(filtered):
        metrics = [c for c in ["num_reactions", "num_comments", "num_shares", "num_likes", "num_loves"] if c in filtered.columns]
        profiles = filtered.groupby("cluster")[metrics].median().round(2)
        st.write("Median engagement values by cluster, after applying sidebar filters.")
        st.dataframe(profiles, use_container_width=True)
        st.bar_chart(profiles)
        mix = pd.crosstab(filtered["cluster"], filtered["status_type"], normalize="index").mul(100).round(1)
        st.write("Post-type composition within each selected cluster (%)")
        st.dataframe(mix, use_container_width=True)
    else:
        st.info("No rows match the selected filters.")

with tab4:
    st.subheader("Clustering experiment comparison")
    if not comparison.empty:
        features = sorted(comparison["feature_set"].dropna().unique().tolist())
        chosen_feature = st.selectbox("Feature set for comparison", features)
        comp = comparison[comparison["feature_set"] == chosen_feature]
        st.dataframe(comp.sort_values("silhouette", ascending=False).round(4), use_container_width=True)
        fig, ax = plt.subplots(figsize=(9, 4))
        sns.lineplot(data=comp, x="k", y="silhouette", hue="algorithm", marker="o", ax=ax)
        ax.set_ylabel("Silhouette score")
        ax.set_xlabel("Number of clusters")
        ax.set_title("Silhouette score by algorithm and cluster count")
        st.pyplot(fig)
    else:
        st.warning("Model comparison file is missing. Run the notebook experiment section and export results.")

st.download_button(
    "Download filtered records as CSV",
    data=filtered.to_csv(index=False).encode("utf-8"),
    file_name="engagement_intelligence_filtered.csv",
    mime="text/csv",
)
