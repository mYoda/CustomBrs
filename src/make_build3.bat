::@echo off
ninja -C out/Release chrome setup
::.\SignUtils\signtool.exe sign /v /f PATH_TO_PFX /p PasswdToPfx /t http://timestamp.verisign.com/scripts/timestamp.dll .\out\Release\Setup.exe
ninja -C out/Release mini_installer
::.\SignUtils\signtool.exe sign /v /f PATH_TO_PFX /p PasswdToPfx /t http://timestamp.verisign.com/scripts/timestamp.dll .\out\Release\mini_installer.exe

::copy .\out\Release\mini_installer.exe ..\OUT_BUILD\