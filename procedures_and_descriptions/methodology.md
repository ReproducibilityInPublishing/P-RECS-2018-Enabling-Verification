# Methodology

We conducted an experiment on the computational physics community to measure 1) how frequently authors shared their code and data directly in their article; 2) Whether authors who didn't would respond to a request for code and data; 3) How far a user skilled in computation, but not an expert in the field could get with the materials received.

Here we discuss the methodology for these three sections.

## Classification of Articles

Three members of our group read each of the 306 articles to determine the presence of information relating to the code they wrote or data they used. We used 6 classifications:

* None - The article contains no information about the code or data used in their work.
* Some - The article contains some type of information about the code or data used in their work, but no actual code. ex: Language used, Computational environment or computer specs used, libraries used, etc..., Pseudocode does not count here.
* Available Upon Request - The authors indicate that they will give their code or data upon email request.
* Link to code given, but broken - The article includes a link to their code or data, but this link is broken.
* Link to Partial code Given - The article includes a link to their code or data, but we believe that more is needed to replicate their work.
* Link Given - The article includes a link to their code or data and we believe that it is everything necessary to replicate their work.

## Email Requests for Code and Data

All articles which did not fall in the 'Link Given' category were emailed a personalized request for code and data. An IRB (#17329) approved email protocol was designed to limit interaction with the authors, and determine what kind of information a student is able to get with simple emails. One email request was sent, and another reminder two weeks later if no reply had yet been received. Each article was read and a request appropriate for the article was written to maximize the likelihood that said code and data are given on the first email.

Replies (or lack thereof) to these emails were classified into 13 categories.

* No Response - No response was received from either email sent out
* Email Bounced - The email listed for the corresponding author was incorrect and the email bounced.
* Auto-response - We received an auto-reply to which the author never followed up with us.
* Impossible to share - The code and data are impossible for the author to share for reasons out of their control. Ex. restrictive licensing, national policy, or events like having lost the code and data
* Refusal to share - The authors refuse to share their code and data, but do not have particularly good reasons for doing so. Ex. Simple refusal, Their code is too messy. Their code is too large or complex. Their work requires large computational power.
* Asks for reason - The authors ask why we want their code and data.
* Asks screening questions - The authors ask screening questions about our group and work.
* Contact another person - The authors ask us to contact another person
* Unfulfilled promise to follow up - The authors promise to follow up with us, but never do.
* Didn't get anything new - The authors sent something by email, but this was already included in a link from the article or in the supplementary materials.
* Directed to supplementary materials - The authors directed us to their supplemental materials (In this case we were asking for more materials)
* Will share after setup - The authors indicate that they will share more necessary information, but they want us to complete some setup on our side first.
* Shared at least some data and code - The authors shared at least some kind of data or code through some means initiated by the email.

## Attempt at Article Replication

For Articles for which we received some code or data, we attempted to replicate all of the results in their article with the provided materials. We alloted ourselves 4 hours for this process, and produced an objective metric of how far we got, and a subjective metric of how far we think a knowledgeable scientist in the field would be able to get with the materials we received and no further communication with the authors. If we reached the end of the 4 hours without successfully replicated all aspects of the article and didn't encounter a definite roadblock preventing us from completing the replication given more time, we made a subjective determination of which category the article belongs in.

We are cognizant of situations where large computational power is necessary to perform the compuational experiment in the article. However in these situations, we will label the article as impossible to reproduce if no necessary source code to complete the experiment is given, regardless of whether or not we have the ability to run it within 4 hours.

We also assessed each of these articles compliance with the 2012 ICERM software and data sharing guidelines.

### Replication Amount

This is the objective replication measurement and contains how far we were able to get with the article materials. There are 5 categories:

* Nothing - We were unable to build code for any part of the article
* Build - We were able to build code which was given to us, but running the built code resulted in crashes or runtime errors.
* Run - We were able to build and run code which was given to us, but we were unable to replicate the computational experiment as shown in the article.
* Partial Replication - We were able to build and run code which was given to us, and were able to reproduce at least one number within the article.
* Replicated - We were able to build and run code which was given to us, and were able to reproduce all aspects of the article.

### Reproducibility Effort

This is the subjective replication measurement and represents how far we think an experienced scientist in the domain would get given the materials we received, more time, and no further contact with the authors. There are 9 categories:

* Impossible to reproduce - We are missing essential code, data, or methodology to complete the replication
* Nearly impossible to reproduce - An unavoidable reason is preventing our replication such as a specialized hardware requirement, intense compuational requirements, sensitive data, human study, etc..
* Difficult to reproduce because of unavoidable inherent complexity - While we have the computational capacity to perform the calculations, it would take longer than 4 hours to perform.
* Reproducible with substantial tedious effort - Some tedious work is required to reproduce the article such as downloading a large number of datasets or changing the format of the data
* Reproducible with substantial intellectual effort - The methods of the article are well defined, but it will require understanding of jargon, the field, and a literature search to find all necessary methodology.
* Could reproduce with fairly substantial skill and knowledge - Reproducibility possible, but some substantial programming skill is necessary to complete some missing implementations or missing scripts
* Reproducible after tweaking - Reproducible after fiddling with some defined parameters, fixing some small bugs, or adding some small method step.
* Minor difficulty in reproducing - Reproducible, but a specialized library or computational platform is necessary.
* Straightforward to reproduce with minimal effort - No substantial effort is required to replicate all aspects of the article.

### ICERM criteria

For these articles, we also evaluated compliance with the 2012 ICERM guidelines for software publication. See the [`column_descriptions.md`](column_descriptions.md) document for more information about how these were evaluated.
