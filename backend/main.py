from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PipelineData(BaseModel):
    nodes: List[Dict[str, Any]]
    edges: List[Dict[str, Any]]

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

@app.post('/pipelines/parse')
def parse_pipeline(pipeline_data: PipelineData):
    nodes = pipeline_data.nodes
    edges = pipeline_data.edges
    
    num_nodes = len(nodes)
    num_edges = len(edges)
    
    is_dag = is_directed_acyclic_graph(nodes, edges)
    return {
        'num_nodes': num_nodes,
        'num_edges': num_edges,
        'is_dag': is_dag
    }

def is_directed_acyclic_graph(nodes, edges):
    graph = {}
    node_ids = {node['id'] for node in nodes}
    
    for node_id in node_ids:
        graph[node_id] = []

    for edge in edges:
        source = edge.get('source')
        target = edge.get('target')
        if source in graph and target in graph:
            graph[source].append(target)
    
    state = {node_id: 0 for node_id in node_ids}
    
    def has_cycle(node):
        if state[node] == 1:  
            return True
        if state[node] == 2:
            return False
        state[node] = 1  
        
        for neighbor in graph[node]:
            if has_cycle(neighbor):
                return True
        state[node] = 2  
        return False
    
    for node_id in node_ids:
        if state[node_id] == 0:
            if has_cycle(node_id):
                return False  
    return True  