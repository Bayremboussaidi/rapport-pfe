"""
Figure 2: Use Case Diagram Generator
Based on database structure and system requirements
"""

def generate_customer_usecase_diagram():
    """
    Generate Figure 2: Customer Use Case Diagram
    
    Based on database analysis:
    - Customer table with authentication
    - Booking table with car reservations
    - Car/Voiture table with vehicles
    - Chat system for communication
    - Blog/Comment system for engagement
    """
    
    mermaid_code = """graph TB
    subgraph "CUSTOMER ACTOR"
        Customer["👤 Customer<br/>(Registered User)"]
        Guest["🌐 Visitor<br/>(Guest User)"]
    end
    
    subgraph "AUTHENTICATION SYSTEM"
        UC1["🔐 Login/Register<br/>• Email/Password<br/>• Profile Management<br/>• Account Verification"]
        UC2["👤 Manage Profile<br/>• Update Information<br/>• Change Password<br/>• Upload Photo"]
    end
    
    subgraph "VEHICLE SEARCH & BOOKING"
        UC3["🔍 Browse Cars<br/>• Filter by Category<br/>• Search by Location<br/>• View Availability"]
        UC4["📅 Check Availability<br/>• Select Dates<br/>• Compare Prices<br/>• Real-time Updates"]
        UC5["🚗 Book Vehicle<br/>• Choose Car<br/>• Set Pickup/Dropoff<br/>• Confirm Details"]
        UC6["💳 Make Payment<br/>• Online Payment<br/>• Secure Transaction<br/>• Confirmation Receipt"]
    end
    
    subgraph "BOOKING MANAGEMENT"
        UC7["📋 View Bookings<br/>• Current Reservations<br/>• Booking History<br/>• Status Updates"]
        UC8["✏️ Modify Booking<br/>• Change Dates<br/>• Update Locations<br/>• Cancel Reservation"]
        UC9["📄 Generate Contract<br/>• PDF Agreement<br/>• QR Code<br/>• Email Delivery"]
    end
    
    subgraph "COMMUNICATION & SUPPORT"
        UC10["💬 Chat with Agency<br/>• Real-time Messaging<br/>• Support Queries<br/>• Booking Assistance"]
        UC11["🤖 AI Chatbot<br/>• Instant Help<br/>• FAQ Responses<br/>• 24/7 Availability"]
        UC12["📧 Receive Notifications<br/>• Booking Confirmations<br/>• Status Updates<br/>• Promotional Offers"]
    end
    
    subgraph "CONTENT INTERACTION"
        UC13["📖 Read Blog Posts<br/>• Company News<br/>• Car Reviews<br/>• Travel Tips"]
        UC14["💬 Leave Comments<br/>• Share Opinions<br/>• Rate Services<br/>• Community Interaction"]
        UC15["👥 Follow Agency<br/>• Stay Updated<br/>• Special Offers<br/>• New Vehicle Alerts"]
    end
    
    %% Customer Interactions
    Customer --> UC1
    Customer --> UC2
    Customer --> UC3
    Customer --> UC4
    Customer --> UC5
    Customer --> UC6
    Customer --> UC7
    Customer --> UC8
    Customer --> UC9
    Customer --> UC10
    Customer --> UC11
    Customer --> UC12
    Customer --> UC13
    Customer --> UC14
    Customer --> UC15
    
    %% Guest Interactions (Limited)
    Guest --> UC3
    Guest --> UC1
    Guest --> UC13
    Guest --> UC11
    Guest --> UC15
    
    %% Dependencies
    UC1 -.-> UC2
    UC4 --> UC5
    UC5 --> UC6
    UC6 --> UC9
    UC5 -.-> UC7
    UC7 --> UC8
    
    classDef actor fill:#FFE0B2,stroke:#FF8C00,stroke-width:2px
    classDef auth fill:#E8F5E8,stroke:#4CAF50,stroke-width:2px
    classDef booking fill:#E3F2FD,stroke:#2196F3,stroke-width:2px
    classDef management fill:#F3E5F5,stroke:#9C27B0,stroke-width:2px
    classDef communication fill:#FFF3E0,stroke:#FF9800,stroke-width:2px
    classDef content fill:#F5F5F5,stroke:#757575,stroke-width:2px
    
    class Customer,Guest actor
    class UC1,UC2 auth
    class UC3,UC4,UC5,UC6 booking
    class UC7,UC8,UC9 management
    class UC10,UC11,UC12 communication
    class UC13,UC14,UC15 content"""
    
    return mermaid_code

def generate_agency_usecase_diagram():
    """
    Generate Figure 3: Agency Use Case Diagram
    Based on database structure for agency operations
    """
    
    mermaid_code = """graph TB
    subgraph "AGENCY ACTOR"
        Agency["🏢 Agency<br/>(Car Rental Business)"]
    end
    
    subgraph "FLEET MANAGEMENT"
        UC1["🚗 Manage Fleet<br/>• Add New Vehicles<br/>• Update Car Details<br/>• Set Availability"]
        UC2["💰 Set Pricing<br/>• Daily Rates<br/>• Seasonal Pricing<br/>• Special Offers"]
        UC3["📍 Manage Locations<br/>• Pickup Points<br/>• Service Areas<br/>• Geographic Coverage"]
    end
    
    subgraph "BOOKING OPERATIONS"
        UC4["📋 View Reservations<br/>• Pending Bookings<br/>• Confirmed Rentals<br/>• Booking Calendar"]
        UC5["✅ Confirm Bookings<br/>• Validate Requests<br/>• Check Availability<br/>• Send Confirmations"]
        UC6["❌ Reject Bookings<br/>• Unavailable Dates<br/>• Policy Violations<br/>• Fleet Maintenance"]
        UC7["📊 Generate Reports<br/>• Revenue Analytics<br/>• Fleet Utilization<br/>• Customer Statistics"]
    end
    
    subgraph "CUSTOMER INTERACTION"
        UC8["💬 Chat with Customers<br/>• Answer Inquiries<br/>• Provide Support<br/>• Resolve Issues"]
        UC9["📧 Send Notifications<br/>• Booking Updates<br/>• Payment Reminders<br/>• Service Alerts"]
        UC10["👥 Manage Followers<br/>• Agency Promotions<br/>• Special Announcements<br/>• Loyalty Programs"]
    end
    
    subgraph "CONTENT MANAGEMENT"
        UC11["📝 Create Blog Posts<br/>• Company Updates<br/>• Vehicle Showcases<br/>• Marketing Content"]
        UC12["📸 Upload Vehicle Photos<br/>• Car Galleries<br/>• Interior/Exterior Views<br/>• High-Quality Images"]
        UC13["📱 Update Agency Profile<br/>• Contact Information<br/>• Service Description<br/>• Operating Hours"]
    end
    
    subgraph "AUTHENTICATION & PROFILE"
        UC14["🔐 Agency Login<br/>• Secure Access<br/>• Role Verification<br/>• Dashboard Access"]
        UC15["⚙️ Manage Settings<br/>• Agency Preferences<br/>• Notification Settings<br/>• Security Options"]
    end
    
    %% Agency Interactions
    Agency --> UC1
    Agency --> UC2
    Agency --> UC3
    Agency --> UC4
    Agency --> UC5
    Agency --> UC6
    Agency --> UC7
    Agency --> UC8
    Agency --> UC9
    Agency --> UC10
    Agency --> UC11
    Agency --> UC12
    Agency --> UC13
    Agency --> UC14
    Agency --> UC15
    
    %% Dependencies
    UC14 -.-> UC15
    UC1 --> UC2
    UC4 --> UC5
    UC4 --> UC6
    UC5 -.-> UC9
    UC1 -.-> UC12
    
    classDef actor fill:#FFE0B2,stroke:#FF8C00,stroke-width:2px
    classDef fleet fill:#E8F5E8,stroke:#4CAF50,stroke-width:2px
    classDef booking fill:#E3F2FD,stroke:#2196F3,stroke-width:2px
    classDef interaction fill:#FFF3E0,stroke:#FF9800,stroke-width:2px
    classDef content fill:#F3E5F5,stroke:#9C27B0,stroke-width:2px
    classDef auth fill:#F5F5F5,stroke:#757575,stroke-width:2px
    
    class Agency actor
    class UC1,UC2,UC3 fleet
    class UC4,UC5,UC6,UC7 booking
    class UC8,UC9,UC10 interaction
    class UC11,UC12,UC13 content
    class UC14,UC15 auth"""
    
    return mermaid_code

def generate_admin_usecase_diagram():
    """
    Generate Figure 4: Administrator Use Case Diagram
    Based on admin table and system administration needs
    """
    
    mermaid_code = """graph TB
    subgraph "ADMIN ACTOR"
        Admin["👨‍💼 Administrator<br/>(System Manager)"]
    end
    
    subgraph "SYSTEM ADMINISTRATION"
        UC1["🏢 Manage Agencies<br/>• Approve New Agencies<br/>• Suspend Accounts<br/>• Monitor Performance"]
        UC2["👤 Manage Users<br/>• Customer Accounts<br/>• User Verification<br/>• Account Management"]
        UC3["🔧 System Configuration<br/>• Platform Settings<br/>• Security Policies<br/>• Feature Management"]
        UC4["📊 Analytics Dashboard<br/>• Platform Metrics<br/>• Usage Statistics<br/>• Performance Reports"]
    end
    
    subgraph "CONTENT MODERATION"
        UC5["📝 Moderate Content<br/>• Review Blog Posts<br/>• Approve Comments<br/>• Content Guidelines"]
        UC6["🚫 Handle Reports<br/>• User Complaints<br/>• Policy Violations<br/>• Dispute Resolution"]
        UC7["📢 Manage Announcements<br/>• Platform Updates<br/>• Policy Changes<br/>• System Notifications"]
    end
    
    subgraph "FINANCIAL OVERSIGHT"
        UC8["💰 Revenue Management<br/>• Transaction Monitoring<br/>• Commission Tracking<br/>• Payment Disputes"]
        UC9["📈 Financial Reports<br/>• Revenue Analytics<br/>• Agency Earnings<br/>• Platform Growth"]
        UC10["💳 Payment System<br/>• Gateway Management<br/>• Transaction Security<br/>• Refund Processing"]
    end
    
    subgraph "SECURITY & COMPLIANCE"
        UC11["🛡️ Security Monitoring<br/>• Fraud Detection<br/>• Suspicious Activity<br/>• Access Control"]
        UC12["📋 Compliance Checks<br/>• Regulatory Requirements<br/>• Data Protection<br/>• Legal Compliance"]
        UC13["🔐 Access Management<br/>• Role Permissions<br/>• System Access<br/>• Security Policies"]
    end
    
    subgraph "SYSTEM MAINTENANCE"
        UC14["⚙️ Platform Maintenance<br/>• System Updates<br/>• Bug Fixes<br/>• Performance Optimization"]
        UC15["📊 Database Management<br/>• Data Backup<br/>• Performance Tuning<br/>• Data Integrity"]
        UC16["🔍 System Monitoring<br/>• Server Health<br/>• Application Performance<br/>• Error Tracking"]
    end
    
    %% Admin Interactions
    Admin --> UC1
    Admin --> UC2
    Admin --> UC3
    Admin --> UC4
    Admin --> UC5
    Admin --> UC6
    Admin --> UC7
    Admin --> UC8
    Admin --> UC9
    Admin --> UC10
    Admin --> UC11
    Admin --> UC12
    Admin --> UC13
    Admin --> UC14
    Admin --> UC15
    Admin --> UC16
    
    %% Dependencies
    UC3 -.-> UC13
    UC11 --> UC12
    UC14 --> UC15
    UC15 --> UC16
    UC1 -.-> UC8
    
    classDef actor fill:#FFE0B2,stroke:#FF8C00,stroke-width:2px
    classDef admin fill:#FFEBEE,stroke:#F44336,stroke-width:2px
    classDef content fill:#E8F5E8,stroke:#4CAF50,stroke-width:2px
    classDef financial fill:#E3F2FD,stroke:#2196F3,stroke-width:2px
    classDef security fill:#FFF3E0,stroke:#FF9800,stroke-width:2px
    classDef maintenance fill:#F3E5F5,stroke:#9C27B0,stroke-width:2px
    
    class Admin actor
    class UC1,UC2,UC3,UC4 admin
    class UC5,UC6,UC7 content
    class UC8,UC9,UC10 financial
    class UC11,UC12,UC13 security
    class UC14,UC15,UC16 maintenance"""
    
    return mermaid_code

if __name__ == "__main__":
    import os
    import subprocess
    
    # Generate all use case diagrams
    diagrams = [
        ("customer-usecase.mmd", generate_customer_usecase_diagram(), "customer-usecase-diagram.png"),
        ("agency-usecase.mmd", generate_agency_usecase_diagram(), "agency-usecase-diagram.png"),
        ("admin-usecase.mmd", generate_admin_usecase_diagram(), "admin-usecase-diagram.png")
    ]
    
    os.makedirs("../img", exist_ok=True)
    
    for mmd_file, content, png_file in diagrams:
        # Save Mermaid file
        with open(f"../{mmd_file}", 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Generate PNG
        png_path = f"../img/{png_file}"
        try:
            cmd = ['mmdc', '-i', f"../{mmd_file}", '-o', png_path, '--width', '1400', '--height', '1000', '--scale', '2']
            subprocess.run(cmd, check=True)
            print(f"✅ Generated: {png_path}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to generate {png_file}: {e}")
        except FileNotFoundError:
            print(f"❌ Mermaid CLI not found. Manual generation needed for {mmd_file}")
    
    print("\n🎯 Use Case Diagrams Generated:")
    print("- Figure 2: Customer Use Case Diagram")
    print("- Figure 3: Agency Use Case Diagram") 
    print("- Figure 4: Administrator Use Case Diagram")