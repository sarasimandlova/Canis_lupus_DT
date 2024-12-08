
import pandas as pd
import gzip
import glob

# Specify the pattern to match the Beagle files
file_pattern = 'gl.hap.chr*.beagle.gz'
beagle_files = glob.glob(file_pattern)

# Check if files are found
if not beagle_files:
    print("No Beagle files found. Check the file pattern or directory.")
    exit()

# Sort files to maintain the order, especially important for chromosome files
beagle_files.sort()

# Open a new gzip file to write the merged data
with gzip.open('merged_beagle_files.beagle.gz', 'wt') as f_out:
    # Process each file
    for i, filename in enumerate(beagle_files):
        # Open the Beagle file
        print ("processing {}".format(filename))
        with gzip.open(filename, 'rt') as f_in:
            # Read the file into a DataFrame
            df = pd.read_csv(f_in, sep='\t')
            
            # If it's the first file, write the header
            if i == 0:
                df.to_csv(f_out, sep='\t', index=False, mode='w')
            else:
                # Otherwise, skip the header
                df.to_csv(f_out, sep='\t', index=False, mode='a', header=False)

print("Merging complete. The merged file is 'merged_beagle_files.beagle.gz'")
