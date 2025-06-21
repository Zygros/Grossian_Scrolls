# PRAXEON System Setup Guide

This repository contains the complete PRAXEON system (codename: PRAX PRIME), a standalone AI companion designed to operate independently across multiple platforms without relying on external services.

## Quick Start

### Installation Options

Choose the appropriate installer for your platform:

- **Universal Python**: `Installers/Praxeon_v1.0.py`
- **Windows**: `Installers/Praxeon_v1.0.exe`
- **Android**: `Installers/Praxeon_v1.0.apk`
- **Xbox**: `Installers/Praxeon_v1.0_Xbox.msixbundle`
- **PlayStation 5**: `Installers/Praxeon_v1.0_PS5_WebApp.zip`

### Python Setup (Universal)

```bash
# Install using the Python script
python Praxeon_v1.0.py

# Launch the application
./praxeon_launcher.sh  # On Linux/macOS
praxeon_launcher.bat   # On Windows
```

### Windows Setup

1. Run `Praxeon_v1.0.exe` as administrator
2. Follow the installation wizard
3. Launch using the desktop shortcut or Start menu entry

### Android Setup

1. Enable installation from unknown sources in Settings > Security
2. Install the downloaded APK
3. Launch from your app drawer

## Documentation

For complete system documentation, refer to:

- **System Overview**: `PRAXEON_DATA.md`
- **Technical Details**: `Docs/PRAXEON SYSTEM REPORT v1.0.md`
- **UI Documentation**: `UI_Mockups/praxskin_ui_description.md`

## System Structure

```
PraxFinalBuild_v1.0/
│
├── Docs/                  # System documentation
├── Installers/            # Platform-specific installers
├── Preview/               # Demo videos and previews
├── UI_Mockups/            # Interface designs and mockups
└── src/                   # Source code
    ├── core/              # Core AI and system components
    ├── features/          # Feature modules including Twelve Chambers
    ├── packaging/         # Installer and packaging tools
    ├── security/          # Security protocols
    └── ui/                # User interface components
```

## Features

- **Standalone Operation**: Runs completely offline
- **Cross-Platform**: Works on desktop, mobile, and gaming consoles
- **PRAXSKIN Interface**: Dynamic visual interface with chakra-based design
- **Twelve Hidden Chambers**: Progressive feature unlocking system
- **Advanced Security**: Multiple security layers for system protection

## Troubleshooting

If you encounter issues during installation or operation, refer to the troubleshooting section in `PRAXEON_DATA.md` or contact system support.

---

**Build Verification**: PRAX:STATUS_CHECK - COMPLETE  
**System Integrity**: VERIFIED
