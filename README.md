# the-electionary

## IMPORTANT - DISCLAIMER

This software is released under the MIT license. However, the transcripts collected by the program are subject to copyright and it is your sole responsibility to ensure that you use any data collected during your use of the software in accordance with the law.

## What this is

Software to download a series of debate transcripts from the [American Presidency Project](http://presidency.ucsb.edu/debates.php) and process them.

## How to use it

### Prerequisites for downloading the HTML files

You must have `scrapy` installed before using this code.

To install `scrapy`, run the following in Terminal:

`pip install scrapy`

(this applies only to macOS/OS X - look at the documentation for other platforms).

### Downloading the transcripts

Go to Terminal, and navigate to the `the-electionary/scrapy` directory in the terminal.

Then run `scrapy crawl urlfetch`. This fetches the list of URLs to download from.

Then run `scrapy crawl download`. This downloads all the HTML files containing the transcripts.

Be aware that this will take some time. The spider has been set to delay between downloading each file, to reduce server load for the host.
**There should not be any need to do this more than once.**

The HTML files will be stored in `html-files`. 
 
### Processing the transcripts

Now that you have all the HTML downloaded, you can now do any processing from the local files, which will be much faster and will prevent unnecessary load on the host.
As a starting point, try running `transcript-postprocessor.py`.
This will produce a transcript for each candidate's speech in an individual debate in JSON format, located in the `transcripts` folder.

If you want to access the text or other attributes from these JSON files, have a look at ``