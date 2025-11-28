"""
Figure 2.1: Customer Use Case Diagram - Final Version
Clean, organized layout with grouped functionality and serial bus connections
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np
import os

def create_final_customer_usecase():
    """Generate the final Customer Use Case Diagram with organized layout"""
    
    fig, ax = plt.subplots(figsize=(18, 12))
    
    # Actors on left side (clean vertical layout)
    customer_box = FancyBboxPatch((1, 8), 2.5, 1.2,
                                 boxstyle="round,pad=0.1",
                                 facecolor='#E8F4FD', 
                                 edgecolor='#1976D2', 
                                 linewidth=3)
    ax.add_patch(customer_box)
    ax.text(2.25, 8.6, 'Customer', ha='center', va='center', fontsize=12, weight='bold')
    
    visitor_box = FancyBboxPatch((1, 5), 2.5, 1.2,
                                boxstyle="round,pad=0.1",
                                facecolor='#E8F4FD', 
                                edgecolor='#1976D2', 
                                linewidth=3)
    ax.add_patch(visitor_box)
    ax.text(2.25, 5.6, 'Visitor', ha='center', va='center', fontsize=12, weight='bold')
    
    # System boundary
    system_boundary = FancyBboxPatch((5, 1), 16, 11,
                                   boxstyle="round,pad=0.2",
                                   facecolor='#F8F9FA', 
                                   edgecolor='#1976D2', 
                                   linewidth=3)
    ax.add_patch(system_boundary)
    ax.text(13, 11.5, 'Car Rental Platform', ha='center', va='center', 
            fontsize=14, weight='bold', color='#1976D2')
    
    # Organized functional groups (horizontal serial layout - NO CHAOS!)
    groups = [
        # Row 1: Core Authentication & Profile
        {
            'title': 'Authentication',
            'x': 6, 'y': 9, 'width': 3.5, 'height': 2,
            'cases': [
                ('Login', 7.75, 10.3),
                ('Register', 7.75, 9.7), 
                ('Manage Profile', 7.75, 9.1)
            ]
        },
        # Row 1: Vehicle Operations
        {
            'title': 'Vehicle Browsing',
            'x': 10.5, 'y': 9, 'width': 3.5, 'height': 2,
            'cases': [
                ('Browse Cars', 12.25, 10.3),
                ('Search Vehicles', 12.25, 9.7),
                ('Check Availability', 12.25, 9.1)
            ]
        },
        # Row 1: Booking Process
        {
            'title': 'Booking Flow',
            'x': 15, 'y': 9, 'width': 3.5, 'height': 2,
            'cases': [
                ('Book Vehicle', 16.75, 10.3),
                ('Make Payment', 16.75, 9.7),
                ('Download Contract', 16.75, 9.1)
            ]
        },
        
        # Row 2: Booking Management
        {
            'title': 'Booking Management',
            'x': 6, 'y': 5.5, 'width': 4, 'height': 2,
            'cases': [
                ('View Bookings', 8, 6.8),
                ('Modify Booking', 8, 6.2),
                ('Cancel Booking', 8, 5.9)
            ]
        },
        # Row 2: Communication
        {
            'title': 'Communication',
            'x': 11, 'y': 5.5, 'width': 4, 'height': 2,
            'cases': [
                ('Chat with Agency', 13, 6.8),
                ('Use Chatbot', 13, 6.2),
                ('Receive Notifications', 13, 5.9)
            ]
        },
        # Row 2: Content & Social
        {
            'title': 'Content & Social',
            'x': 16, 'y': 5.5, 'width': 4, 'height': 2,
            'cases': [
                ('Read Blog', 18, 6.8),
                ('Leave Comments', 18, 6.2),
                ('Follow Agency', 18, 5.9)
            ]
        }
    ]
    
    # Draw groups and use cases
    for group in groups:
        # Group boundary (subtle)
        group_box = FancyBboxPatch((group['x'], group['y']), group['width'], group['height'],
                                  boxstyle="round,pad=0.15",
                                  facecolor='#FAFAFA', 
                                  edgecolor='#E0E0E0', 
                                  linewidth=1)
        ax.add_patch(group_box)
        
        # Group title
        ax.text(group['x'] + group['width']/2, group['y'] + group['height'] - 0.3, 
                group['title'], ha='center', va='center', fontsize=10, 
                weight='bold', color='#555', style='italic')
        
        # Use cases within group
        for text, x, y in group['cases']:
            ellipse = patches.Ellipse((x, y), 2.8, 0.6, 
                                    facecolor='white', 
                                    edgecolor='#424242', 
                                    linewidth=1.5)
            ax.add_patch(ellipse)
            ax.text(x, y, text, ha='center', va='center', fontsize=9)
    
    # ORGANIZED CONNECTION LINES - Serial Bus Pattern (NO CHAOS!)
    
    # Main horizontal bus from Customer
    ax.plot([3.5, 5], [8.6, 8.6], 'k-', linewidth=3, alpha=0.8)  # Customer main trunk
    
    # Top row connections (parallel branches)
    top_groups = [(7.75, 10), (12.25, 10), (16.75, 10)]
    for gx, gy in top_groups:
        # Vertical drop to group
        ax.plot([5, gx], [8.6, gy], 'k--', linewidth=1.5, alpha=0.7)
        # Connection point
        ax.plot(gx, gy, 'ko', markersize=4, alpha=0.7)
    
    # Bottom row connections (parallel branches)  
    bottom_groups = [(8, 6.5), (13, 6.5), (18, 6.5)]
    for gx, gy in bottom_groups:
        # Vertical drop to group
        ax.plot([5, gx], [8.6, gy], 'k--', linewidth=1.5, alpha=0.7)
        # Connection point
        ax.plot(gx, gy, 'ko', markersize=4, alpha=0.7)
    
    # Visitor connections (limited, organized)
    visitor_trunk = [3.5, 4.5]  # Short trunk from visitor
    ax.plot(visitor_trunk, [5.6, 5.6], 'k-', linewidth=2, alpha=0.6)
    
    # Specific visitor connections (only to accessible use cases)
    visitor_targets = [(7.75, 9.7), (12.25, 10.3), (13, 6.2), (18, 6.8)]  # Register, Browse, Chatbot, Blog
    for vx, vy in visitor_targets:
        ax.plot([4.5, vx], [5.6, vy], 'k:', linewidth=1, alpha=0.5)
        ax.plot(vx, vy, 'ko', markersize=3, alpha=0.5)
    
    # Include relationships (clean arrows within groups)
    # Login includes Manage Profile
    ax.annotate('', xy=(7.75, 9.1), xytext=(7.75, 10.3), 
                arrowprops=dict(arrowstyle='->', color='#1976D2', lw=2))
    ax.text(8.4, 9.7, '<<includes>>', fontsize=8, color='#1976D2', rotation=90)
    
    # Check Availability includes Book Vehicle
    ax.annotate('', xy=(16.75, 10.3), xytext=(12.25, 9.1), 
                arrowprops=dict(arrowstyle='->', color='#1976D2', lw=1.5))
    ax.text(14.5, 9.5, '<<includes>>', fontsize=8, color='#1976D2')
    
    ax.set_xlim(0, 22)
    ax.set_ylim(0, 13)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Figure 2.1: Customer Use Case Diagram\nOrganized Functional Groups with Serial Bus Architecture', 
                fontsize=16, weight='bold', pad=20)
    
    plt.tight_layout()
    
    # Save in figure directory
    output_path = 'customer-usecase-diagram-final.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"✅ Generated: {output_path}")
    
    # Also save as main version
    plt.savefig('../../../img/customer-usecase-diagram.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"✅ Updated main: img/customer-usecase-diagram.png")
    
    plt.close()

if __name__ == "__main__":
    print("🎯 Generating Figure 2.1: Customer Use Case Diagram")
    print("📋 Features:")
    print("- ✅ Organized functional groups")
    print("- ✅ Serial bus connection pattern") 
    print("- ✅ No chaotic arrow mess")
    print("- ✅ Professional UML compliance")
    print("- ✅ Clean visual hierarchy")
    print("")
    
    create_final_customer_usecase()
    
    print("\n🎉 Figure 2.1 completed successfully!")
    print("💡 This is the FINAL organized version - no more chaos!")