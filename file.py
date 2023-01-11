def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w")

    file.write("Company, Position, Verifyed, Region, Salary\n")
    for job in jobs:
        file.write(f"{job['company']}, {job['positon']}, {job['verified']}, {job['region']}, {job['salary']}\n")

    file.close()