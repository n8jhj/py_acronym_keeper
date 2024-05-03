"""Root of the CLI."""

from pathlib import Path

import click

from py_acronym_keeper.printer import Printer
from py_acronym_keeper.toml_store import TOMLStore


@click.group
@click.option(
    "-f", "--file", type=click.Path(exists=False, file_okay=True, dir_okay=False)
)
@click.pass_context
def root_group(ctx: click.Context, file: Path):
    """\b
     _  _ |
    |_)(_||<      Py Acronym Keeper
    |
    """
    # Thanks to Patrick Gillespie for the ASCII art:
    # https://patorjk.com/software/taag/#p=display&f=Three%20Point&t=pak
    #
    # Ensure that ctx.obj exists and is a dict (in case we are called by means
    # other than `root_group(obj={})`).
    ctx.ensure_object(dict)
    ctx.obj["store"] = TOMLStore(file)


# TODO: pak list kl* : List acronyms starting with "kl"
# TODO: pak list *p : List acronyms ending with "*p"
# TODO: pak list -c ONFi : Case-sensitive list of acronyms matching "ONFi" (default insensitive)


@root_group.command("list")
@click.pass_context
def list_command(ctx: click.Context) -> None:
    """List acronyms."""
    store: TOMLStore = ctx_store if (ctx_store := ctx.obj["store"]) else TOMLStore()
    store.load()
    printer: Printer = Printer()
    click.echo(printer.stringify_pack(store.acronyms))


# TODO: pak add ONFi : Prompt for fields of, and add, ONFi
