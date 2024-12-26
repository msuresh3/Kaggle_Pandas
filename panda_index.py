import pandas as pd

df = pd.DataFrame({'city': ['New York', 'London', 'Paris']})

# Create a dictionary to map cities to countries
city_to_country = {'New York': 'USA', 'London': 'UK', 'Paris': 'France'}

# Add a new column 'country' using map()
df['country'] = df['city'].map(city_to_country)

#print(df)

#import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3]})

# Square each element in column 'A'
df['A_squared'] = df['A'].apply(lambda x: x**2)

print(df)