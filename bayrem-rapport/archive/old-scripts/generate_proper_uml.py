"""
Proper UML Use Case Diagram Generator using Matplotlib
Following exact UML standards: stick figures, ellipses, proper layout
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Ellipse, FancyBboxPatch
import numpy as np

def create_stick_figure(ax, x, y, name, size=0.3):
    """Draw a proper UML stick figure actor"""
    
    # Head (circle)
    head = plt.Circle((x, y + size*0.7), size*0.15, fill=False, color='black', linewidth=2)
    ax.add_patch(head)
    
    # Body (vertical line)
    ax.plot([x, x], [y + size*0.55, y + size*0.2], 'k-', linewidth=2)
    
    # Arms (horizontal line)
    ax.plot([x - size*0.2, x + size*0.2], [y + size*0.45, y + size*0.45], 'k-', linewidth=2)
    
    # Legs (diagonal lines)
    ax.plot([x, x - size*0.15], [y + size*0.2, y], 'k-', linewidth=2)
    ax.plot([x, x + size*0.15], [y + size*0.2, y], 'k-', linewidth=2)
    
    # Name label
    ax.text(x, y - size*0.3, name, ha='center', va='center', fontsize=10, fontweight='bold')

def create_use_case(ax, x, y, width, height, text, fontsize=9):
    """Draw a proper UML use case ellipse"""
    
    ellipse = Ellipse((x, y), width, height, fill=False, color='black', linewidth=1.5)
    ax.add_patch(ellipse)
    
    # Multi-line text handling
    lines = text.split('\\n') if '\\n' in text else [text]
    line_height = 0.15
    start_y = y + (len(lines) - 1) * line_height / 2
    
    for i, line in enumerate(lines):
        ax.text(x, start_y - i * line_height, line, ha='center', va='center', 
                fontsize=fontsize, wrap=True)

def draw_system_boundary(ax, x, y, width, height, title):
    """Draw system boundary rectangle"""
    
    rect = FancyBboxPatch((x - width/2, y - height/2), width, height,
                         boxstyle="round,pad=0.1", 
                         fill=False, color='black', linewidth=2)
    ax.add_patch(rect)
    
    # System title
    ax.text(x, y + height/2 + 0.3, title, ha='center', va='bottom', 
            fontsize=12, fontweight='bold')

def generate_customer_usecase_proper():
    """Generate proper UML Customer Use Case Diagram"""
    
    fig, ax = plt.subplots(1, 1, figsize=(16, 10))
    ax.set_xlim(-1, 15)
    ax.set_ylim(-1, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Title
    ax.text(7, 9.5, 'Customer Use Case Diagram', ha='center', va='center', 
            fontsize=16, fontweight='bold')
    ax.text(7, 9, 'Myloc Car Rental Platform', ha='center', va='center', 
            fontsize=12, style='italic')
    
    # System boundary
    draw_system_boundary(ax, 7, 4.5, 10, 7, 'Car Rental Platform')
    
    # Left side actors
    create_stick_figure(ax, 0.5, 6, 'Customer')
    create_stick_figure(ax, 0.5, 2.5, 'Visitor')
    
    # Use cases inside system boundary - organized in groups
    use_cases = [
        # Authentication group
        (4, 7.5, 1.8, 0.6, 'Login/Register'),
        (4, 6.5, 1.6, 0.6, 'Manage Profile'),
        
        # Vehicle operations
        (7, 7.5, 1.6, 0.6, 'Browse Cars'),
        (7, 6.5, 1.8, 0.6, 'Check Availability'),
        (10, 7.5, 1.6, 0.6, 'Book Vehicle'),
        (10, 6.5, 1.6, 0.6, 'Make Payment'),
        
        # Booking management
        (4, 5, 1.6, 0.6, 'View Bookings'),
        (7, 5, 1.6, 0.6, 'Modify Booking'),
        (10, 5, 1.8, 0.6, 'Download Contract'),
        
        # Communication
        (4, 3.5, 1.8, 0.6, 'Chat with Agency'),
        (7, 3.5, 1.6, 0.6, 'Use Chatbot'),
        
        # Content
        (4, 2, 1.6, 0.6, 'Read Blog'),
        (7, 2, 1.6, 0.6, 'Leave Comments'),
        (10, 2, 1.6, 0.6, 'Follow Agency'),
    ]
    
    # Draw use cases
    for x, y, w, h, text in use_cases:
        create_use_case(ax, x, y, w, h, text)
    
    # Draw associations with proper curved/angled lines
    def draw_smooth_line(ax, x1, y1, x2, y2, curve_factor=0.3):
        """Draw a smooth curved line between two points"""
        if abs(x2 - x1) > 2:  # Use curves for longer distances
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2 + curve_factor
            
            # Create smooth curve using quadratic bezier
            t = np.linspace(0, 1, 50)
            curve_x = (1-t)**2 * x1 + 2*(1-t)*t * mid_x + t**2 * x2
            curve_y = (1-t)**2 * y1 + 2*(1-t)*t * mid_y + t**2 * y2
            ax.plot(curve_x, curve_y, 'k-', linewidth=1, alpha=0.8)
        else:  # Use angled lines for shorter distances
            mid_x = x1 + (x2 - x1) * 0.7
            ax.plot([x1, mid_x, x2], [y1, y1, y2], 'k-', linewidth=1, alpha=0.8)
    
    customer_connections = [
        (4, 7.5), (4, 6.5), (7, 7.5), (7, 6.5), (10, 7.5), (10, 6.5),
        (4, 5), (7, 5), (10, 5), (4, 3.5), (7, 3.5), 
        (4, 2), (7, 2), (10, 2)
    ]
    
    visitor_connections = [(4, 7.5), (7, 7.5), (7, 3.5), (4, 2)]
    
    # Customer lines with smooth routing
    for uc_x, uc_y in customer_connections:
        draw_smooth_line(ax, 0.8, 6, uc_x - 0.9, uc_y, 
                        curve_factor=0.2 if uc_y > 6 else -0.2)
    
    # Visitor lines with smooth routing
    for uc_x, uc_y in visitor_connections:
        draw_smooth_line(ax, 0.8, 2.5, uc_x - 0.9, uc_y,
                        curve_factor=0.2 if uc_y > 2.5 else -0.2)
    
    # Include relationships (dashed lines with <<include>>)
    include_relations = [
        ((7, 6.5), (10, 7.5), 'includes'),  # Check Availability -> Book Vehicle
        ((10, 7.5), (10, 6.5), 'includes'), # Book Vehicle -> Make Payment
        ((10, 6.5), (10, 5), 'includes'),   # Make Payment -> Download Contract
    ]
    
    for (x1, y1), (x2, y2), label in include_relations:
        ax.plot([x1, x2], [y1, y2], 'k--', linewidth=1)
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mid_x, mid_y + 0.2, f'<<{label}>>', ha='center', va='center', 
                fontsize=8, style='italic')
    
    plt.tight_layout()
    return fig

def generate_agency_usecase_proper():
    """Generate proper UML Agency Use Case Diagram"""
    
    fig, ax = plt.subplots(1, 1, figsize=(14, 9))
    ax.set_xlim(-1, 13)
    ax.set_ylim(-1, 9)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Title
    ax.text(6, 8.5, 'Agency Use Case Diagram', ha='center', va='center', 
            fontsize=16, fontweight='bold')
    ax.text(6, 8, 'Myloc Agency Management System', ha='center', va='center', 
            fontsize=12, style='italic')
    
    # System boundary
    draw_system_boundary(ax, 6, 4, 8, 6, 'Agency Management System')
    
    # Left side actor
    create_stick_figure(ax, 0.5, 4, 'Agency')
    
    # Use cases organized in logical groups
    use_cases = [
        # Authentication
        (3.5, 6.5, 1.4, 0.5, 'Login'),
        (3.5, 5.8, 1.6, 0.5, 'Manage Profile'),
        
        # Fleet Management
        (6, 6.5, 1.4, 0.5, 'Add Vehicle'),
        (6, 5.8, 1.4, 0.5, 'Edit Vehicle'),
        (8.5, 6.5, 1.4, 0.5, 'Set Pricing'),
        (8.5, 5.8, 1.6, 0.5, 'Upload Photos'),
        
        # Booking Operations
        (3.5, 4.5, 1.6, 0.5, 'View Requests'),
        (6, 4.5, 1.6, 0.5, 'Accept Booking'),
        (8.5, 4.5, 1.6, 0.5, 'Reject Booking'),
        
        # Communication & Reports
        (3.5, 3, 1.8, 0.5, 'Chat with Customer'),
        (6, 3, 1.8, 0.5, 'Send Notifications'),
        (8.5, 3, 1.6, 0.5, 'Generate Reports'),
        
        # Content Management
        (6, 1.8, 1.8, 0.5, 'Create Blog Post'),
    ]
    
    # Draw use cases
    for x, y, w, h, text in use_cases:
        create_use_case(ax, x, y, w, h, text)
    
    # Draw associations with smooth lines
    def draw_smooth_line(ax, x1, y1, x2, y2, curve_factor=0.3):
        """Draw a smooth curved line between two points"""
        if abs(x2 - x1) > 2:  # Use curves for longer distances
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2 + curve_factor
            
            # Create smooth curve using quadratic bezier
            t = np.linspace(0, 1, 50)
            curve_x = (1-t)**2 * x1 + 2*(1-t)*t * mid_x + t**2 * x2
            curve_y = (1-t)**2 * y1 + 2*(1-t)*t * mid_y + t**2 * y2
            ax.plot(curve_x, curve_y, 'k-', linewidth=1, alpha=0.8)
        else:  # Use angled lines for shorter distances
            mid_x = x1 + (x2 - x1) * 0.7
            ax.plot([x1, mid_x, x2], [y1, y1, y2], 'k-', linewidth=1, alpha=0.8)
    
    agency_connections = [uc[:2] for uc in use_cases]
    
    for uc_x, uc_y in agency_connections:
        draw_smooth_line(ax, 0.8, 4, uc_x - 0.7, uc_y, 
                        curve_factor=0.2 if uc_y > 4 else -0.2)
    
    plt.tight_layout()
    return fig

def generate_admin_usecase_proper():
    """Generate proper UML Administrator Use Case Diagram"""
    
    fig, ax = plt.subplots(1, 1, figsize=(14, 9))
    ax.set_xlim(-1, 13)
    ax.set_ylim(-1, 9)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Title
    ax.text(6, 8.5, 'Administrator Use Case Diagram', ha='center', va='center', 
            fontsize=16, fontweight='bold')
    ax.text(6, 8, 'Myloc Platform Administration', ha='center', va='center', 
            fontsize=12, style='italic')
    
    # System boundary
    draw_system_boundary(ax, 6, 4, 8, 6, 'Platform Administration')
    
    # Left side actor
    create_stick_figure(ax, 0.5, 4, 'Administrator')
    
    # Use cases
    use_cases = [
        # User Management
        (3.5, 6.5, 1.6, 0.5, 'Manage Agencies'),
        (6, 6.5, 1.8, 0.5, 'Manage Customers'),
        (8.5, 6.5, 1.6, 0.5, 'View Analytics'),
        
        # Content & System
        (3.5, 5.5, 1.8, 0.5, 'Moderate Content'),
        (6, 5.5, 1.6, 0.5, 'Handle Reports'),
        (8.5, 5.5, 1.6, 0.5, 'System Config'),
        
        # Financial
        (3.5, 4.5, 1.6, 0.5, 'View Revenue'),
        (6, 4.5, 1.8, 0.5, 'Generate Reports'),
        (8.5, 4.5, 1.8, 0.5, 'Manage Payments'),
        
        # Maintenance
        (3.5, 3, 1.6, 0.5, 'Monitor System'),
        (6, 3, 1.4, 0.5, 'Backup Data'),
        (8.5, 3, 1.6, 0.5, 'Update System'),
    ]
    
    # Draw use cases
    for x, y, w, h, text in use_cases:
        create_use_case(ax, x, y, w, h, text)
    
    # Draw associations with smooth lines
    def draw_smooth_line(ax, x1, y1, x2, y2, curve_factor=0.3):
        """Draw a smooth curved line between two points"""
        if abs(x2 - x1) > 2:  # Use curves for longer distances
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2 + curve_factor
            
            # Create smooth curve using quadratic bezier
            t = np.linspace(0, 1, 50)
            curve_x = (1-t)**2 * x1 + 2*(1-t)*t * mid_x + t**2 * x2
            curve_y = (1-t)**2 * y1 + 2*(1-t)*t * mid_y + t**2 * y2
            ax.plot(curve_x, curve_y, 'k-', linewidth=1, alpha=0.8)
        else:  # Use angled lines for shorter distances
            mid_x = x1 + (x2 - x1) * 0.7
            ax.plot([x1, mid_x, x2], [y1, y1, y2], 'k-', linewidth=1, alpha=0.8)
    
    admin_connections = [uc[:2] for uc in use_cases]
    
    for uc_x, uc_y in admin_connections:
        draw_smooth_line(ax, 0.8, 4, uc_x - 0.8, uc_y,
                        curve_factor=0.2 if uc_y > 4 else -0.2)
    
    plt.tight_layout()
    return fig

if __name__ == "__main__":
    import os
    
    os.makedirs("../img", exist_ok=True)
    
    # Generate proper UML use case diagrams
    diagrams = [
        (generate_customer_usecase_proper(), "customer-usecase-diagram.png"),
        (generate_agency_usecase_proper(), "agency-usecase-diagram.png"), 
        (generate_admin_usecase_proper(), "admin-usecase-diagram.png")
    ]
    
    for fig, filename in diagrams:
        filepath = f"../img/{filename}"
        fig.savefig(filepath, dpi=300, bbox_inches='tight', 
                   facecolor='white', edgecolor='none')
        print(f"✅ Generated proper UML diagram: {filepath}")
        plt.close(fig)
    
    print("\n🎯 Proper UML Use Case Diagrams Generated:")
    print("- ✅ Stick figure actors (UML standard)")
    print("- ✅ Elliptical use cases (UML standard)")
    print("- ✅ System boundary boxes")
    print("- ✅ Proper space distribution")
    print("- ✅ Neutral colors (black/white)")
    print("- ✅ Professional layout")