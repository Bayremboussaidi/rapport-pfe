#!/bin/bash
# LaTeX Build Script for bayrem-rapport
# This script compiles the LaTeX document and manages auxiliary files

echo "🚀 Starting LaTeX compilation..."

# Set working directory to script location
cd "$(dirname "$0")"

# Function to clean auxiliary files
clean_aux_files() {
    echo "🧹 Cleaning auxiliary files..."
    rm -f *.aux *.log *.toc *.lof *.lot *.idx *.bbl *.blg *.mtc* *.out *.fls *.fdb_latexmk *.maf *.run.xml 2>/dev/null
    rm -f tpl/*.aux 2>/dev/null
}

# Function to move compilation files to a separate directory
organize_files() {
    echo "📁 Organizing compilation files..."
    mkdir -p build
    mv *.aux *.log *.toc *.lof *.lot *.idx *.bbl *.blg *.mtc* *.out *.fls *.fdb_latexmk *.maf *.run.xml build/ 2>/dev/null
    mv tpl/*.aux build/ 2>/dev/null
    echo "📄 Compilation files moved to build/ directory"
}

# Check if main.tex exists
if [ ! -f "main.tex" ]; then
    echo "❌ Error: main.tex not found in current directory"
    exit 1
fi

# Clean previous compilation files
clean_aux_files

echo "📝 First LaTeX pass..."
pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1

if [ $? -ne 0 ]; then
    echo "⚠️  Warning: First pass completed with errors (this is normal)"
fi

echo "📝 Second LaTeX pass (for TOC and references)..."
pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1

if [ $? -ne 0 ]; then
    echo "⚠️  Warning: Second pass completed with errors (this is normal due to enumitem package conflicts)"
fi

# Check if PDF was created
if [ -f "main.pdf" ]; then
    echo "✅ Compilation successful! PDF generated: main.pdf"
    
    # Create output directory if it doesn't exist
    mkdir -p output
    
    # Get PDF info before moving
    pages=$(pdfinfo main.pdf 2>/dev/null | grep Pages | awk '{print $2}')
    size=$(ls -lh main.pdf | awk '{print $5}')
    
    # Move PDF to output directory
    mv main.pdf output/
    echo "📄 PDF moved to output/main.pdf"
    
    echo "📊 Document info:"
    echo "   - Pages: ${pages:-Unknown}"
    echo "   - Size: ${size:-Unknown}"
    
    # Ask user what to do with auxiliary files
    echo ""
    echo "What would you like to do with compilation files?"
    echo "1) Move to build/ directory (recommended)"
    echo "2) Delete them"
    echo "3) Keep them in current directory"
    
    read -p "Choose option (1-3): " choice
    
    case $choice in
        1)
            organize_files
            ;;
        2)
            clean_aux_files
            echo "🗑️  Auxiliary files deleted"
            ;;
        3)
            echo "📂 Files kept in current directory"
            ;;
        *)
            echo "❓ Invalid choice. Files kept in current directory"
            ;;
    esac
    
else
    echo "❌ Compilation failed! PDF not generated."
    echo "Check the log file for errors:"
    echo "   tail -n 50 main.log"
    exit 1
fi

echo ""
echo "🎉 Build process completed!"
echo "📄 Your document is ready: output/main.pdf"