from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

companies = {}
company_database = []


@app.post("/company")
def create_company():
    company_data = request.get_json()
    company_id = uuid.uuid4().hex

    new_company = {**company_data, "id": company_id}

    companies[company_id] = new_company

    company_database.append(new_company)

    return {company_id: new_company}



@app.get("/company")
def fetch_all_companies():

    return companies

@app.get("/company/<string:company_id>")
def fetch_individual_company(company_id):

    return companies[company_id]

@app.put("/company/<string:id>")
def update_company_details(id):

    for selected_companies in companies:
        if selected_companies["id"] == id:
            new_company_data = request.get_json()
            selected_companies["email"] = new_company_data.get("email", companies["email"])
            return jsonify(selected_companies)
    return {"Error": "selected company not found"}

@app.delete("/company/<string:id>")
def delete_company(id):
    for selected_companies in companies:
        if selected_companies["id"] == id:
            companies.remove(selected_companies)
            return jsonify(selected_companies)
    return {"error": "no such company"}





