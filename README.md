# Web Scraper Bot

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Build the Docker Image](#build-the-docker-image)
  - [Run the Docker Container](#run-the-docker-container)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Next Steps](#next-steps)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## Overview

The **Web Scraper Bot** is a versatile and user-friendly tool designed to extract data from any website. Whether you need to gather titles, headings, links, or paragraphs, this bot simplifies the process by providing an intuitive web interface accessible via your local browser. Containerized with Docker, the application ensures seamless deployment without the hassle of managing dependencies on your local machine.

## Features

- **Dynamic Web Scraping:** Capable of handling both static and dynamic websites.
- **User-Friendly Interface:** Simple web interface to input URLs and view scraped data.
- **Organized Data Presentation:** Displays titles, headings, paragraphs, and links in a structured format.
- **Dockerized Deployment:** Easily deployable using Docker, ensuring consistent environments across different systems.
- **Responsive Design:** Optimized for various devices, including desktops and mobile devices.

## Technologies Used

- **Frontend:**
  - HTML5
  - CSS3 (with responsive design)
  - JavaScript (ES6)
  - Google Fonts (Roboto)
- **Backend:**
  - Python 3.11
  - Flask
  - BeautifulSoup4
  - Requests
- **Containerization:**
  - Docker

## Project Structure


- **app/**: Contains the backend and frontend code.
  - **static/**: Holds static files like CSS.
  - **templates/**: Contains HTML templates for Flask.
  - **scraper.py**: Handles the web scraping logic.
  - **app.py**: The Flask application managing routes and API endpoints.
- **Dockerfile**: Instructions to build the Docker image.
- **requirements.txt**: Lists Python dependencies.
- **README.md**: Documentation for the project.

## Installation

### Prerequisites

- **Docker:** Ensure Docker is installed on your machine. You can download it from [here](https://www.docker.com/get-started).

### Clone the Repository

```bash
git clone https://github.com/yourusername/webscraper-bot.git
cd webscraper-bot

### Build the Docker Image

```bash
docker build -t webscraper-bot .
```

### Run the Docker Container

```bash
docker run -p 5000:5000 webscraper-bot
```

## Usage

1. Open your browser and navigate to `http://localhost:5000`.
2. Enter the URL you want to scrape.
3. Click the "Scrape" button.
4. The scraped data will be displayed in the result section.

## Screenshots

![Screenshot 1](https://github.com/yourusername/webscraper-bot/assets/123456789/e5a1a8f8-a7b7-4f1b-b4a6-e2c3c5d6e7f8)

![Screenshot 2](https://github.com/yourusername/webscraper-bot/assets/123456789/e5a1a8f8-a7b7-4f1b-b4a6-e2c3c5d6e7f8)

## Next Steps

- Add more features to the application.
- Improve the user interface.                             
- Optimize the performance of the web scraping process.
- Add more error handling and logging.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to [Flask](https://flask.palletsprojects.com/) for providing a simple and flexible web framework.
- Thanks to [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for parsing HTML and extracting data.
- Thanks to [Requests](https://requests.readthedocs.io/en/master/) for handling HTTP requests.

## Contact

If you have any questions or need further assistance, feel free to contact me at [ryan.c.lanman@gmail.com](mailto:ryan.c.lanman@gmail.com).