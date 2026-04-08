# 🧹 Excel to CSV Cleaner — Automated ETL Pipeline

A Python pipeline that automatically detects, cleans, validates and transforms
messy real-world Excel files into structured, analysis-ready CSV data.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Pandas](https://img.shields.io/badge/Pandas-latest-green)
![ETL](https://img.shields.io/badge/ETL-Pipeline-orange)

---

## 🚀 Overview

Real-world Excel files are rarely clean. This pipeline handles the most common
data quality problems found in business operations data (sales, purchases,
reports) and produces a clean, consistent dataset ready for analysis,
dashboards or machine learning.

---

## ⚙️ What It Does

### 1. Automatic Header Detection
Scans the file to find where the actual data starts, ignoring titles,
empty rows or garbage above the table.
Row 1: report title        ← ignored
Row 2: (empty)             ← ignored
Row 3: product | qty | ... ← detected as real header

### 2. Data Cleaning
- **Numbers**: converts European formats → `"1.234,56"` becomes `1234.56`
- **Dates**: normalizes multiple formats (`"01/02/23"`, `"2023-02-01"`) to consistent `datetime`
- **Nulls**: handles empty cells and invalid values
- **Types**: enforces coherent types — floats, datetimes, strings

### 3. Validation
- Verifies dataset structure
- Detects inconsistencies without breaking the pipeline
- Logs all issues found

### 4. Transformation
- Standardizes column names
- Prepares dataset for downstream analysis

---

## 📤 Output

| Output | Location | Description |
|--------|----------|-------------|
| Cleaned dataset | `output/cleaned_YYYYMMDD.csv` | Final clean CSV |
| Intermediate preview | `output/preview_post_header.csv` | Post-header detection view |
| Automated report | `reports/report_XXXX.txt` | Processing summary |
| Pipeline log | `logs/pipeline.log` | Technical execution log |

### Report includes:
- File processed
- Detected header row
- Record count
- Problems found
- Transformations applied

---

## 🗂️ Project Structure
excel_to_csv_cleaner/
├── src/
│   ├── main.py        # Pipeline entry point
│   ├── config.py      # Configuration
│   ├── io_excel.py    # Excel reading and loading
│   ├── transform.py   # Cleaning and transformation logic
│   ├── validate.py    # Data validation
│   └── report.py      # Report generation
├── input/             # Place your Excel files here
├── output/            # Cleaned CSV output
├── logs/              # Execution logs
└── requirements.txt

---

## ▶️ Local Setup

```bash
git clone https://github.com/NenriquezC/excel-to-csv-cleaner.git
cd excel-to-csv-cleaner

python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

Place your Excel file in the `input/` folder and run:

```bash
python src/main.py
```

---

## 💡 Use Cases

- Cleaning exported reports from ERP systems
- Preprocessing data for Pandas / BI tools
- Automating manual data preparation workflows
- ETL pipelines for data engineering projects

---

## 📌 Roadmap

- [ ] Support for multiple sheets
- [ ] CSV and JSON input support
- [ ] REST API endpoint (FastAPI)
- [ ] Docker deployment

---

## 👤 Author

**Néstor Enríquez**  
Python Backend Developer | Data Engineering  
[GitHub](https://github.com/NenriquezC) · [LinkedIn](www.linkedin.com/in/nestor-enriquez-cifuentes-6447a650)
