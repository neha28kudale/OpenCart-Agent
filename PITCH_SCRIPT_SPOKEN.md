Agent-to-agent commerce is happening right now. NPCI's UAP, ACP, AP2, x402 — every major protocol race this year is about letting AI agents buy things on behalf of people. But almost every merchant today is invisible to those agents. Their catalog lives in HTML made for humans, not machines. Their checkout has no concept of an AI buyer at all. So even if a shopping agent wants to buy from a small Indian merchant, it simply can't — there's no safe, structured way in.

That's the gap I built OpenCart Agent for. It's a checkout agent that sits in front of a merchant's store and makes them transactable by AI buyers, safely. It exposes the catalog in a structured format any AI agent can query, matches purchase intents to real inventory, and runs every transaction through spend guardrails before a single rupee moves.

Let me show you exactly how it works with five real requests from AI buyer-agents.

First, a ChatGPT-style shopper wants a white t-shirt under eight hundred rupees. It matches, it's in stock, it's within every guardrail — so it's completed instantly, charged through Razorpay in test mode.

Next, a request comes in for a black hoodie priced at twelve ninety-nine. That's above our one-thousand rupee auto-approve threshold, so the agent doesn't just charge it blindly — it pauses and asks for explicit confirmation first. That's the gated part of the brief, working exactly as intended.

Same request, now confirmed — and it goes through cleanly.

Now here's an important one. A rogue agent tries to buy a denim jacket worth twenty-nine ninety-nine, even with confirmation already set to true. Doesn't matter — it's above our twenty-five-hundred rupee hard ceiling, so it's blocked outright. No override, no exception. Merchant-set limits are absolute, no matter what the buyer agent claims or confirms.

And last — a buyer wants that same black hoodie, but in size L. It matches perfectly... except it's out of stock. Instead of silently substituting a different size, or guessing what the buyer might accept, the agent declines cleanly and tells you exactly why.

Every single one of these five decisions is sitting right here in the audit trail — timestamped, with the buyer's exact request, and a plain-English reason for what happened and why. Nothing about this system acts silently.

This maps directly onto what the track asked for. It grows merchant revenue by opening a completely new sales channel — AI buyer-agents — without merchants having to build anything themselves. And it hits the bar exactly: every money action is explainable, bounded by hard limits, gated by confirmation where needed, fully audited, and handles failure gracefully instead of guessing.

Right now, this runs on Python with a simulated Razorpay test-mode charge and a mock catalog. The next step is wiring it to a real Razorpay test key, and supporting an actual agent-commerce protocol handshake — ACP or AP2 — so any compliant AI buyer can talk to it directly, not just the simulated ones I built for this demo.

OpenCart Agent — making any merchant instantly transactable by AI buyers, safely, explainably, and without giving up control. Thank you.
