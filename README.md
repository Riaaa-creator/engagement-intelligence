# Engagement Intelligence
### Behavioral Pattern Discovery and Comparative Analytics

Engagement Intelligence explores how Facebook posts differ in reactions, comments, shares, and reaction categories. It combines exploratory data analysis (EDA), feature engineering, K-Means and Agglomerative clustering, internal evaluation, cluster profiling, and an interactive Streamlit dashboard.

## Dataset and attribution

The project uses **Facebook Live Sellers in Thailand**, created by Nassim Dehouche and hosted by the UCI Machine Learning Repository.

- **Official dataset page:** https://archive.ics.uci.edu/dataset/488/facebook%2Blive%2Bsellers%2Bin%2Bthailand
- **Direct CSV source:** https://archive.ics.uci.edu/ml/machine-learning-databases/00488/Live.csv
- **Research article:** https://pmc.ncbi.nlm.nih.gov/articles/PMC7218155/
- **Dataset DOI:** https://doi.org/10.24432/C5R60S
- **Licence:** CC BY 4.0 (attribute the dataset creator and source)

The raw dataset is intentionally **not included** in this repository. The notebook reads it from the public UCI URL at runtime.

## Project contents

- `Engagement_Intelligence.ipynb` — complete analysis, data audit, EDA, feature construction, clustering experiments, evaluation, cluster interpretation, stability check, and result export.
- `app.py` — Streamlit dashboard for exploring the precomputed results.
- `outputs/` — generated clustered records, cluster profiles, model-comparison tables, sensitivity results, stability results, and experiment metadata.
- `PROJECT REPORT.pdf` — structured technical report.
- `requirements.txt` — Python dependencies.

## Run the dashboard locally

Python 3.10+ is recommended.

```bash
python -m venv .venv
# Windows:
.venv\\Scripts\\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

The dashboard reads the generated files in `outputs/`. These are included so the dashboard can run without first rerunning the notebook.

## Re-run the analysis

Open `Engagement_Intelligence.ipynb` in Jupyter or Google Colab, install dependencies from `requirements.txt`, and run all cells from top to bottom. Internet access is required for the notebook to download the source dataset from UCI. The export section regenerates the files in `outputs/`.

## Deployment: Streamlit Community Cloud

1. Create a GitHub repository and upload the contents of this project folder (not the enclosing ZIP folder).
2. Confirm that `app.py`, `requirements.txt`, and `outputs/` are at the repository root.
3. Visit https://share.streamlit.io/ and sign in with GitHub.
4. Choose **Create app**, select your repository and branch, and set the main file path to `app.py`.
5. Deploy. Streamlit will provide a public app URL.

**GitHub repository URL:** https://github.com/Riaaa-creator/engagement-intelligence/  
**Live dashboard URL:** https://engagement-intelligence-pzretlsxzxg3mtgzhxw9wy.streamlit.app/

## Method overview

1. Audit columns, data types, missing values, invalid engagement counts, and duplicate records.
2. Explore post types, engagement distributions, publication-time patterns, and correlations.
3. Compare a compact feature set (`num_reactions`, `num_comments`, `num_shares`) with a detailed reaction-mix feature set.
4. Apply `log1p` transformation and standardization to numeric counts.
5. Compare K-Means and Ward-linkage Agglomerative Clustering on a reproducible sample.
6. Inspect cluster profiles and post-type composition; test a post-type-aware sensitivity configuration.
7. Export reusable results and explore them in Streamlit.

## Interpretation cautions

Cluster labels are descriptive groupings, not ground-truth categories. Silhouette scores and inertia are internal measures; neither proves business value or causality. Results can depend on the selected features, transformation, scaling, sample, and number of clusters. The dataset describes posts from a particular set of sellers and historical period; results should not automatically be generalized to all platforms or current audiences.

## Citation

Dehouche, N. (2018). *Facebook Live Sellers in Thailand* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5R60S
