from gemini_client import generate

def build_prompt(schema, rows):
    return f"""
You are a synthetic data generator.

Generate {rows} rows of realistic data based on this SQL schema.

Rules:
- Respect column data types
- Respect foreign keys if present
- Output JSON only
- No explanation text

Schema:
{schema}
"""

def generate_data(schema, rows):
    prompt = build_prompt(schema, rows)
    return generate(prompt)