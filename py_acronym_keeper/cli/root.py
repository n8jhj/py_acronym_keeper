"""Root of the CLI."""

import click


@click.group
def root_group():
    """\b
     _  _ |
    |_)(_||<      Py Acronym Keeper
    |
    """
    # Thanks to Patrick Gillespie for the ASCII art:
    # https://patorjk.com/software/taag/#p=display&f=Three%20Point&t=pak
    ...


# TODO: pak list kl* : List acronyms starting with "kl"
# TODO: pak list *p : List acronyms ending with "*p"
# TODO: pak list -c ONFi : Case-sensitive list of acronyms matching "ONFi" (default insensitive)
# TODO: pak add ONFi : Prompt for fields of, and add, ONFi
