import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash
from .app import app
from dash.dependencies import Input, Output
from . import filtros
from .dados import contratoB

flts = filtros.reuni_filtros(contratoB)

modal = [
    dbc.ModalHeader("Filtros Aplicados na Página"),
    dbc.ModalBody([
        html.Div([
            html.H5('TIPO DE CONTRATO'),
            html.Div([
                    html.Button(id="btn-tipo-contrato", className="dropbtn"),
                    dbc.FormGroup(
                        [
                            dbc.Checklist(
                                options=[
                                    {"label": "Todos", "value": 'TD'},
                                ],
                                value=['TD'],
                                id="checklist-tipo-contrato-todos",
                            ),
                            filtros.cria_checklist(flts['TIPO DE CONTRATO'],"checklist-tipo-contrato-valores"),
                        ], id="check-list-tipo-contrato", className="dropdown-content2"
                    ),
                ],className="dropdown2")
        ], className="modal-item"),
        
        html.Div([
            html.H5('SUBMERCADO'),
            html.Div([
                    html.Button('Todos', id="btn-submercado", className="dropbtn"),
                    dbc.FormGroup(
                        [
                            dbc.Checklist(
                                options=[
                                    {"label": "Todos", "value": 'TD'},
                                ],
                                value=['TD'],
                                id="checklist-submercado-todos",
                            ),
                            filtros.cria_checklist(flts['SUBMERCADO'],"checklist-submercado-valores"),
                        ], id="check-list-submercado", className="dropdown-content2"
                    ),
                ],className="dropdown2")
        ], className="modal-item"),
        
        html.Div([
            html.H5('LEILÃO'),
            html.Div([
                    html.Button('Todos', id="btn-leilao", className="dropbtn"),
                    dbc.FormGroup(
                        [
                            dbc.Checklist(
                                options=[
                                    {"label": "Todos", "value": 'TD'},
                                ],
                                value=['TD'],
                                id="checklist-leilao-todos",
                            ),
                            filtros.cria_checklist(flts['TIPO DE LEILÃO'],"checklist-leilao-valores"),
                        ], id="check-list-leilao", className="dropdown-content2"
                    ),
                ],className="dropdown2")
        ], className="modal-item"),
        
        html.Div([
            html.H5('STATUS'),
            html.Div([
                    html.Button('Todos', id="btn-status", className="dropbtn"),
                    dbc.FormGroup(
                        [
                            dbc.Checklist(
                                options=[
                                    {"label": "Todos", "value": 'TD'},
                                ],
                                value=['TD'],
                                id="checklist-status-todos",
                            ),
                            filtros.cria_checklist(flts['STATUS'],"checklist-status-valores"),
                        ], id="check-list-status", className="dropdown-content2"
                    ),
                ],className="dropdown2")
        ], className="modal-item"),
        
        html.Div([
            html.H5('PRODUTO'),
            html.Div([
                    html.Button('Todos', id="btn-produto", className="dropbtn"),
                    dbc.FormGroup(
                        [
                            dbc.Checklist(
                                options=[
                                    {"label": "Todos", "value": 'TD'},
                                ],
                                value=['TD'],
                                id="checklist-produto-todos",
                            ),
                            filtros.cria_checklist(flts['PRODUTO'],"checklist-produto-valores"),
                        ], id="check-list-produto", className="dropdown-content2"
                    ),
                ],className="dropdown2")
        ], className="modal-item"),
        
        html.Div([
            html.H5('VENDEDOR'),
            html.Div([
                    html.Button('Todos', id="btn-vendedor", className="dropbtn"),
                    dbc.FormGroup(
                        [
                            dbc.Checklist(
                                options=[
                                    {"label": "Todos", "value": 'TD'},
                                ],
                                value=['TD'],
                                id="checklist-vendedor-todos",
                            ),
                            filtros.cria_checklist(flts['VENDEDOR'],"checklist-vendedor-valores"),
                        ], id="check-list-vendedor", className="dropdown-content2"
                    ),
                ],className="dropdown2")
        ], className="modal-item"),
        
        html.Div([
            html.H5('INÍCIO DE SUPRIMENTO'),
            html.Div([
                    html.Button('Todos', id="btn-inicio-suprimento", className="dropbtn"),
                    dbc.FormGroup(
                        [
                            dbc.Checklist(
                                options=[
                                    {"label": "Todos", "value": 'TD'},
                                ],
                                value=['TD'],
                                id="checklist-inicio-suprimento-todos",
                            ),
                            filtros.cria_checklist(flts['INÍCIO DE SUPRIMENTO'],"checklist-inicio-suprimento-valores"),
                        ], id="check-list-inicio-suprimento", className="dropdown-content2"
                    ),
                ],className="dropdown2")
        ], className="modal-item"),
        
        html.Div([
            html.H5('FIM DE SUPRIMENTO'),
            html.Div([
                    html.Button('Todos', id="btn-fim-suprimento", className="dropbtn"),
                    dbc.FormGroup(
                        [
                            dbc.Checklist(
                                options=[
                                    {"label": "Todos", "value": 'TD'},
                                ],
                                value=['TD'],
                                id="checklist-fim-suprimento-todos",
                            ),
                            filtros.cria_checklist(flts['FIM DE SUPRIMENTO'],"checklist-fim-suprimento-valores"),
                        ], id="check-list-fim-suprimento", className="dropdown-content2"
                    ),
                ],className="dropdown2")
        ], className="modal-item"),
    ]),
    dbc.ModalFooter([
        dbc.Button("Limpar Alterações", id="limpar-alteracoes", color="primary", className="mr-auto", style={'display': 'inline-block', 'marginLeft':'20px'}),
        dbc.Button("Fechar", id="close", color="danger", className="ml-auto", style={'display': 'inline-block', 'marginRight':'20px'}),
        ]
    )
]


@app.callback(Output('check-list-tipo-contrato', 'style'), [Input('btn-tipo-contrato', 'n_clicks')])
def troca_tipo_contrato(n_clicks):
    if n_clicks == None:
        return {'display': 'none'}
    else:
        if n_clicks % 2 == 0:
            return {'display': 'none'}
        else: 
            return {'display': 'block'}
    
@app.callback(
    Output('checklist-tipo-contrato-todos', 'value'),
    Output('checklist-tipo-contrato-valores', 'value'),
    Output('btn-tipo-contrato', 'children'),
    Input('checklist-tipo-contrato-todos', 'value'),
    Input('checklist-tipo-contrato-valores', 'value'),
    Input('limpar-alteracoes', 'n_clicks'),
    Input('borracha', 'n_clicks')
)
def rotina_todos_tipo_contrato(value_todos,value,n_click,n_borracha):
    ctx =  dash.callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    valores = value
    boolean = True
    seta = html.Span('',className="seta ml-auto", id="seta")
    if input_id == 'limpar-alteracoes' or input_id == 'borracha':
        return ['TD'],flts['TIPO DE CONTRATO'],['Todos',seta]
    else:
        for i in flts['TIPO DE CONTRATO']:
            if boolean:
                boolean = i in value
       
        if boolean:
            if input_id != 'checklist-tipo-contrato-todos':
                valores = value
                todos = ['TD']
            else:
                if 'TD' in value_todos:
                    valores = []
                    todos = []
                else:
                    todos = value_todos
        else:
            if input_id == 'checklist-tipo-contrato-todos':
                valores = flts['TIPO DE CONTRATO']
                todos = ['TD']
            else:
                todos = []
        
        if 'TD' in todos:
            return todos,valores,['Todos',seta]
        elif len(value) > 1:
            return todos,valores,['Seleções Múltiplas',seta]
        elif len(value) == 1:
            return todos,valores,[value[0],seta]
        else:
            return todos,valores,['Todos',seta]
            
@app.callback(Output('check-list-submercado', 'style'), [Input('btn-submercado', 'n_clicks')])
def troca_submercado(n_clicks):
    if n_clicks == None:
        return {'display': 'none'}
    else:
        if n_clicks % 2 == 0:
            return {'display': 'none'}
        else: 
            return {'display': 'block'}
    
@app.callback(
    Output('checklist-submercado-todos', 'value'),
    Output('checklist-submercado-valores', 'value'),
    Output('btn-submercado', 'children'),
    Input('checklist-submercado-todos', 'value'),
    Input('checklist-submercado-valores', 'value'),
    Input('limpar-alteracoes', 'n_clicks'),
    Input('borracha', 'n_clicks')
)
def rotina_todos_submercado(value_todos,value,n_click,n_borracha):
    ctx =  dash.callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    valores = value
    boolean = True
    seta = html.Span('',className="seta ml-auto", id="seta")
    if input_id == 'limpar-alteracoes' or input_id == 'borracha':
        return ['TD'],flts['SUBMERCADO'],['Todos',seta]
    else:
        for i in flts['SUBMERCADO']:
            if boolean:
                boolean = i in value
                
        if boolean:
            if input_id != 'checklist-submercado-todos':
                valores = value
                todos = ['TD']
            else:
                if 'TD' in value_todos:
                    valores = []
                    todos = []
                else:
                    todos = value_todos
            return todos,valores,['Todos',seta]
        else:
            if input_id == 'checklist-submercado-todos':
                valores = flts['SUBMERCADO']
                todos = ['TD']
            else:
                todos = []
                
        if 'TD' in todos:
            return todos,valores,['Todos',seta]
        elif len(value) > 1:
            return todos,valores,['Seleções Múltiplas',seta]
        elif len(value) == 1:
            return todos,valores,[value[0],seta]
        else:
            return todos,valores,['Todos',seta] 

        
@app.callback(Output('check-list-leilao', 'style'), [Input('btn-leilao', 'n_clicks')])
def troca_leilao(n_clicks):
    if n_clicks == None:
        return {'display': 'none'}
    else:
        if n_clicks % 2 == 0:
            return {'display': 'none'}
        else: 
            return {'display': 'block'}
    
@app.callback(
    Output('checklist-leilao-todos', 'value'),
    Output('checklist-leilao-valores', 'value'),
    Output('btn-leilao', 'children'),
    Input('checklist-leilao-todos', 'value'),
    Input('checklist-leilao-valores', 'value'),
    Input('limpar-alteracoes', 'n_clicks'),
    Input('borracha', 'n_clicks')
)
def rotina_todos_leilao(value_todos,value,n_click,n_borracha):
    ctx =  dash.callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    valores = value
    boolean = True
    seta = html.Span('',className="seta ml-auto", id="seta")
    if input_id == 'limpar-alteracoes' or input_id == 'borracha':
        return ['TD'],flts['TIPO DE LEILÃO'],['Todos',seta]
    else:
        for i in flts['TIPO DE LEILÃO']:
            if boolean:
                boolean = i in value
                
        if boolean:
            if input_id != 'checklist-leilao-todos':
                valores = value
                todos = ['TD']
            else:
                if 'TD' in value_todos:
                    valores = []
                    todos = []
                else:
                    todos = value_todos
            return todos,valores,['Todos',seta]
        else:
            if input_id == 'checklist-leilao-todos':
                valores = flts['TIPO DE LEILÃO']
                todos = ['TD']
            else:
                todos = []
                    
        if 'TD' in todos:
            return todos,valores,['Todos',seta]
        elif len(value) > 1:
            return todos,valores,['Seleções Múltiplas',seta]
        elif len(value) == 1:
            return todos,valores,[value[0],seta]
        else:
            return todos,valores,['Todos',seta]


@app.callback(Output('check-list-status', 'style'), [Input('btn-status', 'n_clicks')])
def troca_status(n_clicks):
    if n_clicks == None:
        return {'display': 'none'}
    else:
        if n_clicks % 2 == 0:
            return {'display': 'none'}
        else: 
            return {'display': 'block'}
    
@app.callback(
    Output('checklist-status-todos', 'value'),
    Output('checklist-status-valores', 'value'),
    Output('btn-status', 'children'),
    Input('checklist-status-todos', 'value'),
    Input('checklist-status-valores', 'value'),
    Input('limpar-alteracoes', 'n_clicks'),
    Input('borracha', 'n_clicks')
)
def rotina_todos_status(value_todos,value,n_click,n_borracha):
    ctx =  dash.callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    valores = value
    boolean = True
    seta = html.Span('',className="seta ml-auto", id="seta")
    if input_id == 'limpar-alteracoes' or input_id == 'borracha':
        return ['TD'],flts['STATUS'],['Todos',seta]
    else:
        for i in flts['STATUS']:
            if boolean:
                boolean = i in value
                
        if boolean:
            if input_id != 'checklist-status-todos':
                valores = value
                todos = ['TD']
            else:
                if 'TD' in value_todos:
                    valores = []
                    todos = []
                else:
                    todos = value_todos
            return todos,valores,['Todos',seta]
        else:
            if input_id == 'checklist-status-todos':
                valores = flts['STATUS']
                todos = ['TD']
            else:
                todos = []
            
        if 'TD' in todos:
            return todos,valores,['Todos',seta]
        elif len(value) > 1:
            return todos,valores,['Seleções Múltiplas',seta]
        elif len(value) == 1:
            return todos,valores,[value[0],seta]
        else:
            return todos,valores,['Todos',seta]

@app.callback(Output('check-list-produto', 'style'), [Input('btn-produto', 'n_clicks')])
def troca_produto(n_clicks):
    if n_clicks == None:
        return {'display': 'none'}
    else:
        if n_clicks % 2 == 0:
            return {'display': 'none'}
        else: 
            return {'display': 'block'}
    
@app.callback(
    Output('checklist-produto-todos', 'value'),
    Output('checklist-produto-valores', 'value'),
    Output('btn-produto', 'children'),
    Input('checklist-produto-todos', 'value'),
    Input('checklist-produto-valores', 'value'),
    Input('limpar-alteracoes', 'n_clicks'),
    Input('borracha', 'n_clicks')
)
def rotina_todos_produto(value_todos,value,n_click,n_borracha):
    ctx =  dash.callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    valores = value
    boolean = True
    seta = html.Span('',className="seta ml-auto", id="seta")
    if input_id == 'limpar-alteracoes' or input_id == 'borracha':
        return ['TD'],flts['PRODUTO'],['Todos',seta]
    else:
        for i in flts['PRODUTO']:
            if boolean:
                boolean = i in value
                
        if boolean:
            if input_id != 'checklist-produto-todos':
                valores = value
                todos = ['TD']
            else:
                if 'TD' in value_todos:
                    valores = []
                    todos = []
                else:
                    todos = value_todos
            return todos,valores,['Todos',seta]
        else:
            if input_id == 'checklist-produto-todos':
                valores = flts['PRODUTO']
                todos = ['TD']
            else:
                todos = ['TD']
            
        if 'TD' in todos:
            return todos,valores,['Todos',seta]
        elif len(value) > 1:
            return todos,valores,['Seleções Múltiplas',seta]
        elif len(value) == 1:
            return todos,valores,[value[0],seta]
        else:
            return todos,valores,['Todos',seta]


@app.callback(Output('check-list-vendedor', 'style'), [Input('btn-vendedor', 'n_clicks')])
def troca_vendedor(n_clicks):
    if n_clicks == None:
        return {'display': 'none'}
    else:
        if n_clicks % 2 == 0:
            return {'display': 'none'}
        else: 
            return {'display': 'block'}
    
@app.callback(
    Output('checklist-vendedor-todos', 'value'),
    Output('checklist-vendedor-valores', 'value'),
    Output('btn-vendedor', 'children'),
    Input('checklist-vendedor-todos', 'value'),
    Input('checklist-vendedor-valores', 'value'),
    Input('limpar-alteracoes', 'n_clicks'),
    Input('borracha', 'n_clicks')
)
def rotina_todos_vendedor(value_todos,value,n_click,n_borracha):
    ctx =  dash.callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    valores = value
    boolean = True
    seta = html.Span('',className="seta ml-auto", id="seta")
    if input_id == 'limpar-alteracoes' or input_id == 'borracha':
        return ['TD'],flts['VENDEDOR'],['Todos',seta]
    else:
        for i in flts['VENDEDOR']:
            if boolean:
                boolean = i in value
                
        if boolean:
            if input_id != 'checklist-vendedor-todos':
                valores = value
                todos = ['TD']
            else:
                if 'TD' in value_todos:
                    valores = []
                    todos = []
                else:
                    todos = value_todos
            return todos,valores,['Todos',seta]
        else:
            if input_id == 'checklist-vendedor-todos':
                valores = flts['VENDEDOR']
                todos = ['TD']
            else:
                todos = []
            
        if 'TD' in todos:
            return todos,valores,['Todos',seta]
        elif len(value) > 1:
            return todos,valores,['Seleções Múltiplas',seta]
        elif len(value) == 1:
            return todos,valores,[value[0],seta]
        else:
            return todos,valores,['Todos',seta]


@app.callback(Output('check-list-inicio-suprimento', 'style'), [Input('btn-inicio-suprimento', 'n_clicks')])
def troca_inicio_suprimento(n_clicks):
    if n_clicks == None:
        return {'display': 'none'}
    else:
        if n_clicks % 2 == 0:
            return {'display': 'none'}
        else: 
            return {'display': 'block'}
    
@app.callback(
    Output('checklist-inicio-suprimento-todos', 'value'),
    Output('checklist-inicio-suprimento-valores', 'value'),
    Output('btn-inicio-suprimento', 'children'),
    Input('checklist-inicio-suprimento-todos', 'value'),
    Input('checklist-inicio-suprimento-valores', 'value'),
    Input('limpar-alteracoes', 'n_clicks'),
    Input('borracha', 'n_clicks')
)
def rotina_todos_inicio_suprimento(value_todos,value,n_click,n_borracha):
    ctx =  dash.callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    valores = value
    boolean = True
    seta = html.Span('',className="seta ml-auto", id="seta")
    if input_id == 'limpar-alteracoes' or input_id == 'borracha':
        return ['TD'],flts['INÍCIO DE SUPRIMENTO'],['Todos',seta]
    else:
        for i in flts['INÍCIO DE SUPRIMENTO']:
            if boolean:
                boolean = i in value
                
        if boolean:
            if input_id != 'checklist-inicio-suprimento-todos':
                valores = value
                todos = ['TD']
            else:
                if 'TD' in value_todos:
                    valores = []
                    todos = []
                else:
                    todos = value_todos
            return todos,valores,['Todos',seta]
        else:
            if input_id == 'checklist-inicio-suprimento-todos':
                valores = flts['INÍCIO DE SUPRIMENTO']
                todos = ['TD']
            else:
                todos = []
            
        if 'TD' in todos:
            return todos,valores,['Todos',seta]
        elif len(value) > 1:
            return todos,valores,['Seleções Múltiplas',seta]
        elif len(value) == 1:
            return todos,valores,[value[0],seta]
        else:
            return todos,valores,['Todos',seta] 
        

@app.callback(Output('check-list-fim-suprimento', 'style'), [Input('btn-fim-suprimento', 'n_clicks')])
def troca_fim_suprimento(n_clicks):
    if n_clicks == None:
        return {'display': 'none'}
    else:
        if n_clicks % 2 == 0:
            return {'display': 'none'}
        else: 
            return {'display': 'block'}
    
@app.callback(
    Output('checklist-fim-suprimento-todos', 'value'),
    Output('checklist-fim-suprimento-valores', 'value'),
    Output('btn-fim-suprimento', 'children'),
    Input('checklist-fim-suprimento-todos', 'value'),
    Input('checklist-fim-suprimento-valores', 'value'),
    Input('limpar-alteracoes', 'n_clicks'),
    Input('borracha', 'n_clicks')
)
def rotina_todos_fim_suprimento(value_todos,value,n_click,n_borracha):
    ctx =  dash.callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    valores = value
    boolean = True
    seta = html.Span('',className="seta ml-auto", id="seta")
    if input_id == 'limpar-alteracoes' or input_id == 'borracha':
        return ['TD'],flts['FIM DE SUPRIMENTO'],['Todos',seta]
    else:
        for i in flts['FIM DE SUPRIMENTO']:
            if boolean:
                boolean = i in value
                
        if boolean:
            if input_id != 'checklist-fim-suprimento-todos':
                valores = value
                todos = ['TD']
            else:
                if 'TD' in value_todos:
                    valores = []
                    todos = []
                else:
                    todos = value_todos
            return todos,valores,['Todos',seta]
        else:
            if input_id == 'checklist-fim-suprimento-todos':
                valores = flts['FIM DE SUPRIMENTO']
                todos = ['TD']
            else:
                todos = []
                
        if 'TD' in todos:
            return todos,valores,['Todos',seta]
        elif len(value) > 1:
            return todos,valores,['Seleções Múltiplas',seta]
        elif len(value) == 1:
            return todos,valores,[value[0],seta]
        else:
            return todos,valores,['Todos',seta]   
        
    