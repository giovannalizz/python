with open("hr_system.txt") as hrsystem:
    for line in hrsystem:
        parts = line.split()
        name = parts[0]
        id = parts[1]
        jobs = parts[2]
        salary = float(parts[3])

        payment = salary / 24

        if jobs == "Engineer":
            payment += 1000

        print(f"{name} (ID: {id}), {jobs} - ${payment:.2f}")