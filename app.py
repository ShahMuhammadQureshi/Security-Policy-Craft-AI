import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import joblib
from fpdf import FPDF

# Load data from CSV
data = pd.read_csv('recommendations.csv')

# Separate features and target
X = data[['network_size', 'connected_devices', 'internet_usage', 'data_sensitivity']]
y = data['Recommendation']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize categorical features using TF-IDF
vectorizer = TfidfVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train.apply(lambda x: ' '.join(x), axis=1))
X_test_vectorized = vectorizer.transform(X_test.apply(lambda x: ' '.join(x), axis=1))

# Train SVM model
model = SVC(kernel='linear')
model.fit(X_train_vectorized, y_train)


# Save model and vectorizer
joblib.dump(model, 'recommendation_model.pkl')
joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')

import tkinter as tk
from tkinter import messagebox
import joblib

# Load trained model and vectorizer
model = joblib.load('recommendation_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

def create_pdf(selected_recommendations):
    pdf = FPDF()
    pdf.add_page()

    # Set font for the title
    pdf.set_font("Arial", style='B', size=26)

    for i in range (2):
        pdf.ln()

    # Title
    pdf.multi_cell(200, 10, txt="Smart \n\nSecurity_Policy \n\nGenerator", align='C')


    for i in range (4):
        pdf.ln()

    # Specific Recommendations
    pdf.set_font("Arial", style='B', size=20)
    pdf.cell(200, 10, txt="\nSecurity Policies", ln=True, align='C')
    pdf.set_font("Arial", size=12)

    # Convert the selected recommendations to a list of strings
    recommendations_list = selected_recommendations.split("\n")
    
    for rec in recommendations_list:
        # Remove any leading or trailing whitespaces
        rec = rec.strip()
        
        # Skip empty lines
        if rec:
            pdf.multi_cell(0, 10, txt=rec)

    pdf_output = "security_policies.pdf"
    pdf.output(pdf_output)

    print(f"PDF file '{pdf_output}' created successfully.")


def generate_pdf_on_click(selected_recommendations):
    # Call the function to create PDF with recommendations
    create_pdf(selected_recommendations)



# Function to make recommendations based on user input
def make_recommendation():
    # Get user input from entry widgets
    network_size = network_size_var.get()
    connected_devices = connected_devices_var.get()
    internet_usage = internet_usage_var.get()
    data_sensitivity = data_sensitivity_var.get()
    
    # Vectorize user input
    input_text = ' '.join([network_size, connected_devices, internet_usage, data_sensitivity])
    input_vectorized = vectorizer.transform([input_text])
    
    # Make prediction
    recommendation = model.predict(input_vectorized)[0]
    
    # Show recommendation in a message box
    messagebox.showinfo("Recommendation", f"Recommendation: {recommendation}")
    print(recommendation)
    pdf_button = tk.Button(root, text="Generate PDF", command=lambda: generate_pdf_on_click(recommendation))
    pdf_button.grid(row=7, column=0, columnspan=2)

# Create GUI
root = tk.Tk()
root.title("Policy Craft")
root.geometry("200x200")

network_size_label = tk.Label(root, text="Network Type:")
network_size_label.grid(row=0, column=0)
network_size_var = tk.StringVar(root)
network_size_dropdown = tk.OptionMenu(root, network_size_var, "home", "office")
network_size_dropdown.grid(row=0, column=1)

connected_devices_label = tk.Label(root, text="Connected Devices: ")
connected_devices_label.grid(row=1, column=0)
connected_devices_var = tk.StringVar(root)
connected_devices_dropdown = tk.OptionMenu(root, connected_devices_var, "laptops", "desktops", "IoT devices")
connected_devices_dropdown.grid(row=1, column=1)

internet_usage_label = tk.Label(root, text="Internet Usage: ")
internet_usage_label.grid(row=2, column=0)
internet_usage_var = tk.StringVar(root)
internet_usage_dropdown = tk.OptionMenu(root, internet_usage_var, "work", "entertainment", "online transactions")
internet_usage_dropdown.grid(row=2, column=1)

data_sensitivity_label = tk.Label(root, text="Data sensitivity: ")
data_sensitivity_label.grid(row=3, column=0)
data_sensitivity_var = tk.StringVar(root)
data_sensitivity_dropdown = tk.OptionMenu(root, data_sensitivity_var, "low", "medium", "high")
data_sensitivity_dropdown.grid(row=3, column=1)

recommend_button = tk.Button(root, text="Get Recommendation", command=make_recommendation)
recommend_button.grid(row=4, columnspan=2)

root.mainloop()
