#!/bin/bash
# Generate all organized use case diagrams using Mermaid CLI

echo "🎯 Generating Organized Use Case Diagrams with Mermaid..."

# Function to generate diagram
generate_diagram() {
    local figure_dir=$1
    local mmd_file=$2
    local output_file=$3
    local main_output=$4
    
    echo "📋 Processing $figure_dir..."
    
    cd "figures/$figure_dir"
    
    # Check if mmdc is available
    if command -v mmdc &> /dev/null; then
        # Generate with high quality settings
        mmdc -i "$mmd_file" -o "$output_file" \
             --width 1600 --height 1200 \
             --scale 2 \
             --backgroundColor white \
             --configFile ../../mermaid-config.json 2>/dev/null || \
        mmdc -i "$mmd_file" -o "$output_file" \
             --width 1600 --height 1200 \
             --scale 2 \
             --backgroundColor white
        
        if [ $? -eq 0 ]; then
            echo "✅ Generated: $output_file"
            # Copy to main img directory
            cp "$output_file" "../../img/$main_output"
            echo "✅ Updated: img/$main_output"
        else
            echo "❌ Failed to generate $output_file"
        fi
    else
        echo "⚠️ Mermaid CLI not found. Install with: npm install -g @mermaid-js/mermaid-cli"
        echo "📝 Manual generation needed for: $mmd_file"
    fi
    
    cd ../..
}

# Generate all diagrams
generate_diagram "figure-2.1-customer-usecase" "customer-usecase.mmd" "customer-usecase-diagram.png" "customer-usecase-diagram.png"
generate_diagram "figure-2.2-agency-usecase" "agency-usecase.mmd" "agency-usecase-diagram.png" "agency-usecase-diagram.png"  
generate_diagram "figure-2.3-admin-usecase" "admin-usecase.mmd" "admin-usecase-diagram.png" "admin-usecase-diagram.png"

echo ""
echo "🎉 All organized use case diagrams completed!"
echo "📋 Features:"
echo "- ✅ Clean Mermaid layout with grouped functionality"
echo "- ✅ Professional UML styling"
echo "- ✅ Organized connection patterns (no chaos)"
echo "- ✅ High resolution output (scale 2, 1600x1200)"
echo "- ✅ Ready for LaTeX integration"
echo ""
echo "💡 If Mermaid CLI is not installed:"
echo "   npm install -g @mermaid-js/mermaid-cli"