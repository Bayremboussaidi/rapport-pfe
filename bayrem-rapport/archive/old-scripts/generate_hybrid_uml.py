"""
Hybrid UML Use Case Diagrams: Mermaid + Custom Stick Figure Assets
Best of both worlds: Mermaid's layout + proper UML stick figures
"""

def generate_customer_usecase_hybrid():
    """Generate hybrid Customer Use Case Diagram"""
    
    mermaid_code = """flowchart LR
    %% Custom stick figure actors (using our PNG assets)
    Customer["<img src='../assets/icons/customer.png' width='50'/><br/>Customer"]
    Visitor["<img src='../assets/icons/visitor.png' width='50'/><br/>Visitor"]
    
    %% System boundary with proper UML styling
    subgraph System ["🏛️ Car Rental Platform"]
        direction TB
        
        %% Authentication cluster
        subgraph Auth [" "]
            UC1("Login")
            UC2("Register") 
            UC3("Manage Profile")
        end
        
        %% Vehicle operations cluster
        subgraph Vehicle [" "]
            UC4("Browse Cars")
            UC5("Search Vehicles")
            UC6("Check Availability")
            UC7("Book Vehicle")
            UC8("Make Payment")
        end
        
        %% Booking management cluster
        subgraph Booking [" "]
            UC9("View Bookings")
            UC10("Modify Booking")
            UC11("Cancel Booking")
            UC12("Download Contract")
        end
        
        %% Communication cluster
        subgraph Comm [" "]
            UC13("Chat with Agency")
            UC14("Use Chatbot")
            UC15("Receive Notifications")
        end
        
        %% Content cluster
        subgraph Content [" "]
            UC16("Read Blog")
            UC17("Leave Comments")
            UC18("Follow Agency")
        end
    end
    
    %% Customer associations
    Customer -.-> UC1
    Customer -.-> UC3
    Customer -.-> UC4
    Customer -.-> UC5
    Customer -.-> UC6
    Customer -.-> UC7
    Customer -.-> UC8
    Customer -.-> UC9
    Customer -.-> UC10
    Customer -.-> UC11
    Customer -.-> UC12
    Customer -.-> UC13
    Customer -.-> UC14
    Customer -.-> UC15
    Customer -.-> UC16
    Customer -.-> UC17
    Customer -.-> UC18
    
    %% Visitor associations (limited)
    Visitor -.-> UC2
    Visitor -.-> UC4
    Visitor -.-> UC14
    Visitor -.-> UC16
    
    %% Include/Extend relationships
    UC1 -.->|"<<includes>>"| UC3
    UC6 -.->|"<<includes>>"| UC7
    UC7 -.->|"<<includes>>"| UC8
    UC8 -.->|"<<includes>>"| UC12
    
    %% Clean UML styling
    classDef actor fill:#FFFFFF,stroke:#000000,stroke-width:2px,color:#000000
    classDef usecase fill:#FFFFFF,stroke:#000000,stroke-width:1px,color:#000000
    classDef system fill:#F8F9FA,stroke:#000000,stroke-width:2px,color:#000000
    classDef cluster fill:transparent,stroke:transparent
    
    class Customer,Visitor actor
    class UC1,UC2,UC3,UC4,UC5,UC6,UC7,UC8,UC9,UC10,UC11,UC12,UC13,UC14,UC15,UC16,UC17,UC18 usecase
    class System system
    class Auth,Vehicle,Booking,Comm,Content cluster"""
    
    return mermaid_code

def generate_agency_usecase_hybrid():
    """Generate hybrid Agency Use Case Diagram"""
    
    mermaid_code = """flowchart LR
    %% Custom stick figure actor
    Agency["<img src='../assets/icons/agency.png' width='50'/><br/>Agency"]
    
    %% System boundary
    subgraph System ["🏢 Agency Management System"]
        direction TB
        
        %% Authentication cluster
        subgraph Auth [" "]
            UC1("Login")
            UC2("Manage Profile")
        end
        
        %% Fleet management cluster
        subgraph Fleet [" "]
            UC3("Add Vehicle")
            UC4("Edit Vehicle")
            UC5("Delete Vehicle")
            UC6("Set Pricing")
            UC7("Upload Photos")
            UC8("Manage Availability")
        end
        
        %% Booking operations cluster
        subgraph Booking [" "]
            UC9("View Requests")
            UC10("Accept Booking")
            UC11("Reject Booking")
            UC12("Generate Reports")
        end
        
        %% Communication cluster
        subgraph Comm [" "]
            UC13("Chat with Customer")
            UC14("Send Notifications")
        end
        
        %% Content cluster
        subgraph Content [" "]
            UC15("Create Blog Post")
            UC16("Manage Followers")
        end
    end
    
    %% Agency associations
    Agency -.-> UC1
    Agency -.-> UC2
    Agency -.-> UC3
    Agency -.-> UC4
    Agency -.-> UC5
    Agency -.-> UC6
    Agency -.-> UC7
    Agency -.-> UC8
    Agency -.-> UC9
    Agency -.-> UC10
    Agency -.-> UC11
    Agency -.-> UC12
    Agency -.-> UC13
    Agency -.-> UC14
    Agency -.-> UC15
    Agency -.-> UC16
    
    %% Include relationships
    UC1 -.->|"<<includes>>"| UC2
    UC3 -.->|"<<includes>>"| UC6
    UC3 -.->|"<<includes>>"| UC7
    UC10 -.->|"<<includes>>"| UC14
    
    %% Clean UML styling
    classDef actor fill:#FFFFFF,stroke:#000000,stroke-width:2px,color:#000000
    classDef usecase fill:#FFFFFF,stroke:#000000,stroke-width:1px,color:#000000
    classDef system fill:#F8F9FA,stroke:#000000,stroke-width:2px,color:#000000
    classDef cluster fill:transparent,stroke:transparent
    
    class Agency actor
    class UC1,UC2,UC3,UC4,UC5,UC6,UC7,UC8,UC9,UC10,UC11,UC12,UC13,UC14,UC15,UC16 usecase
    class System system
    class Auth,Fleet,Booking,Comm,Content cluster"""
    
    return mermaid_code

def generate_admin_usecase_hybrid():
    """Generate hybrid Administrator Use Case Diagram"""
    
    mermaid_code = """flowchart LR
    %% Custom stick figure actor
    Admin["<img src='../assets/icons/admin.png' width='50'/><br/>Administrator"]
    
    %% System boundary
    subgraph System ["⚙️ Platform Administration"]
        direction TB
        
        %% User management cluster
        subgraph Users [" "]
            UC1("Manage Agencies")
            UC2("Manage Customers")
            UC3("Manage Users")
        end
        
        %% System configuration cluster
        subgraph Config [" "]
            UC4("Configure System")
            UC5("Manage Permissions")
            UC6("View Analytics")
        end
        
        %% Content management cluster
        subgraph Content [" "]
            UC7("Moderate Content")
            UC8("Manage Blog Posts")
            UC9("Handle Reports")
        end
        
        %% Financial management cluster
        subgraph Finance [" "]
            UC10("View Revenue")
            UC11("Generate Reports")
            UC12("Manage Payments")
        end
        
        %% System maintenance cluster
        subgraph Maintenance [" "]
            UC13("Monitor System")
            UC14("Backup Data")
            UC15("Update System")
        end
    end
    
    %% Admin associations
    Admin -.-> UC1
    Admin -.-> UC2
    Admin -.-> UC3
    Admin -.-> UC4
    Admin -.-> UC5
    Admin -.-> UC6
    Admin -.-> UC7
    Admin -.-> UC8
    Admin -.-> UC9
    Admin -.-> UC10
    Admin -.-> UC11
    Admin -.-> UC12
    Admin -.-> UC13
    Admin -.-> UC14
    Admin -.-> UC15
    
    %% Include relationships
    UC4 -.->|"<<includes>>"| UC5
    UC6 -.->|"<<includes>>"| UC11
    UC13 -.->|"<<includes>>"| UC14
    
    %% Clean UML styling
    classDef actor fill:#FFFFFF,stroke:#000000,stroke-width:2px,color:#000000
    classDef usecase fill:#FFFFFF,stroke:#000000,stroke-width:1px,color:#000000
    classDef system fill:#F8F9FA,stroke:#000000,stroke-width:2px,color:#000000
    classDef cluster fill:transparent,stroke:transparent
    
    class Admin actor
    class UC1,UC2,UC3,UC4,UC5,UC6,UC7,UC8,UC9,UC10,UC11,UC12,UC13,UC14,UC15 usecase
    class System system
    class Users,Config,Content,Finance,Maintenance cluster"""
    
    return mermaid_code

if __name__ == "__main__":
    import os
    import subprocess
    
    # Generate hybrid UML diagrams
    diagrams = [
        ("customer-usecase-hybrid.mmd", generate_customer_usecase_hybrid(), "customer-usecase-diagram.png"),
        ("agency-usecase-hybrid.mmd", generate_agency_usecase_hybrid(), "agency-usecase-diagram.png"),
        ("admin-usecase-hybrid.mmd", generate_admin_usecase_hybrid(), "admin-usecase-diagram.png")
    ]
    
    os.makedirs("../img", exist_ok=True)
    
    for mmd_file, content, png_file in diagrams:
        # Save Mermaid file
        with open(f"../{mmd_file}", 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Created hybrid Mermaid file: {mmd_file}")
        
        # Generate PNG
        png_path = f"../img/{png_file}"
        try:
            cmd = ['mmdc', '-i', f"../{mmd_file}", '-o', png_path, '--width', '1600', '--height', '1000', '--scale', '2']
            subprocess.run(cmd, check=True)
            print(f"✅ Generated hybrid UML diagram: {png_path}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to generate {png_file}: {e}")
        except FileNotFoundError:
            print(f"❌ Mermaid CLI not found. Manual generation needed for {mmd_file}")
    
    print("\n🎯 Hybrid UML Use Case Diagrams Generated:")
    print("- ✅ Mermaid layout engine (clean, organized)")
    print("- ✅ Custom stick figure assets (proper UML)")
    print("- ✅ Clustered use cases (logical grouping)")
    print("- ✅ Professional appearance")
    print("- ✅ Easy to edit and maintain")