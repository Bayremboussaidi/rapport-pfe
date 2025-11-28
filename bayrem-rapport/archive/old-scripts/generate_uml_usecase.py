"""
Proper UML Use Case Diagrams Generator
Following UML standards with actors, system boundaries, and use cases
"""

def generate_customer_usecase_uml():
    """
    Generate proper UML Customer Use Case Diagram
    """
    
    mermaid_code = """---
title: Customer Use Case Diagram - Myloc Car Rental Platform
---
flowchart TD
    subgraph System ["📦 Myloc Car Rental Platform"]
        direction TB
        
        %% Authentication Use Cases
        UC1(("🔐 Login/Register"))
        UC2(("👤 Manage Profile"))
        
        %% Vehicle & Booking Use Cases  
        UC3(("🔍 Browse Cars"))
        UC4(("📅 Check Availability"))
        UC5(("🚗 Book Vehicle"))
        UC6(("💳 Make Payment"))
        
        %% Booking Management
        UC7(("📋 View Bookings"))
        UC8(("✏️ Modify Booking"))
        UC9(("📄 Download Contract"))
        
        %% Communication
        UC10(("💬 Chat with Agency"))
        UC11(("🤖 Use AI Chatbot"))
        
        %% Content Interaction
        UC12(("📖 Read Blog Posts"))
        UC13(("💬 Leave Comments"))
        UC14(("👥 Follow Agency"))
    end
    
    %% Actors
    Customer["👤<br/>Customer"]
    Visitor["🌐<br/>Visitor"]
    
    %% Customer connections
    Customer --- UC1
    Customer --- UC2
    Customer --- UC3
    Customer --- UC4
    Customer --- UC5
    Customer --- UC6
    Customer --- UC7
    Customer --- UC8
    Customer --- UC9
    Customer --- UC10
    Customer --- UC11
    Customer --- UC12
    Customer --- UC13
    Customer --- UC14
    
    %% Visitor connections (limited access)
    Visitor --- UC3
    Visitor --- UC11
    Visitor --- UC12
    Visitor --- UC1
    
    %% Dependencies
    UC4 --> UC5
    UC5 --> UC6
    UC6 --> UC9
    UC1 -.-> UC2
    
    %% Styling
    classDef actor fill:#FFE0B2,stroke:#FF8C00,stroke-width:3px,color:#000
    classDef usecase fill:#E3F2FD,stroke:#1976D2,stroke-width:2px,color:#000
    classDef system fill:#F5F5F5,stroke:#424242,stroke-width:3px,color:#000
    
    class Customer,Visitor actor
    class UC1,UC2,UC3,UC4,UC5,UC6,UC7,UC8,UC9,UC10,UC11,UC12,UC13,UC14 usecase
    class System system"""
    
    return mermaid_code

def generate_agency_usecase_uml():
    """
    Generate proper UML Agency Use Case Diagram
    """
    
    mermaid_code = """---
title: Agency Use Case Diagram - Myloc Car Rental Platform
---
flowchart TD
    subgraph System ["📦 Myloc Agency Management System"]
        direction TB
        
        %% Authentication & Profile
        UC1(("🔐 Agency Login"))
        UC2(("⚙️ Manage Settings"))
        
        %% Fleet Management
        UC3(("🚗 Manage Fleet"))
        UC4(("💰 Set Pricing"))
        UC5(("📸 Upload Photos"))
        
        %% Booking Operations
        UC6(("📋 View Reservations"))
        UC7(("✅ Confirm Bookings"))
        UC8(("❌ Reject Bookings"))
        UC9(("📊 Generate Reports"))
        
        %% Communication
        UC10(("💬 Chat with Customers"))
        UC11(("📧 Send Notifications"))
        
        %% Content Management
        UC12(("📝 Create Blog Posts"))
        UC13(("👥 Manage Followers"))
    end
    
    %% Actor
    Agency["🏢<br/>Agency"]
    
    %% Agency connections
    Agency --- UC1
    Agency --- UC2
    Agency --- UC3
    Agency --- UC4
    Agency --- UC5
    Agency --- UC6
    Agency --- UC7
    Agency --- UC8
    Agency --- UC9
    Agency --- UC10
    Agency --- UC11
    Agency --- UC12
    Agency --- UC13
    
    %% Dependencies
    UC1 -.-> UC2
    UC3 --> UC4
    UC3 --> UC5
    UC6 --> UC7
    UC6 --> UC8
    UC7 -.-> UC11
    
    %% Styling
    classDef actor fill:#FFE0B2,stroke:#FF8C00,stroke-width:3px,color:#000
    classDef usecase fill:#E8F5E8,stroke:#388E3C,stroke-width:2px,color:#000
    classDef system fill:#F5F5F5,stroke:#424242,stroke-width:3px,color:#000
    
    class Agency actor
    class UC1,UC2,UC3,UC4,UC5,UC6,UC7,UC8,UC9,UC10,UC11,UC12,UC13 usecase
    class System system"""
    
    return mermaid_code

def generate_admin_usecase_uml():
    """
    Generate proper UML Administrator Use Case Diagram
    """
    
    mermaid_code = """---
title: Administrator Use Case Diagram - Myloc Platform Management
---
flowchart TD
    subgraph System ["📦 Myloc Platform Administration"]
        direction TB
        
        %% System Administration
        UC1(("🏢 Manage Agencies"))
        UC2(("👤 Manage Users"))
        UC3(("🔧 System Config"))
        UC4(("📊 View Analytics"))
        
        %% Content Moderation
        UC5(("📝 Moderate Content"))
        UC6(("🚫 Handle Reports"))
        UC7(("📢 Manage Announcements"))
        
        %% Financial Management
        UC8(("💰 Revenue Management"))
        UC9(("📈 Financial Reports"))
        
        %% Security & Maintenance
        UC10(("🛡️ Security Monitor"))
        UC11(("🔐 Access Management"))
        UC12(("⚙️ System Maintenance"))
    end
    
    %% Actor
    Admin["👨‍💼<br/>Administrator"]
    
    %% Admin connections
    Admin --- UC1
    Admin --- UC2
    Admin --- UC3
    Admin --- UC4
    Admin --- UC5
    Admin --- UC6
    Admin --- UC7
    Admin --- UC8
    Admin --- UC9
    Admin --- UC10
    Admin --- UC11
    Admin --- UC12
    
    %% Dependencies
    UC3 -.-> UC11
    UC10 --> UC11
    UC1 -.-> UC8
    UC4 --> UC9
    
    %% Styling
    classDef actor fill:#FFE0B2,stroke:#FF8C00,stroke-width:3px,color:#000
    classDef usecase fill:#FFEBEE,stroke:#F44336,stroke-width:2px,color:#000
    classDef system fill:#F5F5F5,stroke:#424242,stroke-width:3px,color:#000
    
    class Admin actor
    class UC1,UC2,UC3,UC4,UC5,UC6,UC7,UC8,UC9,UC10,UC11,UC12 usecase
    class System system"""
    
    return mermaid_code

if __name__ == "__main__":
    import os
    import subprocess
    
    # Generate compact UML use case diagrams
    diagrams = [
        ("customer-usecase-uml.mmd", generate_customer_usecase_uml(), "customer-usecase-diagram.png"),
        ("agency-usecase-uml.mmd", generate_agency_usecase_uml(), "agency-usecase-diagram.png"),
        ("admin-usecase-uml.mmd", generate_admin_usecase_uml(), "admin-usecase-diagram.png")
    ]
    
    os.makedirs("../img", exist_ok=True)
    
    for mmd_file, content, png_file in diagrams:
        # Save Mermaid file
        with open(f"../{mmd_file}", 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Generate PNG with optimized dimensions for space
        png_path = f"../img/{png_file}"
        try:
            cmd = ['mmdc', '-i', f"../{mmd_file}", '-o', png_path, '--width', '1200', '--height', '800', '--scale', '2']
            subprocess.run(cmd, check=True)
            print(f"✅ Generated: {png_path}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to generate {png_file}: {e}")
        except FileNotFoundError:
            print(f"❌ Mermaid CLI not found. Manual generation needed for {mmd_file}")
    
    print("\n🎯 UML Use Case Diagrams Generated:")
    print("- Customer Use Case (Compact & UML-compliant)")
    print("- Agency Use Case (Compact & UML-compliant)")
    print("- Administrator Use Case (Compact & UML-compliant)")