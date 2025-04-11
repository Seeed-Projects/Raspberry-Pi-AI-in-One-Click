# HailoAI Run

A command-line tool to pull and run Hailo AI applications in Docker containers.

## Installation

```bash
pip install hailoairun
```

## Usage

To run a Hailo AI application:

```bash
hailoairun object_detection
```

This will:
1. Pull the `hailoairun/object_detection` Docker image
2. Run the container with the Hailo runtime

## Requirements

- Python 3.6 or higher
- Docker installed and running
- Hailo runtime installed

## Development

To install for development:

```bash
git clone https://github.com/yourusername/hailoairun.git
cd hailoairun
pip install -e .
```

## License

MIT License 