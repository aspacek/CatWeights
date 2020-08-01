CatWeights.py
  - Reads in an input of cat weights and plots them.

Input file
  - Needs to be 4 columns of data, separated by tabs.
  - Any non-data in the file needs to be more or less than 4 columns on a line, so it can be ignored.
  - Columns are: Date, Location, Cat, Weight
  - See "CatWeights_Example.txt" for an example input file.

Output file
  - A single plot of all of the input data.
  - See "CatWeights_Example.png" for an example output file.

Running the program:
  - The program is run using the following input format:
    (the number of cat_name inputs at the end just need to match the cat_number given)

  >> python CatWeights.py input_file output_file cat_number cat_name_1 cat_name_2

  - An example command to run the example input file and create the example output file:

  >> python CatWeights.py CatWeights_Example.txt CatWeights_Example.png 2 Pookie Snowbll

