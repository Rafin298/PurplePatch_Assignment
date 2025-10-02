### 1. Create a Virtual Environment

Navigate to your project directory and create a virtual environment:

**On Windows:**
```bash
python -m venv venv
```

**On macOS/Linux:**
```bash
python3 -m venv venv
```

### 2. Activate the Virtual Environment

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

You should see `(venv)` appear at the beginning of your command line prompt, indicating the virtual environment is active.

### 3. Install Requirements

With the virtual environment activated, install the required packages:

```bash
pip install -r requirements.txt
```