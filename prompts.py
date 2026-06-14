CLAIM_PROMPT = """
Extract all factual and verifiable claims from the text.

Rules:
1. Only extract factual claims.
2. Ignore opinions.
3. Return one claim per line.
4. Do not add numbering.
5. Keep claims concise.

TEXT:
{text}
"""


VERIFY_PROMPT = """
You are a professional fact-checking expert.

Claim:
{claim}

Evidence:
{evidence}

Instructions:

- VERIFIED → Evidence clearly supports the claim.
- INACCURATE → Claim is partially true, outdated, or lacks precision.
- FALSE → Evidence clearly contradicts the claim.

Return ONLY valid JSON:

{{
  "status": "VERIFIED",
  "explanation": "Short explanation",
  "correct_fact": "Correct information"
}}
"""