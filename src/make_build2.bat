::@echo off
set GYP_GENERATORS=ninja
set GYP_DEFINES=branding=Chromium buildtype=Official fastbuild=1
python build\gyp_chromium -Dbranding=Chromium -Dbuildtype=Official -Dfastbuild=1