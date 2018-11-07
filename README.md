# engineroom-wikipedia-edit-metrics
### Compute Wikipedia articles activity metrics

The python scripts are to be executed on the Wikimedia Toolforge servers. To get an account, you can follow the instructions here: https://tools.wmflabs.org/ 
Once obtained access to the Database, create a file DB_info containing on the first line your username, and on the second line your password (you should find this information file "tool_labs.cfg" in your home directory).

The Jupyter notebook file can be run locally to process and visualize the data extracted from the Wikimedia servers.

### Execution

#### Single language metrics

On the Wikimedia Toolforge server, execute the following steps for processing data on one Wikipedia language version:
1. python	get_article_ids.py input_file output_file lang -> to get the Wikipedia ids of the articles, given a list of titles (one per line in the input file) in a given Wikipedia language edition (e.g. "en" for English, "pl" for Polish) 
2. python wiki_edits_monthly_metrics.py data_directory name input_file lang -> to get activity metrics for the list of articles contained in "input_file" (it should include the ids, obtained in the previous step)

#### Multilanguage metrics

For processing the same articles across multiple Wikipedia language editions, execute the following steps: 
1. python get_article_multilanguage_ids.py input_file output_file
2. execute a bash script like "multilanguage_wiki_edits_monthly_metrics_social" to get results in multiple languages.

#### Metrics monthly visualization

Once copied the results on your hard drive, run locally the Jupyter Notebook script: Visualizations.ipynb

### Metric descpription

* **pageviews**: numer of times an article has been accessed during one month.

* **month_edits**: number of revisions of the article during a given month, i.e. number of times it has been edited. 

* **month_reverts**: number of reverts on the article during a given month, i.e. number of times a user has canceled the edit of another user.

* **month_mutual_reverts**: number of mutual reverts on the article during a given month, i.e. number of times two users have mutually canceled each other's edit.

* **month_users**: number of distinct users who edited the article during a given month, counting different IPs (anonymous editors) as different users.

* **month_users_reg**: number of distinct registered users who edited the article during a given month (excluding anonymous editors).

* **month_reverting_users**: number of distinct users who made some revert in the article during a given month.

* **month_mutual_reverting_users**: number of distinct users involved in some mutual revert in the article during a given month.


