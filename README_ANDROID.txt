WONDEROUS SOUL - ANDROID VERSION

This project is based on the current Wonderous Soul Python/Pygame game.

ANDROID CONTROLS
- Left / Right: bottom-left buttons
- Up / Down: small directional buttons above/below the left/right controls
- JUMP: bottom-right
- NAIL: bottom-right upper button
- DASH: lower-middle/right button (after the cloak is acquired)
- SOUL: hold to Focus/heal when available
- USE: interact with NPCs, doors, and benches

The touch controls occupy the lower corners only. The center of the screen remains
clear so they do not cover the main gameplay/camera area.

BUILDING

Buildozer packages Python applications for Android, but its Android toolchain runs
on Linux/macOS; on Windows, WSL is normally used. This project is configured for
landscape fullscreen and ARM64 + ARMv7 Android builds.

From a Linux/WSL terminal in this folder:

    python3 -m pip install --user buildozer
    buildozer -v android debug

The resulting APK should be in the bin/ folder.

IMPORTANT

This environment cannot compile the final Android APK because the Android SDK,
NDK and python-for-android build toolchain are not installed here. The included
project is the Android-ready source/build configuration.
