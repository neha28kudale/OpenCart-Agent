"""
Agent-readable catalog.
Exposes a merchant's products in a structured, machine-queryable format so
external AI buyer-agents (ChatGPT shopping, Perplexity buyer-agent, etc.)
can discover and reason about what's purchasable - no HTML scraping needed.

In production this would be served at /.well-known/agent-catalog.json
and kept in sync with the merchant's actual inventory via Razorpay/Shopify webhooks.
"""

CATALOG = [
    {
        "sku": "HD-BLK-M",
        "name": "Classic Black Hoodie",
        "category": "apparel",
        "attributes": {"color": "black", "size": "M", "material": "cotton fleece"},
        "price": 1299,
        "currency": "INR",
        "stock": 14,
        "description": "Unisex black hoodie, regular fit, cotton fleece.",
    },
    {
        "sku": "HD-BLK-L",
        "name": "Classic Black Hoodie",
        "category": "apparel",
        "attributes": {"color": "black", "size": "L", "material": "cotton fleece"},
        "price": 1299,
        "currency": "INR",
        "stock": 0,  # deliberately out of stock - used for the graceful-failure demo
        "description": "Unisex black hoodie, regular fit, cotton fleece.",
    },
    {
        "sku": "TS-WHT-M",
        "name": "Everyday White Tee",
        "category": "apparel",
        "attributes": {"color": "white", "size": "M", "material": "cotton"},
        "price": 499,
        "currency": "INR",
        "stock": 40,
        "description": "Soft cotton crew-neck t-shirt.",
    },
    {
        "sku": "JK-DNM-L",
        "name": "Denim Jacket",
        "category": "apparel",
        "attributes": {"color": "blue", "size": "L", "material": "denim"},
        "price": 2999,
        "currency": "INR",
        "stock": 8,
        "description": "Classic washed denim jacket.",
    },
    {
        "sku": "CP-BLK-OS",
        "name": "Black Baseball Cap",
        "category": "accessories",
        "attributes": {"color": "black", "size": "one size"},
        "price": 399,
        "currency": "INR",
        "stock": 25,
        "description": "Adjustable cotton baseball cap.",
    },
]


def find_matches(query_attributes: dict, max_price: float = None):
    """
    Match catalog items against an AI buyer-agent's structured purchase intent.
    query_attributes example: {"category": "apparel", "color": "black", "size": "M"}
    """
    matches = []
    for item in CATALOG:
        score = 0
        total_fields = 0
        for key, value in query_attributes.items():
            total_fields += 1
            if key == "category" and item.get("category") == value:
                score += 1
            elif item["attributes"].get(key, "").lower() == str(value).lower():
                score += 1

        if total_fields == 0:
            continue
        match_ratio = score / total_fields

        if match_ratio >= 0.6:  # reasonably strong match
            if max_price is None or item["price"] <= max_price:
                matches.append({**item, "match_ratio": round(match_ratio, 2)})

    matches.sort(key=lambda x: (-x["match_ratio"], x["price"]))
    return matches
