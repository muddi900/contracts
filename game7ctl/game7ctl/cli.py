import argparse
from typing import Callable

from .core import generate_cli as core_generate_cli
from .InventoryFacet import generate_cli as inventory_generate_cli
from .DiamondLoupeFacet import generate_cli as dloupe_generate_cli
from .DiamondCutFacet import generate_cli as dcut_generate_cli
from .OwnershipFacet import generate_cli as own_generate_cli
from .version import VERSION


def add_subparser(cmd_name: str, subparser: argparse.ArgumentParser, cli_gen: Callable):
    subcommand = cli_gen()
    subparser.add_parser(cmd_name, parents=[subcommand], add_help=False)


def generate_cli() -> argparse.ArgumentParser:
    """
    Generates the argument parsers for the game7ctl command-line tool.
    """
    parser = argparse.ArgumentParser(
        description="Development tools for Game7 smart contracts"
    )
    parser.add_argument(
        "-v", "--version", action="version", version=VERSION, help="Print version"
    )
    parser.set_defaults(func=lambda _: parser.print_help())

    subparsers = parser.add_subparsers()

    add_subparser(
        "core",
        subparsers,
        core_generate_cli,
    )
    add_subparser("inventory", subparsers, inventory_generate_cli)
    add_subparser("diamond-loupe", subparsers, dloupe_generate_cli)
    add_subparser("diamond-cut", subparsers, dcut_generate_cli)
    add_subparser("ownership", subparsers, own_generate_cli)

    return parser


def main() -> None:
    """
    Executes the game7ctl command line tool
    """
    parser = generate_cli()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
