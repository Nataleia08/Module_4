emp_location = {
    "name": "Alise",
    "age": 25,
    "salary": 1200,
    "city": "New York"
}

emp_location["location"] = emp_location.pop("city")
print(emp_location)
