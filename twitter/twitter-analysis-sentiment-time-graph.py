import json
import os
import matplotlib.pyplot as plt

from commonfunctions import commonfunctions as cf

root_directory = os.path.dirname(os.path.abspath(os.curdir))

months = [None, "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]
print months

candidates = ['Trump', 'Hillary']
for candidate in candidates:
    if candidate == 'Hillary':
        import_filename = 'HillaryClintonTweetsResults.json'
        export_filename = 'images/twitter-analysis-sentiment-time-hillary.svg'
        username = 'HillaryClinton'
    else:
        import_filename = 'realDonaldTrumpTweetsResults.json'
        export_filename = 'images/twitter-analysis-sentiment-time-trump.svg'
        username = 'realDonaldTrump'

    export_filename = os.path.join(root_directory, export_filename)

    title = 'Positive and negative words in tweets - @' + username

    with open(import_filename, 'r') as f:
        statuses = json.load(f)

    results = {}
    for status in statuses:
        month = cf.iso_to_datetime(status['date']).month
        year = cf.iso_to_datetime(status['date']).year
        if year == 2016:
            if month not in results:
                results[month] = [status]
            else:
                results[month].append(status)

    positive_results = [(month_no, cf.mean([status['total_pos_words'] for status in results[month_no]]))
                        for month_no in results]
    negative_results = [(month_no, cf.mean([status['total_neg_words'] for status in results[month_no]]))
                        for month_no in results]
    tweet_volume = [(month_no, len(results[month_no])) for month_no in results]

    print positive_results
    print negative_results
    print tweet_volume

    if candidate == 'Hillary':
        # REMOVE THE FIRST AND LAST POINT...
        positive_results, negative_results, tweet_volume = positive_results[1:-1], \
                                                           negative_results[1:-1], tweet_volume[
                                                                                   1:-1]

    plt.style.use('ggplot')
    fig = plt.figure()
    ax = fig.gca()
    ax.grid(b=False)
    ax.set_axis_bgcolor('white')

    ax2 = ax.twinx()
    ax2.grid(b=False)
    ax2.set_axis_bgcolor('white')

    labels = ['Negative', 'Positive']
    colors = ['#d8b365', '#5ab4ac']
    for labelno, data in enumerate([negative_results, positive_results]):
        data2 = zip(*data)
        ax.plot(data2[0], data2[1], label=labels[labelno], color=colors[labelno], lw=2.5)

    ax.set_xlabel('month')
    ax.set_ylabel('Proportion of words in  dictionaries')
    ax.set_title(title, y=1.05)
    ax.legend(loc='center right')

    ax2.set_ylabel('Tweet Volume')

    data2 = zip(*tweet_volume)
    ax2.bar(data2[0], data2[1], color='black', alpha=0.1, align='center')

    # print [item.get_text() for item in ax2.get_xticklabels(which='both')]
    # labels = [int(item.get_text()) for item in ax2.get_xticklabels()]
    # labels2 = labels
    # for label in labels:
    #     if label in months:
    #         labels2[label] = months[label][0:3]
    #     else:
    #         labels2[label] = ""
    #
    # ax2.set_xticklabels(labels2)

    plt.savefig(export_filename, format='svg')
