import sys
import os
import argparse
import sqlite3
import csv

# Setup argument parser
parser = argparse.ArgumentParser("PRECSNumbers")
parser.add_argument('-i', '--input', type=str, help="Path to anonymized DB", required=True)

# Parse Args
args = parser.parse_args()

rows = []
with open(args.input, 'r') as infile:
    csvreader = csv.reader(infile, delimiter=",", quotechar='"')
    for row in csvreader:
        rows.append(row)

# Remove column definitions
column_titles = rows[0]

del rows[0]

def add_one_to_dictionary(key, the_dict):
    if key not in the_dict:
        the_dict[key] = 1
    else:
        the_dict[key] += 1

article_classifications = {}
num_articles = 0
email_responses = {}
num_emails = 0
replication_amounts = {}
reproducibility_efforts = {}
replication_origins = {}
icerm_criteria = {}
num_replications = 0

for row in rows:
    num_articles += 1
    article_code_id = int(row[1])
    add_one_to_dictionary(article_code_id, article_classifications)
    reply_code_id = -1
    if row[2] != "":
        reply_code_id = int(row[2])
    else:
        add_one_to_dictionary(-1, replication_origins)
    if reply_code_id != -1:
        num_emails += 1
        add_one_to_dictionary(reply_code_id, email_responses)
    #if reply_code_id > 2:
    #    num_replies += 1
    
    replication_amount_id = -1
    reproducibility_effort_id = -1
    if row[3] != "":
        if row[2] != "":
            add_one_to_dictionary(reply_code_id, replication_origins)
        replication_amount_id = int(row[3])
        reproducibility_effort_id = int(row[4])
        add_one_to_dictionary(replication_amount_id, replication_amounts)
        add_one_to_dictionary(reproducibility_effort_id, reproducibility_efforts)
        # Store criteria

        for column_idx in range(5,len(row)):
            criteria_num = column_idx-4
            # Skip criteria 8.
            if criteria_num >= 8:
                criteria_num += 1
            # I know.. confusing..
            if int(row[column_idx]) == 0:
                add_one_to_dictionary(criteria_num, icerm_criteria)

        num_replications += 1

def percentage(ratio):
    return "%3.1f%%" % (100*ratio)

print("\nTable 1: Artifact Access via Information in the Article: (N = {})".format(num_articles))
print("No discussion in the article, and no artifacts made available: {} {}".format(article_classifications[0], percentage(article_classifications[0]/num_articles)))
print("Some discussion of artifacts, none made available: {} {}".format(article_classifications[1], percentage(article_classifications[1]/num_articles)))
rest = 0
for key in article_classifications:
    if key > 1:
        rest += article_classifications[key]
print("Some artifacts made available: {} {}".format(rest, percentage(rest/num_articles)))

print("\nArtifact Access by Direct Email Request (N = {} *(we sent 298 emails, but two of these emails asked about two articles each, so we emailed about {} articles.))".format(num_emails, num_emails))
no_response = 0
response_no_code = 0
response_some_code = 0
for key in email_responses:
    if key < 3:
        no_response += email_responses[key]
    elif 3 <= key and key <= 11:
        response_no_code += email_responses[key]
    elif key > 11:
        response_some_code += email_responses[key]
print("No response: {} {}".format(no_response, percentage(no_response/num_emails)))
print("Response, but no artifacts made available: {} {}".format(response_no_code, percentage(response_no_code/num_emails)))
print("Some artifacts made available: {} {}".format(response_some_code, percentage(response_some_code/num_emails)))

print("\nArticle Artifiact Origins")
print("Article, no email: {} {}".format(replication_origins[-1], percentage(replication_origins[-1]/num_replications)))
#print("Emailed, no response: {} {}".format(replication_origins[1], percentage(replication_origins[1]/num_replications)))
#print("Emailed, didn't get anything new: {} {}".format(replication_origins[9], percentage(replication_origins[9]/num_replications)))
#print("Emailed, directed to supplementary materials: {} {}".format(replication_origins[10], percentage(replication_origins[10]/num_replications)))
print("Emailed, got some: {} {}".format(replication_origins[12], percentage(replication_origins[12]/num_replications)))
print("Emailed for more, no reply or nothing new: {} {}".format((replication_origins[1]+replication_origins[9]+replication_origins[10]), percentage((replication_origins[1]+replication_origins[9]+replication_origins[10])/num_replications)))

print("\nTable 2: ICERM Article Information Evaluation Criteria Implementation (n={})".format(num_replications))
print("A precise statement of assertions to be made in the paper: {} {}".format(icerm_criteria[1], percentage(icerm_criteria[1]/num_replications)))
print("Full statement (or valid summary) of experimental results: {} {}".format(icerm_criteria[2], percentage(icerm_criteria[2]/num_replications)))
print("Salient details of data reduction & statistical analysis methods: {} {}".format(icerm_criteria[3], percentage(icerm_criteria[3]/num_replications)))
print("Necessary run parameters were given: {} {}".format(icerm_criteria[4], percentage(icerm_criteria[4]/num_replications)))
print("A statement of the computational approach, and why it rigorously tests the hypothesized assertions: {} {}".format(icerm_criteria[5], percentage(icerm_criteria[5]/num_replications)))
print("Complete statements of, or references to, algorithms and salient software details: {} {}".format(icerm_criteria[6], percentage(icerm_criteria[6]/num_replications)))
print("Discussion of the adequacy of parameters such as precision level and grid resolution: {} {}".format(icerm_criteria[7], percentage(icerm_criteria[7]/num_replications)))
print("Availability of computer code, input and output data, with some reasonable level of documentation: {} {}".format(icerm_criteria[9], percentage(icerm_criteria[9]/num_replications)))
try:
    print("Avenues of exploration examined throughout development, including negative findings: {} {}".format(icerm_criteria[10], percentage(icerm_criteria[10]/num_replications)))
except:
    print("Avenues of exploration examined throughout development, including negative findings: {} {}".format(0, percentage(0./num_replications)))
print("Instructions for repeating computational experiments described in the article: {} {}".format(icerm_criteria[11], percentage(icerm_criteria[11]/num_replications)))
print("Precise functions were given, with settings: {} {}".format(icerm_criteria[12], percentage(icerm_criteria[12]/num_replications)))
print("Salient details of the test environment e.g. hardware, system software, and number of processors used: {} {}".format(icerm_criteria[13], percentage(icerm_criteria[13]/num_replications)))


print("\nTable 3: Evaluation of Artifacts and Archiving (n={})".format(num_replications))
print("Data documented to clearly explain what each part represents: {} {}".format(icerm_criteria[14], percentage(icerm_criteria[14]/num_replications)))
print("Data archived with significant longevity expected: {} {}".format(icerm_criteria[15], percentage(icerm_criteria[15]/num_replications)))
print("Data location provided in the acknowledgements: {} {}".format(icerm_criteria[16], percentage(icerm_criteria[16]/num_replications)))
print("Authors have documented use and licensing rights: {} {}".format(icerm_criteria[17], percentage(icerm_criteria[17]/num_replications)))
print("Software documented well enough to run it and what it ought to do: {} {}".format(icerm_criteria[18], percentage(icerm_criteria[18]/num_replications)))
print("The code is publicly available with no download requirements: {} {}".format(icerm_criteria[19], percentage(icerm_criteria[19]/num_replications)))
print("There was some method to track software changes, and some persistence of archiving: {} {}".format(icerm_criteria[20], percentage(icerm_criteria[20]/num_replications)))

print("\nTable 4: Computational Reproducibility Evaluation (n={})".format(num_replications))
try:
    print("Straightforward to reproduce with minimal effort: {} {}".format(reproducibility_efforts[8], percentage(reproducibility_efforts[8]/num_replications)))
except:
    print("Straightforward to reproduce with minimal effort: {} {}".format(0, percentage(0./num_replications)))
try:
    print("Minor difficulty in reproducing: {} {}".format(reproducibility_efforts[7], percentage(reproducibility_efforts[7]/num_replications)))
except:
    print("Minor difficulty in reproducing: {} {}".format(0, percentage(0./num_replications)))
print("Reproducible after some tweaking: {} {}".format(reproducibility_efforts[6], percentage(reproducibility_efforts[6]/num_replications)))
print("Could reproduce with fairly substantial skill and knowledge: {} {}".format(reproducibility_efforts[5], percentage(reproducibility_efforts[5]/num_replications)))
print("Reproducible with substantial intellectual effort: {} {}".format(reproducibility_efforts[4], percentage(reproducibility_efforts[4]/num_replications)))
print("Reproducible with substantial tedious effort: {} {}".format(reproducibility_efforts[3], percentage(reproducibility_efforts[3]/num_replications)))
print("Difficult to reproduce because of unavoidable inherent complexity: {} {}".format(reproducibility_efforts[2], percentage(reproducibility_efforts[2]/num_replications)))
print("Nearly impossible to reproduce: {} {}".format(reproducibility_efforts[1], percentage(reproducibility_efforts[1]/num_replications)))
print("Impossible to reproduce: {} {}".format(reproducibility_efforts[0], percentage(reproducibility_efforts[0]/num_replications)))

print("\nReplication Status (n={})".format(num_replications))
try:
    print("Fully Replicated: {} {}".format(replication_amounts[4], percentage(replication_amounts[4]/num_replications)))
except:
    print("Fully Replicated: {} {}".format(0, percentage(0./num_replications)))
print("Partially Replicated: {} {}".format(replication_amounts[3], percentage(replication_amounts[3]/num_replications)))
print("Ran: {} {}".format(replication_amounts[2], percentage(replication_amounts[2]/num_replications)))
print("Build: {} {}".format(replication_amounts[1], percentage(replication_amounts[1]/num_replications)))
print("Nothing: {} {}".format(replication_amounts[0], percentage(replication_amounts[0]/num_replications)))
