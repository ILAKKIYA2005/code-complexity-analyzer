#  Code Complexity Analyzer

A web-based tool that analyzes source code and estimates its **time complexity** with visualization and downloadable reports.



##  Live Demo


https://code-complexity-analyzer-33yw.onrender.com/


##  Features

* Analyze time complexity (O(n), O(n²), etc.)
* Graph visualization of complexity
* Upload code files (.py, .java, .cpp)
* Download analysis as PDF
* Clean and responsive UI

---

## Tech Stack

**Frontend**

* HTML5
* CSS3
* JavaScript
* Chart.js

**Backend**

* Python
* Flask

**Tools**

* Git & GitHub
* Render (Deployment)

---

## Installation (Run Locally)

### 1️.Clone the repository

```bash
git clone https://github.com/ILAKKIYA2005/code-complexity-analyzer.git
cd code-complexity-analyzer
```

### 2️.Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️.Install dependencies

```bash
pip install -r requirements.txt
```

### 4️.Run the app

```bash
python app.py
```

### 5️.Open in browser

```
http://127.0.0.1:5000
```

---

## Project Structure

```
code-complexity-analyzer/
│
├── app.py
├── analyzer.py
├── requirements.txt
├── Procfile
│
├── templates/
│   └── index.html
│
├── static/
│   └── (CSS / JS files)
```

---

## Example

Input:

```
for i in range(n):
    for j in range(n):
        print(i, j)
```

Output:

```
Time Complexity: O(n²)
```

---

## Future Improvements

* Better complexity detection (O(log n), recursion)
* User history storage
* AI-based code explanation
* Multi-language support

---

## Author

**ILAKKIYA N**

---

If you like this project, don’t forget to **star the repo!**

