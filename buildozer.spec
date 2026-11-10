[app]
title = Naruto App
package.name = narutoapp
package.domain = org.naruto.narutoapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_exts = spec
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
