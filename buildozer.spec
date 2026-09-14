[app]

# (str) Title of your application
title = My App

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (list) Source files to include (let empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of directory to include (let empty to include all)
source.include_dirs = 

# (list) List of exclusions to pack
source.exclude_exts = spec

# (list) List of exclusion patterns
source.exclude_patterns = license, images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (list) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.dir = ../../../kivy

# (list) Permissions
#android.permissions = INTERNET

# (str) Architectural to build for, options: armeabi-v7a, arm64-v8a, x86, x86_64
# Оставляем только arm64-v8a для стабильности сборки
android.archs = arm64-v8a

# (list) Bootstrap to use for android builds
# p4a bootstrap to use: sdl2, webview
# p4a.bootstrap = sdl2

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 24

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --public storage (False)
# android.private_storage = True

# (str) Supported orientations (landscape, portrait, all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color
# android.presplash_color = #FFFFFF

# (string) Icon background color
# android.icon_background_color = #FFFFFF


[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1