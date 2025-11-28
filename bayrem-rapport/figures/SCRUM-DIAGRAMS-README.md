# Scrum Diagrams and Charts

This folder contains Mermaid source files for Scrum-related diagrams used in the PFE report.

## Files

| File | Description | Output |
|------|-------------|--------|
| `scrum-process-flow.mmd` | Scrum methodology process diagram | `img/scrum-process-flow.png` |
| `scrum-team-structure.mmd` | Team roles and structure | `img/scrum-team-structure.png` |
| `project-burndown-chart.mmd` | Project-level burndown chart | `img/project-burndown-chart.png` |
| `velocity-chart.mmd` | Team velocity per sprint | `img/velocity-chart.png` |

## How to Generate PNG Images

### Option 1: Mermaid Live Editor (Recommended)
1. Go to https://mermaid.live
2. Paste the `.mmd` file contents
3. Export as PNG with transparent background
4. Save to `img/` folder with the appropriate name

### Option 2: Mermaid CLI
```bash
# Install mermaid-cli
npm install -g @mermaid-js/mermaid-cli

# Generate PNG
mmdc -i scrum-process-flow.mmd -o ../img/scrum-process-flow.png -b transparent
mmdc -i scrum-team-structure.mmd -o ../img/scrum-team-structure.png -b transparent
```

### Option 3: VS Code Extension
1. Install "Mermaid Markdown Syntax Highlighting" extension
2. Open `.mmd` file
3. Use preview and export to PNG

## Burndown & Velocity Charts

For the charts (`project-burndown-chart.mmd` and `velocity-chart.mmd`), you may get better results using:

### Excel/Google Sheets Method
Use this data to create charts:

**Burndown Data:**
| Sprint | Ideal Remaining | Actual Remaining |
|--------|-----------------|------------------|
| Start  | 210             | 210              |
| S1     | 183.75          | 186              |
| S2     | 157.5           | 158              |
| S3     | 131.25          | 127              |
| S4     | 105             | 103              |
| S5     | 78.75           | 86               |
| S6     | 52.5            | 55               |
| S7     | 26.25           | 34               |
| S8     | 0               | 0                |

**Velocity Data:**
| Sprint   | Story Points |
|----------|--------------|
| Sprint 1 | 24           |
| Sprint 2 | 28           |
| Sprint 3 | 31           |
| Sprint 4 | 24           |
| Sprint 5 | 17           |
| Sprint 6 | 31           |
| Sprint 7 | 21           |
| Sprint 8 | 34           |
| Average  | 26.25        |

## Required Images for Report

Make sure these images exist in `img/` folder:
- [ ] `scrum-process-flow.png`
- [ ] `scrum-team-structure.png`
- [ ] `project-burndown-chart.png`
- [ ] `velocity-chart.png`
