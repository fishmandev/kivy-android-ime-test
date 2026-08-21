[app]
title = Kivy Keyboard Test
package.name = kivykeyboardtest
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

# A modern target API. Buildozer/python-for-android will install SDK components
# during the first build if they are not already present.
android.api = 35
android.minapi = 24
android.archs = arm64-v8a

# Keep the test minimal; no special permissions are required.
android.permissions =

# Console logging is useful while testing with adb logcat.
android.logcat_filters = *:S python:D

[buildozer]
log_level = 2
warn_on_root = 1
