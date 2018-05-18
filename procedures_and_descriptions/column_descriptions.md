# Dataset Description

We lay out here the description of our dataset csv file. Each row represents an article which was part of our study. Below we detail the purpose of each column along with what values it may take. We number columns starting from 0 as the left-most column and increasing to the right.

## Article Specific Columns

These columns refer to data contained in the article itself.

**0 - Article ID**: A randomly selected integer representing the article.

**1 - Article Code ID**: Each article was read and it’s code content was classified into one of seven categories. These categories are indicated in this column with an integer from 0 to 5. The key for this code is here and is listed in order of increasing code information disclosure:

## Emailing Information

When code information wasn’t forthcoming from the article, the authors were emailed for code or information. An initial email was sent along with a reminder if no response is recorded. These columns concern the emailing process.

**2 - Email Reply Code ID**: Replies from authors to email solicitation for code and data were categorized based on their content regarding the code and data which was asked for. If no email was sent, this column will be empty. The below codes are listed in increasing code disclosure.

* 0 - No Response: No response to the email was received
* 1 - Email Bounced: The email was incorrect or no longer active, and a bounce message was received
* 2 - Auto-response: An email auto-response was received, but the author didn’t get back to us.
* 3 - Impossible to share: The authors give a reason such as export control restrictions or licensing issues which make it impossible for them to share their code
* 4 - Refusal to share: The authors give reasons such as that their code is messy, or the codebase is too big for why they don’t want to share their code.
* 5 - Asks for reason: The authors ask why they should share their code
* 6 - Asks screening questions: The authors ask questions about our group in an effort to screen whether we’re worth their time
* 7 - Contact another person: The authors ask us to contact another person in their group for the source code
* 8 - Unfulfilled promise to follow up: The authors say they’ll get back to us with the requested code or data. They never do.
* 9 - Didn’t get anything new: The authors sent something, but it wasn’t something not already included in the supplementary materials or the article itself.
* 10 - Directed to supplementary materials: The authors directed us to their supplemental materials (supplemental materials were considered before emailing the authors for more information)
* 11 - Will share after setup: The authors offered to share necessary data after some preliminary setup was completed.
* 12 - Shared at least some data and code: The authors sent at least some code and data.

## Replication Information

These fields are associated with work we did to replicate the authors results

**3 - Replication Amount**: This is an objective measure of how much of the article we were able to replicate within a 4 hour time limit. If no code or data was received from the article, this column will be blank.

* 0 - Nothing: We were not able to build any code sent to us. The Build process was either not documented well enough or failed with errors we were unable to fix in the time limit.
* 1 - Build: We were able to build the code sent to us, but running the code caused crashes that we were unable to resolve in the time limit.
* 2 - Run: We were able to build and run the code sent to us, but were unable to replicate any of the numbers or figures in the article.
* 3 - Partial Replication: We were able to build, run, and replicate at least some of the numbers in tables or figures in the article.
* 4 - Replicated: We were able to build, and run the code we received and replicate all results reported in the article.

**4 - Reproducibility Effort ID**: This represents our subjective assessment of the effort required for a knowledgable scientist in the domain to replicate all aspects of the article. In some cases, the category the article falls in was apparent either because all aspects of the article were easy to reproduce, or because essential data was missing. In the case that such a clear determination could not be made before the time limit, we made a subjective determination whether or not it was possible to complete the replication given special skill, time, and effort, and placed the article in the appropriate category.

* 0 - Impossible to reproduce: the given code/data is missing essential code, data,or methodology
* 1 - Nearly impossible to reproduce: specialized hardware,intense computation requirements, sensitive data,human study, or other unavoidable reasons preventing reproduction.
* 2 - Difficult to reproduce because of unavoidable inherent complexity: Difficulties with reproduction which are unavoidable because of the problem. e.g., requiring 300 million Markov chain Monte Carlo steps on each dataset, or needing months to do runs
* 3 - Reproducible with substantial tedious effort:  e.g.,individual download of a large number of datasets,hand coding of data into a new format, i.e., from an image, many archiving steps required
* 4 - Reproducible with substantial intellectual effort: e.g.,methods well defined but required some knowledge of jargon or understanding of the field; or down the rabbit hole references to past articles required to reproduce; etc.
* 5 - Could reproduce with fairly substantial skill and knowledge: e.g., required GPU programing abilities to run code that wasn’t given; translating complex models into MATLAB code; pseudo code with functions not detailed described in text into code; missing scripts
* 6 - Reproducible after tweaking: e.g., missing parameters required fiddling to find, missing modified code lines, missing arguments required for differing architecture; missing minor method step
* 7 - Minor difficulty in reproducing: e.g., installing a specialized library, converting to a different computational system
* 8 - Straightforward to reproduce with minimal effort

## ICERM Criteria

The following columns are all various ICERM criteria. In each case, an article can either be compliant with the criteria or non compliant. The following criteria are listed along with our evaluation criteria. When we did not receive code/data from the authors we did not evaluate these criteria. When we did not evaluate a given criteria the corresponding column is blank.

* 0 - Compliant: The article complies with the criteria
* 1 - Not Compliant: The article does not comply with the criteria.

**5 - A precise statement of assertions to be made in the paper**: The article or compendium materials received contain a precise statement of the assertions to be made in the paper (usually in the abstract or introduction)

**6 - Full statement (or valid summary) of experimental results**: The article or compendium materials received contain a full statement of experimental results (usually in the conclusion section)

**7 - Salient details of data reduction & statistical analysis methods**: Appropriate definitions of plot axes and table values are in the article.

**8 - Necessary run parameters were given**: For each test, table, and figure, necessary parameters are given in the article.

**9 - A statement of the computational approach, and why it constitutes a rigorous test of the hypothesized assertions**: We looked for this in the methodology section of the article.

**10 - Complete statements of, or references to, every algorithm used, and salient details of auxiliary software (both research and commercial software) used in the computation**: Here we especially looked for references to commercial software or libraries which were used for the article. If the authors let us know by email about a specific library they used which was not mentioned in the article, that article was marked as non-compliant.

**11 - Discussion of the adequacy of parameters such as precision level and grid resolution**: Here, we were looking for plots or tables showing computation error versus such parameters. If the article focus was not on computation error but on reduction of a specific phenomena, we looked for a discussion about parameters related to this phenomena.

**12 - Availability of computer code, input and output data, with some reasonable level of documentation**: Articles only satisfied this criteria if they made available all of their code and data with enough documentation to build and run their code.

**13 - Avenues of exploration examined throughout development, including information about negative findings**: We looked for this information in the article itself.

**14 - Instructions for repeating computational experiments described in the article**: Each computational experiment in the article should have detailed instructions describing how the experiment was conducted. Experiments on un-cited data sets for example cause an article to be non-compliant.

**15 - Precise functions were given, with settings**: This criteria was only satisfied if we were able to replicate part of the article with the code/data given to us.

**16 - Salient details of the test environment, including hardware, system software, and number of processors used**: We looked especially for mention of what hardware the authors used.

**17 - Data documented to clearly explain what each part represents**: The documentation included with the compendium materials we received should be enough to know the data format as well as to build and run the code.

**18 - Data archived with significant longevity expected**: The compendium materials we received from the authors were from a code sharing website or other site from which long term storage is expected. Compendium materials sent to us via email were not compliant.

**19 - Data location provided in the acknowledgements**: The authors provide a link to the compendium materials in the article somewhere.

**20 - Authors have documented use and licensing rights**: The authors needed to include either a license file or license statement somewhere in their compendium materials. Authors that did not include this were not compliant.

**21 - Software documented well enough to run it and what it ought to do**: The authors provide documentation either as a separate file or as comments inline with enough information to figure out what should happen. This does not mean that we were able to replicate their results however.

**22 - the code is publicly available with no download requirements**: The link we received from the authors either from the article or by email should be accessible to the public.

**23 - There was some method to track changes/to the software, as well as some certainty that the code is securely archived**: The code the authors gave us was already in a github repository or some other version control system.
