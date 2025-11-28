# Figures Directory

This directory is intended for storing figures, diagrams, and images used in the LaTeX document.

## Usage

Place your image files here and reference them in your LaTeX documents using:

```latex
\includegraphics[width=\textwidth]{figures/your-image.png}
```

## Supported Formats

- PDF (recommended for vector graphics)
- PNG (for screenshots and photos)
- JPG/JPEG (for photos)
- EPS (Encapsulated PostScript)
- SVG (with inkscape package)

## Organization Suggestions

```
figures/
├── diagrams/       # System diagrams, flowcharts
├── screenshots/    # Application screenshots  
├── charts/         # Graphs and statistical charts
├── logos/          # Company and institutional logos
└── photos/         # Photographs and pictures
```

## Notes

- Keep image file names descriptive and without spaces
- Use lowercase with hyphens: `user-interface-mockup.png`
- Optimize image sizes for faster compilation
- Vector formats (PDF, SVG) scale better than raster formats