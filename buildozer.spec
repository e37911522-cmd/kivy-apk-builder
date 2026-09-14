[app]
title = My Application
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait

# Автоматическое принятие лицензий SDK
android.accept_sdk_license = True

# Версии API
android.api = 33
android.minapi = 24

# Явное указание путей к системным SDK и NDK из GitHub Actions
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724

[buildozer]
log_level = 2
warn_on_root = 1
