## API Documentation

### Base URL:
https://pdf.2kauto.com


### Forms for PDF Generation:

1. **MV-6 Form**:
   - URL: `https://pdf.2kauto.com/mv6`
   - HTTP Method: `GET`
   - Description: Used to generate a PDF file for the MV-6 form.

   #### Parameters (URL Parameters):
   
   - `bussines_name` (string): Business name
   - `bus_id` (string): Business ID
   - `street` (string): Street
   - `city` (string): City
   - `state` (string): State
   - `zip` (string): ZIP code
   - `vin` (string): Vehicle Identification Number (VIN)
   - `year` (string): Vehicle year
   - `make` (string): Vehicle make
   - `odometer` (string): Odometer reading
   - `inspector_name` (string): Inspector's name
   - `date` (string): Date

   #### Example Request:

https://pdf.2kauto.com/mv6?bussines_name=AutoService&bus_id=123456&street=789%20Broadway&city=NewYork&state=NY&zip=10001&vin=testvin&year=2024&make=Toyota&odometer=150000&inspector_name=JaneDoe&date=09/10/2024


2. **MV-426 Form**:
- URL: `https://pdf.2kauto.com/mv426`
- HTTP Method: `GET`
- Description: Used to generate a PDF file for the MV-426 form, which consists of three pages.

#### Parameters (URL Parameters):

- `bussines_name` (string): Business name
- `bus_id` (string): Business ID
- `street` (string): Street
- `city` (string): City
- `state` (string): State
- `zip` (string): ZIP code
- `vin` (string): Vehicle Identification Number (VIN)
- `station_number` (string): Station number
- `inspector_name` (string): Inspector's name
- `station_phone` (string): Station phone number
- `inspector_number` (string): Inspector's number
- `date` (string): Date

#### Example Request:

https://pdf.2kauto.com/mv426?bussines_name=AutoService&bus_id=123456&street=789%20Broadway&city=NewYork&state=NY&zip=10001&vin=testvin&station_number=456789&inspector_name=JaneDoe&station_phone=5551234567&inspector_number=654321&date=09/10/2024