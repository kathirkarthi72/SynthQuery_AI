import sqlparse

def extract_tables(schema_text):
    parsed = sqlparse.parse(schema_text)
    return [str(stmt) for stmt in parsed]