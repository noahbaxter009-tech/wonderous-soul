[app]
# Wonderous Soul Android build configuration
# Build with: buildozer -v android debug

# (str) Title of your application
title = Wonderous Soul

# (str) Package name
package.name = wonderoussoul

# (str) Package domain (used as part of the package name)
package.domain = org.wonderoussoul

# (str) Source code where main.py lives
source.dir = .

# (str) Application version
version = 1.0.0

# (str) Application requirements
requirements = python3,pygame

# (str) Supported orientation (landscape is best for the 960x544 game)
orientation = landscape

# (bool) Fullscreen mode
fullscreen = 1

# (str) Presplash image (leave blank for none)
presplash.filename =

# (str) Icon filename
icon.filename =

# (str) Supported architectures
android.archs = arm64-v8a, armeabi-v7a

# (str) Android API / SDK settings
android.api = 35
android.minapi = 23
android.ndk = 27b

# (str) Python-for-Android bootstrap
p4a.bootstrap = sdl2

# (bool) Android permissions
android.permissions = VIBRATE

# (str) Extra source/include extensions
source.include_exts = py,txt,png,jpg,jpeg,wav,ogg,mp3

# (bool) Keep the app fullscreen and prevent accidental resize behavior
android.allow_backup = False

# (str) Log level
log_level = 2

[buildozer]
# (int) Log level (0 = error only, 1 = warning, 2 = info, 3 = debug)
log_level = 2
warn_on_root = 1
