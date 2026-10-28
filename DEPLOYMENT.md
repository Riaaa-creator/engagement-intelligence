# GitHub and deployment checklist

## Before publishing
- [ ] Review the notebook top-to-bottom and confirm the UCI source URL downloads successfully.
- [ ] Keep the raw dataset out of the repository; it is downloaded by the notebook when needed.
- [ ] Keep `outputs/` in the repository because the dashboard reads those generated CSV files.
- [ ] Check that `requirements.txt`, `app.py`, and `outputs/` are at the repository root.
- [ ] Add the final GitHub repository and live dashboard URLs to `README.md` and `PROJECT REPORT.pdf` after they exist.

## Publish to GitHub
1. Create a public repository named `engagement-intelligence` (or another suitable name).
2. Upload the *contents* of this project folder.
3. Ensure the root of the GitHub repository contains `app.py`, `requirements.txt`, `README.md`, `Engagement_Intelligence.ipynb`, `outputs/`, and `PROJECT REPORT.pdf`.

## Deploy on Streamlit Community Cloud
1. Sign in at https://share.streamlit.io/ using GitHub.
2. Select **Create app**.
3. Select the repository and branch.
4. Set **Main file path** to `app.py`.
5. Deploy and wait for the build to complete.
6. Open the app URL and verify the filters, tabs, charts, and CSV download.
7. Copy the actual repository URL and actual app URL into the README and report.

## URL placeholders
GitHub repository: `ADD_AFTER_PUBLISHING`  
Live Streamlit app: `ADD_AFTER_DEPLOYMENT`

These are intentionally placeholders. They must be replaced with the real URLs after publishing/deployment; do not submit placeholders as if they were working links.
