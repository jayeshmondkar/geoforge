from geoforge.core.registry import registry


def export_claude():
    skills = registry.list()

    tools = []

    for s in skills:
        tools.append({
            "name": s,
            "description": f"GEO skill: {s}",
            "input_schema": {
                "type": "object",
                "properties": {
                    "input": {"type": "string"}
                }
            }
        })

    return {"tools": tools}