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
    prepopulate_context(ctx, file)


def prepopulate_context(ctx: click.Context, file: Path) -> None:
    ctx.ensure_object(dict)
    if "store" not in ctx.obj or not ctx.obj["store"]:
        ctx.obj["store"] = TOMLStore(file)
    if "printer" not in ctx.obj or not ctx.obj["printer"]:
        ctx.obj["printer"] = Printer()


# TODO: pak list kl* : List acronyms starting with "kl"
# TODO: pak list *p : List acronyms ending with "*p"
# TODO: pak list -c ONFi : Case-sensitive list of acronyms matching "ONFi" (default insensitive)


def validate_max_line_length(ctx, param, value: int | None) -> int | None:
    if value is None:
        return value

    printer: Printer = ctx.obj["printer"]
    try:
        printer.max_line_length = value
    except ValueError as e:
        raise click.BadParameter(str(e))
    return value


@root_group.command("list")
@click.argument("pattern", nargs=-1)
@click.option(
    "--max-length",
    "-m",
    type=int,
    callback=validate_max_line_length,
    help="Maximum length to limit output lines to. Use -1 for no limit.",
)
@click.pass_context
def list_command(
    ctx: click.Context, pattern: list[str], max_length: int | None
) -> None:
    """List acronyms that match PATTERN."""
    store: TOMLStore = ctx_store if (ctx_store := ctx.obj["store"]) else TOMLStore()
    store.load()
    printer = ctx.obj["printer"]
    if max_length is not None:
        printer.max_line_length = max_length
    click.echo(printer.stringify_pack(store.acronyms))


# TODO: pak add ONFi : Prompt for fields of, and add, ONFi
