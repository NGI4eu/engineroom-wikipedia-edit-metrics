# engineroom-wikipedia-edit-metrics
### Compute metrics to quantify activity on different articles

The python scripts are to be executed on the Wikimedia Toolforge servers. To get an account, you can follow the instructions here: https://tools.wmflabs.org/ 
Once obtained access to the Database, create a file DB_info containing on the first line your username, and on the second line your password (you should find this information file "tool_labs.cfg" in your home directory).

The Jupyter notebook file can be run locally to process and visualize the data extracted from the Wikimedia servers.

#### Single language metrics

On the Wikimedia Toolforge server, execute the following steps for processing data on one Wikipedia language version:
1. python	get_article_ids.py input_file output_file lang -> to get the Wikipedia ids of the articles, given a list of titles (one per line in the input file) in a given Wikipedia language edition (e.g. "en" for English, "pl" for Polish) 
2. python wiki_edits_monthly_metrics.py data_directory name input_file lang -> to get activity metrics for the list of articles contained in "input_file" (it should include the ids, obtained in the previous step)

#### Multilanguage metrics

For processing the same articles across multiple Wikipedia language editions, execute the following steps: 
1. python get_article_multilanguage_ids.py input_file output_file
2. execute a bash script like the one in "multilanguage_wiki_edits_monthly_metrics_social" to get results in multiple languages.

#### Metrics monthly visualization

Once copied the results on your hard drive, run locally the Jupyter Notebook script: Visualizations.ipynb
