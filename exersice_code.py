import csv

def add_segment_length(input_file, output_file):
    # Open the input CSV file for reading
    with open(input_file, mode='r') as infile:
        # Create a CSV reader object
        reader = csv.DictReader(infile)
        
        # Get the fieldnames from the input file and add the new column 'segment_length'
        fieldnames = reader.fieldnames + ['segment_length']
        
        # Open the output CSV file for writing
        with open(output_file, mode='w') as outfile:
            # Create a CSV writer object
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            
            # Write the header to the output file
            writer.writeheader()
            
            # Iterate over each row in the input file
            for row in reader:
                # Calculate the segment length
                segment_length = int(row['loc.end']) - int(row['loc.start'])
                
                # Add the segment length to the row
                row['segment_length'] = segment_length
                
                # Write the updated row to the output file
                writer.writerow(row)

# Define the input and output file paths
input_file_path = 'brca_cnvs_tcga-1-2.csv'  # Replace with your input file path
output_file_path = 'output_file_exercise_HNO.csv'  # Replace with your desired output file path

# Call the function to process the file
add_segment_length(input_file_path, output_file_path)