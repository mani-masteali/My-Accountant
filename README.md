<h1>MyAccountant -- Desktop Personal Finance Manager</h1>
<h2>
 
Overview
 
</h2>
 
This project builds a desktop-based personal finance management system
using PyQt6 and SQLite. The goal was not to create a visually polished
product, but to structure a functional, database-backed application with
clear separation of concerns and deterministic behavior.

The system allows users to:

-   Create and authenticate user accounts
-   Register income and expense transactions
-   Create and manage transaction categories
-   Search transactions using multiple filters
-   Generate filtered financial reports
-   Persist all data locally using SQLite

The emphasis of this project is architectural clarity, validation
integrity, and structured state management rather than UI aesthetics.

<h2>
 
Architecture
 
</h2>
 
The application is separated into distinct layers:

 
<h3>
 
1.  UI Layer (ui.py)
     
    </h3>
     
    Handles:

-   All PyQt6 interface components
-   Menu navigation
-   Input collection
-   Rendering of search and reporting results

 
<h4>
 
Why:
 
</h4>
 
Separating UI logic prevents business rules from being tightly coupled
to interface code.

 
<h3>
 
2.  Logic Layer (logic.py)
     
    </h3>
     
    Handles:

-   Input validation
-   Business rule enforcement
-   Transaction validation
-   Search and reporting orchestration
-   Coordination between UI and database layer

 
<h4>
 
Why:
 
</h4>
 
Centralizing validation ensures consistency and prevents duplication of
rules across the interface.

 
<h3>
 
3.  Database Layer (db.py)
     
    </h3>
     
    Handles:

-   SQLite connection management
-   Table creation
-   Repository-style insert operations
-   Data persistence

 
<h4>
 
Why:
 
</h4>
 
Encapsulating database access improves maintainability and reduces
direct SQL usage inside UI code.

 
<h3>
 
4.  Entry Point (main.py)
     
    </h3>
     
    Initializes the application and launches the main window.

 
<h2>
 
Database Structure
 
</h2>
 
SQLite database file: ElmosBalance.db

Tables:

-   users
-   income_categories
-   expense_categories
-   income_fine
-   expense_fine

Parameterized queries are used for insert operations to prevent SQL
injection during write operations.

 
<h2>
 
Core Functionality
 
</h2>
 
 
<h3>
 
1.  User Management
     
    </h3>
     

Each user is validated before being stored:

-   First and last name validation (English letters only)
-   National ID format validation
-   Phone number validation
-   Password complexity enforcement
-   Email format validation
-   Birth date format validation

Login authentication is performed against stored credentials. A basic
password recovery flow is implemented using a security question.

 
<h4>
 
Why:
 
</h4>
 
Input validation ensures structural consistency in stored data and
prevents malformed records.

 
<h3>
 
2.  Transaction Registration
     
    </h3>
     

Users can:

-   Register income
-   Register expenses
-   Select predefined categories
-   Attach descriptions
-   Validate amount (positive numeric)
-   Validate date format (YYYY/MM/DD)

Transactions are stored in:

-   income_fine
-   expense_fine

 
<h4>
 
Why:
 
</h4>
 
Separating income and expense tables simplifies filtering and reporting
logic.

 
<h3>
 
3.  Category Management
     
    </h3>
     

Users can:

-   Add income categories
-   Add expense categories
-   Enforce maximum length constraints
-   Restrict names to alphanumeric values
-   Prevent duplicate category names

 
<h4>
 
Why:
 
</h4>
 
Explicit validation avoids silent duplication and ensures clean
categorical grouping.

 
<h3>
 
4.  Search System
     
    </h3>
     

The search module supports filtering by:

-   Day
-   Month
-   Year
-   Transaction type (income / expense / both)
-   Amount range
-   Category or description

Results are dynamically rendered in a QTableView using
QStandardItemModel.

 
<h4>
 
Why:
 
</h4>
 
Providing multi-dimensional filters allows structured inspection of
financial activity without exporting data externally.

 
<h3>
 
5.  Reporting
     
    </h3>
     

Reports are generated based on selected filters and displayed in
structured tabular format.

Filters include:

-   Date-based filtering
-   Type filtering
-   Amount range filtering
-   Category filtering

 
<h4>
 
Why:
 
</h4>
 
Reporting logic reuses validated query construction rather than
duplicating filtering rules.

 
<h2>
 
How to Run
 
</h2>
 
  bash
pip install PyQt6
python main.py
 

 
<h2>
 
Design Principles
 
</h2>
 
This project intentionally avoids:

-   Monolithic single-file structure
-   Mixing UI rendering with validation logic
-   Hard-coded schema assumptions
-   External service dependencies

The system is local-first, deterministic, and structured around
separation of concerns.

 
<h2>
 
Limitations
 
</h2>
 
-   Passwords are stored in plaintext (no hashing implemented)
-   No migration system for schema evolution
-   Search query construction could be further abstracted
-   No automated unit tests
-   No multi-user session ownership model

 
<h2>
 
Purpose
 
</h2>
 
This project demonstrates:

-   Desktop application development with PyQt6
-   SQLite database integration
-   Layered architecture in Python
-   Validation-driven data persistence
-   Iterative refactoring of legacy-style code

The focus is structural clarity and architectural growth rather than
production-level polish.
