import typer
import json
from geoforge.core.registry import registry

# IMPORTANT: load skills
import geoforge.skills  

app = typer.Typer()


@app.command()
def export():
    from geoforge.exporters.advanced_exporter import export_claude
    data = export_claude()
    print(data)
def hello():
    print("GeoForge is working")


@app.command("list")
def list_skills():
    print("Registered skills:", registry.list())


@app.command()
def run(
    name: str,
    param: list[str] = typer.Option(None, "--param", "-p")
):
    """
    Run a skill

    Example:
    geoforge run citation-gap -p target_url=... -p competitor_url=...
    """

    if name not in registry.list():
        print(f"❌ Skill '{name}' not found")
        return

    skill = registry.get(name)()

    kwargs = {}

    if param:
        for p in param:
            if "=" not in p:
                print(f"Invalid param: {p}")
                return
            key, value = p.split("=", 1)
            kwargs[key] = value

    result = skill.run(**kwargs)

    print(json.dumps(result.model_dump(), indent=2))


if __name__ == "__main__":
    app()