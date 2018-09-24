VictorOps-SalesForce
====================

Integration using VictorOps Alert Ingestion API.

## Customer Email Domains

To produce a .csv file of known customer email domains, without duplicates and excluding common email providers:

* In Salesforce, access Reports >> Operations Support folder >> Customer Email Domains

* Run the report and then export it as a .csv file to your Downloads folder

* In your Downloads folder, change the name of the exported report from "report....." to "customer_email_domains.csv"

* Run the `process_exported_email_domains.py` script

* In your downloads folder, you will find a new file called "customer_email_domains_final.csv"
