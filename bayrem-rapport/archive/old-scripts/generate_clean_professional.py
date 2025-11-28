"""
Generate clean, professional Use Case Diagrams using matplotlib
Without stick figures - just clean boxes and proper UML layout
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import matplotlib.lines as mlines

def create_clean_usecase():
    """Generate clean Use Case Diagrams with professional layout"""
    
    # Figure 1: Customer Use Case Diagram
    fig, ax = plt.subplots(figsize=(16, 10))
    
    # System boundary
    boundary = FancyBboxPatch((3, 1), 12, 8,
                             boxstyle="round,pad=0.1",
                             facecolor='#F8F9FA', 
                             edgecolor='black', 
                             linewidth=2)
    ax.add_patch(boundary)
    ax.text(9, 8.5, 'Car Rental Platform', ha='center', va='center', 
            fontsize=14, weight='bold')
    
    # Actors (simple rectangles)
    customer_box = FancyBboxPatch((0.5, 7), 2, 1,
                                 boxstyle="round,pad=0.05",
                                 facecolor='white', 
                                 edgecolor='black', 
                                 linewidth=2)
    ax.add_patch(customer_box)
    ax.text(1.5, 7.5, 'Customer', ha='center', va='center', fontsize=11, weight='bold')
    
    visitor_box = FancyBboxPatch((0.5, 4), 2, 1,
                                boxstyle="round,pad=0.05",
                                facecolor='white', 
                                edgecolor='black', 
                                linewidth=2)
    ax.add_patch(visitor_box)
    ax.text(1.5, 4.5, 'Visitor', ha='center', va='center', fontsize=11, weight='bold')
    
    # Use cases (ellipses)
    use_cases = [
        # Row 1
        (5, 7.5, "Login"),
        (7.5, 7.5, "Register"), 
        (10, 7.5, "Manage Profile"),
        (12.5, 7.5, "Browse Cars"),
        
        # Row 2
        (5, 6, "Search Vehicles"),
        (7.5, 6, "Check Availability"),
        (10, 6, "Book Vehicle"),
        (12.5, 6, "Make Payment"),
        
        # Row 3
        (5, 4.5, "View Bookings"),
        (7.5, 4.5, "Modify Booking"),
        (10, 4.5, "Cancel Booking"),
        (12.5, 4.5, "Download Contract"),
        
        # Row 4
        (5, 3, "Chat with Agency"),
        (7.5, 3, "Use Chatbot"),
        (10, 3, "Receive Notifications"),
        (12.5, 3, "Read Blog"),
    ]
    
    # Draw use cases
    for x, y, text in use_cases:
        ellipse = patches.Ellipse((x, y), 2, 0.8, 
                                 facecolor='white', 
                                 edgecolor='black', 
                                 linewidth=1)
        ax.add_patch(ellipse)
        ax.text(x, y, text, ha='center', va='center', fontsize=9, wrap=True)
    
    # Customer associations (clean dotted lines)
    customer_cases = [(5, 7.5), (10, 7.5), (12.5, 7.5), (5, 6), (7.5, 6), (10, 6), (12.5, 6),
                     (5, 4.5), (7.5, 4.5), (10, 4.5), (12.5, 4.5), (5, 3), (7.5, 3), (10, 3), (12.5, 3)]
    
    for x, y in customer_cases:
        ax.plot([2.5, x-1], [7.5, y], 'k--', alpha=0.6, linewidth=1)
    
    # Visitor associations (limited - dotted lines)
    visitor_cases = [(7.5, 7.5), (12.5, 7.5), (7.5, 3), (12.5, 3)]
    for x, y in visitor_cases:
        ax.plot([2.5, x-1], [4.5, y], 'k--', alpha=0.6, linewidth=1)
    
    # Include relationships (solid arrows)
    # Login includes Manage Profile
    ax.annotate('', xy=(10, 7.5), xytext=(5, 7.5), 
                arrowprops=dict(arrowstyle='->', color='black', lw=1))
    ax.text(7.5, 7.8, '<<includes>>', fontsize=8, ha='center')
    
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Customer Use Case Diagram', fontsize=16, weight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('../img/customer-usecase-diagram.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()

def create_agency_usecase():
    """Generate Agency Use Case Diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # System boundary
    boundary = FancyBboxPatch((3, 1), 10, 8,
                             boxstyle="round,pad=0.1",
                             facecolor='#F8F9FA', 
                             edgecolor='black', 
                             linewidth=2)
    ax.add_patch(boundary)
    ax.text(8, 8.5, 'Agency Management System', ha='center', va='center', 
            fontsize=14, weight='bold')
    
    # Actor
    agency_box = FancyBboxPatch((0.5, 4.5), 2, 1,
                               boxstyle="round,pad=0.05",
                               facecolor='white', 
                               edgecolor='black', 
                               linewidth=2)
    ax.add_patch(agency_box)
    ax.text(1.5, 5, 'Agency', ha='center', va='center', fontsize=11, weight='bold')
    
    # Use cases
    use_cases = [
        # Column 1
        (5, 7, "Login"),
        (5, 5.5, "Manage Profile"),
        (5, 4, "Add Vehicle"),
        (5, 2.5, "Generate Reports"),
        
        # Column 2  
        (8, 7, "Edit Vehicle"),
        (8, 5.5, "Delete Vehicle"),
        (8, 4, "Set Pricing"),
        (8, 2.5, "Chat with Customer"),
        
        # Column 3
        (11, 7, "Upload Photos"),
        (11, 5.5, "View Requests"),
        (11, 4, "Accept/Reject Booking"),
        (11, 2.5, "Send Notifications"),
    ]
    
    # Draw use cases
    for x, y, text in use_cases:
        ellipse = patches.Ellipse((x, y), 2.2, 0.8, 
                                 facecolor='white', 
                                 edgecolor='black', 
                                 linewidth=1)
        ax.add_patch(ellipse)
        ax.text(x, y, text, ha='center', va='center', fontsize=9, wrap=True)
    
    # Association lines
    for x, y, _ in use_cases:
        ax.plot([2.5, x-1.1], [5, y], 'k--', alpha=0.6, linewidth=1)
    
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Agency Use Case Diagram', fontsize=16, weight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('../img/agency-usecase-diagram.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()

def create_admin_usecase():
    """Generate Administrator Use Case Diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # System boundary
    boundary = FancyBboxPatch((3, 1), 10, 8,
                             boxstyle="round,pad=0.1",
                             facecolor='#F8F9FA', 
                             edgecolor='black', 
                             linewidth=2)
    ax.add_patch(boundary)
    ax.text(8, 8.5, 'Platform Administration', ha='center', va='center', 
            fontsize=14, weight='bold')
    
    # Actor
    admin_box = FancyBboxPatch((0.5, 4.5), 2, 1,
                              boxstyle="round,pad=0.05",
                              facecolor='white', 
                              edgecolor='black', 
                              linewidth=2)
    ax.add_patch(admin_box)
    ax.text(1.5, 5, 'Administrator', ha='center', va='center', fontsize=11, weight='bold')
    
    # Use cases
    use_cases = [
        # Column 1
        (5, 7, "Manage Agencies"),
        (5, 5.5, "Manage Customers"),
        (5, 4, "Configure System"),
        (5, 2.5, "View Revenue"),
        
        # Column 2  
        (8, 7, "Manage Users"),
        (8, 5.5, "View Analytics"),
        (8, 4, "Monitor System"),
        (8, 2.5, "Generate Reports"),
        
        # Column 3
        (11, 7, "Moderate Content"),
        (11, 5.5, "Manage Blog Posts"),
        (11, 4, "Handle Reports"),
        (11, 2.5, "Manage Payments"),
    ]
    
    # Draw use cases
    for x, y, text in use_cases:
        ellipse = patches.Ellipse((x, y), 2.2, 0.8, 
                                 facecolor='white', 
                                 edgecolor='black', 
                                 linewidth=1)
        ax.add_patch(ellipse)
        ax.text(x, y, text, ha='center', va='center', fontsize=9, wrap=True)
    
    # Association lines
    for x, y, _ in use_cases:
        ax.plot([2.5, x-1.1], [5, y], 'k--', alpha=0.6, linewidth=1)
    
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Administrator Use Case Diagram', fontsize=16, weight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('../img/admin-usecase-diagram.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()

if __name__ == "__main__":
    import os
    os.makedirs('../img', exist_ok=True)
    
    print("🎯 Generating Clean Professional Use Case Diagrams...")
    
    create_clean_usecase()
    print("✅ Customer Use Case Diagram: img/customer-usecase-diagram.png")
    
    create_agency_usecase()
    print("✅ Agency Use Case Diagram: img/agency-usecase-diagram.png")
    
    create_admin_usecase()
    print("✅ Administrator Use Case Diagram: img/admin-usecase-diagram.png")
    
    print("\n🎉 All Clean Use Case Diagrams completed!")
    print("📋 Features:")
    print("- ✅ Clean rectangular actors (no stick figures)")
    print("- ✅ Professional elliptical use cases") 
    print("- ✅ Clear system boundaries")
    print("- ✅ Clean dotted association lines")
    print("- ✅ Proper spacing and layout")
    print("- ✅ High resolution (300 DPI)")
    print("- ✅ Ready for academic presentation")