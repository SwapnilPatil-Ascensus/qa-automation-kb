# GitLab Project Manager — Setup for Change Set Investigation

Local utility for querying GitLab MRs, commits, and branches by project and date range.  
**Separate repo** — not part of qa-automation-kb.

---

## Prerequisites

| Item | Requirement |
|------|-------------|
| Python | 3.8+ (3.11 recommended) |
| Node.js | 16+ (20 recommended) |
| GitLab PAT | `read_api` or `api` scope — [create token](https://gitlab.com/-/user_settings/personal_access_tokens) |

**Security:** Store token in `.env` or **Manage Token** UI only. Never commit to git.

---

## Get the project

Clone or copy `GitlabInfoProjUI` to your machine.

Example path: `C:\Development\Workspace\GitlabInfoProjUI`

---

## Windows setup (two terminals)

### Terminal 1 — Backend

```powershell
cd <path-to>\GitlabInfoProjUI

python -m venv venv
.\venv\Scripts\activate
pip install -r backend\requirements.txt

# Option A: .env file in project root
# GITLAB_TOKEN=your-token-here

# Option B: session env var
$env:GITLAB_TOKEN="your-gitlab-token-here"

python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

Verify: http://localhost:8000/health

### Terminal 2 — Frontend

```powershell
cd <path-to>\GitlabInfoProjUI\ui
npm install
npm start
```

Open: http://localhost:3000

### Token via UI

1. Click **Manage Token** in header
2. Paste PAT → Save (writes to `.env`, reloads app)

---

## Linux / macOS

```bash
cd <path-to>/GitlabInfoProjUI
python3 -m venv venv && source venv/bin/activate
pip install -r backend/requirements.txt
export GITLAB_TOKEN="your-token"
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

# Second terminal
cd ui && npm install && npm start
```

---

## Bug lifecycle usage

| Step | Action |
|------|--------|
| 1 | Note last **green** run date and **failure** date |
| 2 | Select **Project** → `monolith` first |
| 3 | Set **Start Date** / **End Date** (or Last 7 days preset) |
| 4 | **Merge Requests** → filter **Merged** |
| 5 | **Commits** tab → same range |
| 6 | **Copy** or **Export** → paste into JIRA / email Change Set |
| 7 | Repeat for `automation`, `qa-automation` if needed |

### Fields to capture per MR

- Title · Author · Merged by · source → target branch · Merged At (EST)

Then use `prompts/03-gitlab-change-set.md` in Cursor to format summary.

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Backend won't start | Check `GITLAB_TOKEN` is set — backend refuses start without it |
| CORS / API errors | Ensure backend on :8000 before starting frontend |
| Empty results | Widen date range; MR filter uses `updated_at` — include day before last green run |
| Stale data | Token update clears cache; or `POST /cache/clear` |
| SSL errors | `GITLAB_VERIFY_SSL=false` in `.env` (corporate proxy) |

Full docs in GitlabInfoProjUI repo: `README.md`, `SETUP.md`, `docs/USER_GUIDE.md`

---

## Docker (optional)

```powershell
cd GitlabInfoProjUI
# Set GITLAB_TOKEN in .env first
docker-compose up
```

Frontend: http://localhost:3000
