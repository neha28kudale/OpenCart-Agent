Right now, AI agents are starting to shop on behalf of people. You've probably heard of things like NPCI's UAP, or protocols like ACP, AP2, and x402. All of these are trying to solve one problem — letting an AI agent buy something for you, safely.

But here's the issue. Most small merchants today can't sell to these AI agents at all. Their product catalog is built for humans to read, not for machines to understand. Their checkout page has no idea an AI agent might be the one buying. So even if an AI shopping assistant wants to buy from a small Indian merchant, it simply can't get in.

That's the problem I'm solving with OpenCart Agent.

It's a checkout agent that sits in front of a merchant's store and makes that merchant easy to buy from — for AI agents. It does three things. It shows the product catalog in a format AI agents can actually read. It matches what the AI agent wants to what's really in stock. And most importantly, it checks every purchase against safety rules before any money moves.

Let me show you exactly how this works, with five real examples.

First, an AI shopping agent asks for a white t-shirt under eight hundred rupees. It's in stock, it's within the price limit, so it goes through right away. Payment is completed using Razorpay test mode.

Second, an agent asks for a black hoodie priced at twelve ninety-nine. This is above our limit of one thousand rupees, so the system doesn't pay automatically. It pauses and asks for confirmation first. This is the safety gate working exactly as it should.

Third, the same request comes back, this time confirmed. Now it goes through smoothly.

Fourth — and this one's important. A different agent tries to buy a denim jacket worth twenty-nine ninety-nine. Even though it says "confirmed," the system still blocks it. Why? Because twenty-nine ninety-nine is above our maximum limit of twenty-five hundred rupees. No confirmation can override that hard limit. The merchant's rules always come first.

Fifth, an agent asks for the same black hoodie, but in size L. It's a perfect match — except it's out of stock. Instead of guessing or swapping in a different size on its own, the system simply says no, and explains exactly why.

Every single one of these five actions is recorded in an audit log. You can see the time, what the AI agent asked for, and the plain reason behind every decision. Nothing happens quietly in the background.

This is exactly what the challenge asked for. It helps merchants earn more by opening up a brand new way to sell — through AI agents — without merchants doing any extra work. And every money action here is explainable, has clear limits, needs approval when required, is fully logged, and fails safely instead of guessing.

Right now, this is built using Python, with a simulated Razorpay test payment and sample product data. The next step is connecting it to a real Razorpay test account, and making it work with an actual AI-agent commerce protocol like ACP or AP2, so any real AI shopping agent can use it, not just the examples I built for this demo.

That's OpenCart Agent — a simple way to make any merchant ready for AI-agent shopping, safely, clearly, and without losing control. Thank you.
