# Commands
!! Path to files is from path of project_cli/project_cli, hence the `data/` dir for example's path is `../data` !!
ALL COMMANDS HAVE TO BE PREFIXED BY `mycli`.
## check-key
- Prints whether MODAT Magnify API Key is Set or not and Valid or Invalid
## set-key
- Saves user input key after checking it is valid
## manual-call
- User makes service_search (`manual-call services`), host_search (`manual-call hosts`) or history_search (`manual-call histories`) based on input and can save the JSON response (which gets saved in data)
## get-from-csv
- Given a user input csv with a column for queries with "query" column for services and hosts (`get-from-csv services`, `get-from-csv hosts`) or the different query columns of history ("since", "ip", "port", "transport") (`get-from-csv histories`), this command runs the queries with MODAT Magnify API and stores result "page"/"history" in results and number of results in "n_results"
## extract-from-csv
- Using a csv outputed from the `get-from-csv` command, extract the result column and make it into a csv of its own. (`extract-from-csv services`) (only works for sevices for now)
## generate-history-queries
- Using a csv of services results of MODAT Magnify service search API Call, generate a csv with history search queries to then run `get-from-csv histories`