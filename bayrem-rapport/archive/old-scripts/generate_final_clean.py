"""
Generate Clean Mermaid Diagram - Final Version
Creates the clean architecture diagram we discussed
"""

def create_clean_mermaid():
    """Create the clean Mermaid diagram code"""
    
    mermaid_code = """graph TD
    subgraph "PRESENTATION LAYER"
        A["Angular Frontend<br/><br/>• Component Architecture<br/>• Responsive Design<br/>• State Management<br/>• Route Guards & Navigation"]
    end
    
    subgraph " "
        spacer1[" "]
        style spacer1 fill:transparent,stroke:transparent
    end
    
    subgraph "APPLICATION SERVICES"
        B["Spring Boot API<br/><br/>• REST Services<br/>• Business Logic<br/>• Security Integration<br/>• Data Processing"]
        
        C["FastAPI Chatbot<br/><br/>• AI Assistant<br/>• OpenAI Integration<br/>• Real-time Chat<br/>• NLP Processing"]
        
        D["Keycloak Identity<br/><br/>• OAuth2 Authentication<br/>• JWT Token Management<br/>• Role-based Access<br/>• Single Sign-On"]
    end
    
    subgraph "  "
        spacer2[" "]
        style spacer2 fill:transparent,stroke:transparent
    end
    
    subgraph "DATA PERSISTENCE"
        E["MySQL Database<br/><br/>• User & Agency Data<br/>• Vehicle Inventory<br/>• Booking Records<br/>• Content Management"]
    end
    
    subgraph "   "
        spacer3[" "]
        style spacer3 fill:transparent,stroke:transparent
    end
    
    subgraph "INFRASTRUCTURE & DEPLOYMENT"
        F["Docker<br/>Containerization<br/><br/>• Service Isolation<br/>• Portable Deployment"]
        
        G["Kubernetes<br/>Orchestration<br/><br/>• Auto-scaling<br/>• Load Balancing"] 
        
        H["GitLab CI/CD<br/>Automation<br/><br/>• Automated Testing<br/>• Continuous Deployment"]
    end
    
    A -->|"HTTPS REST API"| B
    A -->|"WebSocket Chat"| C
    A -->|"Authentication Flow"| D
    
    B -->|"JPA/JDBC Queries"| E
    B <-->|"OAuth2/JWT Validation"| D
    
    F --> G
    G --> H
    
    spacer1 -.->|""| spacer2
    spacer2 -.->|""| spacer3
    
    classDef frontend fill:#E3F2FD,stroke:#1976D2,stroke-width:2px
    classDef backend fill:#E8F5E8,stroke:#388E3C,stroke-width:2px
    classDef ai fill:#FFF3E0,stroke:#F57C00,stroke-width:2px
    classDef auth fill:#F5F5F5,stroke:#757575,stroke-width:2px
    classDef database fill:#F3E5F5,stroke:#7C3AED,stroke-width:2px
    classDef infra fill:#F0F4FF,stroke:#1565C0,stroke-width:2px
    classDef spacer fill:transparent,stroke:transparent
    
    class A frontend
    class B backend
    class C ai
    class D auth
    class E database
    class F,G,H infra
    class spacer1,spacer2,spacer3 spacer"""
    
    # Save to file
    with open('myloc-architecture-final.mmd', 'w') as f:
        f.write(mermaid_code)
    
    print("Clean Mermaid diagram code generated: myloc-architecture-final.mmd")
    print("\nTo generate PNG:")
    print("1. Copy the content of myloc-architecture-final.mmd")
    print("2. Go to https://mermaid.live") 
    print("3. Paste the code")
    print("4. Click Export -> PNG (1200x900 or higher)")
    print("5. Save as system-architecture-overview.png in ../img/")
    
    print("\nAlternative - Use Mermaid CLI if available:")
    print("mmdc -i myloc-architecture-final.mmd -o ../img/system-architecture-overview.png -w 1200 -H 900 --scale 2")

def create_simple_backup():
    """Create a simple matplotlib version as backup"""
    
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    from matplotlib.patches import FancyBboxPatch
    import os
    
    # Simple, clean diagram
    fig, ax = plt.subplots(1, 1, figsize=(10, 12))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Clean colors
    colors = {
        'frontend': '#E3F2FD',
        'backend': '#E8F5E8', 
        'ai': '#FFF3E0',
        'auth': '#F5F5F5',
        'database': '#F3E5F5',
        'infra': '#F0F4FF'
    }
    
    fig.patch.set_facecolor('white')
    
    # Title
    plt.suptitle('Myloc Agency - System Architecture', fontsize=14, fontweight='500', y=0.95)
    
    # Simple boxes with good spacing
    boxes = [
        (2, 10, 6, 1.2, colors['frontend'], 'Angular Frontend\nPresentation Layer'),
        (1, 8, 2.5, 1.2, colors['backend'], 'Spring Boot\nAPI Services'),
        (3.75, 8, 2.5, 1.2, colors['ai'], 'FastAPI\nChatbot'),
        (6.5, 8, 2.5, 1.2, colors['auth'], 'Keycloak\nAuthentication'),
        (2, 6, 6, 1.2, colors['database'], 'MySQL Database\nData Persistence'),
        (1, 4, 2.5, 1.2, colors['infra'], 'Docker\nContainers'),
        (3.75, 4, 2.5, 1.2, colors['infra'], 'Kubernetes\nOrchestration'),
        (6.5, 4, 2.5, 1.2, colors['infra'], 'GitLab\nCI/CD')
    ]
    
    for x, y, w, h, color, text in boxes:
        box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1", 
                           facecolor=color, edgecolor='#BDBDBD', linewidth=1)
        ax.add_patch(box)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', 
                fontsize=10, fontweight='500')
    
    os.makedirs('../img', exist_ok=True)
    fig.savefig('../img/system-architecture-overview.png', dpi=300, 
                bbox_inches='tight', facecolor='white', pad_inches=0.2)
    
    print("Backup diagram generated: ../img/system-architecture-overview.png")
    plt.close()

if __name__ == "__main__":
    print("Generating clean architecture diagram...")
    
    # Create Mermaid version (preferred)
    create_clean_mermaid()
    
    # Create backup matplotlib version
    create_simple_backup()
    
    print("\nDiagram generation complete!")
    print("Primary: Use Mermaid version for best quality")
    print("Backup: Simple matplotlib version available")