"""Console script for {{cookiecutter.project_slug}}."""
import logging
import logging.config
import sys
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}
{% if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- endif %}

from {{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug.replace('_', ' ').title().replace(' ', '') }}

def _init_logging(verbose: int) -> None:
    level = logging.ERROR

    logger = logging.getLogger()
    handler = logging.StreamHandler(stream=sys.stdout)
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    if verbose == 1:
        level = logging.WARNING
    elif verbose == 2:
        level = logging.INFO
    elif verbose > 2:
        level = logging.DEBUG

    handler.setLevel(level)
    logger.setLevel(level)


{% if cookiecutter.command_line_interface|lower == 'click' %}
@click.command()
@click.option("-v", "--verbose", default=1, count=True)
def main(verbose: int, args=None) -> None:
    """Console script for {{cookiecutter.project_slug}}."""
    _init_logging(verbose)
    logger = logging.getLogger("cli.main")

    logger.debug("Logger initialized")

    {{ cookiecutter.project_slug }} = {{ cookiecutter.project_slug.replace('_', ' ').title().replace(' ', '') }}()  # noqa: F841

    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
def main():
    """Console script for {{cookiecutter.project_slug}}."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "{{cookiecutter.project_slug}}.cli.main")
    return 0
{%- endif %}


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
