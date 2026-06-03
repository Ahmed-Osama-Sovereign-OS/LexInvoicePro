from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

class PDFGenerator:
    def __init__(self, filename):
        self.filename = filename

    def create_invoice_pdf(self, client_name, service, amount, tax, total):
        c = canvas.Canvas(self.filename, pagesize=A4)
        width, height = A4

        # التصميم (Minimal Business Style)
        c.setFont("Helvetica-Bold", 24)
        c.drawString(50, height - 50, "LexInvoice Pro")
        
        c.setFont("Helvetica", 12)
        c.drawString(50, height - 80, f"Client: {client_name}")
        c.drawString(50, height - 100, f"Date: {datetime.now().strftime('%Y-%m-%d')}")
        
        # الجدول
        c.line(50, height - 120, 550, height - 120)
        c.drawString(50, height - 140, f"Service: {service}")
        c.drawString(400, height - 140, f"Price: ${amount}")
        
        # الإجمالي
        c.setFont("Helvetica-Bold", 16)
        c.drawString(400, height - 200, f"Total: ${total}")
        
        # تذييل الصفحة
        c.setFont("Helvetica-Oblique", 10)
        c.drawString(200, 50, "Thank you for your business - Ahmed Osama")
        
        c.save()
