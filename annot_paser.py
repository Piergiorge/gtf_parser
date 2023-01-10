# Open the GTF file
with open("genes.gtf") as f:
    # Read the file line by line
    for line in f:
        # Split the line into fields
        fields = line.strip().split("\t")
        
        # Extract the gene ID and gene size from the fields
        gene_id = fields[8].split(";")[0].split(" ")[1]
        gene_size = int(fields[4]) - int(fields[3])
        
        # Print the gene ID and size
        print(f"Gene {gene_id}: {gene_size} bp")
