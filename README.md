# SarafAI

**Alternate Credit Scoring & Cash-Flow Intelligence for MSMEs — bringing Pakistan's unbanked kiryana stores into the formal financial system.**

## The Problem

Over 70% of Pakistan's economy is informal. Small merchants (kiryana stores, dhabas, micro-suppliers) have no formal credit score — no bank statements, no salary slips, no collateral. Banks can't underwrite them, so millions of viable businesses are locked out of formal credit and forced toward expensive informal lenders, while their commerce stays invisible to the tax net.

## The Solution

SarafAI is an AI ledger that ingests the data these merchants **already produce**:

- Scanned physical receipts & supplier invoice photos (OCR)
- Handwritten khata ledger notes
- Mobile wallet transaction histories (Easypaisa, JazzCash)

It reconciles these heterogeneous sources into a verifiable transaction ledger and auto-generates an **SME Credit Health Score (300–900)** — an explainable score built from six cash-flow factors: revenue scale, cash-flow consistency, growth trend, business activity, digital documentation, and recency. Fintechs and banks consume this score to originate collateral-free micro-loans with lower default rates.

## Why It Matters (Economic Impact)

- **Financial inclusion:** unlocks micro-loans for unbanked micro-businesses with no credit history
- **Lower default risk:** loans underwritten on actual, verified cash flows instead of guesswork
- **Documentation:** every scanned receipt is a tax record — organically pulling informal commerce into the documented economy

## How to Run the Demo

The MVP is a zero-dependency single-file web app:

1. Open `index.html` in any browser. That's it — no install, no build step.

**Demo script (60 seconds):**
1. **Dashboard** — see the SME Credit Health Score for a sample Karachi kiryana store, with its six explainable score factors, cash-flow metrics, and a live collateral-free loan offer sized from actual monthly inflows.
2. **Scan Receipt** — click any sample receipt (or drop an image). Watch Qwen-VL-style OCR extract date, counterparty, line items and amount with confidence scores, then confirm.
3. The ledger updates and the **score instantly recalculates** — showing how a merchant's creditworthiness grows as they digitize more of their business.

## Architecture (Production Design)

```
Receipt/Khata photos ──► Qwen-VL OCR (Alibaba Cloud) ──► Transaction normalizer
Wallet APIs (Easypaisa/JazzCash) ──────────────────────────► │
                                                              ▼
                                        PostgreSQL / AnalyticDB (verified ledger)
                                                              ▼
                                        Scoring engine (cash-flow factors, 300–900)
                                                              ▼
                                    Lender API ──► Collateral-free micro-loan offers
```

**Tech stack:** Document OCR (Qwen-VL), predictive cash-flow credit-risk modeling, Alibaba Cloud PostgreSQL / AnalyticDB, single-page web app.

## Status

MVP: working interactive demo of the full loop — ingestion → extraction → reconciliation → explainable scoring → loan offer. The scoring engine in the MVP is transparent and rule-based (by design, for auditability); production uses the same factors calibrated on repayment data.

## Team

Built for the Bano Qabil × Alibaba Cloud AI Hackathon 2026 — Finance track.
