# -*- coding: utf-8 -*-
#
# Spatial methods for neuroimaging documentation build configuration file, created by
# sphinx-quickstart on Tue Aug 23 15:22:22 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import sphinx_rtd_theme
sys.path.insert(0, os.path.abspath('../../pcntoolkit'))
sys.path.insert(0, os.path.abspath('../../pcntoolkit/dataio'))
sys.path.insert(0, os.path.abspath('../../pcntoolkit/model'))
sys.path.insert(0, os.path.abspath('../../pcntoolkit/normative_model'))
sys.path.insert(0, os.path.abspath('../../pcntoolkit/utils'))



# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx_tabs.tabs', 
              'sphinx.ext.autodoc',
              'sphinx.ext.imgmath',
              'sphinx.ext.githubpages',
              'sphinx.ext.autosectionlabel', 
              'sphinx.ext.autosummary',
              'sphinx_automodapi.automodapi',
              #'sphinx.ext.doctest',
              #'sphinx.ext.intersphinx',
              #'sphinx.ext.mathjax',
              'sphinx.ext.napoleon',
              'sphinx.ext.viewcode',
              #'sphinxarg.ext',
              ]

autosummary_generate = True
autodoc_default_options = {'members': True, 'inherited-members': True}
numpydoc_show_class_members = False
autoclass_content = "class"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

highlight_language ='none'

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Predictive Clinical Neuroscience Toolkit'
copyright = u'2020, Andre F. Marquand'
author = u'Saige Rutherford, Andre F. Marquand'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'0.20'
# The full version, including alpha/beta/rc tags.
release = u'0.20'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_options = { 'style_nav_header_background': '#1E90FF'}


pygments_style = 'sphinx'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['pages/_templates']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['pages/_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = ['pages/css/pcntoolkit.css', 
                  'pages/css/pcntoolkit_nomaxwidth.css']

# add custom files that are stored in _static
def setup(app):
   app.add_css_file('pages/css/pcntoolkit_tabs.css')

# add logo
html_logo = "pcn-logo.png"
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}

# Output file base name for HTML help builder.
htmlhelp_basename = 'PCNtoolkitdoc'
