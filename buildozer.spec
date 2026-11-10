[app]
title = Naruto App
package.name = narutoapp
package.domain = org.naruto.narutoapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_exts = spec
version = 0.1
requirements = python3,kivy,pillow
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.sdk = 33
android.ndk = 25b
android.gradle_dependencies =
android.add_gradle_repositories =
p4a.branch = v2024.01.21
android.archs = arm64-v8a
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0

[buildozer]
log_level = 2
warn_on_root = 1
