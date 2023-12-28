import csv

# Open the CSV file and read in the data
with open('Attendance.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    # Skip the header row
    next(reader)
    # Create dictionaries to store the attendance data
    present_counts = {}
    absent_counts = {}
    for row in reader:
        name = row[0]
        arrival_time = row[1]
        if arrival_time <= '08:45':
            present_counts[name] = present_counts.get(name, 0) + 1
        else:
            absent_counts[name] = absent_counts.get(name, 0) + 1

# Create an HTML file to display the attendance data
with open('index.html', 'w') as htmlfile:
    # Write the HTML header
    htmlfile.write('<html>\n<head>\n<title>Attendance</title>\n')
    # Add CSS styles to the HTML file for a more presentable table
    htmlfile.write('<style>\n')
    htmlfile.write('table {\n')
    htmlfile.write('    border-collapse: collapse;\n')
    htmlfile.write('    width: 100%;\n')
    htmlfile.write('}\n')
    htmlfile.write('th, td {\n')
    htmlfile.write('    text-align: left;\n')
    htmlfile.write('    padding: 8px;\n')
    htmlfile.write('}\n')
    htmlfile.write('th {\n')
    htmlfile.write('    background-color: #4CAF50;\n')
    htmlfile.write('    color: white;\n')
    htmlfile.write('}\n')
    htmlfile.write('tr:nth-child(even) {\n')
    htmlfile.write('    background-color: #f2f2f2;\n')
    htmlfile.write('}\n')
    htmlfile.write('</style>\n')
    htmlfile.write('</head>\n<body>\n')
    # Write a table to display the attendance data
    htmlfile.write('<h1>Attendance</h1>\n')
    htmlfile.write('<table>\n<thead>\n<tr><th>Name</th><th>Present</th><th>Absent</th></tr>\n</thead>\n<tbody>\n')
    for name in sorted(set(list(present_counts.keys()) + list(absent_counts.keys()))):
        present_count = present_counts.get(name, 0)
        absent_count = absent_counts.get(name, 0)
        htmlfile.write(f'<tr><td>{name}</td><td>{present_count}</td><td>{absent_count}</td></tr>\n')
    # Write the HTML footer
    htmlfile.write('</tbody>\n</table>\n</body>\n</html>\n')
