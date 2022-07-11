# Schedule

[Zoom link](https://arizona.zoom.us/my/picoral)

* Week 1: training: data wrangling with prison initiative data
* Week 2: training: data modeling with COMPAS data
* Week 3: training: data visualization with Google mobility data
* Week 4: choose data question: community ecology of ephemeral desert pools data set, or Tucson Audubon Data
* Week 5: Work on data wrangling
* Week 6: Work on data modeling
* Week 7: Work on data visualization
* Week 8: Finalize final report and present results

## Week 1

Training: data wrangling with prison initiative data

Monday: 9am to 11am

Topics:

* Introductions
* Git and GitHub
* Markdown (for learning diary)
* Python and R installation
* How to ask for help

Tuesday: 2pm to 4pm

Topics:

* Tidy data -- concept and discussion
* Reading data in Python and R
* Wrangling data -- filtering, mutating, pivoting

Tasks:

* Read in a different sheet from the excel file
* Play around with the data to report results (share on your GitHub repo) -- we encourage you to work with your fellow interns on this
* Fill out [pre-survey](https://uarizona.co1.qualtrics.com/jfe/form/SV_elhIacPHXWbKFds)
* Create learning diary entries

## Week 2

Reference materials (these will help contextualize the data modeling we will be doing this week):

* [Citations Needed Podcast, Episode 162: How the "Data-Driven" Label Sanitizes Cruel Austerity Politics](https://citationsneeded.libsyn.com/episode-162-how-the-data-driven-label-sanitizes-cruel-austerity-politics)
* [ProPublica's How We Analyzed the COMPAS Recidivism Algorithm](https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm)


Monday: 9am to 11am

Topics:

* Analysis Presentation
* Share repo links with Adriana
* Modeling -- what is it? 
* Demonstration in R

## Week 3

During this week you will be working with [mobility data from Google](https://www.google.com/covid19/mobility/) and [from Facebook](https://dataforgood.facebook.com/dfg/covid-19) to answer the following question:

> How has COVID-19 impacted people over the past 2.5 years?

## Week 4/5

For the rest of this program, we will be implementing a computer vision solution to a research problem. 

Resources:
* [calculating the size of objects in images](https://www.uniquesoftwaredev.com/calculating-the-size-of-objects-in-photos-with-computer-vision/)

Practice classification problems:
* [Classifying blood cell types](https://www.kaggle.com/datasets/paultimothymooney/blood-cells)
* [Classifying crops](https://www.kaggle.com/datasets/aman2000jaiswal/agriculture-crop-images)

You can find some of the data we will be working on at this [Rock pool water repo](https://github.com/cct-datascience/Rock-Pool-Data). A quick exploratory analysis of the data, not including the original images) will reveal that date and water levels correlate. In that sense, the classification could rely only on date. But we do want to use the images. Here are some questions for reflection:

* How would you approach the problem? What steps are needed to solve this?
* What are the advantages and disadvantages of each approach?

## Week 6 to 8

* Present solutions for Titanic classifier
* Two projects:
  * Water Pool Classifier: Elena and Alyssa
  * Tucson Bird Count: Roberto and Ernesto

### Water Pool Data

* [Repo with data and info](https://github.com/cct-datascience/Rock-Pool-Data)
* [Arizona box folder with images](https://arizona.box.com/s/ufrmwkoqw68x9k8egk4rdnb82qde96qn)

### Tucson Bird Count Data

* [Repo with data and info](https://github.com/ezylstra/TBC_UACollab)
* Final product: interactive dashboard

* Use the files in the MergedData folder 
* TBC_counts.csv will be the primary source of data for this project.
* When volunteers conduct these surveys, they count the number of birds of each species observed (values in the count column). However, because these surveys aren't replicated within a given season and aren't conducted in a way that allows us to account for the fact that some birds will be missed by observers, be somewhat reluctant to use those counts to estimate absolute abundance (or the number of birds present).  Instead, it's a little more practical to think about presence or distribution of a particular bird species or even relative abundance.  
* Where are the birds detected? On what proportion of surveys (across locations in a given year or over years at one location) do observers detect a particular bird species? Has the distribution of a bird species changed through time?  Is the distribution of a species associated with notable environmental features (like riparian/stream channels, proximity to mountain foothills, etc).


* We had a severe drought in Tucson in 2020, and many think this has negatively affected some of the bird populations (e.g., Cactus wren, Black-tailed gnatcatchers, Northern cardinals, Pyrrhuloxia, others?).  It might be interesting to see how the distribution or relative abundance of birds might have changed between 2019 (pre-drought), 2020 (drought year), and 2021 (post drought).
* The distributions of some species in the Tucson Valley have clearly changed over the last 20 years.  Some species, like Cooper’s hawks and Anna’s hummingbird, seem to be more common.  Other species have become much less common (e.g., Inca dove, whose decline may be related to an increase in the number of Cooper’s hawks, since they’re a primary predator of Inca doves).  Are there some special patterns to these distributional changes?  
* What do the distributions of non-native species look like, and have they changed over time?  One species that might be particularly interesting is the Eurasian Collared-Dove, which has become more common in many western cities.
* Finally, Tucson Audubon would be particularly interested in several species that are linked to some of our bigger programs.  We have a large nestbox program for Lucy's warblers (distributing hundreds of nestboxes to households in the Tucson area), so it would be interesting to see whether Lucy's detections have increased in the last few years.  Tucson Audubon is also focused on conserving saguaros for birds and other wildlife, so any information about species that nest in saguaros (e.g., Gila woodpecker, Gilded flicker, Brown-crested flycatcher) would be of great interest.




