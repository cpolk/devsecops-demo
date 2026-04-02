lines = ["INFO start", "ERROR timeout", "INFO done", "ERROR disk"]

count = 0

for line in lines:
    if "ERROR" in line:
        count += 1

print(count)
