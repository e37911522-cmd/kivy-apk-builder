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

# Фиксация рабочих версий API и NDK для стабильной сборки
android.api = 33
android.minapi = 24
android.ndk = 25b
android.sdk = 31

[buildozer]
log_level = 2
warn_on_root = 1
