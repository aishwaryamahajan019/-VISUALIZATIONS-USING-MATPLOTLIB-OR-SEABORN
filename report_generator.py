import pandas as pd
from fpdf import FPDF

# Load data from CSV
data = pd.read_csv("data.csv")

# Analyze data
total_sales = data['Sales'].sum()
avg_sales = data['Sales'].mean()
sales_by_dept = data.groupby("Department")["Sales"].sum()

# Initialize PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Automated Sales Report", ln=True, align='C')

# Summary Section
pdf.set_font("Arial", size=12)
pdf.ln(10)
pdf.cell(200, 10, txt=f"Total Sales: Rs{total_sales}", ln=True)
pdf.cell(200, 10, txt=f"Average Sales: Rs{avg_sales:.2f}", ln=True)

# Department-wise Sales
pdf.ln(10)
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, txt="Sales by Department:", ln=True)
pdf.set_font("Arial", size=12)
for dept, sales in sales_by_dept.items():
    pdf.cell(200, 10, txt=f"- {dept}: Rs{sales}", ln=True)

# Table Header
pdf.ln(10)
pdf.set_font("Arial", 'B', 12)
pdf.cell(60, 10, txt="Name", border=1)
pdf.cell(60, 10, txt="Department", border=1)
pdf.cell(60, 10, txt="Sales", border=1)
pdf.ln()

# Table Content
pdf.set_font("Arial", size=12)
for index, row in data.iterrows():
    pdf.cell(60, 10, txt=str(row["Name"]), border=1)
    pdf.cell(60, 10, txt=str(row["Department"]), border=1)
    pdf.cell(60, 10, txt=str(row["Sales"]), border=1)
    pdf.ln()

# Save PDF
pdf.output("sales_report.pdf")
print("✅ Report generated: sales_report.pdf")
