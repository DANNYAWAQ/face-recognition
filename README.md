# Face Detection Using OpenCV and Haar Cascades

A beginner computer vision project that detects frontal faces in a still image, draws green bounding boxes around the detections, prints the number of detected faces, and saves the annotated image.

Built with **Python, OpenCV, and Matplotlib**. The application uses OpenCV's pretrained Haar Cascade model; it does not train a new model or identify who a person is.

## Table of contents

- [Features](#features)
- [Project files](#project-files)
- [Installation on Windows](#installation-on-windows)
- [Running the project](#running-the-project)
- [Examples](#examples)
- [How the code works](#how-the-code-works)
- [Detection settings](#detection-settings)
- [Troubleshooting](#troubleshooting)
- [Testing and evaluation](#testing-and-evaluation)
- [Limitations](#limitations)
- [Publishing on GitHub](#publishing-on-github)
- [Future improvements](#future-improvements)
- [Interview preparation](#interview-preparation)
- [References](#references)

## Features

- Reads a local image named `image.png`.
- Uses the pretrained `haarcascade_frontalface_default.xml` classifier bundled with the selected OpenCV 4 package.
- Converts the image to grayscale before detection.
- Detects candidate frontal faces at multiple scales.
- Prints the detection count in the terminal.
- Draws green rectangles around detected regions.
- Saves the result as `output.png`.
- Displays the result using Matplotlib.
- Checks for an unreadable image and an unloaded classifier.

**Current scope:** still-image face detection. Webcam processing, face recognition, a custom graphical interface, and model training are not implemented.

## Project files

| File | Purpose |
| --- | --- |
| `face_detection.py` | The Python script containing the image loading, detection, drawing, saving, and display code |
| `image.png` | An input image supplied by the user |
| `output.png` | The annotated image generated when the program runs |
| `README.md` | Project documentation |
| `requirements.txt` | Recommended dependency file; create it using the contents below |
| `.gitignore` | Recommended Git exclusions; see the publishing section |
| `.venv/` | Local Python environment; do not upload it to GitHub |

This README documents the existing `face_detection.py` code. It does not include sample image files or measured benchmark results.

## Installation on Windows

### 1. Check Python

Open PowerShell in the project folder and run:

```powershell
py --version
```

These instructions use the Windows `py` launcher. If it is unavailable, install Python for Windows from [python.org](https://www.python.org/downloads/windows/), reopen the terminal, and check again.

### 2. Create a virtual environment

```powershell
py -m venv .venv
```

If `.venv` already exists from your earlier setup, reuse it and continue to the installation step.

### 3. Install dependencies

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install --no-cache-dir --only-binary=:all: "opencv-python==4.13.0.92" matplotlib
```

**Why pin OpenCV?** This script calls `cv2.CascadeClassifier`. OpenCV 5 moved the legacy Haar detector to the extra `xobjdetect` module. The pinned OpenCV 4 version keeps the API used by this script, avoiding a code migration.

Create `requirements.txt` with:

```text
opencv-python==4.13.0.92
matplotlib
```

Future installations can then use:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

OpenCV is pinned for API compatibility; Matplotlib is not pinned here. After verifying your installation, record its exact working versions if you need a fully reproducible environment.

### 4. Verify OpenCV

```powershell
.\.venv\Scripts\python.exe -c "import cv2; print('Version:', cv2.__version__); print('CascadeClassifier available:', hasattr(cv2, 'CascadeClassifier'))"
```

Expected compatibility check:

```text
Version: 4.13.0
CascadeClassifier available: True
```

This is expected output, not a claim that every machine has been tested.

### 5. Select the interpreter in VS Code

1. Open the project folder in VS Code.
2. Press **Ctrl + Shift + P**.
3. Select **Python: Select Interpreter**.
4. Choose the interpreter ending in `.venv\Scripts\python.exe`.
5. Use **Run Python File in Terminal**, or run the explicit command below.

The commands use the environment's executable directly, so PowerShell activation is unnecessary. On machines with MSYS2 installed, the plain `python` command may point to MSYS2 instead of Windows Python.

## Running the project

1. Save the supplied program as `face_detection.py`.
2. Place a readable photo named `image.png` in the project folder. Use an image with clear, reasonably large, front-facing faces for your first run.
3. Open PowerShell **in that folder**.
4. Run:

```powershell
.\.venv\Scripts\python.exe face_detection.py
```

The program prints the count, writes `output.png`, and opens a Matplotlib window. Close the window when finished.

The paths `image.png` and `output.png` are relative to the terminal's current working directory, not automatically to the script's location. Each successful run overwrites `output.png` in that directory.

## Examples

The following examples are illustrative. The actual count depends on the image and detection settings.

### Example 1: One clear frontal face

With a suitable portrait saved as `image.png`, a possible terminal result is:

```text
Found 1 faces!
```

The saved and displayed image contains one green rectangle. The wording follows the script's existing print statement.

### Example 2: Group photo

For a photo containing three clearly visible faces, a possible result is:

```text
Found 3 faces!
```

A group photo can still produce fewer detections than the number of people present, particularly when faces are small or turned away.

### Example 3: Image with no detections

```text
Found 0 faces!
```

The script still saves and displays the image without rectangles. Zero detections does not prove that no person is present.

### Example 4: Missing or unreadable image

```text
Image not found! Check image.png
```

OpenCV may also print a warning before this message. Check the working directory, filename, extension, and whether the file is a valid image.

### Adding a real visual demo

After running the project successfully, add a permitted sample image and its actual output to the repository. A GitHub Markdown table can show them side by side:

```markdown
| Input | Detection output |
| --- | --- |
| ![Input image](image.png) | ![Detected faces](output.png) |
```

Only add this preview once those files exist in the repository. Avoid publishing private photos without permission.

## How the code works

1. **Load the pretrained model.** `cv2.data.haarcascades` provides the directory containing the XML cascade. `cv2.CascadeClassifier(cascPath)` loads it.
2. **Read the image.** `cv2.imread(imagePath)` returns an image array, or `None` if loading fails.
3. **Check inputs.** The program exits if the image could not be read or if `faceCascade.empty()` indicates the classifier was not loaded.
4. **Convert to grayscale.** `cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)` produces the single-channel image used by the detector.
5. **Detect faces.** `detectMultiScale()` searches at different scales and returns rectangles represented as `(x, y, w, h)`.
6. **Draw results.** `(x, y)` is the top-left corner; `(x + w, y + h)` is the opposite corner. The color `(0, 255, 0)` is green in OpenCV's BGR format, and `2` is the line thickness in pixels.
7. **Save and display.** `cv2.imwrite()` writes the annotated image. A BGR-to-RGB conversion gives Matplotlib the expected channel order before `plt.imshow()` displays it.

### What is a Haar Cascade?

It is a classical machine learning detector. Haar-like features compare brightness between rectangular image regions. An integral image makes region-sum calculations efficient. During training, boosting selects useful features and combines weak classifiers. At inference time, a cascade of stages rejects many non-face windows early and applies more checks to the remaining candidates.

This project loads an already trained cascade. Its contribution is the Python application and image-processing workflow, rather than training the classifier. It does not use a neural network.

## Detection settings

```python
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)
```

| Setting | Meaning | Example tradeoff |
| --- | --- | --- |
| `scaleFactor=1.1` | Controls the step between image scales | A value closer to 1 searches more scales and usually takes longer |
| `minNeighbors=5` | Sets how much support from neighboring candidate rectangles is required | Raising it can reduce false detections while missing some real faces |
| `minSize=(30, 30)` | Ignores face candidates smaller than 30 by 30 pixels | Raising it can skip small faces and reduce work |

For an experiment, try `minNeighbors=3` and compare the saved results with `minNeighbors=5`. Change one setting at a time and record missed faces, false detections, and processing time. Do not assume that one setting is best for every image.

## Troubleshooting

| Error or symptom | Likely explanation | Action |
| --- | --- | --- |
| `No module named cv2` | OpenCV is missing from the interpreter running the file | Install using `.\.venv\Scripts\python.exe -m pip install -r requirements.txt` and run with that same executable |
| MSYS2 Python reports `No module named pip` | The plain `python` command selected MSYS2 | Use `py` to create the environment, then use its executable directly |
| `cv2` has no attribute `CascadeClassifier` | OpenCV 5 API change, a conflicting local module, or an incomplete installation | Check the version and `cv2.__file__`; install the pinned OpenCV 4 package |
| A project file is named `cv2.py` | It can hide the installed OpenCV module | Rename that file and rerun the program |
| `No module named matplotlib` | Matplotlib is absent from the selected environment | Install it using the same environment's `-m pip` command |
| `Image not found!` | Wrong working directory, wrong name, or unreadable image | Open the terminal in the project folder and check `image.png` |
| `Haar Cascade model not found!` | The XML classifier failed to load | Check the cascade path and reinstall the pinned package if necessary |
| No faces detected | Pose, lighting, size, blur, or settings may prevent detection | Start with a clear frontal photo, then compare settings |
| False rectangles | Background patterns resemble the detector's learned features | Compare larger `minNeighbors` values and document the tradeoff |
| VS Code runs `tempCodeRunnerFile.py` | Code Runner may be executing selected text | Save and run the complete `face_detection.py` file |

Useful diagnostic command:

```powershell
.\.venv\Scripts\python.exe -c "import cv2; print(cv2.__file__); print(cv2.__version__); print(hasattr(cv2, 'CascadeClassifier'))"
```

Do not install several OpenCV package variants into the same environment; they share the `cv2` namespace.

## Testing and evaluation

The following is a **manual test plan**, not a completed results report. No accuracy, speed, or success-rate measurements are claimed for this project yet.

| Test | What to check |
| --- | --- |
| Clear single-face image | Compare the rectangle with the visible face |
| Group photo | Count correctly detected faces and missed faces |
| No-face image | Check for unwanted rectangles |
| Side-facing, blurred, or dimly lit face | Record where the frontal detector fails |
| Missing `image.png` | Confirm the custom error message and absence of a new result |
| Corrupt image file | Confirm the unreadable-image handling |
| Repeated run | Confirm the output is overwritten with the current result |

An old `output.png` can remain after a failed run; check its modification time before treating it as a new result.

For a stronger evaluation, manually label face boxes in a varied image set. Match predicted and labeled boxes one-to-one using a stated overlap criterion, such as intersection-over-union of at least 0.5. Count matched detections as true positives, unmatched predictions as false positives, and unmatched labeled faces as false negatives.

- **Precision:** `TP / (TP + FP)`.
- **Recall:** `TP / (TP + FN)`.
- **F1:** `2 * precision * recall / (precision + recall)`.

Report undefined cases explicitly when a denominator is zero. Face count alone is not an accuracy metric. For speed, time the detection call separately from loading, drawing, saving, and the interactive display. State the CPU, image sizes, sample count, and timing method. The present script does not calculate these metrics.

## Limitations

- Designed around a pretrained frontal-face detector; large rotations and side profiles are challenging.
- Can miss small, blurred, occluded, or poorly lit faces.
- Can produce false detections on background textures.
- Does not identify people, verify identity, or recognize expressions.
- Processes one hardcoded input filename per run.
- Does not provide confidence probabilities, evaluation reports, or latency measurements.
- Does not check the Boolean return value from `cv2.imwrite()`; a write failure is not explicitly reported.
- Error branches currently use `exit()`; explicit `sys.exit(1)` would improve failure status handling.
- Detection quality can vary across image conditions and populations; representative evaluation is still needed.

## Publishing on GitHub

1. Create a repository, for example `opencv-haar-face-detection`.
2. Add `face_detection.py`, this file named `README.md`, and the `requirements.txt` described above.
3. Add a `.gitignore` with:

```gitignore
.venv/
__pycache__/
*.py[cod]
.vscode/
tempCodeRunnerFile.py
```

4. Add a permitted demo input and its actual `output.png` if you want the visual preview.
5. Use GitHub's **Add file → Upload files**, or your usual Git workflow, to commit the files.
6. Verify the README renders correctly and that another person can follow the setup instructions.

Do not upload `.venv`. Installable dependencies belong in `requirements.txt`. Choose a license before inviting reuse; a license is not supplied by this README. Third-party packages, pretrained models, and images retain their own license terms.

## Future improvements

These ideas are **not implemented in the current version**:

- Add command-line options for input path, output path, and detector settings.
- Resolve paths relative to the script or accept explicit paths.
- Validate output saving and use clear failure exit codes.
- Process a folder of images and export a CSV summary.
- Add webcam detection and face blurring for a privacy-focused demo.
- Compare Haar Cascades with a modern detector on the same labeled image set.
- Measure precision, recall, and inference time under consistent conditions.
- Add tests for missing files, invalid paths, and the output pipeline.

## Interview preparation

**What did you build?** A Python still-image detection pipeline that loads a pretrained classifier, prepares an image, finds candidate face regions, annotates them, and saves/displays the result.

**Detection versus recognition?** Detection locates faces. Recognition determines or verifies identity. This project performs detection only.

**Did you train the model?** No. The application uses OpenCV's pretrained XML classifier.

**Why grayscale?** The cascade uses intensity-based features, so the detector operates on a grayscale image without needing color channels.

**Why convert BGR to RGB?** OpenCV loads color images in BGR order, while Matplotlib expects RGB for a color image array.

**What does `minNeighbors` do?** It filters candidate detections according to support from neighboring rectangles; increasing it makes acceptance more selective.

**Why was OpenCV pinned?** The code uses the OpenCV 4 cascade API. Pinning avoids the incompatible OpenCV 5 module change encountered during setup.

**How would you improve it?** Add input/output options, evaluate labeled images, measure runtime, and compare a modern detector before claiming better quality.

### Honest resume wording

After running and verifying the project, a suitable description is:

> **Face Detection with OpenCV — Python, OpenCV, Matplotlib**  
> Implemented a still-image face detection pipeline using a pretrained Haar Cascade, with grayscale preprocessing, face-count reporting, bounding-box visualization, and annotated image export.

Only add benchmark numbers or claims about improvements after measuring them. This is a foundational learning project; additional engineering and evaluation would make it more distinctive for an AI-focused portfolio.

## References

- [OpenCV 4 cascade classifier tutorial](https://docs.opencv.org/4.13.0/db/d28/tutorial_cascade_classifier.html)
- [OpenCV 4 to 5 migration guide](https://github.com/opencv/opencv/wiki/OpenCV-4-to-5-migration)
- [OpenCV Python package and installation guidance](https://pypi.org/project/opencv-python/)
- [Pinned OpenCV package version](https://pypi.org/project/opencv-python/4.13.0.92/)

## Author

**Tanishq Awale**  
[GitHub](https://github.com/DANNYAWAQ)
