# ComSto
The repository describes the implementation of the ComSto data storytelling framework. ComSto framework automatically generates histograms comparison report.
This framework makes it easy for data scientists to quickly generate comparison reports for a pair of histograms.

The following following python3 libraries are required to successfully run the program:

- numpy
- pandas
- matplotlib
- yattag
- scipy
- clipspy==0.3.3

Run the program by typing the following:

python3 main_prog.py <csv_input_file> <story_type>

Two arguments are expected. The first argument is the csv file containing the datasets of the two histograms to be compared (see input files in the data folder). 
The second argument is the type of story you want to see. Three options are available for the story type, they are either "short", "detailed" or "both".




