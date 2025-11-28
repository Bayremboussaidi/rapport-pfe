"""
Generate UML Use Case Diagrams using matplotlib
Clean, professional, proper UML standards with stick figures
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

def create_stick_figure(ax, x, y, size=0.08, name="Actor"):
    """Draw a proper UML stick figure at position (x, y)"""
    # Head
    head = plt.Circle((x, y + size*0.7), size*0.2, color='black', fill=False, linewidth=2)
    ax.add_patch(head)
    
    # Body (vertical line)
    ax.plot([x, x], [y + size*0.5, y - size*0.1], 'k-', linewidth=2)
    
    # Arms (horizontal line)
    ax.plot([x - size*0.3, x + size*0.3], [y + size*0.2, y + size*0.2], 'k-', linewidth=2)
    
    # Legs
    ax.plot([x, x - size*0.2], [y - size*0.1, y - size*0.5], 'k-', linewidth=2)
    ax.plot([x, x + size*0.2], [y - size*0.1, y - size*0.5], 'k-', linewidth=2)
    
    # Name below
    ax.text(x, y - size*0.8, name, ha='center', va='center', fontsize=10, weight='bold')

def create_use_case(ax, x, y, width, height, text):
    """Draw a UML use case (ellipse) with text"""
    ellipse = patches.Ellipse((x, y), width, height, 
                             facecolor='white', edgecolor='black', linewidth=1)
    ax.add_patch(ellipse)
    ax.text(x, y, text, ha='center', va='center', fontsize=8, wrap=True)

def draw_system_boundary(ax, x, y, width, height, title):
    """Draw system boundary rectangle"""
    rect = FancyBboxPatch((x - width/2, y - height/2), width, height,
                         boxstyle="round,pad=0.02",
                         facecolor='#F8F9FA', edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    ax.text(x, y + height/2 - 0.1, title, ha='center', va='center', 
            fontsize=12, weight='bold')

def create_customer_usecase():
    """Generate Customer Use Case Diagram"""
    fig, ax = plt.subplots(figsize=(16, 12))
    
    # Actors on the left
    create_stick_figure(ax, 1, 8, name="Customer")
    create_stick_figure(ax, 1, 4, name="Visitor")
    
    # System boundary
    draw_system_boundary(ax, 8, 6, 12, 10, "Car Rental Platform")
    
    # Use cases arranged in logical groups
    use_cases = [
        # Authentication & Profile
        (5, 10, "Login"),
        (5, 9, "Register"), 
        (5, 8, "Manage Profile"),
        
        # Vehicle browsing
        (8, 10, "Browse Cars"),
        (8, 9, "Search Vehicles"),
        (8, 8, "Check Availability"),
        
        # Booking process  
        (11, 10, "Book Vehicle"),
        (11, 9, "Make Payment"),
        (11, 8, "Download Contract"),
        
        # Booking management
        (5, 6, "View Bookings"),
        (8, 6, "Modify Booking"),
        (11, 6, "Cancel Booking"),
        
        # Communication
        (5, 4, "Chat with Agency"),
        (8, 4, "Use Chatbot"),
        (11, 4, "Receive Notifications"),
        
        # Content
        (5, 2, "Read Blog"),
        (8, 2, "Leave Comments"),
        (11, 2, "Follow Agency"),
    ]
    
    # Draw use cases
    for x, y, text in use_cases:
        create_use_case(ax, x, y, 2.2, 0.8, text)
    
    # Association lines (dotted)
    customer_cases = [(5,10), (5,8), (8,10), (8,9), (8,8), (11,10), (11,9), (11,8), 
                     (5,6), (8,6), (11,6), (5,4), (8,4), (11,4), (5,2), (8,2), (11,2)]
    
    for x, y in customer_cases:
        ax.plot([1, x-1.1], [8, y], 'k--', alpha=0.7, linewidth=1)
    
    # Visitor associations (limited)
    visitor_cases = [(5,9), (8,10), (8,4), (5,2)]
    for x, y in visitor_cases:
        ax.plot([1, x-1.1], [4, y], 'k--', alpha=0.7, linewidth=1)
    
    # Include relationships (solid arrows)
    ax.annotate('', xy=(5, 8), xytext=(5, 10), 
                arrowprops=dict(arrowstyle='->', color='black', lw=1))
    ax.text(4.5, 9, 'includes', fontsize=7, rotation=90)
    
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 12)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Customer Use Case Diagram', fontsize=16, weight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('../img/customer-usecase-diagram.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_agency_usecase():
    """Generate Agency Use Case Diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Actor on the left
    create_stick_figure(ax, 1, 6, name="Agency")
    
    # System boundary
    draw_system_boundary(ax, 7.5, 6, 11, 8, "Agency Management System")
    
    # Use cases
    use_cases = [
        # Authentication & Profile
        (4, 9, "Login"),
        (4, 8, "Manage Profile"),
        
        # Vehicle management
        (7, 9, "Add Vehicle"),
        (7, 8, "Edit Vehicle"),
        (7, 7, "Delete Vehicle"),
        (10, 9, "Set Pricing"),
        (10, 8, "Upload Photos"),
        (10, 7, "Manage Availability"),
        
        # Booking management
        (4, 6, "View Requests"),
        (7, 6, "Accept Booking"),
        (10, 6, "Reject Booking"),
        
        # Reporting & Communication
        (4, 4, "Generate Reports"),
        (7, 4, "Chat with Customer"),
        (10, 4, "Send Notifications"),
        
        # Content management
        (4, 2, "Create Blog Post"),
        (7, 2, "Manage Followers"),
    ]
    
    # Draw use cases
    for x, y, text in use_cases:
        create_use_case(ax, x, y, 2, 0.7, text)
    
    # Association lines
    for x, y, _ in use_cases:
        ax.plot([1, x-1], [6, y], 'k--', alpha=0.7, linewidth=1)
    
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 11)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Agency Use Case Diagram', fontsize=16, weight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('../img/agency-usecase-diagram.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_admin_usecase():
    """Generate Administrator Use Case Diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Actor on the left
    create_stick_figure(ax, 1, 6, name="Administrator")
    
    # System boundary
    draw_system_boundary(ax, 7.5, 6, 11, 8, "Platform Administration")
    
    # Use cases
    use_cases = [
        # User management
        (4, 9, "Manage Agencies"),
        (4, 8, "Manage Customers"),
        (4, 7, "Manage Users"),
        
        # System configuration
        (7, 9, "Configure System"),
        (7, 8, "Manage Permissions"),
        (7, 7, "Update System"),
        
        # Monitoring & Analytics
        (10, 9, "View Analytics"),
        (10, 8, "Monitor System"),
        (10, 7, "Backup Data"),
        
        # Content moderation
        (4, 5, "Moderate Content"),
        (7, 5, "Manage Blog Posts"),
        (10, 5, "Handle Reports"),
        
        # Financial management
        (4, 3, "View Revenue"),
        (7, 3, "Generate Reports"),
        (10, 3, "Manage Payments"),
    ]
    
    # Draw use cases
    for x, y, text in use_cases:
        create_use_case(ax, x, y, 2, 0.7, text)
    
    # Association lines
    for x, y, _ in use_cases:
        ax.plot([1, x-1], [6, y], 'k--', alpha=0.7, linewidth=1)
    
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 11)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Administrator Use Case Diagram', fontsize=16, weight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('../img/admin-usecase-diagram.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    import os
    os.makedirs('../img', exist_ok=True)
    
    print("🎯 Generating Professional UML Use Case Diagrams...")
    
    create_customer_usecase()
    print("✅ Customer Use Case Diagram generated: img/customer-usecase-diagram.png")
    
    create_agency_usecase()
    print("✅ Agency Use Case Diagram generated: img/agency-usecase-diagram.png")
    
    create_admin_usecase()
    print("✅ Administrator Use Case Diagram generated: img/admin-usecase-diagram.png")
    
    print("\n🎉 All UML Use Case Diagrams completed!")
    print("📋 Features:")
    print("- ✅ Proper UML stick figures")
    print("- ✅ Elliptical use cases") 
    print("- ✅ System boundaries")
    print("- ✅ Dotted association lines")
    print("- ✅ Professional layout")
    print("- ✅ High resolution (300 DPI)")