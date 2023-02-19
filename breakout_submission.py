#vertice colouring function
def colour_vertices(graph):
    vertices = sorted((list(graph.keys()))) #ls of keys
    colour_graph = {} #dictionary of person and its colour
    for vertex in vertices:  #for person in ls of people, whr each person is a node
        unused_colours = [True]*len(vertices) #colours list 
        for adjacent_vertex in graph[vertex]: #for friends of current person
            if adjacent_vertex in colour_graph: #if already coloured, set colour to used
                colour = colour_graph[adjacent_vertex] 
                unused_colours[colour] = False
        for colour, unused in enumerate(unused_colours): 
            if unused: #if colour is unused, we colour the vertex
                colour_graph[vertex] = colour 
                break
    return colour_graph, unused_colours.count(False)

#sample data
#d = {'Chris': {'Paul', 'Dave'}, 'Paul': {'Dave'}, 'Dave': {'Sarah', 'Chris'}, 'Sarah': {'Lisa'}, 'Lisa': {'Sarah'}, 'Alex': {'Jane'}, 'Jane': {'Alex'}, 'Tom': {'Kim'}, 'Kim': {'Alex'}}
#d = {'Chris': {'Paul', 'Dave','Monica'}, 'Paul': {'Dave','Hendricks','Fanny'}, 'Dave': {'Sarah', 'Chris'}, 'Sarah': {'Lisa','Vernon'}, 'Lisa': {'Sarah','Irfan','Ethan'}, 'Alex': {'Jane','Benedict'}, 'Jane': {'Alex','Xavier'}, 'Tom': {'Kim'}, 'Kim': {'Alex'},'Monica':{'Chris','Norman'},'Norman':{'Monica'},'Hendricks':{'Paul'},'Fanny':{'Paul'},'Vernon':{'Sarah'},'Irfan':{'Lisa'},'Ethan':{'Lisa'},'Benedict':{'Alex','Zack'},'Zack':{'Benedict','Gloria'},'Gloria':{'Zack'},'Xavier':{'Jane'}}
#d = {'Alex':{'Hina','Gloria','Fanny'},
#     'Benedict':{'Hina','Derek','Chris'},
#     'Chris':{'Benedict','Hina','Gloria','Ethan','Derek'},
#     'Derek':{'Chris','Benedict','Ethan'},
#     'Ethan':{'Chris','Derek','Fanny','Gloria'},
#     'Fanny':{'Alex','Ethan','Gloria'},
#     'Gloria':{'Alex','Chris','Ethan','Fanny'},
#     'Hina':{'Alex','Benedict','Chris'},
#    }

#take inputs
d = {}
n = int(input("Number of names in list: "))
for i in range(n):
    name = input("name: ")
    friends = list(map(str, input(name+"'s friends: ").split(",")))
    d[name] = friends

#call vertice colouring function
result, numOfGrps = colour_vertices(d)
#print(result)

#place same grp-colouring members into same list
grps = [[]for i in range(numOfGrps+1)]
for key, value in result.items():
    grps[value].append(key)

#display grps
for i in range(len(grps)):
    print ("\nGroup "+str(i+1)+":")
    print ("("+str(len(grps[i]))+" members)")
    for member in grps[i]:
        print(member)
    

