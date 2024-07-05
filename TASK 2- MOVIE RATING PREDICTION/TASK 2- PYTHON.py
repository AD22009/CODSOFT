# -*- coding: utf-8 -*-
"""Abhi_Task-2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KEXZPbie8VsCyGsZtD81jpLQZ3pgdYFR

***TASK 2: MOVIE RATING PREDICTION USING PYTHON***
**Name: Abhishek Bara**i
**Batch: July**
***Domain: Data Science ***
"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_movie = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/IMDb Movies India.csv', sep=',', engine='python', encoding='latin-1')
df_movie.dropna(inplace=True)
df_movie.head()

df_movie.shape

df_movie.isna().sum()

df_movie.head()

df_movie.info()

df_movie.describe()

df_movie.isnull().sum()

df_movie.dropna(subset=["Rating"], inplace=True)

df_movie.dropna(subset=["Actor 1","Actor 2","Actor 3","Director","Genre"], inplace=True)

df_movie.isnull().sum()

df_movie.head()

df_movie['Votes'] = df_movie['Votes'].str.replace(',','').astype(int)

df_movie['Year'] = df_movie['Year'].str.strip('()').astype(int)

df_movie['Duration'] = df_movie['Duration'].str.strip('min')

df_movie['Duration'].fillna(df_movie['Duration'].median(), inplace=True)

df_movie.isnull().sum()

df_movie.info()

df_movie.head()

top_movie = df_movie.loc[df_movie['Rating'].sort_values(ascending=False)[:10].index]
top_movie

sns.histplot(data=top_movie, x="Year",hue="Rating",multiple="stack")
plt.title("Top 10 Movies", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Rating", fontsize=14)
plt.tight_layout()
plt.show()

genre_count = df_movie['Genre'].value_counts().reset_index()
genre_count.columns = ['Genre', 'Count']

top_n_genres = genre_count.head(5)
top_n_genres

plt.figure(figsize=(4, 4))
plt.pie(top_n_genres['Count'], labels=top_n_genres['Genre'], autopct='%1.1f%%',startangle=140,colors=sns.color_palette('pastel')[0:5])
plt.title('Movie genres distribution',fontsize=20)
plt.axis('equal')
plt.show

director_avg_rating = df_movie.groupby('Director')['Rating'].mean().reset_index()
director_avg_rating = df_movie.sort_values(by='Rating', ascending=False)

top_directors = director_avg_rating.head(10)
top_directors

plt.figure(figsize=(12, 6))
sns.barplot(x='Rating', y='Director',data=top_directors, palette='viridis')
plt.title('Top 10 Directors by Average Rating', fontsize=18)
plt.xlabel('Director', fontsize=14)
plt.ylabel('Average Rating', fontsize=14)
plt.show()

plt.figure(figsize=(12, 6))
sns.scatterplot(x='Rating', y='Votes', data=df_movie)
plt.title('Rating vs Votes', fontsize=18)
plt.xlabel('Rating', fontsize=14)
plt.ylabel('Votes', fontsize=14)
plt.show

actors_count = df_movie['Actor 1'].value_counts().reset_index()
actors_count.columns = ['Actor', 'MovieCount']

top_n_actors = actors_count.head(10)
top_n_actors

plt.figure(figsize=(12, 6))
sns.barplot(x='MovieCount', y='Actor', data=top_n_actors, orient='h')
plt.title('Top 10 Actors by Movie Count', fontsize=18)
plt.xlabel('Movie Count', fontsize=14)
plt.ylabel('Actor', fontsize=14)
plt.show()

yearly_movie_count = df_movie['Year'].value_counts().reset_index()
yearly_movie_count.columns = ['Year', 'MovieCount']
yearly_movie_count = yearly_movie_count.sort_values(by='Year')
yearly_movie_count

plt.figure(figsize=(12, 6))
sns.lineplot(data=yearly_movie_count, x='Year', y='MovieCount')
plt.title('Movie Count by Year', fontsize=18)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Movie Count', fontsize=14)
plt.show()

filtered_df = df_movie[(df_movie['Rating'] > 8) & (df_movie['Votes'] > 10000)]
filtered_df.head(10)

plt.figure(figsize=(12, 6))
ax=sns.barplot(data=filtered_df, x='Name', y='Votes',hue='Rating',dodge=False,width=0.5, palette='muted')

ax.set_xticklabels(ax.get_xticklabels(),rotation=90,ha='right')
ax.legend(loc='upper right')
ax.set_xlabel('Movie Name')
ax.set_ylabel('Votes')
ax.set_title('Movies with Rating > 8 and Votes > 10000')
plt.show()

df_movie['Duration']= df_movie['Duration'].astype(int)
df_movie['year']= df_movie['Year'].astype(int)

plt.figure(figsize=(12, 6))
sns.lineplot(data=df_movie, x='year', y='Duration',errorbar=None)
plt.title('Movie Duration by Year', fontsize=18)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Duration', fontsize=14)
plt.xticks(np.arange (1917,2023,5))
plt.show()

df_movie['Genre'] = df_movie['Genre'].str.split(',')

genre_df = df_movie.explode('Genre')
genre_df

plt.figure(figsize=(12, 6))
sns.countplot(data=genre_df, x='Genre', order=genre_df['Genre'].value_counts().index,palette='viridis')
plt.title('Movie Genre Distribution', fontsize=18)
plt.xlabel('Genre', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(rotation=90)
plt.show()

average_rating_by_genre = genre_df.groupby('Genre')['Rating'].mean().reset_index()
average_rating_by_genre = average_rating_by_genre.sort_values(by='Rating', ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(data=average_rating_by_genre, x='Genre', y='Rating', palette='coolwarm')
plt.title('Average Rating by Genre', fontsize=18)
plt.xlabel('Genre', fontsize=14)
plt.ylabel('Average Rating', fontsize=14)
plt.xticks(rotation=90)
plt.show()

from sklearn.preprocessing import LabelEncoder
labelenconder = LabelEncoder()

trans_data= df_movie.drop(['Name'],axis=1)
trans_data['Director'] = labelenconder.fit_transform(df_movie['Actor 1'])

trans_data['Actor 1'] = labelenconder.fit_transform(df_movie['Actor 1'])
trans_data['Actor 2'] = labelenconder.fit_transform(df_movie['Actor 2'])
trans_data['Actor 3'] = labelenconder.fit_transform(df_movie['Actor 3'])

trans_data['Genre'] = labelenconder.fit_transform(df_movie['Genre'].apply(lambda x: ','.join(x)))
trans_data.head()

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
sc_data = scaler.fit_transform(trans_data)
sc_df = pd.DataFrame(sc_data, columns=trans_data.columns)
sc_df.head()

corr_df = sc_df.corr()
sns.heatmap(corr_df, annot=False, cmap='coolwarm')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

x= trans_data.drop(['Rating'],axis=1)

y= trans_data['Rating']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model= LinearRegression()
model.fit(x_train, y_train)

x_test= np.array(x_test)

y_pred = model.predict(x_test)
y_pred

!pip install scikit-learn
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

print('R2 score:', r2_score(y_test, y_pred))
print('Mean Squared Error:', mean_squared_error(y_test, y_pred))
print('Mean absolute Error:', mean_absolute_error(y_test, y_pred))

print(y_test)

"""***TASK 2: COMPLETED***"""