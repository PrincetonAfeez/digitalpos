import csv

staff = [
    {"name": "Flores, Ever", "dept": "BOH", "hourly_rate": 22.00},
    {"name": "Ramirez, Edward", "dept": "BOH", "hourly_rate": 22.00},
    {"name": "Gong, Bai", "dept": "BOH", "hourly_rate": 21.00},
    {"name": "Espinosa, Jose", "dept": "BOH", "hourly_rate": 23.00},
    {"name": "Verrera, Jorge", "dept": "BOH", "hourly_rate": 25.00},
    {"name": "Manilla, Maureen", "dept": "FOH", "hourly_rate": 18.00},
    {"name": "Quintilla, Cindy", "dept": "FOH", "hourly_rate": 18.00},
    {"name": "Adler, Samantha", "dept": "FOH", "hourly_rate": 18.00},
    {"name": "Manni, Malina", "dept": "FOH", "hourly_rate": 18.00},
    {"name": "Crawford, Nichole", "dept": "FOH", "hourly_rate": 18.00}
]

# Writing to the CSV file
with open("staff.csv", "w", newline="") as file:
    # Define the headers based on your dictionary keys
    fieldnames = ["name", "dept", "hourly_rate"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(staff)

print("✅ staff.csv has been generated successfully!")
