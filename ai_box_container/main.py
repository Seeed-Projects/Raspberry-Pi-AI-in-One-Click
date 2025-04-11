import docker

def pull_and_run(image_name):
    client = docker.from_env()
    print(f"Pulling {image_name}...")
    client.images.pull(image_name)
    print(f"Running {image_name}...")
    container = client.containers.run(image_name, detach=True)
    print(f"Container {container.id} is running.")

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: ai-box-container <image-name>")
        sys.exit(1)
    image_name = sys.argv[1]
    pull_and_run(image_name)
