[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_pattern = assets/*.png,images/*.png

# (list) Source files to exclude (let it empty to exclude nothing)
#source.exclude_exts = spec

# (list) List of exclusion patterns using pattern matching
#source.exclude_pattern = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (list) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.recipename = ../../source/recipename

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (landscape, portrait, all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PYTHON_SCRIPT,NAME2:ENTRYPOINT_TO_PYTHON_SCRIPT2

#
# OSX Specific
#

#
# Author: Name/Organization to be displayed on the application about dialog
#
#osx.package.domain = org.kivy
#osx.sign.identity = 3rd Party Mac Developer Application: PyGame Developer (HX2AQWDXZ9)


[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
#bin_dir = ./bin

# (str) Path to build output (defaults to ./bin)
#build_dir = .buildozer

# (str) Dir where source files are located
source.dir = .
