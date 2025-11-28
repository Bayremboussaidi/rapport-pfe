#!/bin/bash
# Clean script for LaTeX project
# Removes all auxiliary files generated during compilation

echo "🧹 Cleaning LaTeX auxiliary files..."

# Set working directory to script location
cd "$(dirname "$0")"

# Remove auxiliary files
rm -f *.aux *.log *.toc *.lof *.lot *.idx *.bbl *.blg *.mtc* *.out *.fls *.fdb_latexmk *.maf *.run.xml
rm -f tpl/*.aux
rm -rf build/

# Optionally clean output (uncomment if needed)
# rm -rf output/

echo "✅ Clean completed! All auxiliary files removed."
echo "📄 Source files (.tex) and images preserved."

# List remaining important files
echo ""
echo "📂 Remaining files:"
ls -la *.tex *.bib *.py *.sh *.bat *.md 2>/dev/null || echo "   (No additional files to show)"
echo ""
echo "📁 Directory structure:"
ls -la output/ figures/ 2>/dev/null || echo "   (Directories may be empty)"