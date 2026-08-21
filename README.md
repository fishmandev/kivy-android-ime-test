# Kivy Keyboard Test

Minimal Android test app for reproducing the Sideband/Samsung keyboard issue.

The important line is:

```python
Window.softinput_mode = "below_target"
```

The app lets you switch at runtime between:

- `below_target`
- `pan`
- `resize`
- no special mode

The message composer is intentionally placed at the bottom of the screen. Tap it and check whether the input field and `Send` button remain visible above the Android keyboard.

## What to test

For every mode:

1. Select the mode.
2. Tap the bottom input field.
3. Type several characters.
4. Record whether the input field remains visible.
5. Hide the keyboard with Android Back.
6. Try the next mode.

Also test the Samsung Keyboard `Translate` action if `below_target` reproduces the bug.

## Build on Debian/Ubuntu

Install the usual Android/Kivy build dependencies, then:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install buildozer cython

buildozer android debug
```

The APK should appear under:

```text
bin/
```

The first build can take a long time because Buildozer downloads the Android SDK/NDK and python-for-android components.

## Install with ADB

```bash
adb install -r bin/*.apk
```

## Why this test is useful

If the same keyboard-covering bug occurs here with `below_target`, the issue is reproducible without Sideband, LXMF or Reticulum and is much more likely to be in Kivy / python-for-android / SDL2 / Android IME interaction.

If another mode works reliably, that gives a concrete workaround candidate for Sideband.


## Easiest build: GitHub Actions

You do not need Android Studio, SDK, NDK, Java or Buildozer installed locally.

1. Create a new empty GitHub repository.
2. Upload all files from this project, including the hidden `.github` directory.
3. Commit/push them to the `main` branch.
4. Open the repository's **Actions** tab.
5. Open **Build Android APK**.
6. If it did not start automatically, click **Run workflow**.
7. Wait for the build to finish.
8. Open the completed workflow run.
9. Download the artifact named **kivy-keyboard-test-apk**.
10. Extract the ZIP artifact and install the `.apk` on Android.

The workflow definition is:

`.github/workflows/android.yml`

### Important

GitHub may ask you to enable Actions for a brand-new repository. That is normal.

The generated APK is a debug APK, which is exactly what we want for this test.
