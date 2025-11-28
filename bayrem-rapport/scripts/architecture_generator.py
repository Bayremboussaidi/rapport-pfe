"""
System Architecture Diagram Generator - FINAL VERSION
This is the only script needed for Figure 1: System Architecture Overview

Usage: python architecture_generator.py
Output: ../img/system-architecture-overview.png

The script generates a clean Mermaid diagram and compiles it to PNG
"""

def generate_clean_architecture():
    """Generate the final clean architecture diagram"""
    
    mermaid_code = """graph TD
    subgraph "PRESENTATION LAYER"
        A["🅰️ Angular Frontend<br/><br/>• Component Architecture<br/>• Responsive Design<br/>• State Management<br/>• Route Guards"]
    end
    
    subgraph "APPLICATION SERVICES"
        B["🍃 Spring Boot API<br/><br/>• REST Services<br/>• Business Logic<br/>• Security Integration<br/>• Data Processing"]
        
        C["⚡ FastAPI Chatbot<br/><br/>• AI Assistant<br/>• OpenAI Integration<br/>• Real-time Chat<br/>• NLP Processing"]
        
        D["🔐 Keycloak Identity<br/><br/>• OAuth2 Authentication<br/>• JWT Token Management<br/>• Role-based Access<br/>• Single Sign-On"]
    end
    
    subgraph "DATA PERSISTENCE"
        E["🗃️ MySQL Database<br/><br/>• User & Agency Data<br/>• Vehicle Inventory<br/>• Booking Records<br/>• Content Management"]
    end
    
    subgraph "INFRASTRUCTURE"
        F["🐳 Docker<br/>Containerization<br/><br/>• Service Isolation<br/>• Portable Deployment"]
        
        G["☸️ Kubernetes<br/>Orchestration<br/><br/>• Auto-scaling<br/>• Load Balancing"] 
        
        H["🦊 GitLab CI/CD<br/>Automation<br/><br/>• Automated Testing<br/>• Continuous Deployment"]
    end
    
    A -->|"HTTPS REST"| B
    A -->|"WebSocket"| C
    A -->|"Auth Flow"| D
    
    B -->|"JDBC"| E
    B <-->|"JWT"| D
    
    B --> F
    C --> F
    D --> F
    F --> G
    G --> H
    
    classDef frontend fill:#E3F2FD,stroke:#1976D2,stroke-width:2px
    classDef backend fill:#E8F5E8,stroke:#388E3C,stroke-width:2px
    classDef ai fill:#FFF3E0,stroke:#F57C00,stroke-width:2px
    classDef auth fill:#F5F5F5,stroke:#757575,stroke-width:2px
    classDef database fill:#F3E5F5,stroke:#7C3AED,stroke-width:2px
    classDef infra fill:#F0F4FF,stroke:#1565C0,stroke-width:2px
    
    class A frontend
    class B backend
    class C ai
    class D auth
    class E database
    class F,G,H infra"""
    
    import os
    
    # Save Mermaid file
    with open('../archive/architecture-clean.mmd', 'w') as f:
        f.write(mermaid_code)
    
    # Generate PNG using mermaid CLI
    os.makedirs('../img', exist_ok=True)
    
    # Command to run
    cmd = 'mmdc -i ../archive/architecture-clean.mmd -o ../img/system-architecture-overview.png --width 1200 --height 900 --scale 2'
    
    print("Generated files:")
    print("- Mermaid source: ../archive/architecture-clean.mmd")
    print("- PNG diagram: ../img/system-architecture-overview.png")
    print(f"\nTo regenerate, run: {cmd}")
    
    # Run the command
    result = os.system(cmd)
    if result == 0:
        print("✅ PNG generated successfully!")
    else:
        print("❌ PNG generation failed")
        print("Try running the command manually or use mermaid.live")

if __name__ == "__main__":
    generate_clean_architecture()