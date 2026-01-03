from __future__ import annotations

project = "Fedora packaging guide"
author = "Cristian Le"
copyright = "Cristian Le"

extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx.ext.todo",
    "sphinx_subfigure",
    "sphinx_togglebutton",
]

html_theme = "furo"

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
myst_heading_anchors = 2
