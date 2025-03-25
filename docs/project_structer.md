# Alzheimer's Disease Prediction - Project Structure

```
alzheimers-prediction/
│
├── data/
│
├── logs/
│
├── models/
│
├── config.py
│
├── pyproject.toml # for poetry configuration
│
├── src/
│   ├── data/
│   │   ├── __init__.py
│   │   ├── preprocessing.py      # Image preprocessing functions
│   │   └── data_loader.py        # Data loading and generation functions
│   │
│   ├── model/
│   │   ├── __init__.py
│   │   ├── architecture.py       
│   │   └── training.py          
│   │
│   ├── evaluation/
│   │   ├── __init__.py
│   │   ├── metrics.py            
│   │   └── visualization.py      
│   │
│   ├── prediction/
│   │   ├── __init__.py
│   │   └── inference.py          # Functions for making predictions
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   └── logger.py
│   │
│   └── main.py
│
├── tests/
└── requirements.txt
```