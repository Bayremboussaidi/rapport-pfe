"""
Figure 2.3: Administrator Use Case Diagram - Final Version
Clean, organized layout with grouped functionality
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import os

def create_final_admin_usecase():
    """Generate the final Administrator Use Case Diagram"""
    
    fig, ax = plt.subplots(figsize=(16, 10))
    
    # Actor
    admin_box = FancyBboxPatch((1, 4.5), 2.5, 1.2,
                              boxstyle="round,pad=0.1",
                              facecolor='#E8F4FD', 
                              edgecolor='#1976D2', 
                              linewidth=3)
    ax.add_patch(admin_box)
    ax.text(2.25, 5.1, 'Administrator', ha='center', va='center', fontsize=12, weight='bold')
    
    # System boundary  
    system_boundary = FancyBboxPatch((5, 1), 13, 8,
                                   boxstyle="round,pad=0.2",
                                   facecolor='#F8F9FA', 
                                   edgecolor='#1976D2', 
                                   linewidth=3)
    ax.add_patch(system_boundary)
    ax.text(11.5, 8.5, 'Platform Administration', ha='center', va='center', 
            fontsize=14, weight='bold', color='#1976D2')
    
    # Organized groups
    groups = [
        {
            'title': 'User Management',
            'x': 6, 'y': 6.5, 'width': 3, 'height': 1.8,
            'cases': [('Manage Agencies', 7.5, 7.6), ('Manage Users', 7.5, 6.9)]
        },
        {
            'title': 'System Configuration',
            'x': 10, 'y': 6.5, 'width': 3, 'height': 1.8,
            'cases': [('Configure System', 11.5, 7.6), ('Manage Permissions', 11.5, 6.9)]
        },
        {
            'title': 'Analytics & Monitoring',
            'x': 14, 'y': 6.5, 'width': 3.5, 'height': 1.8,
            'cases': [('View Analytics', 15.75, 7.6), ('Monitor System', 15.75, 6.9)]
        },
        {
            'title': 'Content & Finance',
            'x': 8, 'y': 3.5, 'width': 6, 'height': 1.8,
            'cases': [('Moderate Content', 11, 4.6), ('View Revenue', 11, 4.1), ('Generate Reports', 11, 3.6)]
        }
    ]
    
    # Draw groups
    for group in groups:
        group_box = FancyBboxPatch((group['x'], group['y']), group['width'], group['height'],
                                  boxstyle="round,pad=0.15",
                                  facecolor='#FAFAFA', 
                                  edgecolor='#E0E0E0', 
                                  linewidth=1)
        ax.add_patch(group_box)
        
        ax.text(group['x'] + group['width']/2, group['y'] + group['height'] - 0.3, 
                group['title'], ha='center', va='center', fontsize=10, 
                weight='bold', color='#555', style='italic')
        
        for text, x, y in group['cases']:
            ellipse = patches.Ellipse((x, y), 2.6, 0.6, 
                                    facecolor='white', 
                                    edgecolor='#424242', 
                                    linewidth=1.5)
            ax.add_patch(ellipse)
            ax.text(x, y, text, ha='center', va='center', fontsize=9)
    
    # Clean organized connections
    ax.plot([3.5, 5], [5.1, 5.1], 'k-', linewidth=3, alpha=0.8)
    
    group_centers = [(7.5, 7.2), (11.5, 7.2), (15.75, 7.2), (11, 4.2)]
    for gx, gy in group_centers:
        ax.plot([5, gx], [5.1, gy], 'k--', linewidth=1.5, alpha=0.7)
        ax.plot(gx, gy, 'ko', markersize=4, alpha=0.7)
    
    ax.set_xlim(0, 19)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Figure 2.3: Administrator Use Case Diagram\nPlatform Management Operations', 
                fontsize=16, weight='bold', pad=20)
    
    plt.tight_layout()
    
    output_path = 'admin-usecase-diagram-final.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.savefig('../../../img/admin-usecase-diagram.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    
    plt.close()
    print(f"✅ Generated Figure 2.3: {output_path}")

if __name__ == "__main__":
    create_final_admin_usecase()