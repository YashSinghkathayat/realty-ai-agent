from flask import Flask, render_template, request
from app.services.property_service import get_property_count
from app.services.qualification_service import qualify_lead

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Collect form data
        data = {
            "name": request.form.get('name', ''),
            "location": request.form.get('location', ''),
            "type": request.form.get('property_type', ''),
            "subtype": request.form.get('subtype', ''),
            "budget": request.form.get('budget', ''),
            "consent": request.form.get('consent', '')
        }
        
        # Process logic using existing services
        property_count = get_property_count(
            data["location"],
            data["type"],
            data["budget"]
        )
        status = qualify_lead(data, property_count)
        
        # Render result
        return render_template(
            'result.html',
            name=data["name"],
            property_count=property_count,
            status=status
        )
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
