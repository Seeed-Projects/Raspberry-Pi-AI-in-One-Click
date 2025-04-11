import argparse
import logging
from .runner import HailoRunner

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def list_applications():
    """List all available Hailo AI applications"""
    applications = [
        "object_detection",
        "pose_estimation",
        "instance_segmentation",
        "clip"
    ]
    print("\nAvailable Hailo AI applications:")
    for app in applications:
        print(f"  - {app}")
    print("\nUsage: hailoairun <application_name>")
    print("Example: hailoairun object_detection")

def main():
    setup_logging()
    parser = argparse.ArgumentParser(
        description='Run Hailo AI applications',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  hailoairun object_detection    # Run object detection
  hailoairun pose_estimation    # Run pose estimation
  hailoairun instance_segmentation  # Run instance segmentation
  hailoairun clip              # Run CLIP model
  hailoairun --list            # List all available applications
"""
    )
    
    parser.add_argument(
        'application',
        nargs='?',
        help='Name of the application to run'
    )
    parser.add_argument(
        '--list',
        action='store_true',
        help='List all available applications'
    )
    
    args = parser.parse_args()
    
    if args.list or not args.application:
        list_applications()
        return
    
    runner = HailoRunner()
    success = runner.run_application(args.application)
    
    if not success:
        logging.error(f"Failed to run application: {args.application}")
        exit(1)

if __name__ == '__main__':
    main() 