# Configuration file for the Sphinx documentation builder.

# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Project information
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
from datetime import date

sys.path.insert(0, os.path.abspath("../"))

from cloudcord import __version__

project = "cloudcord"
copyright = f"{date.today().year}, Chill_Fabo"
author = "Chill_Fabo"
release = __version__

version = __version__


# General configuration
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
]

simplify_optional_unions = True

autodoc_member_order = "bysource"

intersphinx_mapping = {
    "py": ("https://docs.python.org/3", None),
    "aio": ("https://docs.aiohttp.org/en/stable/", None),
    "req": ("https://requests.readthedocs.io/en/latest/", None),
    "dc": ("https://docs.pycord.dev/en/master/", None),
    "dpy": ("https://discordpy.readthedocs.io/en/stable/", None),
    "sql": ("https://aiosqlite.omnilib.dev/en/stable/", None),
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# Options for HTML output and furo customisation
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# https://pradyunsg.me/furo/customisation/

html_experimental_html5_writer = True

html_theme = "furo"

html_title = f"{project} v{release} Documentation"

base_colors = {
    "white": "#ffffff",
    "grey-1": "#f9f9fa",
    "grey-1-8": "rgba(249, 249, 250, 0.8)",
    "grey-2": "#ededf0",
    "grey-3": "#d7d7db",
    "grey-4": "#b1b1b3",
    "grey-5": "#2a2a2b",
    "grey-6": "#4a4a4f",
    "grey-7": "#2a2a2b",
    "grey-8": "#1e1e1f",
    "black": "#0c0c0d",
    "blue-1": "#3399ff",
    "blue-2": "#0a84ff",
    "blue-3": "#0060df",
    "blue-4": "#003eaa",
    "blue-5": "#002275",
    "blue-6": "#000f40",
    "blurple": "#7289da",
}

html_theme_options = {
    "source_repository": "https://github.com/littxle/cloudcord",
    "source_branch": "master",
    "source_directory": "docs/",
    "light_css_variables": {
        # Theme
        # "color-brand-primary": "#5865f2",
        "font-stack": "'Outfit', sans-serif",
        # Custom
        **base_colors,
        "attribute-table-title": "var(--grey-6)",
        "attribute-table-entry-border": "var(--grey-3)",
        "attribute-table-entry-text": "var(--grey-5)",
        "attribute-table-entry-hover-border": "var(--blue-2)",
        "attribute-table-entry-hover-background": "var(--grey-2)",
        "attribute-table-entry-hover-text": "var(--blue-2)",
        "attribute-table-badge": "var(--grey-7)",
        "light-snake-display": "unset",
        "dark-snake-display": "none",
    },
    "dark_css_variables": {
        # Theme
        # "color-foreground-primary": "#fff",
        # "color-brand-primary": "#5865f2",
        # "color-background-primary": "#17181a",
        # "color-background-secondary": "#1a1c1e",
        # "color-background-hover": "#33373a",
        # Custom
        "attribute-table-title": "var(--grey-3)",
        "attribute-table-entry-border": "var(--grey-5)",
        "attribute-table-entry-text": "var(--grey-3)",
        "attribute-table-entry-hover-border": "var(--blue-1)",
        "attribute-table-entry-hover-background": "var(--grey-6)",
        "attribute-table-entry-hover-text": "var(--blue-1)",
        "attribute-table-badge": "var(--grey-4)",
        "light-snake-display": "none",
        "dark-snake-display": "unset",
    },
}


html_logo = "_static/cloudcord_logo.png"
html_favicon = "_static/favicon.ico"

html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_js_files = ["js/custom.js"]
