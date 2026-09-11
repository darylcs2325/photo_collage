[app]
title = Photo Collage Creator
package.name = photocollage
package.domain = org.app_chayo

source.dir = .
source.include_exts = py,png,jpg,ttf

version = 0.1

requirements = python3,flet,pillow,python-dotenv

orientation = portrait
fullscreen = 0
android.permissions = INTERNET,CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE
android.features = android.hardware.camera

[buildozer]
log_level = 2
warn_on_root = 1
