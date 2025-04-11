import docker
import logging
from typing import Optional, Dict
import os

class HailoRunner:
    def __init__(self):
        self.client = docker.from_env()
        self.logger = logging.getLogger(__name__)
        
        # Define available applications and their Docker image configurations
        self.applications: Dict[str, Dict] = {
            "object_detection": {
                "image": "hailoairun/object_detection",
                "runtime": "hailort",
                "environment": {
                    "HAILO_MODEL": "yolov5s",
                    "HAILO_DEVICE": "hailo8"
                }
            },
            "pose_estimation": {
                "image": "hailoairun/pose_estimation",
                "runtime": "hailort",
                "environment": {
                    "HAILO_MODEL": "movenet",
                    "HAILO_DEVICE": "hailo8"
                }
            },
            "instance_segmentation": {
                "image": "hailoairun/instance_segmentation",
                "runtime": "hailort",
                "environment": {
                    "HAILO_MODEL": "mask_rcnn",
                    "HAILO_DEVICE": "hailo8"
                }
            },
            "clip": {
                "image": "hailoairun/clip",
                "runtime": "hailort",
                "environment": {
                    "HAILO_MODEL": "clip",
                    "HAILO_DEVICE": "hailo8"
                }
            }
        }

    def pull_image(self, image_name: str) -> bool:
        """Pull a Docker image"""
        try:
            self.logger.info(f"Pulling image: {image_name}")
            self.client.images.pull(image_name)
            return True
        except Exception as e:
            self.logger.error(f"Failed to pull image {image_name}: {str(e)}")
            return False

    def run_container(self, app_config: Dict, command: Optional[str] = None) -> bool:
        """Run a Docker container with specific configuration"""
        try:
            image_name = app_config["image"]
            self.logger.info(f"Running container from image: {image_name}")
            
            # Create container with specific configuration
            container = self.client.containers.run(
                image_name,
                command=command,
                detach=True,
                runtime=app_config["runtime"],
                environment=app_config["environment"],
                volumes={
                    os.path.expanduser("~/.hailo"): {
                        "bind": "/root/.hailo",
                        "mode": "rw"
                    }
                }
            )
            
            self.logger.info(f"Container started with ID: {container.id}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to run container: {str(e)}")
            return False

    def run_application(self, app_name: str) -> bool:
        """Run a specific Hailo AI application"""
        if app_name not in self.applications:
            self.logger.error(f"Application '{app_name}' not found")
            return False
            
        app_config = self.applications[app_name]
        image_name = app_config["image"]
        
        if not self.pull_image(image_name):
            return False
            
        return self.run_container(app_config)

    def get_available_applications(self) -> list:
        """Get list of available applications"""
        return list(self.applications.keys()) 