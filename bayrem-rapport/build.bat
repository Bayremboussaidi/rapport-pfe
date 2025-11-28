@echo off
REM LaTeX Build Script for bayrem-rapport (Windows Version)
REM This script compiles the LaTeX document and manages auxiliary files

echo 🚀 Starting LaTeX compilation...

REM Change to script directory
cd /d "%~dp0"

REM Check if main.tex exists
if not exist "main.tex" (
    echo ❌ Error: main.tex not found in current directory
    pause
    exit /b 1
)

REM Clean previous compilation files
echo 🧹 Cleaning auxiliary files...
del *.aux *.log *.toc *.lof *.lot *.idx *.bbl *.blg *.mtc* *.out *.fls *.fdb_latexmk *.maf *.run.xml >nul 2>&1
del tpl\*.aux >nul 2>&1

echo 📝 First LaTeX pass...
pdflatex -interaction=nonstopmode main.tex >nul 2>&1

echo 📝 Second LaTeX pass (for TOC and references)...
pdflatex -interaction=nonstopmode main.tex >nul 2>&1

REM Check if PDF was created
if exist "main.pdf" (
    echo ✅ Compilation successful! PDF generated: main.pdf
    
    REM Create output directory if it doesn't exist
    if not exist "output" mkdir output
    
    REM Get PDF info before moving
    for %%I in (main.pdf) do set filesize=%%~zI
    
    REM Move PDF to output directory
    move main.pdf output\ >nul
    echo 📄 PDF moved to output\main.pdf
    
    echo 📊 Document info:
    echo    - Size: %filesize% bytes
    
    echo.
    echo What would you like to do with compilation files?
    echo 1^) Move to build\ directory ^(recommended^)
    echo 2^) Delete them
    echo 3^) Keep them in current directory
    
    set /p choice="Choose option (1-3): "
    
    if "%choice%"=="1" (
        echo 📁 Organizing compilation files...
        if not exist "build" mkdir build
        move *.aux *.log *.toc *.lof *.lot *.idx *.bbl *.blg *.mtc* *.out *.fls *.fdb_latexmk *.maf *.run.xml build\ >nul 2>&1
        move tpl\*.aux build\ >nul 2>&1
        echo 📄 Compilation files moved to build\ directory
    ) else if "%choice%"=="2" (
        del *.aux *.log *.toc *.lof *.lot *.idx *.bbl *.blg *.mtc* *.out *.fls *.fdb_latexmk *.maf *.run.xml >nul 2>&1
        del tpl\*.aux >nul 2>&1
        echo 🗑️ Auxiliary files deleted
    ) else if "%choice%"=="3" (
        echo 📂 Files kept in current directory
    ) else (
        echo ❓ Invalid choice. Files kept in current directory
    )
    
) else (
    echo ❌ Compilation failed! PDF not generated.
    echo Check the log file for errors:
    echo    type main.log ^| more
    pause
    exit /b 1
)

echo.
echo 🎉 Build process completed!
echo 📄 Your document is ready: output\main.pdf
pause