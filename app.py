from flask import Flask, request, send_file
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

app = Flask(__name__)

@app.route('/generate_pdf', methods=['GET'])
def generate_pdf():
    # Отримання параметрів
    name = request.args.get('name', 'No Name')
    vin = request.args.get('vin', 'Unknown VIN')
    year = request.args.get('year', '2024')
    make = request.args.get('make', 'Unknown Make')
    odometer = request.args.get('odometer', '000000')
    street = request.args.get('street', 'Unknown Street')
    city = request.args.get('city', 'Unknown City')
    state = request.args.get('state', 'Unknown State')
    zip_code = request.args.get('zip', '00000')
    agent = request.args.get('agent', 'Unknown Agent')
    date = request.args.get('date', '01/01/2024')
    id = request.args.get('id', '000000')  # ID один і використовується двічі

    # Шлях до шаблону PDF
    template_path = 'MV-6.pdf'
    reader = PdfReader(template_path)
    writer = PdfWriter()

    # Створюємо новий PDF у пам'яті, щоб записати нові дані
    output_pdf = BytesIO()

    # Працюємо з першою сторінкою PDF
    page = reader.pages[0]

    # Додаємо текст у відповідні поля (координати вказують на розташування)
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    # Використовуємо надані координати для заповнення полів
    can.drawString(50, 580, f"{name}")
    can.drawString(475, 580, f"{id}")         # ID заповнюється двічі, один параметр
    can.drawString(90, 545, f"{street}")
    can.drawString(60, 525, f"{city}")
    can.drawString(439, 525, f"{state}")
    can.drawString(510, 525, f"{zip_code}")
    can.drawString(270, 485, f"{vin}")
    can.drawString(50, 465, f"{year}")
    can.drawString(150, 465, f"{make}")
    can.drawString(290, 450, f"{odometer}")
    can.drawString(130, 325, f"{vin}")             # VIN заповнюється вдруге
    can.drawString(50, 275, f"{id}")          # ID заповнюється вдруге
    can.drawString(265, 275, f"{agent}")
    can.drawString(425, 32, f"{date}")

    can.save()

    # Переміщуємо позицію на початок
    packet.seek(0)

    # Читання нового контенту і злиття його з шаблоном
    reader_for_text = PdfReader(packet)
    page.merge_page(reader_for_text.pages[0])  # Злиття сторінки з текстом

    # Записуємо злиту сторінку назад у PDF
    writer.add_page(page)

    # Записуємо результат у файл
    writer.write(output_pdf)
    output_pdf.seek(0)

    # Відправляємо PDF-файл користувачеві
    return send_file(output_pdf, as_attachment=True, download_name="filled_form.pdf", mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
