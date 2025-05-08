import os
import sys
sys.path.insert(0, os.path.abspath('..'))



project = 'Ultrasound Processing'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.viewcode', 'sphinx.ext.githubpages']
exclude_patterns = []
html_theme = 'sphinx_rtd_theme' #sphinx_rtd_theme - lehet hogy külön kell telepíteni
