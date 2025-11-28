# 📝 LaTeX Report Compilation Guide

Simple setup to compile this PFE report using LaTeX.

## 🔧 LaTeX Distribution Required

**Install TeX Live (recommended):**
- **Windows:** Download from [tug.org/texlive](https://www.tug.org/texlive/) - Select "Full installation" 
- **Linux:** `sudo apt-get install texlive-full`
- **macOS:** `brew install --cask mactex`

**Alternative - MiKTeX (Windows only):**
- Download from [miktex.org](https://miktex.org/download)
- Enable automatic package installation during setup

## 📦 Required LaTeX Packages

The following packages are used (auto-installed with full distributions):

### Core Packages:
- `babel` - French language support
- `inputenc`, `fontenc` - UTF-8 and font encoding  
- `geometry` - Page layout and margins
- `graphicx` - Image inclusion support
- `hyperref` - PDF hyperlinks and bookmarks

### Formatting Packages:
- `enumitem` - Enhanced lists
- `fancyhdr` - Custom headers/footers
- `titlesec` - Section title formatting
- `caption`, `subcaption` - Figure captions
- `xcolor` - Color support

### Math & Code:
- `amsmath`, `amsfonts` - Mathematical typesetting
- `listings` - Code syntax highlighting
- `algorithm2e` - Algorithm pseudocode

### Tables:
- `longtabu` - Advanced table layouts

## 🚀 Compilation

### Using Build Script (Recommended):
```bash
./build.sh     # Linux/macOS
build.bat      # Windows
```

### Manual Compilation:
```bash
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex  
pdflatex -interaction=nonstopmode main.tex
```

## 📄 Output
- **Result:** `output/main.pdf` (47 pages)
- **Build artifacts:** Moved to `build/` directory
- **Images:** Pre-generated in `img/` directory

## 🛠️ Troubleshooting

**Package not found errors:**
- TeX Live: `tlmgr update --self --all`
- MiKTeX: Enable auto-install in MiKTeX Console

**Missing fonts/encoding issues:**
- Ensure full LaTeX installation (not basic)
- Install language packs for French support

**Bibliography not appearing:**  
- Run the 4-step compilation sequence above
- Check `biblio.bib` file exists