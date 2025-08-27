import typer, hashlib, os

app = typer.Typer()

@app.command(help="Calculate the hash of a file using the specified algorithm")
def calculate_hash(
    file: str = typer.Option(..., "--file", "-f", help="Path to the file to hash"),
    algorithm: str = typer.Option("sha256", "--algorithm", "-a", help="Hashing algorithm to use  (e.g., md5, sha1, sha256)"), 
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Suppress output except for the hash value")
):
    if algorithm not in hashlib.algorithms_available:
            typer.echo(f"Error: Unsupported algorithm '{algorithm}'. Use 'list-algorithms' to see available options.")
            raise typer.Exit(code=1)
    elif not os.path.isfile(file):
            typer.echo(f"Error: File '{file}' does not exist.")
            raise typer.Exit(code=1)
    try:
        with open(file, "rb") as f:
            data = f.read()
        hash_function = getattr(hashlib, algorithm) 
        hash_value = hash_function(data).hexdigest()
        if quiet:
            typer.echo(hash_value)
        else:
            typer.echo(f"{algorithm} hash of {file} is {hash_value}")
    except Exception as e:
        typer.echo(f"Error: {e}")
        raise typer.Exit(code=1)

@app.command(help="List available hashing algorithms")
def list_algorithms():
    algorithms = sorted(hashlib.algorithms_available)
    typer.echo("Available hashing algorigthms:")
    for algo in algorithms:
        typer.echo(f" - {algo}")



if __name__ == "__main__":
    app()