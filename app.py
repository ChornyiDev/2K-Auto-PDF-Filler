from flask import Flask, request, send_file, render_template_string
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

app = Flask(__name__)

# API Documentation HTML
api_documentation = """
<h2>API Documentation</h2>

<h3>Base URL:</h3>
<p><a href="https://pdf.2kauto.com">https://pdf.2kauto.com</a></p>

<h3>Forms for PDF Generation:</h3>

<h4>1. MV-6 Form:</h4>
<ul>
    <li>URL: <code>https://pdf.2kauto.com/mv6</code></li>
    <li>HTTP Method: <code>GET</code></li>
    <li>Description: Used to generate a PDF file for the MV-6 form.</li>
</ul>
<h5>Parameters (URL Parameters):</h5>
<ul>
    <li><code>bussines_name</code> (string): Business name</li>
    <li><code>bus_id</code> (string): Business ID</li>
    <li><code>street</code> (string): Street</li>
    <li><code>city</code> (string): City</li>
    <li><code>state</code> (string): State</li>
    <li><code>zip</code> (string): ZIP code</li>
    <li><code>vin</code> (string): Vehicle Identification Number (VIN)</li>
    <li><code>year</code> (string): Vehicle year</li>
    <li><code>make</code> (string): Vehicle make</li>
    <li><code>odometer</code> (string): Odometer reading</li>
    <li><code>inspector_name</code> (string): Inspector's name</li>
    <li><code>date</code> (string): Date</li>
</ul>
<h5>Example Request:</h5>
<pre>https://pdf.2kauto.com/mv6?bussines_name=AutoService&bus_id=123456&street=789%20Broadway&city=NewYork&state=NY&zip=10001&vin=testvin&year=2024&make=Toyota&odometer=150000&inspector_name=JaneDoe&date=09/10/2024</pre>

<h4>2. MV-426 Form:</h4>
<ul>
    <li>URL: <code>https://pdf.2kauto.com/mv426</code></li>
    <li>HTTP Method: <code>GET</code></li>
    <li>Description: Used to generate a PDF file for the MV-426 form, which consists of three pages.</li>
</ul>
<h5>Parameters (URL Parameters):</h5>
<ul>
    <li><code>bussines_name</code> (string): Business name</li>
    <li><code>bus_id</code> (string): Business ID</li>
    <li><code>street</code> (string): Street</li>
    <li><code>city</code> (string): City</li>
    <li><code>state</code> (string): State</li>
    <li><code>zip</code> (string): ZIP code</li>
    <li><code>vin</code> (string): Vehicle Identification Number (VIN)</li>
    <li><code>station_number</code> (string): Station number</li>
    <li><code>inspector_name</code> (string): Inspector's name</li>
    <li><code>station_phone</code> (string): Station phone number</li>
    <li><code>inspector_number</code> (string): Inspector's number</li>
    <li><code>date</code> (string): Date</li>
</ul>
<h5>Example Request:</h5>
<pre>https://pdf.2kauto.com/mv426?bussines_name=AutoService&bus_id=123456&street=789%20Broadway&city=NewYork&state=NY&zip=10001&vin=testvin&station_number=456789&inspector_name=JaneDoe&station_phone=5551234567&inspector_number=654321&date=09/10/2024</pre>
"""

# The root route for API documentation
@app.route('/')
def api_docs():
    return render_template_string(api_documentation)

# The route for PDF MV-6
@app.route('/mv6', methods=['GET'])
def generate_mv6():
    return generate_pdf('MV-6.pdf', 1)

# The route for PDF MV-426
@app.route('/mv426', methods=['GET'])
def generate_mv426():
    return generate_pdf('MV-426.pdf', 3)

# Function for generation PDF
def generate_pdf(template_path, total_pages):
    # Getting parameters
    bussines_name = request.args.get('bussines_name', '')
    bus_id = request.args.get('bus_id', '')
    street = request.args.get('street', '')
    city = request.args.get('city', '')
    state = request.args.get('state', '')
    zip_code = request.args.get('zip', '')
    vin = request.args.get('vin', '')
    year = request.args.get('year', '')
    make = request.args.get('make', '')
    odometer = request.args.get('odometer', '')
    inspector_name = request.args.get('inspector_name', '')


    station_number = request.args.get('station_number', '')
    station_phone = request.args.get('station_phone', '')
    inspector_number = request.args.get('inspector_number', '')
    date = request.args.get('date', '')

    reader = PdfReader(template_path)
    writer = PdfWriter()

    # Create a new PDF in memory to record new data
    output_pdf = BytesIO()

    if total_pages == 1:  # MV-6
        page = reader.pages[0]
        packet = BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)

        # Paste the text into the appropriate coordinates for MV-6 (your previous code for MV-6)
        can.drawString(50, 580, f"{bussines_name}")
        can.drawString(475, 580, f"{bus_id}")
        can.drawString(90, 545, f"{street}")
        can.drawString(60, 525, f"{city}")
        can.drawString(439, 525, f"{state}")
        can.drawString(510, 525, f"{zip_code}")
        can.drawString(270, 485, f"{vin}")
        can.drawString(50, 465, f"{year}")
        can.drawString(150, 465, f"{make}")
        can.drawString(290, 450, f"{odometer}")
        can.drawString(130, 325, f"{vin}")
        can.drawString(50, 275, f"{bus_id}")
        can.drawString(265, 275, f"{inspector_name}")
        can.drawString(425, 32, f"{date}")

        can.save()

        packet.seek(0)
        reader_for_text = PdfReader(packet)
        page.merge_page(reader_for_text.pages[0])
        writer.add_page(page)

    else:  # MV-426 with three pages
        # Processing page 1
        page1 = reader.pages[0]
        packet1 = BytesIO()
        can1 = canvas.Canvas(packet1, pagesize=letter)

        can1.drawString(40, 614, f"{bussines_name}")
        can1.drawString(410, 614, f"{bus_id}")
        can1.drawString(40, 568, f"{street}")
        can1.drawString(440, 568, f"{bus_id}")
        can1.drawString(40,546, f"{city}")
        can1.drawString(310, 546, f"{state}")
        can1.drawString(360, 546, f"{zip_code}")

        can1.save()
        packet1.seek(0)
        reader_for_text1 = PdfReader(packet1)
        page1.merge_page(reader_for_text1.pages[0])
        writer.add_page(page1)

        # Processing page 2
        page2 = reader.pages[1]
        packet2 = BytesIO()
        can2 = canvas.Canvas(packet2, pagesize=letter)

        can2.drawString(260, 700, f"{date}")
        can2.drawString(410, 700, f"{vin}")
        can2.drawString(260, 675, f"{station_number}")
        can2.drawString(410, 675, f"{inspector_name}")
        can2.drawString(260, 652, f"{station_phone}")
        can2.drawString(410, 652, f"{inspector_number}")
        can2.drawString(455, 478, f"{date}")

        can2.save()
        packet2.seek(0)
        reader_for_text2 = PdfReader(packet2)
        page2.merge_page(reader_for_text2.pages[0])
        writer.add_page(page2)

        # Processing page 3
        page3 = reader.pages[2]
        packet3 = BytesIO()
        can3 = canvas.Canvas(packet3, pagesize=letter)

        can3.drawString(400, 333, f"{date}")
        can3.drawString(520, 333, f"{station_number}")
        can3.drawString(160, 313, f"{inspector_name}")
        can3.drawString(460, 313, f"{inspector_number}")
        can3.drawString(488, 92, f"{date}")
        can3.drawString(130, 63, f"{inspector_name}")
        can3.drawString(430, 63, f"{inspector_number}")

        can3.save()
        packet3.seek(0)
        reader_for_text3 = PdfReader(packet3)
        page3.merge_page(reader_for_text3.pages[0])
        writer.add_page(page3)

    # Write the result to a file
    writer.write(output_pdf)
    output_pdf.seek(0)

    # Sending a PDF to be displayed in a browser
    return send_file(output_pdf, mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
