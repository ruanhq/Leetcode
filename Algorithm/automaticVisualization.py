#More Visualization Python:

#Automatic EDA procedures:

tips = sns.load_dataset("tips")

"""
total_bill	tip	sex	smoker	day	time	size
0	16.99	1.01	Female	No	Sun	Dinner	2
1	10.34	1.66	Male	No	Sun	Dinner	3
2	21.01	3.50	Male	No	Sun	Dinner	3
3	23.68	3.31	Male	No	Sun	Dinner	2
4	24.59	3.61	Female	No	Sun	Dinner	4
"""
#relationship between continuous y and continuous features
#hue means another feature splitting the color.
sns.relplot(data = tips, x = "total_bill",
	y = "tip", hue = "day")
#col means splitting the different plots.
sns.relplot(data = tips, x = "total_bill",
	y = "tip", hue = "day", col = "time")
#row separate the different rows with different level of features
sns.relplot(data = tips, x = "total_bill",
	y = "tip", hue = "day", row = "sex",
	col = "time")
#style means the point style splitted by different levels of features
sns.relplot(data = tips, x = "total_bill",
	y = "tip", size = "size", style = "sex")
#
fmri = sns.load_dataset("fmri")
fmri.head()
"""
	subject	timepoint	event	region	signal
0	s13	18	stim	parietal	-0.017552
1	s5	14	stim	parietal	-0.080883
2	s12	18	stim	parietal	-0.081033
3	s11	18	stim	parietal	-0.046134
4	s10	18	stim	parietal	-0.037970
hue, style and col.
hue represents different colors.
"""
sns.relplot(data = fmri,
x = "timepoint", y = "signal", col = "region",
hue = "event", style = "event", kind = "point", size = "timepoint")
#Perfect one to draw the scatter points:

########
g = sns.relplot(
data = fmri,
x = "timepoint", y = "signal",
hue = "event", style = "event",
col = "region",
height = 4, aspect = 0.75, kind = "line"
)

sns.relplot(x = stocks.index, y = 'close',
data = stocks, kind = 'line', hue = 'symbol')

#Catplot:
df = pd.read_csv("diamonds.csv")
df.head()
"""
	Unnamed: 0	carat	cut	color	clarity	depth	table	price	x	y	z
0	1	0.23	Ideal	E	SI2	61.5	55.0	326	3.95	3.98	2.43
1	2	0.21	Premium	E	SI1	59.8	61.0	326	3.89	3.84	2.31
2	3	0.23	Good	E	VS1	56.9	65.0	327	4.05	4.07	2.31
3	4	0.29	Premium	I	VS2	62.4	58.0	334	4.20	4.23	2.63
4	5	0.31	Good	J	SI2	63.3	58.0	335	4.34	4.35	2.75

"""
sns.catplot(x = 'cut', data = df, kind = 'count')

categoryOrder = ["Fair", "Good", "Very Good", "Premium", "Ideal"]
sns.catplot(x = 'cut', data = df, kind = 'count',
order = categoryOrder)
sns.catplot(x = 'cut', y = 'price', data = df, kind = 'bar',
order = categoryOrder)
sns.catplot(x = 'cut', y = 'price', data = df, kind = 'box',
order = categoryOrder)
#whiskers between 5 th quantile and 95 the quantile:
sns.catplot(x = 'cut', 
y = 'price',
data = df,
kind = 'box',
order = categoryOrder,
whis = [4, 96])#whiskers from 4th quantile to 96th quantile.

sns.catplot(x = 'cut', 
y = 'price',
data = df,
kind = 'box',
order = categoryOrder)

words = ["AAA", "BBB", "CCC"]
dict(zip(words, range(3)))

defaultdict(list)
Counter()









