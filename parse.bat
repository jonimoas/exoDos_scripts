@echo off
set n=^&echo.
V:
for /D %%G in ("V:\exodos\eXoDOS\eXo\eXoDOS\!dos\*") do (
  echo "%%~nxG"
  for %%F in ("%%G\*.bat") do (
    if not "%%~nxF" equ "install.bat" ( 
      if not "%%~nxF" equ "exception.bat" ( 
        echo V:%n%cd "V:\exodos\eXoDOS\eXo\eXoDOS\!dos\%%~nxG"%n%call "%%~nxF") > V:\exodos\eXoDOS\eXo\eXoDOS\!dos\%%~nxF
      )
    )
  )
)
pause