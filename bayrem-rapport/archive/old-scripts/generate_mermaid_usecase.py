"""
Generate Clean Mermaid Use Case Diagrams with Organized Layout
Using same approach as system architecture - clean Mermaid + custom assets
"""

def create_customer_mermaid():
    """Create organized Customer Use Case with grouped connections"""
    
    mermaid_code = """flowchart TD
    %% Actors (will add stick figure assets later)
    Customer[👤 Customer]
    Visitor[👤 Visitor]
    
    %% System boundary with grouped use cases
    subgraph Platform ["🏢 Car Rental Platform"]
        direction TB
        
        %% Authentication group
        subgraph AuthGroup [" "]
            UC1("🔐 Login")
            UC2("📝 Register") 
            UC3("👤 Manage Profile")
        end
        
        %% Vehicle browsing group  
        subgraph BrowseGroup [" "]
            UC4("🚗 Browse Cars")
            UC5("🔍 Search Vehicles")
            UC6("📅 Check Availability")
        end
        
        %% Booking process group
        subgraph BookingGroup [" "]
            UC7("📋 Book Vehicle")
            UC8("💳 Make Payment")
            UC9("📄 Download Contract")
        end
        
        %% Management group
        subgraph ManageGroup [" "]
            UC10("📊 View Bookings")
            UC11("✏️ Modify Booking")
            UC12("❌ Cancel Booking")
        end
        
        %% Communication group
        subgraph CommGroup [" "]
            UC13("💬 Chat with Agency")
            UC14("🤖 Use Chatbot")
            UC15("🔔 Receive Notifications")
        end
        
        %% Content group
        subgraph ContentGroup [" "]
            UC16("📰 Read Blog")
            UC17("💭 Leave Comments")
            UC18("👥 Follow Agency")
        end
    end
    
    %% Clean organized connections - Customer
    Customer -.-> AuthGroup
    Customer -.-> BrowseGroup
    Customer -.-> BookingGroup
    Customer -.-> ManageGroup
    Customer -.-> CommGroup
    Customer -.-> ContentGroup
    
    %% Limited Visitor connections
    Visitor -.-> UC2
    Visitor -.-> UC4
    Visitor -.-> UC14
    Visitor -.-> UC16
    
    %% Include relationships (within groups)
    UC1 -->|includes| UC3
    UC6 -->|includes| UC7
    UC7 -->|includes| UC8
    UC8 -->|includes| UC9
    
    %% Clean styling
    classDef actor fill:#E8F4FD,stroke:#1976D2,stroke-width:3px,color:#000
    classDef usecase fill:#FFFFFF,stroke:#424242,stroke-width:2px,color:#000
    classDef system fill:#F8F9FA,stroke:#1976D2,stroke-width:3px,color:#1976D2
    classDef group fill:#FAFAFA,stroke:#BDBDBD,stroke-width:1px,color:#666
    
    class Customer,Visitor actor
    class UC1,UC2,UC3,UC4,UC5,UC6,UC7,UC8,UC9,UC10,UC11,UC12,UC13,UC14,UC15,UC16,UC17,UC18 usecase
    class Platform system
    class AuthGroup,BrowseGroup,BookingGroup,ManageGroup,CommGroup,ContentGroup group"""
    
    return mermaid_code

def create_agency_mermaid():
    """Create organized Agency Use Case diagram"""
    
    mermaid_code = """flowchart TD
    %% Actor
    Agency[👤 Agency]
    
    %% System boundary with grouped functionality
    subgraph System ["🏢 Agency Management System"]
        direction TB
        
        %% Profile & Authentication
        subgraph ProfileGroup [" "]
            UC1("🔐 Login")
            UC2("👤 Manage Profile")
        end
        
        %% Vehicle Management
        subgraph VehicleGroup [" "]
            UC3("➕ Add Vehicle")
            UC4("✏️ Edit Vehicle")
            UC5("🗑️ Delete Vehicle")
            UC6("💰 Set Pricing")
            UC7("📸 Upload Photos")
            UC8("📅 Manage Availability")
        end
        
        %% Request Handling
        subgraph RequestGroup [" "]
            UC9("📋 View Requests")
            UC10("✅ Accept Booking")
            UC11("❌ Reject Booking")
        end
        
        %% Communication & Reports
        subgraph CommReportGroup [" "]
            UC12("📊 Generate Reports")
            UC13("💬 Chat with Customer")
            UC14("🔔 Send Notifications")
            UC15("📰 Create Blog Post")
            UC16("👥 Manage Followers")
        end
    end
    
    %% Clean organized connections
    Agency -.-> ProfileGroup
    Agency -.-> VehicleGroup  
    Agency -.-> RequestGroup
    Agency -.-> CommReportGroup
    
    %% Include relationships
    UC1 -->|includes| UC2
    UC3 -->|includes| UC6
    UC3 -->|includes| UC7
    UC10 -->|includes| UC14
    
    %% Styling
    classDef actor fill:#E8F4FD,stroke:#1976D2,stroke-width:3px,color:#000
    classDef usecase fill:#FFFFFF,stroke:#424242,stroke-width:2px,color:#000
    classDef system fill:#F8F9FA,stroke:#1976D2,stroke-width:3px,color:#1976D2
    classDef group fill:#FAFAFA,stroke:#BDBDBD,stroke-width:1px,color:#666
    
    class Agency actor
    class UC1,UC2,UC3,UC4,UC5,UC6,UC7,UC8,UC9,UC10,UC11,UC12,UC13,UC14,UC15,UC16 usecase
    class System system
    class ProfileGroup,VehicleGroup,RequestGroup,CommReportGroup group"""
    
    return mermaid_code

def create_admin_mermaid():
    """Create organized Administrator Use Case diagram"""
    
    mermaid_code = """flowchart TD
    %% Actor
    Admin[👤 Administrator]
    
    %% System boundary with grouped functionality  
    subgraph System ["🏢 Platform Administration"]
        direction TB
        
        %% User Management
        subgraph UserMgmtGroup [" "]
            UC1("🏢 Manage Agencies")
            UC2("👥 Manage Customers")
            UC3("👤 Manage Users")
        end
        
        %% System Configuration
        subgraph SysConfigGroup [" "]
            UC4("⚙️ Configure System")
            UC5("🔐 Manage Permissions")
            UC6("🔄 Update System")
        end
        
        %% Analytics & Monitoring
        subgraph AnalyticsGroup [" "]
            UC7("📈 View Analytics")
            UC8("🖥️ Monitor System")
            UC9("💾 Backup Data")
        end
        
        %% Content & Financial
        subgraph ContentFinGroup [" "]
            UC10("🛡️ Moderate Content")
            UC11("📰 Manage Blog Posts")
            UC12("⚠️ Handle Reports")
            UC13("💰 View Revenue")
            UC14("📊 Generate Reports")
            UC15("💳 Manage Payments")
        end
    end
    
    %% Clean organized connections
    Admin -.-> UserMgmtGroup
    Admin -.-> SysConfigGroup
    Admin -.-> AnalyticsGroup
    Admin -.-> ContentFinGroup
    
    %% Include relationships
    UC4 -->|includes| UC5
    UC7 -->|includes| UC14
    UC8 -->|includes| UC9
    
    %% Styling
    classDef actor fill:#E8F4FD,stroke:#1976D2,stroke-width:3px,color:#000
    classDef usecase fill:#FFFFFF,stroke:#424242,stroke-width:2px,color:#000
    classDef system fill:#F8F9FA,stroke:#1976D2,stroke-width:3px,color:#1976D2
    classDef group fill:#FAFAFA,stroke:#BDBDBD,stroke-width:1px,color:#666
    
    class Admin actor
    class UC1,UC2,UC3,UC4,UC5,UC6,UC7,UC8,UC9,UC10,UC11,UC12,UC13,UC14,UC15 usecase
    class System system
    class UserMgmtGroup,SysConfigGroup,AnalyticsGroup,ContentFinGroup group"""
    
    return mermaid_code

if __name__ == "__main__":
    import os
    import subprocess
    
    # Generate organized Mermaid diagrams
    diagrams = [
        ("customer-usecase-organized.mmd", create_customer_mermaid(), "customer-usecase-diagram.png"),
        ("agency-usecase-organized.mmd", create_agency_mermaid(), "agency-usecase-diagram.png"),
        ("admin-usecase-organized.mmd", create_admin_mermaid(), "admin-usecase-diagram.png")
    ]
    
    os.makedirs("../img", exist_ok=True)
    
    for mmd_file, content, png_file in diagrams:
        # Save Mermaid file
        with open(f"../{mmd_file}", 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Created organized Mermaid: {mmd_file}")
        
        # Generate PNG (if mmdc available, otherwise manual)
        png_path = f"../img/{png_file}"
        try:
            cmd = ['mmdc', '-i', f"../{mmd_file}", '-o', png_path, '--width', '1400', '--height', '1000', '--scale', '2', '--backgroundColor', 'white']
            subprocess.run(cmd, check=True)
            print(f"✅ Generated organized diagram: {png_path}")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print(f"⚠️ Mermaid CLI not found. Please generate manually: {mmd_file}")
    
    print("\n🎯 Organized Mermaid Use Case Diagrams:")
    print("- ✅ Grouped related use cases together")
    print("- ✅ Clean organized connection lines") 
    print("- ✅ Logical flow instead of chaotic arrows")
    print("- ✅ Ready for stick figure assets")
    print("- ✅ Professional UML structure")
    print("\n💡 Next: Add custom stick figure assets like system architecture!")