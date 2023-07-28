
# Submission for rtCamp DevOps Engineer role - Aryan Sharma
## WordPress Docker Manager

The WordPress Docker Manager is a command-line script written in Python to easily manage WordPress sites running inside Docker containers using a LEMP stack (Linux, Nginx, MySQL, PHP).

## Prerequisites
Before running the script, make sure you have the following prerequisites installed on your system:

1. **Docker**: Docker is required to create and manage the containers for running WordPress sites. You can check if Docker is installed by running the following command in your terminal:
docker --version


2. **Docker Compose**: Docker Compose is necessary to define and run multi-container Docker applications using the `docker-compose.yml` file. Check if Docker Compose is installed with:
docker-compose --version

### Installing Docker
If Docker is not installed, follow the official Docker installation guide for your operating system:

- [Install Docker on Windows](https://docs.docker.com/docker-for-windows/install/)
- [Install Docker on macOS](https://docs.docker.com/docker-for-mac/install/)
- [Install Docker on Linux](https://docs.docker.com/engine/install/)

### Installing Docker Compose

If Docker Compose is not installed, follow the official Docker Compose installation guide:

- [Install Docker Compose](https://docs.docker.com/compose/install/)


## Installation of the project

Before using the script, make sure you have Docker and Docker Compose installed on your system. If not, the script will attempt to install them for you.

1. Clone the repository:


#### git clone https://github.com/aryan2909/rt-camp-devops-assignment

#### cd wordpress-docker-manager


2. Make the script executable:

#### chmod +x wp_manager.py


## Usage

1. To create a new WordPress site:
 #### python3 wp_manager.py create example.com

2. To start the containers for an existing WordPress site:
 #### python3 wp_manager.py start example.com

3. To stop the containers for an existing WordPress site:
 #### python3 wp_manager.py stop example.com 

4. To delete an existing WordPress site:
 #### python3 wp_manager.py delete example

## WordPress Site Access

After running the Python script to create the WordPress site using Docker Compose, you can access the site by visiting http://example.com:8000/ in your web browser. Please note that the site URL will be replaced with the actual site name you provided as a command-line argument when running the script.

Upon accessing the URL, you will be directed to the WordPress setup page, where you can configure and set up your new WordPress site. Follow the on-screen instructions to choose a language, set up the site title, admin username, password, and email.

Once you have completed the initial setup, you will be redirected to the WordPress login page. Here, you can log in with the admin credentials you set during the setup process.

From the WordPress admin dashboard, you can start customizing your site, creating pages, writing blog posts, installing themes, and adding plugins to enhance the functionality of your WordPress site.


## Troubleshooting

- If you encounter any issues during installation or site management, make sure you have the necessary permissions to run Docker commands and that Docker is properly installed and running.
- If you face any errors related to Docker or Docker Compose during the script execution, you may need to install them manually and ensure they are in your system's PATH.

