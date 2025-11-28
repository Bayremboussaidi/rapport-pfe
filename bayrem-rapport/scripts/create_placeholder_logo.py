"""
Logo placeholder generator for technology icons
Creates standardized placeholder images for the architecture diagram
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

def create_logo_placeholder(size=64):
    """Create a simple placeholder logo"""
    fig, ax = plt.subplots(1, 1, figsize=(1, 1))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    # Simple placeholder design
    circle = plt.Circle((0.5, 0.5), 0.4, facecolor='#E0E0E0', 
                       edgecolor='#BDBDBD', linewidth=2)
    ax.add_patch(circle)
    ax.text(0.5, 0.5, 'LOGO', ha='center', va='center', 
            fontsize=8, fontweight='bold', color='#757575')
    
    # Save
    os.makedirs('../assets', exist_ok=True)
    fig.savefig(f'../assets/logo-placeholder.png', dpi=size, 
                bbox_inches='tight', facecolor='white', 
                edgecolor='none', pad_inches=0, transparent=True)
    plt.close()

if __name__ == "__main__":
    create_logo_placeholder()
    print("📁 Created: ../assets/logo-placeholder.png")