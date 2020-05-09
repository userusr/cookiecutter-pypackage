"""Top-level package for {{ cookiecutter.project_name }}.

{{ cookiecutter.project_short_description }}
"""

__author__ = """{{ cookiecutter.full_name }}"""
__maintainer__ = __author__

__email__ = "{{ cookiecutter.email }}"
__version__ = "{{ cookiecutter.version }}"
{%- if cookiecutter.open_source_license != "Not open source" %}
__license__ = "{{ cookiecutter.open_source_license }}"
{%- endif %}

__all__ = (
    "__author__",
    "__email__",
    "__maintainer__",
    "__version__",
    {% if cookiecutter.open_source_license != "Not open source" -%}
    "__license__",
    {%- endif %}
)
