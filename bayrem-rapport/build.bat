@echo off
echo ========================================
echo Building MyLoc PFE Report...
echo ========================================

:: First pass - generate aux files
pdflatex -interaction=nonstopmode main.tex

:: Run biber for bibliography
biber main

:: Second pass - resolve references
pdflatex -interaction=nonstopmode main.tex

:: Third pass - finalize
pdflatex -interaction=nonstopmode main.tex

echo ========================================
echo Build complete! Check main.pdf
echo ========================================
pause
