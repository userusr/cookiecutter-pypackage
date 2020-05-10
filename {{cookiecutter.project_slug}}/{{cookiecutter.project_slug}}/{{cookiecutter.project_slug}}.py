"""Main module."""
import logging


class {{ cookiecutter.project_slug.replace('_', ' ').title().replace(' ', '') }}():
    """Class for {{ cookiecutter.project_slug }}."""

    def __init__(self) -> None:
        """Constract {{ cookiecutter.project_slug }}."""
        self.logger = logging.getLogger("{{ cookiecutter.project_slug }}")
        self.logger.debug("{{ cookiecutter.project_slug.replace('_', ' ').title().replace(' ', '') }} initialized")
