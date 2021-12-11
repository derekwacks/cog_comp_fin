## Emotion Classification
### XCAL learning on masked and un-masked faces


CLPS 1492 Computational Cognitive Neuroscience

Department of Cognitive, Linguistic, and Psychological Sciences

Brown University


#### Overview
With a network modeled as a Simple Recurrent Network, I explored questions relating to the affect of masks on emotion perception. Specifically, I explored if masks affect a child’s ability to learn how to perceive emotion. This was based on experiments run by psychologists over the past 18 months on the ability of children to properly classify emotions portrayed in image stimuli. I found the network was able to achieve perfect classification accuracy on the test sets, while obtaining a multitude of results in testing scenarios. The network performed highest when trained and tested on opposite image types with the possibility of activation memorization. Experiments five and six showcased the network's ability (or lack there of) to generalize to completely unseen patterns. The network performed better after being trained on unmasked images then it did being trained on masked images. 



#### Main files:

- SRN_Code/srn.go: builds the network, and runs the simulation

- main.py: orchestrates the whole show (undertaking image pre-processing, etc.)

- face_maker.py: provides helper functions to create dataframes and CSV files to read into the emergent network's input layer

- results_analysis.py: performs analysis on different result CSV's from the go code and writes analysis to a CSV



Thank you to Professor Frank, Alana Jaskir & Jason Leng for their support

And to all contributors to the [Emergent project](https://github.com/emer/emergent), which this project heavily relied upon.
