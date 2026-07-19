# Upload with GitHub Desktop

1. In GitHub Desktop, open the existing local repository.
2. Create a backup copy of the entire local folder.
3. Extract `computational-pathology-ai-lab.zip`.
4. Copy the contents of the extracted `computational-pathology-ai-lab` folder into the existing local repository folder. Choose **Replace** for matching files; extraction does not remove the old notebooks.
5. Open PowerShell or Command Prompt in the repository folder and run:
   `python scripts/migrate_legacy.py`
6. Confirm the original notebooks, `submission.csv`, and leaderboard image now appear under `legacy/cu_boulder_original_assignment/`.
7. In GitHub Desktop, review the changed files. Do not commit private data, model weights, or `.env` files.
8. Use summary: `Transform project into Computational Pathology AI Lab v1.0.0`.
9. Click **Commit to main**, then **Push origin**.
10. After the repository is renamed on GitHub, GitHub Desktop normally follows the redirect; use Repository > Repository Settings > Remote if an update is needed.
