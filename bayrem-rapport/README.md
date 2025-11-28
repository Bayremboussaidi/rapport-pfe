# LaTeX Project: Bayrem Rapport

This is a LaTeX document project with automated build scripts for easy compilation and workspace management.

Based on ISI's LaTeX template for internship reports, enhanced with automated build system.

## Project Structure

```
├── main.tex              # Main document file
├── global_config.tex     # Document configuration
├── biblio.bib           # Bibliography database
├── sections/             # All content sections (chapters, intro, etc.)
├── img/                 # Legacy images directory  
├── figures/             # New images and figures directory
├── tpl/                 # Templates and class files
├── build.sh/.bat        # Build scripts (Unix/Windows)
├── clean.sh             # Clean script (Unix)
├── user_feedback.py     # User feedback script
├── output/              # Generated PDF files
└── build/               # Compilation files (auto-generated)
```

## Quick Start

### Option 1: Using Build Script (Recommended)

#### On Unix/Linux/macOS/WSL:
```bash
./build.sh
```

#### On Windows:
```cmd
build.bat
```

The build script will:
- Clean previous compilation files
- Run LaTeX compilation (2 passes)
- Generate PDF with proper TOC and references
- Organize auxiliary files into `build/` directory

### Option 2: Manual Compilation

```bash
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex  # Second pass for TOC/references
```

## Output

The compilation generates:
- **output/main.pdf** - The final document (45 pages)
- **build/** - Directory containing auxiliary files (.aux, .toc, .log, etc.)
- **figures/** - Directory for storing images and diagrams

## Cleaning

To remove all auxiliary files:
```bash
./clean.sh
```

## Features

- ✅ Automated two-pass compilation
- ✅ Table of contents generation
- ✅ List of figures and tables
- ✅ Bibliography support
- ✅ Cross-references
- ✅ Multi-language support (French, English, Arabic)
- ✅ Custom ISI PFE class
- ✅ Organized file management

## Known Issues

- **enumitem package conflicts**: The document uses both `enumitem` and `datatool` packages which may cause some warnings during compilation. These are cosmetic and don't affect the final PDF output.
- **minitoc warnings**: Some warnings about package load order are expected and don't affect functionality.

## User Feedback

After compilation, run the feedback script:
```bash
python user_feedback.py
```

## Requirements

- LaTeX distribution (MiKTeX, TeX Live, etc.)
- Python (for feedback script)
- Standard LaTeX packages (included in most distributions)

---

## Original Template Credits

```
%================================================================%  
% Copyright (C) ISI - All Rights Reserved                        %  
% Proprietary                                                    %  
% Written by Med Hossam <med.hossam@gmail.com>, April 2016       %  
% @author: HEDHILI Med Houssemeddine                             %  
% @linkedin: http://tn.linkedin.com/in/medhossam                 %  
%                                                                %  
% Edited by Mustapha <mustapha.sahli.1993@gmail.com>, Nov 2017   %  
% @collaborator: SAHLI Mustapha                                  %  
% @linkedin: http://tn.linkedin.com/in/mustapha-sahli            %  
%================================================================%  
```

*Generated PDF: output/main.pdf (45 pages, ~426KB)*
