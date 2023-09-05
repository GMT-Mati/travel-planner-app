# Travel Planner App

![App Logo](link-to-your-logo.png)

## Overview

The Travel Planner App is a web-based application that helps users plan and organize their trips and destinations. Users can create and manage trips, add destinations, and view details about their planned adventures. The app also integrates with Azure Maps to provide location-based features.

## Features

- User Registration and Authentication
- Trip Management
- Destination Tracking
- Azure Maps Integration for Location Information
- API for Accessing Trip Data (optional)

## Getting Started

### Prerequisites

- Python 3.x
- Virtual Environment (optional but recommended)
- Flask
- Azure Maps API Key (for Azure Maps integration)
- Docker and Docker Compose (for containerization, optional)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/GMT-Mati/travel-planner-app.git
   cd travel-planner-app
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure your environment variables in `app/config.py`. Set your Azure Maps API Key and other settings as needed.

5. Initialize the database:

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

### Usage

1. Run the application:

   ```bash
   flask run
   ```

2. Access the app in your web browser at `http://localhost:5000`.

3. Register or log in to start using the app.

### API (Optional)

- To access the API for retrieving trip data, use the following endpoint:

  ```
  GET /api/trips
  ```

  Replace `/api/trips` with the desired API endpoints for your application.

### Deployment (Optional)

- You can deploy this app to Azure or any other cloud service of your choice. Be sure to set up appropriate configurations for production deployment.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch to your fork.
5. Create a pull request to the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

- Maintainer: Matt
- Email: mateusz.gruszka@linux.pl
- GitHub: https://github.com/GMT-Mati
- LinkedIn: https://www.linkedin.com/in/mateusz-gruszka-80489a136

Feel free to reach out if you have any questions or need assistance.
