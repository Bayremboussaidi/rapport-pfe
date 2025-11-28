"""
FIGURE GENERATOR TOOLKIT - REPRODUCIBLE & EDITABLE
===============================================

This script provides a clean, reproducible approach for generating all diagram figures.
Each figure has its own function with clear parameters for easy editing.

Dependencies:
- Node.js with @mermaid-js/mermaid-cli installed: npm install -g @mermaid-js/mermaid-cli
- Or use mermaid.live for manual generation

Usage:
    python figure_generator.py --figure 1    # Generate Figure 1 (Architecture)
    python figure_generator.py --all         # Generate all figures
"""

import os
import argparse
import subprocess

class FigureGenerator:
    """Reproducible figure generator for academic report"""
    
    def __init__(self):
        self.output_dir = "../img"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_figure_1_architecture(self):
        """
        Figure 1: System Architecture Overview
        
        Editable parameters:
        - Colors: Change classDef colors below
        - Layout: Modify subgraph structure
        - Content: Update node descriptions
        - Connections: Modify arrows and labels
        """
        
        # EDITABLE CONFIGURATION
        colors = {
            'frontend': '#E3F2FD,stroke:#1976D2',
            'backend': '#E8F5E8,stroke:#388E3C', 
            'ai': '#FFF3E0,stroke:#F57C00',
            'auth': '#F5F5F5,stroke:#757575',
            'database': '#F3E5F5,stroke:#7C3AED',
            'infra': '#F0F4FF,stroke:#1565C0'
        }
        
        # EDITABLE CONTENT
        nodes = {
            'A': '🅰️ Angular Frontend<br/><br/>• Component Architecture<br/>• Responsive Design<br/>• State Management<br/>• Route Guards',
            'B': '🍃 Spring Boot API<br/><br/>• REST Services<br/>• Business Logic<br/>• Security Integration<br/>• Data Processing',
            'C': '⚡ FastAPI Chatbot<br/><br/>• AI Assistant<br/>• OpenAI Integration<br/>• Real-time Chat<br/>• NLP Processing',
            'D': '🔐 Keycloak Identity<br/><br/>• OAuth2 Authentication<br/>• JWT Token Management<br/>• Role-based Access<br/>• Single Sign-On',
            'E': '🗃️ MySQL Database<br/><br/>• User & Agency Data<br/>• Vehicle Inventory<br/>• Booking Records<br/>• Content Management',
            'F': '🐳 Docker<br/>Containerization<br/><br/>• Service Isolation<br/>• Portable Deployment',
            'G': '☸️ Kubernetes<br/>Orchestration<br/><br/>• Auto-scaling<br/>• Load Balancing',
            'H': '🦊 GitLab CI/CD<br/>Automation<br/><br/>• Automated Testing<br/>• Continuous Deployment'
        }
        
        # EDITABLE CONNECTIONS
        connections = [
            'A -->|"HTTPS REST"| B',
            'A -->|"WebSocket"| C', 
            'A -->|"Auth Flow"| D',
            'B -->|"JDBC"| E',
            'B <-->|"JWT"| D',
            'B --> F',
            'C --> F',
            'D --> F',
            'F --> G',
            'G --> H'
        ]
        
        # Generate Mermaid code
        mermaid_code = f'''graph TD
    subgraph "PRESENTATION LAYER"
        A["{nodes['A']}"]
    end
    
    subgraph "APPLICATION SERVICES"
        B["{nodes['B']}"]
        C["{nodes['C']}"]
        D["{nodes['D']}"]
    end
    
    subgraph "DATA PERSISTENCE"
        E["{nodes['E']}"]
    end
    
    subgraph "INFRASTRUCTURE"
        F["{nodes['F']}"]
        G["{nodes['G']}"]
        H["{nodes['H']}"]
    end
    
    {chr(10).join(connections)}
    
    classDef frontend fill:{colors['frontend']},stroke-width:2px
    classDef backend fill:{colors['backend']},stroke-width:2px
    classDef ai fill:{colors['ai']},stroke-width:2px
    classDef auth fill:{colors['auth']},stroke-width:2px
    classDef database fill:{colors['database']},stroke-width:2px
    classDef infra fill:{colors['infra']},stroke-width:2px
    
    class A frontend
    class B backend
    class C ai
    class D auth
    class E database
    class F,G,H infra'''
        
        # Save source file
        mmd_file = "../architecture-clean.mmd"
        with open(mmd_file, 'w', encoding='utf-8') as f:
            f.write(mermaid_code)
        
        # Generate PNG
        png_file = f"{self.output_dir}/system-architecture-overview.png"
        
        try:
            cmd = ['mmdc', '-i', mmd_file, '-o', png_file, '--width', '1200', '--height', '900', '--scale', '2']
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            print(f"✅ Figure 1 generated: {png_file}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Mermaid CLI failed: {e}")
            print(f"📝 Manual generation: Copy {mmd_file} to https://mermaid.live")
            return False
        except FileNotFoundError:
            print("❌ Mermaid CLI not found. Install with: npm install -g @mermaid-js/mermaid-cli")
            print(f"📝 Manual generation: Copy {mmd_file} to https://mermaid.live")
            return False
    
    def generate_figure_2_usecase(self):
        """
        Figure 2: Customer Use Case Diagram
        
        Generated from database analysis showing customer interactions
        with the car rental platform including authentication, booking, 
        and communication features.
        """
        
        # Import the use case generator
        import sys
        import os
        sys.path.append(os.path.dirname(__file__))
        
        from generate_usecase_diagrams import generate_customer_usecase_diagram
        
        # Generate Mermaid code
        mermaid_code = generate_customer_usecase_diagram()
        
        # Save source file
        mmd_file = "../customer-usecase.mmd"
        with open(mmd_file, 'w', encoding='utf-8') as f:
            f.write(mermaid_code)
        
        # Generate PNG
        png_file = f"{self.output_dir}/customer-usecase-diagram.png"
        
        try:
            cmd = ['mmdc', '-i', mmd_file, '-o', png_file, '--width', '1400', '--height', '1000', '--scale', '2']
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            print(f"✅ Figure 2 generated: {png_file}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Mermaid CLI failed: {e}")
            print(f"📝 Manual generation: Copy {mmd_file} to https://mermaid.live")
            return False
        except FileNotFoundError:
            print("❌ Mermaid CLI not found. Install with: npm install -g @mermaid-js/mermaid-cli")
            print(f"📝 Manual generation: Copy {mmd_file} to https://mermaid.live")
            return False
    
    def generate_figure_3_class(self):
        """Figure 3: Class Diagram - TO BE IMPLEMENTED"""  
        print("🔄 Figure 3 (Class Diagram) - Ready for implementation")
        return True
    
    def generate_all_figures(self):
        """Generate all figures"""
        results = []
        results.append(self.generate_figure_1_architecture())
        results.append(self.generate_figure_2_usecase())
        results.append(self.generate_figure_3_class())
        
        success_count = sum(results)
        print(f"\n📊 Generated {success_count}/{len(results)} figures successfully")

def main():
    parser = argparse.ArgumentParser(description='Generate figures for academic report')
    parser.add_argument('--figure', type=int, help='Generate specific figure number (1, 2, 3, etc.)')
    parser.add_argument('--all', action='store_true', help='Generate all figures')
    
    args = parser.parse_args()
    generator = FigureGenerator()
    
    if args.figure == 1:
        generator.generate_figure_1_architecture()
    elif args.figure == 2:
        generator.generate_figure_2_usecase()
    elif args.figure == 3:
        generator.generate_figure_3_class()
    elif args.all:
        generator.generate_all_figures()
    else:
        print("Usage: python figure_generator.py --figure 1 or --all")

if __name__ == "__main__":
    main()