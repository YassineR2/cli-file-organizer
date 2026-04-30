# 📁 File Organizer

A simple and powerful CLI tool to automatically organize files into folders based on their file type.

---

## 🚀 Features

* 📂 Automatically sorts files into categories (Images, Documents, Videos, etc.)
* 🛠 Configurable file categories via `config.json`
* ⚡ Fast file scanning using efficient methods
* 📊 Progress bar using `tqdm`
* 🎨 CLI banner using `pyfiglet`
* 🔁 Handles duplicate file names safely
* 🚫 Ignores non-file items (folders, etc.)

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/file-organizer.git
cd file-organizer
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Linux / Mac
venv\Scripts\activate     # On Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or install as a package:

```bash
pip install .
```

---

## ▶️ Usage

Run the tool:

```bash
python -m organizer.main
```

Or (after installation):

```bash
file-organizer
```

Then enter the directory you want to organize:

```bash
(Enter directory path) >
```

---

## ⚙️ Configuration

File categories are defined in:

```text
organizer/config.json
```

Example:

```json
{
  "Images": ["jpg", "jpeg", "png", "gif"],
  "Documents": ["pdf", "docx", "txt"],
  "Videos": ["mp4", "mkv"]
}
```

You can modify or extend categories as needed.


---

## 📌 Requirements

* Python 3.8+
* `pyfiglet`
* `tqdm`

---

## 👤 Author

**Yassine Rezgui**
