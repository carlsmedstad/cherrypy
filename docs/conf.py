"""CherryPy sphinx doc configuration module."""
# -*- coding: utf-8 -*-
#
# CherryPy documentation build configuration file, created by
# sphinx-quickstart on Sat Feb 20 09:18:03 2010.
#
# This file is execfile()d with the current directory set to its containing
# dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import importlib
import sys

assert sys.version_info > (3, 5), 'Python 3 required to build docs'


def try_import(mod_name):
    """Attempt importing module and suppress failure of doing this."""
    try:
        return importlib.import_module(mod_name)
    except ImportError:
        pass


def get_supported_pythons(classifiers):
    """Return min and max supported Python version from meta as tuples."""
    PY_VER_CLASSIFIER = 'Programming Language :: Python :: '
    vers = filter(lambda c: c.startswith(PY_VER_CLASSIFIER), classifiers)
    vers = map(lambda c: c[len(PY_VER_CLASSIFIER):], vers)
    vers = filter(lambda c: c[0].isdigit() and '.' in c, vers)
    vers = map(lambda c: tuple(map(int, c.split('.'))), vers)
    vers = sorted(vers)
    del vers[1:-1]
    return vers


custom_sphinx_theme = try_import('alabaster')

prj_meta = importlib.metadata.metadata('cherrypy')
prj_author = prj_meta['Author']
prj_license = prj_meta['License']
prj_description = prj_meta['Description']
prj_py_ver_range = get_supported_pythons(prj_meta.get_all('Classifier'))
prj_py_min_supported, prj_py_max_supported = map(
    lambda v: '.'.join(map(str, v)), prj_py_ver_range
)

project = prj_meta['Name']

github_url = 'https://github.com'
github_repo_org = project.lower()
github_repo_name = project.lower()
github_repo_slug = f'{github_repo_org}/{github_repo_name}'
github_repo_url = f'{github_url}/{github_repo_slug}'
cr_github_repo_url = f'{github_url}/{github_repo_org}/cheroot'
github_sponsors_url = f'{github_url}/sponsors'

rst_epilog = f"""
.. |project| replace:: {project}
.. |min_py_supported| replace:: {prj_py_min_supported}
.. |max_py_supported| replace:: {prj_py_max_supported}
"""

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    # Stdlib extensions:
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',

    # Third-party extensions:
    'sphinxcontrib.apidoc',
    'rst.linker',
    'jaraco.packaging.sphinx',
]

extlinks = {
    'issue': (f'{github_repo_url}/issues/%s', '#%s'),
    'pr': (f'{github_repo_url}/pull/%s', 'PR #%s'),
    'commit': (f'{github_repo_url}/commit/%s', '%s'),
    'cr-issue': (f'{cr_github_repo_url}/issues/%s', 'Cheroot #%s'),
    'cr-pr': (f'{cr_github_repo_url}/pull/%s', 'Cheroot PR #%s'),
    'gh': (f'{github_url}/%s', 'GitHub: %s'),
    'user': (f'{github_sponsors_url}/%s', '@%s'),
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'cheroot': ('https://cheroot.cherrypy.dev/en/latest/', None),
    'pytest-docs': ('https://docs.pytest.org/en/latest/', None),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output ---------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = getattr(custom_sphinx_theme, '__name__', 'default')

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {
# "relbarbgcolor": "#880000",
#     "relbartextcolor": "white",
# "relbarlinkcolor": "#FFEEEE",
# "sidebarbgcolor": "#880000",
#     "sidebartextcolor": "white",
# "sidebarlinkcolor": "#FFEEEE",
# "headbgcolor": "#FFF8FB",
#     "headtextcolor": "black",
# "headlinkcolor": "#660000",
# "footerbgcolor": "#880000",
#     "footertextcolor": "white",
# "codebgcolor": "#FFEEEE",
# }
html_theme_options = {
    'logo': 'images/cherrypy_logo_big.png',
    'github_user': project.lower(),
    'github_repo': project.lower(),
    'github_button': True,
    'github_banner': True,
    'github_type': 'star',
    'github_count': True,
    'travis_button': True,
    'codecov_button': True,
    # 'analytics_id': ...,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# html_style = 'cpdocmain.css'

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    'index': [
        'about.html', 'searchbox.html', 'navigation.html', 'python_2_eol.html',
    ],
    '**': [
        'about.html', 'searchbox.html', 'navigation.html', 'python_2_eol.html',
    ],
}

# Output file base name for HTML help builder.
htmlhelp_basename = 'CherryPydoc'


# -- Options for LaTeX output --------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author,
# documentclass [howto/manual]).
latex_documents = [
    (
        'index',
        'CherryPy.tex',
        'CherryPy Documentation',
        'CherryPy Team',
        'manual',
    ),
]


link_files = {
    '../CHANGES.rst': dict(
        using=dict(
            GH='https://github.com',
        ),
        replace=[
            dict(
                pattern=r'^(?m)((?P<scm_version>v?\d+(\.\d+){1,2}))\n[-=]+\n',
                with_scm='{text}\n{rev[timestamp]:%d %b %Y}\n',
            ),
        ],
    ),
}


# Ref: https://github.com/python-attrs/attrs/pull/571/files\
#      #diff-85987f48f1258d9ee486e3191495582dR82
default_role = 'any'


# -- Options for autodoc extension ---------------------------------------

autodoc_mock_imports = [
    'win32api',
    'win32con',
    'win32event',
    'win32service',
    'win32serviceutil',
]


# -- Options for apidoc extension ----------------------------------------

apidoc_excluded_paths = []
apidoc_extra_args = [
    '--implicit-namespaces',
    '--private',  # include “_private” modules
]
apidoc_module_dir = '../cherrypy'
apidoc_module_first = False
apidoc_output_dir = 'pkg'
apidoc_separate_modules = True
apidoc_toc_file = None
