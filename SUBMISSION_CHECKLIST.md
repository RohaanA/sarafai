# Submission Checklist — due in ~25 minutes

## 1. Public repository URL (required)
```bash
# In E:\hackathons\Alibaba\SarafAI:
gh repo create sarafai --public --source=. --push
# (no gh CLI? create empty repo on github.com, then:)
# git remote add origin https://github.com/YOUR_USER/sarafai.git
# git push -u origin main
```
- [ ] Repo is PUBLIC (form checks reachability)
- [ ] No secrets committed (only static files — verified: no .env, no keys)

## 2. Project summary (required, 200–1,500 chars)
- [ ] Copy from `SUBMISSION_TEXT.md`

## 3. Presentation (required, PDF/PPTX, ≤50 MB)
- [ ] Upload `SarafAI_Presentation.pptx` (8 slides, 44 KB)

## 4. Supporting attachments (optional)
- [x] `SarafAI_Demo.mp4` — 71-second narrated, captioned walkthrough of the guided tour (recorded from the live site)

## 5. Demo link (optional)
- [ ] GitHub Pages: repo → Settings → Pages → Branch: main / root → Save
      Live at `https://YOUR_USER.github.io/sarafai/`

## Demo script (60 sec, if recording)
1. Dashboard (15s): "This is a real kiryana store's credit health score — 6 explainable factors, loan offer sized to actual inflows."
2. Scan Receipt (25s): click a sample receipt → OCR extracts fields → confirm.
3. Rescore (15s): score jumps live — "merchants watch their creditworthiness grow as they digitize."
4. Khata tab (5s): auto-reconciled ledger with source tags.
