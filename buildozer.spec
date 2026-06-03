[app]

# (str) Title of your application
title = LexInvoice Pro

# (str) Package name
package.name = lexinvoicepro

# (str) Package domain (needed for android/ios packaging)
package.domain = com.ahmedosama

# (str) Source code where the main.py live
source.include_exts = py,png,jpg,kv,atlas,db

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy,reportlab

# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png

# (str) Presplash of the application
presplash.filename = %(source.dir)s/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Android API to use
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK to use
android.sdk = 23

# (str) Android NDK to use
android.ndk = 25b

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
android.ndk_path = 

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

[buildozer]

# (int) log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
