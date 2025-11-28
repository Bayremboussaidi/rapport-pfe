# Figure Generation Scripts - Myloc Agency Car Rental Platform

**Project:** Car Rental Platform for Myloc Agency  
**Founder:** Amine Ben Chaabane  
**Style:** Technical/Engineering Academic Presentation  
**Tool Preference:** Draw.io compatible layouts  

---

## 🏗️ **Figure 1: System Architecture Overview Diagram**

**Location:** Chapter 1 - Project Context  
**Purpose:** High-level system architecture showing microservices communication

### Visual Description Script:
```
DIAGRAM TYPE: Multi-tier architecture diagram with component boxes and arrows
LAYOUT: Horizontal flow from left to right with 3 main tiers

COMPONENTS:
1. PRESENTATION LAYER (Left):
   - Rectangle: "Angular Frontend" (Blue #2196F3)
   - Icons: Browser, Mobile device
   - Label: "User Interface Layer"

2. APPLICATION LAYER (Center):
   - Rectangle: "Spring Boot API" (Green #4CAF50)
   - Rectangle: "FastAPI Chatbot" (Orange #FF9800)
   - Rectangle: "Keycloak Auth Server" (Red #F44336)
   - Label: "Business Logic Layer"

3. DATA LAYER (Right):
   - Rectangle: "MySQL Database" (Purple #9C27B0)
   - Label: "Data Persistence Layer"

4. DEPLOYMENT LAYER (Bottom):
   - Rectangle: "Docker Containers" (Cyan #00BCD4)
   - Rectangle: "Kubernetes Cluster" (Navy #1976D2)
   - Rectangle: "GitLab CI/CD" (Orange #FF5722)

CONNECTIONS:
- Angular ↔ Spring Boot (HTTPS REST API)
- Angular ↔ FastAPI (WebSocket/HTTP)
- Spring Boot ↔ Keycloak (OAuth2/JWT)
- Spring Boot ↔ MySQL (JPA/JDBC)
- All services ↔ Docker (Containerization)

STYLING:
- Clean rectangles with rounded corners
- Color-coded by function
- Dotted lines for async communication
- Solid lines for synchronous calls
- Drop shadows for depth
```

---

## 👤 **Figure 2: Customer Use Case Diagram**

**Location:** Chapter 2 - Needs Analysis  
**Purpose:** Customer interactions and capabilities

### Visual Description Script:
```
DIAGRAM TYPE: UML Use Case Diagram
LAYOUT: Central actor with surrounding use cases

ACTOR:
- Stick figure: "Customer" (Left side)
- Label: "Authenticated User"

USE CASES (Ellipses around center):
1. "Browse Available Cars" - (Top)
2. "Search and Filter Cars" - (Top right)
3. "Submit Rental Request" - (Right)
4. "View Booking History" - (Bottom right)
5. "Receive Email Notifications" - (Bottom)
6. "Comment on Cars/Blogs" - (Bottom left)
7. "Chat with Support" - (Left)
8. "Manage Profile" - (Top left)
9. "Download PDF Contract" - (Center right)

SYSTEM BOUNDARY:
- Rectangle encompassing all use cases
- Label: "Car Rental Platform"

RELATIONSHIPS:
- Lines from Customer to all use cases
- <<include>> "Login Authentication" (dotted arrow)
- <<extend>> "Payment Processing" from "Submit Rental Request"

STYLING:
- Professional UML notation
- Consistent ellipse sizing
- Clean connection lines
- System boundary clearly marked
```

---

## 🏢 **Figure 3: Agency Use Case Diagram**

**Location:** Chapter 2 - Needs Analysis  
**Purpose:** Agency user interactions and management capabilities

### Visual Description Script:
```
DIAGRAM TYPE: UML Use Case Diagram
LAYOUT: Central actor with business-focused use cases

ACTOR:
- Stick figure: "Agency User" (Left side)
- Label: "Car Rental Agency"

USE CASES (Ellipses around center):
1. "Manage Car Inventory" - (Top)
2. "Add/Edit Car Details" - (Top right)
3. "Upload Car Photos" - (Right)
4. "Review Rental Requests" - (Center right)
5. "Accept/Decline Bookings" - (Bottom right)
6. "Set Car Availability" - (Bottom)
7. "Send Notifications" - (Bottom left)
8. "Chat with Admin" - (Left)
9. "Generate Reports" - (Top left)
10. "Manage Agency Profile" - (Center left)

SYSTEM BOUNDARY:
- Rectangle encompassing all use cases
- Label: "Agency Management Module"

RELATIONSHIPS:
- Lines from Agency to all use cases
- <<include>> "Authentication" (dotted)
- <<extend>> "Email Notifications" from multiple use cases

STYLING:
- Business-oriented color scheme (Green tones)
- Clear actor positioning
- Organized use case groupings
```

---

## 👨‍💼 **Figure 4: Administrator Use Case Diagram**

**Location:** Chapter 2 - Needs Analysis  
**Purpose:** System administration capabilities

### Visual Description Script:
```
DIAGRAM TYPE: UML Use Case Diagram
LAYOUT: Central admin actor with system management use cases

ACTOR:
- Stick figure: "Administrator" (Left side)
- Crown icon or admin badge
- Label: "System Administrator"

USE CASES (Ellipses around center):
1. "Manage Agencies" - (Top)
2. "Manage Customers" - (Top right)
3. "Create/Edit Blogs" - (Right)
4. "Monitor System Health" - (Center right)
5. "Configure Security Settings" - (Bottom right)
6. "View All Bookings" - (Bottom)
7. "Send System Notifications" - (Bottom left)
8. "Chat with Agencies" - (Left)
9. "Generate System Reports" - (Top left)
10. "Backup Management" - (Center left)
11. "User Role Assignment" - (Center)

SYSTEM BOUNDARY:
- Rectangle encompassing all use cases
- Label: "Administrative Control Panel"

RELATIONSHIPS:
- Lines from Administrator to all use cases
- <<include>> "Super Admin Authentication" (dotted)
- <<extend>> "Audit Logging" from critical operations

STYLING:
- Administrative red/blue color scheme
- Hierarchical use case organization
- Security-focused visual elements
```

---

## 📊 **Figure 5: Global Class Diagram (ERD)**

**Location:** Chapter 2 - System Design  
**Purpose:** Database entity relationships and system data model

### Visual Description Script:
```
DIAGRAM TYPE: Enhanced ERD/Class Diagram hybrid
LAYOUT: Centered relationship network with clear associations

MAIN ENTITIES (Rectangles with attributes):

1. USER:
   - id: BIGINT (PK)
   - username: VARCHAR(50)
   - email: VARCHAR(100)
   - password: VARCHAR(64)
   - role: ENUM(admin, agency, customer)
   - created_at: TIMESTAMP

2. AGENCY:
   - id: BIGINT (PK)
   - agency_name: VARCHAR(100)
   - email: VARCHAR(255)
   - phone_number: VARCHAR(20)
   - city: VARCHAR(100)
   - photo: LONGTEXT
   - user_id: BIGINT (FK)

3. VOITURE (CAR):
   - id: BIGINT (PK)
   - name: VARCHAR(100)
   - model: VARCHAR(50)
   - type: VARCHAR(50)
   - price_per_day: DECIMAL(10,2)
   - photos: JSON
   - agency_id: BIGINT (FK)
   - available: BOOLEAN

4. BOOKING:
   - id: BIGINT (PK)
   - customer_id: BIGINT (FK)
   - voiture_id: BIGINT (FK)
   - start_date: DATE
   - end_date: DATE
   - total_price: DECIMAL(10,2)
   - status: ENUM(pending, confirmed, declined)
   - created_at: TIMESTAMP

5. BLOG:
   - id: BIGINT (PK)
   - title: VARCHAR(255)
   - content: TEXT
   - author_id: BIGINT (FK)
   - img_url: VARCHAR(255)
   - published_date: TIMESTAMP

6. NOTIFICATION:
   - id: BIGINT (PK)
   - user_id: BIGINT (FK)
   - message: TEXT
   - type: VARCHAR(50)
   - read_status: BOOLEAN
   - created_at: TIMESTAMP

RELATIONSHIPS:
- USER (1) → (0..*) AGENCY
- AGENCY (1) → (0..*) VOITURE
- USER (1) → (0..*) BOOKING
- VOITURE (1) → (0..*) BOOKING
- USER (1) → (0..*) BLOG
- USER (1) → (0..*) NOTIFICATION

STYLING:
- Clean rectangular entities
- Clear primary/foreign key indicators
- Relationship cardinalities marked
- Color coding by entity type
```

---

## 🖥️ **Figure 6: System Architecture Deployment Diagram**

**Location:** Chapter 3 - Development  
**Purpose:** Docker/Kubernetes deployment architecture

### Visual Description Script:
```
DIAGRAM TYPE: Deployment architecture with containers and nodes
LAYOUT: Multi-layer cloud deployment structure

KUBERNETES CLUSTER (Large container):
├── FRONTEND POD:
│   └── Angular Container (nginx:alpine)
├── BACKEND POD:
│   └── Spring Boot Container (openjdk:17-alpine)
├── DATABASE POD:
│   └── MySQL Container (mysql:8.0)
├── AUTH POD:
│   └── Keycloak Container (keycloak:latest)
└── AI POD:
    └── FastAPI Container (python:3.9-slim)

EXTERNAL SERVICES:
- GitLab CI/CD (Cloud icon)
- Docker Registry (Repository icon)
- Load Balancer (Network icon)

CONNECTIONS:
- Internet → Load Balancer → Frontend Pod
- Frontend → Backend (Service mesh)
- Backend → Database (Internal network)
- Backend ↔ Keycloak (Auth flow)
- Frontend ↔ AI Service (WebSocket)

DATA FLOW:
- Persistent Volumes for MySQL data
- ConfigMaps for application configuration
- Secrets for sensitive data

STYLING:
- Container icons for Docker
- Pod groupings with Kubernetes blue
- Network connections clearly marked
- Cloud-native iconography
```

---

## 📱 **Figure 7: User Interface Flow Diagram**

**Location:** Chapter 4 - Implementation  
**Purpose:** Customer booking workflow visualization

### Visual Description Script:
```
DIAGRAM TYPE: User journey flowchart
LAYOUT: Sequential workflow with decision points

WORKFLOW STEPS (Rounded rectangles):
1. "Homepage/Browse Cars" (Start - Green)
2. "Car Details View" 
3. "Login/Register" (Decision diamond)
4. "Select Dates" 
5. "Availability Check" (Process)
6. "Submit Booking Request"
7. "Agency Review" (Decision diamond)
8. "Email Notification"
9. "Payment Processing" (If accepted)
10. "PDF Contract Generation"
11. "Booking Confirmed" (End - Blue)

DECISION POINTS:
- Authentication required? (Yes/No)
- Car available for dates? (Yes/No)
- Agency accepts request? (Accept/Decline)

PARALLEL PROCESSES:
- Email notifications
- Real-time chat availability
- Chatbot assistance (floating)

STYLING:
- Flowchart with rounded rectangles
- Diamond shapes for decisions
- Color coding for process types
- Arrows showing flow direction
- Parallel process indicators
```

---

## 🤖 **Figure 8: Chatbot Architecture Diagram**

**Location:** Chapter 4 - Implementation  
**Purpose:** AI chatbot service integration

### Visual Description Script:
```
DIAGRAM TYPE: Service architecture with API integration
LAYOUT: Microservice communication pattern

COMPONENTS:
1. ANGULAR FRONTEND:
   - Chat Widget (Bottom right corner)
   - WebSocket connection indicator

2. FASTAPI SERVICE:
   - Chat Controller
   - Intent Processing
   - Response Generator
   - Car Database Connector

3. EXTERNAL SERVICES:
   - OpenAI GPT API (Cloud service)
   - Car Database (MySQL connection)
   - Context Memory (Redis cache)

4. CHAT FEATURES:
   - Car availability queries
   - Booking assistance
   - FAQ responses
   - Multi-language support

DATA FLOW:
User Question → Chat Widget → FastAPI → OpenAI API
OpenAI Response → Context Processing → Car DB Query → Final Response

STYLING:
- Microservice architecture layout
- API connection arrows
- External service cloud icons
- Real-time communication indicators
```

---

## 📈 **Figure 9: System Performance Dashboard**

**Location:** Chapter 4 - Results  
**Purpose:** System metrics and performance visualization

### Visual Description Script:
```
DIAGRAM TYPE: Dashboard mockup with metrics
LAYOUT: Grid-based dashboard layout

METRICS PANELS:
1. Response Time Chart (Line graph)
   - Average: 1.2s
   - Peak: 2.8s
   - Target: <2s

2. User Activity (Bar chart)
   - Daily active users
   - Booking conversions
   - Chat interactions

3. System Health (Gauges)
   - CPU Usage: 65%
   - Memory: 70%
   - Database connections: 45/100

4. Feature Usage (Pie chart)
   - Car browsing: 40%
   - Booking requests: 25%
   - Chat support: 20%
   - Blog reading: 15%

STYLING:
- Modern dashboard UI
- Color-coded status indicators
- Clean chart presentations
- Professional metric displays
```

---

## 🔐 **Figure 10: Authentication & Security Flow**

**Location:** Chapter 3 - Security Implementation  
**Purpose:** Keycloak integration and security architecture

### Visual Description Script:
```
DIAGRAM TYPE: Sequence diagram with security flow
LAYOUT: Actor-to-system interaction timeline

ACTORS & SYSTEMS:
- User (Customer/Agency/Admin)
- Angular Frontend
- Keycloak Server
- Spring Boot Backend
- MySQL Database

AUTHENTICATION FLOW:
1. User → Frontend: Login Request
2. Frontend → Keycloak: Authentication
3. Keycloak → Frontend: JWT Token
4. Frontend → Backend: API Request + JWT
5. Backend → Keycloak: Token Validation
6. Backend → Database: Data Access
7. Database → Backend: Response
8. Backend → Frontend: API Response

SECURITY LAYERS:
- HTTPS encryption
- JWT token validation
- Role-based access control
- Route protection guards

STYLING:
- Sequence diagram format
- Security icons and locks
- Color-coded message types
- Clear actor separation
```

---

## 📋 **Implementation Notes:**

### Recommended Tools:
1. **Draw.io/Diagrams.net** - For all UML and architectural diagrams
2. **PlantUML** - For generating class diagrams from code
3. **Figma/Sketch** - For UI mockups and user flows
4. **Lucidchart** - For complex system diagrams

### Color Scheme:
- **Primary Blue:** #2196F3 (Angular/Frontend)
- **Success Green:** #4CAF50 (Spring Boot/Backend)
- **Warning Orange:** #FF9800 (FastAPI/AI Services)
- **Error Red:** #F44336 (Keycloak/Security)
- **Info Purple:** #9C27B0 (Database/Storage)

### Academic Standards:
- All figures numbered sequentially
- Descriptive captions explaining context
- High-resolution exports (300 DPI minimum)
- Consistent styling across all diagrams
- Professional color palette
- Clear, readable font sizes (minimum 12pt)

---

**Next Steps:**
1. Generate each figure using the scripts above
2. Export in high-quality formats (SVG, PNG)
3. Place in `/img/` directory with proper naming
4. Update LaTeX references in chapters
5. Verify all figures are visible and properly scaled