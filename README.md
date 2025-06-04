# 📁 Python Downloads Organizer

This is a simple Python script that **automatically organizes files** in your `Downloads` folder by type (images, documents, videos, etc.). It helps you keep your downloads clean and clutter-free.

---

## 🧠 How It Works

The script performs the following actions:

1. Detects your `~/Downloads` folder.
2. Defines groups of files based on their **extensions** (e.g., `.jpg`, `.pdf`, `.mp4`).
3. Iterates through each file in the folder.
4. Moves each file into a **subfolder** based on its type:
   - 📷 `Images/`
   - 📄 `Documents/`
   - 🎞 `Videos/`
   - 📦 `ZIPs/`
   - 🛠 `Installers/`
5. If the target subfolder doesn’t exist, it is created automatically.

---

## 📦 Requirements

- Python 3.6 or higher
- Operating system with Python installed (Windows, Linux, or macOS)

No third-party libraries are required. The script uses only **Python’s standard library**.

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/downloads-organizer.git
cd downloads-organizer
