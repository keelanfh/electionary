import plotly.plotly as py

uniqueYears = [1960, 1976, 1980, 1984, 1988, 1992, 1996, 1999, 2000, 2004, 2007, 2008, 2011, 2012, 2015, 2016]
uniquepositivewords = [0.07311850253286972, 0.07107776261937244, 0.06453900709219858, 0.08028646814926499, 0.08184215054424485, 0.06444202635715149, 0.07589090880603332, 0.08036815233384895, 0.0804464559220052, 0.07402100955034084, 0.0736503691514978, 0.0781099857708547, 0.06689946766731542, 0.07150444723195114, 0.06859471843068328, 0.07094215284968643]
uniquenegativewords = [0.032101790375299026, 0.04461118690313779, 0.032446808510638296, 0.04234200276416635, 0.03892087859418051, 0.038931205416515534, 0.039201918038025314, 0.040450770426025996, 0.041144890850883103, 0.043160677428308904, 0.04140433185493742, 0.03853443893783964, 0.03819117908841015, 0.037312152308504, 0.04515713476276044, 0.042973117366154355]

#
# This creates two graphs, but only one is shown with the data for both positive and negative words.
# I don't know why this happens...
# Red is positive and blue is negative

# plt.plot(uniqueYears, uniquepositivewords, 'ro')
# plt.xlabel('Year')
# plt.ylabel('Positive Words')
# plt.show()
# print py.plot_mpl(plt.gcf())

py.plot([{
    'x': uniqueYears,
    'y': uniquepositivewords},{'x':uniqueYears, 'y': uniquenegativewords}])

# plt.plot(uniqueYears, uniquenegativewords, 'bo')
# plt.xlabel('Year')
# plt.ylabel('Negative Words')
# plt.show()
# print py.plot_mpl(plt.gcf())