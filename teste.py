import dash
import dash_table
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

tabela = {}
for x in range(262):
    tabela["Colunaaaaaa " + str(x)] = []
    for y in range(1200):
        if x == 6:
            tabela["Colunaaaaaa " + str(x)].append("Lin - {} Coluna maior {} ".format(y,x))
        else:
            tabela["Colunaaaaaa " + str(x)].append("Lin - {} Col {} ".format(y,x))
            
dic_filtrado = {k:v for (k,v) in tabela.items() if 'Colunaaaaaa 6' in k}
df2 = pd.DataFrame(dic_filtrado)
#print(tabela.items())
#for df in df2:
    #print(df)

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df2.columns],
    data=df2.to_dict('records'),
)

if __name__ == '__main__':
    app.run_server(debug=True)
