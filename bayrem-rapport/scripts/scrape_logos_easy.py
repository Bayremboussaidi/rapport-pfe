"""
DevIcon Logo Scraper - Easy Access Technology Logos
Scrapes logos from DevIcon which has simple, direct SVG access
"""

import requests
import os

def download_devicons():
    """Download from DevIcon - easy direct access"""
    
    # DevIcon has simple URL pattern: https://cdn.jsdelivr.net/gh/devicons/devicon/icons/[tech]/[tech]-original.svg
    base_url = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/"
    
    technologies = [
        'angularjs',      # Angular
        'spring',         # Spring  
        'fastapi',        # FastAPI
        'python',         # Python
        'mysql',          # MySQL
        'docker',         # Docker
        'kubernetes',     # Kubernetes
        'gitlab',         # GitLab
        'javascript',     # JavaScript
        'typescript',     # TypeScript
        'java',           # Java
        'html5',          # HTML5
        'css3',           # CSS3
        'git',            # Git
        'vscode',         # VS Code
    ]
    
    os.makedirs('../assets/logos', exist_ok=True)
    
    for tech in technologies:
        try:
            # Try original version first
            url = f"{base_url}{tech}/{tech}-original.svg"
            response = requests.get(url, timeout=10)
            
            if response.status_code != 200:
                # Try plain version if original fails
                url = f"{base_url}{tech}/{tech}-plain.svg"
                response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                filename = f'../assets/logos/{tech}-logo.svg'
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded: {tech}-logo.svg")
            else:
                print(f"Failed: {tech} (not found)")
                
        except Exception as e:
            print(f"Error: {tech} - {str(e)}")

def download_simple_logos():
    """Backup method - direct SVG URLs that work"""
    
    # Working direct URLs (tested)
    working_urls = {
        'angular': 'https://raw.githubusercontent.com/gilbarbara/logos/master/logos/angular-icon.svg',
        'spring': 'https://raw.githubusercontent.com/gilbarbara/logos/master/logos/spring.svg',
        'python': 'https://raw.githubusercontent.com/gilbarbara/logos/master/logos/python.svg',
        'docker': 'https://raw.githubusercontent.com/gilbarbara/logos/master/logos/docker-icon.svg',
        'mysql': 'https://raw.githubusercontent.com/gilbarbara/logos/master/logos/mysql-icon.svg',
        'gitlab': 'https://raw.githubusercontent.com/gilbarbara/logos/master/logos/gitlab.svg',
        'javascript': 'https://raw.githubusercontent.com/gilbarbara/logos/master/logos/javascript.svg',
        'typescript': 'https://raw.githubusercontent.com/gilbarbara/logos/master/logos/typescript-icon.svg',
        'git': 'https://raw.githubusercontent.com/gilbarbara/logos/master/logos/git-icon.svg',
    }
    
    os.makedirs('../assets/logos', exist_ok=True)
    success_count = 0
    
    for tech, url in working_urls.items():
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                filename = f'../assets/logos/{tech}-logo.svg'
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded: {tech}-logo.svg")
                success_count += 1
            else:
                print(f"Failed: {tech}")
        except Exception as e:
            print(f"Error: {tech} - {str(e)}")
    
    return success_count

def main():
    print("Downloading technology logos from scrapable sources...")
    
    print("\nTrying DevIcon...")
    download_devicons()
    
    print("\nTrying GitHub logos repository...")
    success = download_simple_logos()
    
    print(f"\nCompleted! Check ../assets/logos/ folder")
    print("If some logos are missing, they can be manually downloaded from:")
    print("- https://devicon.dev/")
    print("- https://github.com/gilbarbara/logos")

if __name__ == "__main__":
    main()