
# #Q1
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# import plotly.express as px
# from dash import Dash, html, dcc

# df = pd.read_csv("trafic-annuel-entrant-par-station-du-reseau-ferre-2021.csv")
# df2 = pd.read_csv("emplacement-des-gares-idf.csv")


# df2[['lat', 'lng']] = df2['Geo Point'].str.split(',', expand=True)
# df2['lat'] = df2['lat'].str.strip().astype(float)
# df2['lng'] = df2['lng'].str.strip().astype(float)



# # Sort the dataframe in descending order based on traffic and take the top 10 rows
# top10 = df.sort_values(by='Trafic', ascending=False).head(10)
# grouped = df.groupby('Ville')['Trafic'].sum().sort_values(ascending=False).head(5).reset_index()
# grouped.rename(columns={'Trafic': 'Trafic per city'}, inplace=True)

# grouped2 = df2.groupby('exploitant')['nom_long'].count().sort_values(ascending=False).head(5).reset_index()
# grouped.rename(columns={'nom_long': 'Number of stations'}, inplace=True)

# grouped3 = df2.groupby('ligne')['nom_long'].count().sort_values(ascending=False).reset_index()
# grouped.rename(columns={'nom_long': 'Number of stations per line'}, inplace=True)



# fig_map = px.scatter_mapbox(df2, lat="lat", lon="lng", hover_name="nom_long",
#                             hover_data=["Geo Point", "exploitant"],
#                             color_discrete_sequence=["fuchsia"], zoom=8,
#                             height=600)
# fig_map.update_layout(mapbox_style="open-street-map")
# fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})








# print(grouped)
# # Create the bar chart
# fig = px.bar(top10, x='Station', y='Trafic', 
#              title='Top 10 Stations with the Biggest Trafic')

# # Create the pie chart
# fig2 = px.pie(grouped, values='Trafic per city', names='Ville', 
#               title='Répartition du trafic par ville')

# fig3 = px.bar(grouped2, x='exploitant', y='nom_long', 
#              title='number of stations per exploitant')

# fig4 = px.bar(grouped3, x='ligne', y='nom_long', 
#              title='number of stations per line')


# app = Dash(__name__)

# app.layout = html.Div(children=[
#     html.H1("My first dash application", style={'color': '#ADD8E6'}),
#     html.H2("It's a title2", style={'color': '#00008B'}),
    
#     # dcc.Graph(id='bar-chart', figure=fig),
#     # dcc.Graph(id='bar-chart2', figure=fig2),
#     html.Div(className='row', style={'display': 'flex'}, children=[
#         html.Div(className='col-md-6', children=[
#             dcc.Graph(id='bar-chart', figure=fig)
#         ]),
#         html.Div(className='col-md-6', children=[
#             dcc.Graph(id='pie-chart', figure=fig2)
#         ])
#     ]),
    
#     html.Div(className='row', children=[
#         html.Div(className='col-md-12', children=[
#             dcc.Graph(id='bar-chart3', figure=fig3)
#         ])
#     ]),

#     html.Div(className='row', children=[
#         html.Div(className='col-md-12', children=[
#             dcc.Graph(id='bar-chart4', figure=fig4)
#         ])
#     ]),
#     html.Div(className='row', style={'display': 'flex'}, children=[
#         html.Div(className='col-md-12', children=[
#             dcc.Graph(id='map', figure=fig_map)
#         ],style={'width': '100%'})
#     ])
# ])





# if __name__ == '__main__':
#     app.run_server(debug=True)

# app.css.append_css({
#     'external_url': 'style.css'

# })









