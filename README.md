# 🛡️ Smart Security Policy Generator

A lightweight desktop application that recommends security policies based on user input. Built using Python and machine learning, the app classifies scenarios using a pre-trained SVM model and provides results through a user-friendly GUI.

---
```bash
## 📁 Files Included

├── pro.py # Main Python application (GUI + logic)
└── recommendation_model.pkl # Pre-trained SVM model for prediction


```
---

## 🚀 Features

- 🔐 **ML-based Policy Recommendations**
- 🖥️ **Tkinter GUI for Input**
- 📄 **PDF Export of Suggested Policies**
- 🧠 **Pre-trained Model Included**

---

## ▶️ How to Run

1. **Install Required Libraries**:
   ```bash
   pip install scikit-learn pandas joblib fpdf
Run the App:

```bash

python app.py
```
---

📌 Usage
Select network type, device type, internet usage, and data sensitivity.

Click Get Recommendation to view your security policy.

Click Generate PDF to export the result.

📝 Note
Make sure recommendation_model.pkl is in the same directory as pro.py.

recommendations.csv is not needed — the model is already trained.

