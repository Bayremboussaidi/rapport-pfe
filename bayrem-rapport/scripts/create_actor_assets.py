"""
Create stick figure assets for UML diagrams
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

def create_stick_figure_asset(name, color='black', size=100):
    """Create a stick figure PNG asset"""
    
    fig, ax = plt.subplots(1, 1, figsize=(2, 2))
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Head (circle)
    head = plt.Circle((0, 0.5), 0.2, fill=False, color=color, linewidth=3)
    ax.add_patch(head)
    
    # Body (vertical line)
    ax.plot([0, 0], [0.3, -0.3], color=color, linewidth=3)
    
    # Arms (horizontal line)
    ax.plot([-0.3, 0.3], [0.1, 0.1], color=color, linewidth=3)
    
    # Legs (diagonal lines)
    ax.plot([0, -0.2], [-0.3, -0.7], color=color, linewidth=3)
    ax.plot([0, 0.2], [-0.3, -0.7], color=color, linewidth=3)
    
    # Save as transparent PNG
    os.makedirs('../assets/icons', exist_ok=True)
    fig.patch.set_alpha(0)  # Make background transparent
    fig.savefig(f'../assets/icons/{name}.png', dpi=300, bbox_inches='tight', 
               transparent=True, pad_inches=0)
    plt.close(fig)
    print(f"✅ Created stick figure: {name}.png")

def create_all_actors():
    """Create all actor stick figures"""
    
    actors = [
        ('customer', 'black'),
        ('visitor', 'black'), 
        ('agency', 'black'),
        ('admin', 'black'),
        ('system', 'black')
    ]
    
    for name, color in actors:
        create_stick_figure_asset(name, color)

if __name__ == "__main__":
    print("🎨 Creating UML Actor Assets...")
    create_all_actors()
    print("\n✅ All stick figure assets created!")
    print("📁 Location: assets/icons/")
    print("🔧 Ready for Mermaid integration")