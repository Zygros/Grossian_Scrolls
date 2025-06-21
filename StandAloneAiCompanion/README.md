# Praxion: Standalone AI Companion

Praxion is a cross-platform AI companion that runs locally on your device with visual UI and voice control capabilities.

## Features

- **Standalone Operation**: Runs completely on your local device
- **Cross-Platform**: Works on desktop (Windows, macOS, Linux) and mobile (Android, iOS)
- **Voice Control**: Integrated speech recognition and synthesis
- **Visual Interface**: Modern, responsive UI for both desktop and mobile
- **Offline Capability**: No internet connection required for core functionality

## Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+ (for desktop UI)
- Expo CLI (for mobile UI)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/praxion.git
   cd praxion
   ```

2. Set up the Python environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Start the backend:
   ```bash
   ./scripts/run.sh backend
   # Or directly with: uvicorn src.backend.main:app --reload
   ```

4. Start the desktop UI (in a new terminal):
   ```bash
   ./scripts/run.sh desktop
   # Or directly: cd src/ui/desktop && npm install && npm run dev
   ```

5. Start the mobile UI (in a new terminal):
   ```bash
   ./scripts/run.sh mobile
   # Or directly: cd src/ui/mobile && yarn install && expo start
   ```

### Using Docker

You can also use Docker Compose to run the backend and desktop UI:

```bash
docker-compose up
```

## Development

### Running Tests

```bash
./scripts/run.sh test
# Or directly: pytest tests/
```

### Project Structure

```
praxion/
├── src/
│   ├── backend/         # Python backend
│   │   ├── main.py      # FastAPI entry point
│   │   ├── persona.py   # AI personality engine
│   │   ├── memory.py    # Memory and context system
│   │   ├── voice.py     # Voice recognition and synthesis
│   │   └── llm.py       # Language model integration
│   ├── ui/
│       ├── desktop/     # React desktop UI
│       └── mobile/      # React Native mobile UI
├── tests/               # Test suite
├── scripts/             # Utility scripts
├── resources/           # Resources and models
├── requirements.txt     # Python dependencies
├── pyproject.toml       # Python project configuration
├── Dockerfile           # Docker configuration
└── docker-compose.yml   # Docker Compose configuration
```

## License

[MIT License](LICENSE)
