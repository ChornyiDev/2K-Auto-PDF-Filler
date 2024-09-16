from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def generate_grid():
    c = canvas.Canvas("coordinate_grid.pdf", pagesize=letter)
    width, height = letter
    
    # Малюємо сітку з кроком 50 пікселів по X і Y
    for x in range(0, int(width), 50):
        c.line(x, 0, x, height)
        c.drawString(x, 10, str(x))

    for y in range(0, int(height), 50):
        c.line(0, y, width, y)
        c.drawString(10, y, str(y))

    c.save()

# Генеруємо координатну сітку
generate_grid()
