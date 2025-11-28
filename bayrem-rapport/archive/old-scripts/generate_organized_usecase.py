"""
Generate Organized Use Case Diagrams with Clean Serial Bus Layout
Using matplotlib to render organized Mermaid structure  
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np

def create_organized_customer_diagram():
    """Create Customer Use Case with organized, grouped layout"""
    
    fig, ax = plt.subplots(figsize=(18, 12))
    
    # Actors on left side (vertical bus)
    customer_box = FancyBboxPatch((1, 8), 2.5, 1.2,
                                 boxstyle="round,pad=0.1",
                                 facecolor='#E8F4FD', 
                                 edgecolor='#1976D2', 
                                 linewidth=3)
    ax.add_patch(customer_box)
    ax.text(2.25, 8.6, '👤 Customer', ha='center', va='center', fontsize=12, weight='bold')
    
    visitor_box = FancyBboxPatch((1, 5), 2.5, 1.2,
                                boxstyle="round,pad=0.1",
                                facecolor='#E8F4FD', 
                                edgecolor='#1976D2', 
                                linewidth=3)
    ax.add_patch(visitor_box)
    ax.text(2.25, 5.6, '👤 Visitor', ha='center', va='center', fontsize=12, weight='bold')
    
    # System boundary
    system_boundary = FancyBboxPatch((5, 1), 16, 11,
                                   boxstyle="round,pad=0.2",
                                   facecolor='#F8F9FA', 
                                   edgecolor='#1976D2', 
                                   linewidth=3)
    ax.add_patch(system_boundary)
    ax.text(13, 11.5, '🏢 Car Rental Platform', ha='center', va='center', 
            fontsize=14, weight='bold', color='#1976D2')
    
    # Organized groups (horizontal serial layout)
    groups = [
        # Group 1: Authentication (left)
        {
            'title': 'Authentication',
            'x': 6, 'y': 9, 'width': 3, 'height': 2,
            'cases': [('🔐 Login', 7.5, 10.3), ('📝 Register', 7.5, 9.7), ('👤 Profile', 7.5, 9.1)]
        },
        # Group 2: Vehicle Browsing  
        {
            'title': 'Vehicle Browsing',
            'x': 10, 'y': 9, 'width': 3, 'height': 2,
            'cases': [('🚗 Browse', 11.5, 10.3), ('🔍 Search', 11.5, 9.7), ('📅 Check', 11.5, 9.1)]
        },
        # Group 3: Booking Process
        {
            'title': 'Booking Process', 
            'x': 14, 'y': 9, 'width': 3, 'height': 2,
            'cases': [('📋 Book', 15.5, 10.3), ('💳 Payment', 15.5, 9.7), ('📄 Contract', 15.5, 9.1)]
        },
        # Group 4: Management
        {
            'title': 'Booking Management',
            'x': 18, 'y': 9, 'width': 2.5, 'height': 2,
            'cases': [('📊 View', 19.25, 10.1), ('✏️ Modify', 19.25, 9.5)]
        },
        # Group 5: Communication (bottom row)
        {
            'title': 'Communication',
            'x': 6, 'y': 5.5, 'width': 4, 'height': 2,
            'cases': [('💬 Chat', 7.5, 6.8), ('🤖 Chatbot', 8.5, 6.8), ('🔔 Notifications', 8, 6.2)]
        },
        # Group 6: Content
        {
            'title': 'Content & Social',
            'x': 11, 'y': 5.5, 'width': 4, 'height': 2,
            'cases': [('📰 Blog', 12.5, 6.8), ('💭 Comments', 13.5, 6.8), ('👥 Follow', 13, 6.2)]
        }
    ]
    
    # Draw groups and use cases
    for group in groups:
        # Group boundary
        group_box = FancyBboxPatch((group['x'], group['y']), group['width'], group['height'],
                                  boxstyle="round,pad=0.1",
                                  facecolor='#FAFAFA', 
                                  edgecolor='#BDBDBD', 
                                  linewidth=1)
        ax.add_patch(group_box)
        
        # Group title
        ax.text(group['x'] + group['width']/2, group['y'] + group['height'] - 0.2, 
                group['title'], ha='center', va='center', fontsize=9, 
                weight='bold', color='#666')
        
        # Use cases within group
        for text, x, y in group['cases']:
            ellipse = patches.Ellipse((x, y), 1.5, 0.5, 
                                    facecolor='white', 
                                    edgecolor='#424242', 
                                    linewidth=1.5)
            ax.add_patch(ellipse)
            ax.text(x, y, text, ha='center', va='center', fontsize=8)
    
    # Organized connection lines (serial bus approach)
    # Main bus line from Customer
    ax.plot([3.5, 5], [8.6, 8.6], 'k-', linewidth=2, alpha=0.7)  # Customer main line
    
    # Branch lines to each group (organized, no chaos)
    group_centers = [(7.5, 10), (11.5, 10), (15.5, 10), (19.25, 10), (8, 6.5), (13, 6.5)]
    
    for i, (gx, gy) in enumerate(group_centers):
        if i < 4:  # Top row groups
            ax.plot([5, gx], [8.6, gy], 'k--', linewidth=1, alpha=0.6)
        else:  # Bottom row groups  
            ax.plot([5, gx], [8.6, gy], 'k--', linewidth=1, alpha=0.6)
    
    # Visitor connections (limited, organized)
    ax.plot([3.5, 7.5], [5.6, 9.7], 'k--', linewidth=1, alpha=0.5)  # Register
    ax.plot([3.5, 11.5], [5.6, 10.3], 'k--', linewidth=1, alpha=0.5)  # Browse
    ax.plot([3.5, 8.5], [5.6, 6.8], 'k--', linewidth=1, alpha=0.5)  # Chatbot
    
    # Include relationships (within groups - clean arrows)
    ax.annotate('', xy=(7.5, 9.1), xytext=(7.5, 10.3), 
                arrowprops=dict(arrowstyle='->', color='#1976D2', lw=2))
    ax.text(8.2, 9.7, 'includes', fontsize=7, color='#1976D2')
    
    ax.set_xlim(0, 22)
    ax.set_ylim(0, 13)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Customer Use Case Diagram - Organized Layout', 
                fontsize=16, weight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('../img/customer-usecase-diagram.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()

def create_organized_agency_diagram():
    """Create Agency Use Case with organized layout"""
    
    fig, ax = plt.subplots(figsize=(16, 10))
    
    # Actor
    agency_box = FancyBboxPatch((1, 4.5), 2.5, 1.2,
                               boxstyle="round,pad=0.1",
                               facecolor='#E8F4FD', 
                               edgecolor='#1976D2', 
                               linewidth=3)
    ax.add_patch(agency_box)
    ax.text(2.25, 5.1, '👤 Agency', ha='center', va='center', fontsize=12, weight='bold')
    
    # System boundary
    system_boundary = FancyBboxPatch((5, 1), 13, 8,
                                   boxstyle="round,pad=0.2",
                                   facecolor='#F8F9FA', 
                                   edgecolor='#1976D2', 
                                   linewidth=3)
    ax.add_patch(system_boundary)
    ax.text(11.5, 8.5, '🏢 Agency Management System', ha='center', va='center', 
            fontsize=14, weight='bold', color='#1976D2')
    
    # Organized groups
    groups = [
        {
            'title': 'Profile & Auth',
            'x': 6, 'y': 6.5, 'width': 3, 'height': 1.5,
            'cases': [('🔐 Login', 7.5, 7.5), ('👤 Profile', 7.5, 6.9)]
        },
        {
            'title': 'Vehicle Management',
            'x': 10, 'y': 6.5, 'width': 3.5, 'height': 1.5,
            'cases': [('➕ Add', 11, 7.5), ('✏️ Edit', 12, 7.5), ('💰 Price', 12.5, 6.9)]
        },
        {
            'title': 'Request Handling',
            'x': 14.5, 'y': 6.5, 'width': 3, 'height': 1.5,
            'cases': [('📋 View', 16, 7.5), ('✅ Accept', 16, 6.9)]
        },
        {
            'title': 'Communication',
            'x': 8, 'y': 3.5, 'width': 4, 'height': 1.5,
            'cases': [('💬 Chat', 9.5, 4.5), ('📊 Reports', 10.5, 4.5), ('🔔 Notify', 10, 3.9)]
        }
    ]
    
    # Draw groups
    for group in groups:
        group_box = FancyBboxPatch((group['x'], group['y']), group['width'], group['height'],
                                  boxstyle="round,pad=0.1",
                                  facecolor='#FAFAFA', 
                                  edgecolor='#BDBDBD', 
                                  linewidth=1)
        ax.add_patch(group_box)
        
        ax.text(group['x'] + group['width']/2, group['y'] + group['height'] - 0.2, 
                group['title'], ha='center', va='center', fontsize=9, 
                weight='bold', color='#666')
        
        for text, x, y in group['cases']:
            ellipse = patches.Ellipse((x, y), 1.4, 0.45, 
                                    facecolor='white', 
                                    edgecolor='#424242', 
                                    linewidth=1.5)
            ax.add_patch(ellipse)
            ax.text(x, y, text, ha='center', va='center', fontsize=8)
    
    # Clean organized connections
    ax.plot([3.5, 5], [5.1, 5.1], 'k-', linewidth=2, alpha=0.7)
    
    # Branch to each group center
    group_centers = [(7.5, 7.2), (11.75, 7.2), (16, 7.2), (10, 4.2)]
    for gx, gy in group_centers:
        ax.plot([5, gx], [5.1, gy], 'k--', linewidth=1, alpha=0.6)
    
    ax.set_xlim(0, 19)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Agency Use Case Diagram - Organized Layout', 
                fontsize=16, weight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('../img/agency-usecase-diagram.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()

def create_organized_admin_diagram():
    """Create Administrator Use Case with organized layout"""
    
    fig, ax = plt.subplots(figsize=(16, 10))
    
    # Actor
    admin_box = FancyBboxPatch((1, 4.5), 2.5, 1.2,
                              boxstyle="round,pad=0.1",
                              facecolor='#E8F4FD', 
                              edgecolor='#1976D2', 
                              linewidth=3)
    ax.add_patch(admin_box)
    ax.text(2.25, 5.1, '👤 Administrator', ha='center', va='center', fontsize=12, weight='bold')
    
    # System boundary  
    system_boundary = FancyBboxPatch((5, 1), 13, 8,
                                   boxstyle="round,pad=0.2",
                                   facecolor='#F8F9FA', 
                                   edgecolor='#1976D2', 
                                   linewidth=3)
    ax.add_patch(system_boundary)
    ax.text(11.5, 8.5, '🏢 Platform Administration', ha='center', va='center', 
            fontsize=14, weight='bold', color='#1976D2')
    
    # Organized groups
    groups = [
        {
            'title': 'User Management',
            'x': 6, 'y': 6.5, 'width': 3, 'height': 1.5,
            'cases': [('🏢 Agencies', 7.5, 7.5), ('👥 Users', 7.5, 6.9)]
        },
        {
            'title': 'System Config',
            'x': 10, 'y': 6.5, 'width': 3, 'height': 1.5,
            'cases': [('⚙️ Config', 11.5, 7.5), ('🔐 Permissions', 11.5, 6.9)]
        },
        {
            'title': 'Analytics',
            'x': 14, 'y': 6.5, 'width': 3.5, 'height': 1.5,
            'cases': [('📈 Analytics', 15.75, 7.5), ('🖥️ Monitor', 15.75, 6.9)]
        },
        {
            'title': 'Content & Finance',
            'x': 8, 'y': 3.5, 'width': 5, 'height': 1.5,
            'cases': [('🛡️ Moderate', 9.5, 4.5), ('💰 Revenue', 10.5, 4.5), ('📊 Reports', 11.5, 4.5)]
        }
    ]
    
    # Draw groups
    for group in groups:
        group_box = FancyBboxPatch((group['x'], group['y']), group['width'], group['height'],
                                  boxstyle="round,pad=0.1",
                                  facecolor='#FAFAFA', 
                                  edgecolor='#BDBDBD', 
                                  linewidth=1)
        ax.add_patch(group_box)
        
        ax.text(group['x'] + group['width']/2, group['y'] + group['height'] - 0.2, 
                group['title'], ha='center', va='center', fontsize=9, 
                weight='bold', color='#666')
        
        for text, x, y in group['cases']:
            ellipse = patches.Ellipse((x, y), 1.4, 0.45, 
                                    facecolor='white', 
                                    edgecolor='#424242', 
                                    linewidth=1.5)
            ax.add_patch(ellipse)
            ax.text(x, y, text, ha='center', va='center', fontsize=8)
    
    # Clean organized connections
    ax.plot([3.5, 5], [5.1, 5.1], 'k-', linewidth=2, alpha=0.7)
    
    group_centers = [(7.5, 7.2), (11.5, 7.2), (15.75, 7.2), (10.5, 4.2)]
    for gx, gy in group_centers:
        ax.plot([5, gx], [5.1, gy], 'k--', linewidth=1, alpha=0.6)
    
    ax.set_xlim(0, 19)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Administrator Use Case Diagram - Organized Layout', 
                fontsize=16, weight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('../img/admin-usecase-diagram.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()

if __name__ == "__main__":
    import os
    os.makedirs('../img', exist_ok=True)
    
    print("🎯 Generating Organized Use Case Diagrams...")
    
    create_organized_customer_diagram()
    print("✅ Customer Use Case: Organized serial bus layout")
    
    create_organized_agency_diagram()
    print("✅ Agency Use Case: Clean grouped connections")
    
    create_organized_admin_diagram()
    print("✅ Admin Use Case: Structured organized flow")
    
    print("\n🎉 All Organized Use Case Diagrams completed!")
    print("📋 Key Improvements:")
    print("- ✅ Grouped related use cases together")
    print("- ✅ Serial bus connection pattern (no chaos)")
    print("- ✅ Logical flow organization") 
    print("- ✅ Clean visual hierarchy")
    print("- ✅ Professional emojis for clarity")
    print("- ✅ Ready for stick figure assets integration")