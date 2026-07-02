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
    "sphinx_tippy",
]

html_theme = "furo"

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "attrs_block",
]
myst_heading_anchors = 2

linkcheck_ignore = [
    # Linkcheck treats these as anchors, even though they are not
    r"^https://matrix.to/#/#",
]
linkcheck_request_headers = {
    "*": {
        "Accept": "text/html",
        "User-Agent": "sphinx/linkcheck",
    }
}
