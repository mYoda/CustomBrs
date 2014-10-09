Instructions
1. pull all code from repo...
2. make change the PATH variable in system - add path to the "depot_tools" in current repo.
3. run /src/make_build1.bat. In this step, all tools for build will be installed on your computer
4. run /src/make_build2.bat. All project will be prepare to Release-mode
5. run /src/make_build3.bat. Before running you must edit this batch-file. Please add "PATH_TO_PFX" and PSWD_TO_PFX for signing some binaries after build
6. If build was successfull - you can try mini_installer in OUT_BUILD folder.