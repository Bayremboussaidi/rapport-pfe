"""
Technology Logo Collector for Myloc Agency Architecture
Downloads logos from Simple Icons and other sources
"""

import requests
import os
from urllib.parse import urljoin

def create_assets_structure():
    """Create assets directory structure"""
    os.makedirs('../assets/logos', exist_ok=True)
    print("Created assets/logos directory")

def download_simple_icons():
    """Download logos from Simple Icons (best source)"""
    
    # Simple Icons base URL for direct SVG download
    base_url = "https://cdn.jsdelivr.net/npm/simple-icons@v10.9.0/icons/"
    
    # Technology logos we need
    logos_needed = {
        'angular': 'angular.svg',
        'spring': 'spring.svg', 
        'springboot': 'springboot.svg',
        'fastapi': 'fastapi.svg',
        'python': 'python.svg',
        'mysql': 'mysql.svg',
        'docker': 'docker.svg',
        'kubernetes': 'kubernetes.svg',
        'gitlab': 'gitlab.svg',
        'javascript': 'javascript.svg',
        'typescript': 'typescript.svg',
        'html5': 'html5.svg',
        'css3': 'css3.svg',
        'git': 'git.svg',
        'visualstudiocode': 'visualstudiocode.svg',
        'postman': 'postman.svg',
        'java': 'openjdk.svg'  # OpenJDK logo for Java
    }
    
    success_count = 0
    
    for tech_name, filename in logos_needed.items():
        try:
            url = base_url + filename
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                # Save to assets folder
                filepath = f'../assets/logos/{tech_name}-logo.svg'
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded: {tech_name}-logo.svg")
                success_count += 1
            else:
                print(f"Failed to download: {tech_name} (Status: {response.status_code})")
                
        except Exception as e:
            print(f"Error downloading {tech_name}: {str(e)}")
    
    print(f"\nDownloaded {success_count}/{len(logos_needed)} logos successfully")
    return success_count

def create_logo_list():
    """Create a list of available logos"""
    logo_info = """
# Downloaded Technology Logos

## Available Logos in /assets/logos/:

### Frontend Technologies:
- angular-logo.svg (Angular framework)
- javascript-logo.svg (JavaScript language)
- typescript-logo.svg (TypeScript)
- html5-logo.svg (HTML5)
- css3-logo.svg (CSS3)

### Backend Technologies:
- spring-logo.svg (Spring Framework)
- springboot-logo.svg (Spring Boot)
- java-logo.svg (Java/OpenJDK)
- fastapi-logo.svg (FastAPI)
- python-logo.svg (Python)

### Database:
- mysql-logo.svg (MySQL)

### DevOps & Infrastructure:
- docker-logo.svg (Docker)
- kubernetes-logo.svg (Kubernetes)
- gitlab-logo.svg (GitLab)

### Development Tools:
- git-logo.svg (Git)
- visualstudiocode-logo.svg (VS Code)
- postman-logo.svg (Postman)

## Usage in Diagrams:
All logos are SVG format for scalability.
Consistent sizing: 32x32px to 64x64px recommended.
Official brand colors preserved.

## Logo Sources:
- Simple Icons (https://simpleicons.org/) - Primary source
- Official brand guidelines compliance
- Free and open source licensing
"""
    
    with open('../assets/logo-inventory.md', 'w') as f:
        f.write(logo_info)
    
    print("Created logo inventory file: ../assets/logo-inventory.md")

def main():
    print("Collecting technology logos for architecture diagram...")
    
    # Create directory structure
    create_assets_structure()
    
    # Download logos from Simple Icons
    print("\nDownloading from Simple Icons...")
    success_count = download_simple_icons()
    
    # Create inventory
    create_logo_list()
    
    if success_count > 0:
        print(f"\nSuccess! Downloaded {success_count} technology logos")
        print("Logos saved to: ../assets/logos/")
        print("\nNext steps:")
        print("1. Check ../assets/logos/ folder")
        print("2. All logos are in SVG format") 
        print("3. Ready for integration into architecture diagram")
        print("4. Use in Mermaid or other diagram tools")
    else:
        print("\nNo logos downloaded. Check internet connection.")
        print("Alternative: Manual download from https://simpleicons.org/")

if __name__ == "__main__":
    main()