# from arches.app.models.models import VwExportNodes as Node
# from arches.app.models.models import VwExportEdges as Edges
import csv
from pprint import pprint as pp
import os
from arches.app.models.graph import Graph
from arches.app.utils.betterJSONSerializer import JSONSerializer, JSONDeserializer

def export(export_dir):
    """
    Exports existing graphs as Gephi nodes and edges files to a directory
    """
    write_nodes(export_dir)
    write_edges(export_dir)

def write_nodes(export_dir):
    nodes = Node.objects.all()
    entitytypeids = {}
    for node in nodes:
        if node.assettype not in entitytypeids:
            entitytypeids[node.assettype] = []
        entitytypeids[node.assettype].append([node.id,node.label,node.mergenode,node.businesstablename])

    for k, v in entitytypeids.iteritems():
        with open(os.path.join(export_dir, k + '_nodes.csv'), 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter= ',')
            writer.writerow(['Id','Label','mergenode','businesstablename'])
            writer.writerow([k+':'+k,k,k,''])
            for node in v:
                writer.writerow(node)

def write_edges(export_dir):
    edges = Edge.objects.all()
    entitytypeids = {}
    for edge in edges:
        if edge.assettype not in entitytypeids:
            entitytypeids[edge.assettype] = []
        entitytypeids[edge.assettype].append([edge.source,edge.target,"Directed",edge.target,edge.label,1.0])

    for k, v in entitytypeids.iteritems():
        with open(os.path.join(export_dir, k + '_edges.csv'), 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter= ',')
            writer.writerow(['Source','Target','Type','Id','Label','Weight'])
            for node in v:
                writer.writerow(node)

def get_graphs_for_export(resource_list=None):
    graphs = {}
    if resource_list == None:
        graphs['graph'] = Graph.objects.all().exclude(name='Arches configuration')
    else:
        graphs['graph'] = Graph.objects.filter(graphid__in=resource_list)
    return graphs

def write_graph(export_dir, resource_list):
    resource_graphs = get_graphs_for_export(resource_list)
    graph = {}
    graph['graph'] = resource_graphs

    with open(os.path.join(export_dir, 'graph_export.json'), 'w') as graph_json:
        graph_json.write(JSONSerializer().serialize(graph))