import csv

input_file = 'dataset/1-frontViewTrimmed_frameNo.csv'
output_file = 'dataset/1-frontViewTrimmed_frameNo_2d.csv'
new_z_value = 0.0  # The value to set for all z coordinates

with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Write the header
    header = next(reader)
    writer.writerow(header)

    for row in reader:
        # Update z values
        for i in range(3, len(row), 4):
            row[i] = new_z_value
        writer.writerow(row)

print(f"Updated CSV file saved as {output_file}")