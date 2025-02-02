# **LLM Batch Processor** 🚀  
*A Python package to process CSV text data in batches using OpenAI's GPT API.*

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![OpenAI API](https://img.shields.io/badge/OpenAI-GPT--4-orange.svg)](https://platform.openai.com/)

---

## **📌 Features**
✅ Processes large CSV files (50K+ rows) in **batches of 10 rows**  
✅ Uses **OpenAI GPT-4** API (for now) to generate responses for each row  
✅ Saves the results in a **new CSV column**  
✅ CLI support (`llm-process`) for easy execution  
✅ Modular and scalable package design  

---

## **📂 Project Structure**
```
llm_batch_processor/
│── llm_batch_processor/  # The package
│   │── __init__.py
│   │── config.py         # Configuration settings
│   │── api_client.py     # Handles OpenAI API requests
│   │── processor.py      # Batch processing logic
│── scripts/
│   │── main.py           # CLI entry point
│── data/                 # Place CSV files here
│── setup.py              # Package setup
│── setup.cfg
│── pyproject.toml
│── requirements.txt
│── README.md
│── .gitignore
│── LICENSE
```

---

## **🛠 Installation with repo**

### **1️⃣ Clone the repository**
```bash
git clone https://github.com/karthikRavichandran/llm_batch_processor.git
cd llm_batch_processor
```
Or
### **2️⃣ Install the package**
```bash
pip install llm-batch-process
```

### **3️⃣ Set up OpenAI API Key**  
Create a `.env` file in the root directory and add:
```ini
OPENAI_API_KEY=your_api_key_here
Project_Id=your_project_id #optional
```
or 

```bash
export OPENAI_API_KEY="your_api_key_here"
export Project_Id="your_project_id" #Optional 

```

---

## **🚀 Usage**

### **1️⃣ Prepare your CSV file**
- Place your input CSV file in the `data/` folder.
- Ensure it has a column containing text (default: `"text"`).

### **2️⃣ Run the batch processor**
```bash
llm-process 
```

CLI args
```text
  --api_key API_KEY     OpenAI API Key (default: from environment variable)
  --project_id PROJECT_ID
                        Project ID (default: from environment variable)
  --batch_size BATCH_SIZE
                        Batch size for processing (default: 10)
  --input_csv INPUT_CSV
                        Path to input CSV file (default: data/input.csv)
  --output_csv OUTPUT_CSV
                        Path to output CSV file (default: data/output.csv)
  --text_column TEXT_COLUMN
                        Column name containing input text (default: text)
  --response_column RESPONSE_COLUMN
                        Column name for storing responses (default: response)
  --prompt_file PROMPT_FILE
                        Path to the text file containing the prompt

```
This will:
- Read data from `data/input.csv`
- Process text in batches of 10 rows
- Send each batch to **OpenAI GPT-4**
- Save responses in `data/output.csv` under a new column `"response"`

---

## **⚙️ Configuration**
Modify `config.py` for:
```python
BATCH_SIZE = 10  # Number of rows per batch
INPUT_CSV = "data/input.csv"
OUTPUT_CSV = "data/output.csv"
TEXT_COLUMN = "text"
RESPONSE_COLUMN = "response"
```

---

## **🛠 Development**
### **Install dependencies**
```bash
pip install -r requirements.txt
```

### **Run tests**
(TODO: Add unit tests)
```bash
pytest
```

---

## **📦 Publish to PyPI**
### **1️⃣ Build the package**
```bash
python setup.py sdist bdist_wheel
```
### **2️⃣ Upload to PyPI**
```bash
twine upload dist/*
```
### **3️⃣ Install from PyPI**
```bash
pip install llm_batch_processor
```

---

## **📜 License**
This project is licensed under the **MIT License**.

---

## **💡 Contributing**
1. Fork the repo
2. Create a feature branch (`git checkout -b feature-branch`)
3. Commit changes (`git commit -m "Added new feature"`)
4. Push to branch (`git push origin feature-branch`)
5. Create a **Pull Request** 🚀

---

## **📧 Contact**
For support or collaboration, reach out via [Karthik Ravichandran](tkgravikarthik@gmail.com).  

---
