# the-electionary

## IMPORTANT - DISCLAIMER

This software is released under the MIT license. However, the transcripts collected by the program are subject to copyright and it is your sole responsibility to ensure that you use any data collected during your use of the software in accordance with the law.

## What this is

Software to download a series of US Presidential election debate transcripts from the [American Presidency Project](http://presidency.ucsb.edu/debates.php), process and analyse them. It was used for a project, [The Electionary](https://theelectionary.wordpress.com).

## How to use it

### Dependencies

The project depends on the following external libraries:

`scrapy`, `matplotlib`, `numpy` , `nltk`, which can all be installed through `pip`.

Please note, in testing, we could not get the data collection code to work in Canopy as the `scrapy` dependence was not working. We'd recommend <a href="https://www.continuum.io/downloads">Anaconda</a> (which we used) or plain <a href="https://www.python.org/downloads/">Python</a>.

Optionally, `pypy` can be used to run some of the code faster. `nltk` is a requirement within `pypy` for this code - none of the other external libraries are required in `pypy` and indeed they are not compatible with `pypy`.

### Downloading the transcripts

Navigate to the `electionary/scrapy` directory in Terminal.

Then run `scrapy crawl urlfetch`. This fetches the list of URLs to download from.

Then run `scrapy crawl download`. This downloads all the HTML files containing the transcripts.

Be aware that this will take some time. The spider has been set to delay between downloading each file, to reduce server load for the host.
**There should not be any need to do this more than once.**

The HTML files will be stored in `html-files`. 
 
### Processing the transcripts

Now that you have all the HTML downloaded, you can now do any processing from the local files, which will be much faster and will prevent unnecessary load on the host.
As a starting point, try running `processing/transcript-postprocessor.py`.
This will produce a transcript for each candidate's speech in an individual debate in JSON format, located in the `transcripts` folder.

### Analysis

If you want to access the text or other attributes from these JSON files, have a look at `json-import-example.py`.

All of the analysis that we carried out was done using the code in the `analysis` folder, and our visualisations are in the `images` folder. The `twitter` folder contains everything that we did with Twitter data, including data collection and analysis. 

### A note on interpreters

You shouldn't have any issues running the code in `processing` through the standard CPython interpreter, but the scripts in the `analysis` section can be very slow to run in CPython. It is highly recommended to install [pypy](http://pypy.org) to run the code faster - around 3x faster in simple tests of analysis code, which makes a lot of difference! You will need to install the `nltk` library in `pypy`.

`pypy` is not compatible with `matplotlib`, so graphs cannot be created when using the `pypy` interpreter - you will need to switch back to CPython to produce graphs. The files to produce graphs all end in `-graph.py` so it is easy to switch interpreters and run them separately.