::@echo off
set GYP_GENERATORS=ninja
set GYP_DEFINES=branding=Chromium buildtype=Official fastbuild=1
gclient runhooks --force
