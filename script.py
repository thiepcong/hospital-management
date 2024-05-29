import subprocess
import os

services = [
    'patient',
    'medical_record',
    'appointment',
    'doctor',
    'employee',
    'clinic',
    'pharmacy',
    'invoice'
]
ports = [
    8000,  
    8001, 
    8002, 
    8003, 
    8004, 
    8005, 
    8006,
    8007cd 
]

# Run each project
for service, port in zip(services, ports):
    command = f"py {service}/manage.py runserver {port}"
    subprocess.Popen(command, shell=True)

print("All Django projects have been started.")
