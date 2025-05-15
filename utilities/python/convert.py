from typing_extensions import Annotated
from pathlib import Path
import json
import glob
import typer
import yaml

app = typer.Typer()


@app.command()
def to_json(
    input_dir: Annotated[
        Path,
        typer.Argument(
            exists=True,
            file_okay=True,
            dir_okay=True,
            readable=True,
            resolve_path=True,
        ),
    ],
    output_file: Annotated[typer.FileTextWrite, typer.Argument()]
):
    cypher_queries = glob.glob(f"{input_dir}/**/*.yml", recursive=True)
    typer.echo(f"Converting Queries {len(cypher_queries)} to combined JSON")
    all_objects = []
    for cypher_query in cypher_queries:
        with open(cypher_query, "r") as yaml_file:
            all_objects.append(yaml.safe_load(yaml_file))

    output_file.write(json.dumps(all_objects, indent=2))
    typer.echo(f"Finished converting Cypher queries to JSON to {output_file.name}")


if __name__ == "__main__":
    app()
