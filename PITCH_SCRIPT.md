# OpenCart Agent — 5 Minute Pitch Script

**Total runtime target: ~4:45–5:00**

---

## [0:00–0:40] The Problem (40 sec)

> "Agent-to-agent commerce is happening right now — NPCI's UAP, ACP, AP2, x402 — every
> major protocol race this year is about letting AI agents buy things on behalf of
> people. But almost every merchant today is invisible to those agents. Their catalog
> lives in HTML made for humans, not machines. Their checkout has no concept of an
> AI buyer at all.
>
> So even if a shopping agent wants to buy from a small Indian merchant, it can't —
> there's no safe, structured way in."

*(Show a quick visual: a chat-style AI buyer request bouncing off a normal e-commerce site)*

---

## [0:40–1:10] The Idea (30 sec)

> "OpenCart Agent is a checkout agent that sits in front of a merchant's store and
> makes them transactable by AI buyers, safely. It exposes the catalog in a structured
> format any AI agent can query, matches purchase intents to real inventory, and runs
> every transaction through spend guardrails before a single rupee moves."

---

## [1:10–3:30] Live Demo (2 min 20 sec) — the core of the pitch

*(Screen: run `python3 main.py` live, then flip to the dashboard)*

> "Let's walk through five real requests from AI buyer-agents."

1. **Clean approval** (20 sec)
   > "First — a ChatGPT-style shopper wants a white tee under ₹800. It matches, it's
   > in stock, it's within every guardrail — completed instantly, charged through
   > Razorpay test mode."

2. **Confirmation gate** (25 sec)
   > "Next — a request for a black hoodie at ₹1299. That's above our ₹1000
   > auto-approve threshold, so the agent doesn't just charge it — it asks for
   > explicit confirmation first. That's the 'gated' part of the brief in action."

3. **Confirmed completion** (15 sec)
   > "Same request, now confirmed — it goes through cleanly."

4. **Hard cap block** (25 sec)
   > "Now — a rogue agent tries to buy a ₹2999 denim jacket, even with confirmation
   > already set to true. Doesn't matter. It's above our ₹2500 hard ceiling, so it's
   > blocked outright. No override, no exception — merchant-set limits are absolute."

5. **Graceful failure** (25 sec)
   > "Last one — a buyer wants a black hoodie in size L. It matches perfectly... but
   > it's out of stock. Instead of substituting a different size silently, or
   > guessing what the buyer would accept, the agent declines cleanly and says
   > exactly why."

*(Show the dashboard scrolling through all 5 log entries with reasons visible)*

> "Every single one of these five decisions is sitting right here in the audit
> trail — timestamped, with the buyer's exact request, and a plain-English reason
> for what happened and why."

---

## [3:30–4:15] Why This Fits the Brief (45 sec)

> "This maps directly onto what the track asked for. It grows merchant revenue by
> opening a completely new sales channel — AI buyer-agents — without merchants
> building anything themselves. And it hits the bar exactly: every money action is
> explainable, bounded by hard limits, gated by confirmation where needed, fully
> audited, and handles failure gracefully instead of guessing."

---

## [4:15–4:45] Tech + What's Next (30 sec)

> "Right now this runs on Python with a simulated Razorpay test-mode charge and a
> mock catalog. The next step is wiring it to a real Razorpay test key, and
> supporting an actual agent-commerce protocol handshake — ACP or AP2 — so any
> compliant AI buyer can talk to it directly, not just our simulated ones."

---

## [4:45–5:00] Close (15 sec)

> "OpenCart Agent — making any merchant instantly transactable by AI buyers, safely,
> explainably, and without giving up control. Thanks."

---

### Recording tips
- Keep the terminal output and dashboard as the visual anchor — don't just talk over a slide.
- Practice the demo section (1:10–3:30) out loud at least twice; it's the part that'll run long if you're not careful.
- If you're short on time, cut the "what's next" section before cutting the live demo — the demo is what proves the project works.
