

from distutils.core import setup 
import py2exe 
 
setup(name="ProductEngineer Pallete", 
 version="1.0", 
 description="Palleta de archivos relevantes", 
 author="Adrian Gonzalez", 
 author_email="Adrian.Gonzalez@us.bosch.com", 
 url="ninguna", 
 license="opensource", 
 scripts=["ShortcutsProductEngineering.py", "mrrLinksdefinition.py"],
 console=["ShortcutsProductEngineering.py", "mrrLinksdefinition.py"],
 options={"py2exe": {"bundle_files": 1}}, 
 zipfile=None,
)