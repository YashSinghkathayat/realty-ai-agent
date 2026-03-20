from flask import Flask, render_template, request
from services.property_service import get_property_count
from services.qualification_service import qualify_lead

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = {
            "name": request.form.get('name', ''),
            "location": request.form.get('location', ''),
            "type": request.form.get('property_type', ''),
            "subtype": request.form.get('subtype', ''),
            "budget": request.form.get('budget', ''),
            "consent": request.form.get('consent', '')
        }

        property_count = get_property_count(
            data["location"],
            data["type"],
            data["budget"]
        )

        status = qualify_lead(data, property_count)

        return render_template(
            'result.html',
            name=data["name"],
            property_count=property_count,
            status=status
        )

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)