import os
import sys
import subprocess
import getpass

def check_dependencies():
    try:
        subprocess.check_call(["docker", "--version"])
        subprocess.check_call(["docker-compose", "--version"])
    except subprocess.CalledProcessError:
        print("Docker or Docker Compose is not installed. Installing...")
        install_dependencies()

def install_dependencies():
    try:
        subprocess.check_call(["sudo", "apt-get", "update"])
        subprocess.check_call(["sudo", "apt-get", "install", "-y", "docker.io", "docker-compose"])
        print("Docker and Docker Compose have been installed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to install Docker and Docker Compose. Please install them manually.")
        sys.exit(1)

def create_wordpress_site(site_name):
    check_dependencies()
    docker_compose_content = f"""version: '3'
services:
  db:
    image: mysql:latest
    volumes:
      - db_data:/var/lib/mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: example_root_password
      MYSQL_DATABASE: {site_name}
      MYSQL_USER: {site_name}
      MYSQL_PASSWORD: {site_name}_password
  wordpress:
    depends_on:
      - db
    image: wordpress:latest
    ports:
      - "8000:80"
    restart: always
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_NAME: {site_name}
      WORDPRESS_DB_USER: {site_name}
      WORDPRESS_DB_PASSWORD: {site_name}_password
volumes:
  db_data: {{}}
"""

    project_path = f"{site_name}_wordpress"
    os.makedirs(project_path, exist_ok=True)

    with open(os.path.join(project_path, "docker-compose.yml"), "w") as f:
        f.write(docker_compose_content)

    try:
        with open("/etc/hosts", "a") as f:
            f.write(f"\n127.0.0.1 {site_name}")
    except PermissionError:
        print("The script needs elevated privileges to modify the /etc/hosts file.")
        print("Please enter your password:")
        password = getpass.getpass()
        try:
            subprocess.run(["sudo", "sh", "-c", f"echo '127.0.0.1 {site_name}' >> /etc/hosts"], input=password.encode())
        except subprocess.CalledProcessError:
            print("Failed to add entry to /etc/hosts. Please run the script with elevated privileges.")
            sys.exit(1)

    print(f"WordPress site '{site_name}' created and running. Visit http://{site_name}:8000 in your browser.")



def start_stop_site(site_name, action):
    project_path = f"{site_name}_wordpress"
    try:
        subprocess.check_call(["docker-compose", action], cwd=project_path)
        print(f"WordPress site '{site_name}' {action}ed.")
    except subprocess.CalledProcessError:
        print(f"Failed to {action} the WordPress site '{site_name}'.")

def delete_site(site_name):
    project_path = f"{site_name}_wordpress"
    try:
        subprocess.check_call(["docker-compose", "down", "-v"], cwd=project_path)
        os.remove(os.path.join(project_path, "docker-compose.yml"))
        print(f"WordPress site '{site_name}' deleted successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to delete the WordPress site '{site_name}'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python wp_manager.py <command> [<site_name>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "create":
        if len(sys.argv) < 3:
            print("Please provide the site name.")
            sys.exit(1)
        site_name = sys.argv[2]
        create_wordpress_site(site_name)
    elif command == "start" or command == "stop":
        if len(sys.argv) < 3:
            print("Please provide the site name.")
            sys.exit(1)
        site_name = sys.argv[2]
        start_stop_site(site_name, command)
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Please provide the site name.")
            sys.exit(1)
        site_name = sys.argv[2]
        delete_site(site_name)
    else:
        print("Invalid command. Use 'create', 'start', 'stop', or 'delete'.")
        sys.exit(1)
