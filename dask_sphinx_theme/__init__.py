import os
from os import path
from sphinx import addnodes

__version__ = "2.0.0"


def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = path.abspath(path.dirname(path.dirname(__file__)))
    return cur_dir

def remove_toctrees(app, doctree, docname):
    """Remove toctrees from pages a user provides.
    This happens at the end of the build process, so even though the toctrees
    are removed, it won't raise sphinx warnings about un-referenced pages.
    """
    pages = app.config.html_theme_options.get("remove_toctrees_from", [])
    if isinstance(pages, str):
        pages = [pages]
    for pagename in pages:
        pagename = os.path.splitext(pagename)[0]
        for toctree in app.env.tocs[pagename].traverse(addnodes.toctree):
            toctree.parent.remove(toctree)


# See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
def setup(app):
    app.add_html_theme("dask_sphinx_theme", path.abspath(path.dirname(__file__)))
    app.connect("doctree-resolved", remove_toctrees)
