from typing_extensions import Annotated, Optional
from pathlib import Path
from schema import CypherQuery
from io import TextIOWrapper
import json
import typer
import yaml
import zipfile


ALLOWED_FORMATS = ["json", "zip"]

app = typer.Typer()


def validate_format(value: str):
    if value.lower() not in ALLOWED_FORMATS:
        raise typer.BadParameter(f"Only {', '.join(ALLOWED_FORMATS)} is allowed")
    return value


class QueryBundle:
    def __init__(self, queries: list[CypherQuery]):
        self.queries = queries

    @staticmethod
    def load_query(cypher_query: Path) -> CypherQuery:
        with open(cypher_query, "r") as yaml_file:
            yaml_obj = yaml.safe_load(yaml_file)
            return CypherQuery(**yaml_obj)

    @classmethod
    def from_path(cls, input_dir: Path) -> "QueryBundle":
        cypher_queries = list(input_dir.rglob("*.yml"))
        queries = [
            QueryBundle.load_query(cypher_query) for cypher_query in cypher_queries
        ]
        return cls(queries)

    def to_json(self, output_file: TextIOWrapper) -> None:
        all_objects = [query.model_dump() for query in self.queries]
        output_file.write(json.dumps(all_objects, indent=2))

    def to_zip(self, output_file: TextIOWrapper) -> None:
        with zipfile.ZipFile(
            file=output_file.name,
            mode="w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=9,
        ) as archive:
            for query in self.queries:
                archive.writestr(
                    zinfo_or_arcname=f"{query.name}.json",
                    data=query.model_dump_json().encode(),
                )


@app.command()
def convert(
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
    output_file: Annotated[typer.FileTextWrite, typer.Argument()],
    file_format: Annotated[
        Optional[str],
        typer.Option(help="Format for export (json/zip)", callback=validate_format),
    ] = "json",
):

    typer.echo(f"Converting queries to {file_format} output")
    cypher_queries = QueryBundle.from_path(input_dir=input_dir)

    if file_format == "json":
        cypher_queries.to_json(output_file)

    else:
        cypher_queries.to_zip(output_file)

    typer.echo(
        f"Finished converting {len(cypher_queries.queries)} Cypher queries ({file_format}) to {output_file.name}"
    )


if __name__ == "__main__":
    app()
