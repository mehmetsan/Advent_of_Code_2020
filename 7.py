class Vertex:
    def __init__(self, node):
        self.name = node
        self.neighbors = {}
        self.vert_count = 0

    def get_id(self):
        return self.name

    def add_neighbor(self, neighbor, count):
        self.vert_count = self.vert_count + 1
        self.neighbors[neighbor] = count

    def get_connections(self):
        return self.neighbors.keys()  

class Graph:
    def __init__(self):
        self.vert_dict = {}

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):

        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None
    
    def add_edge(self, frm, to, count):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], count)


    def get_vertices(self):
        return self.vert_dict.keys()

def get_lines():    
    input_file = open('7_input.txt', 'r') 
    lines = input_file.readlines()
    all_lines = [each.strip() for each in lines]

    return all_lines

all_lines = get_lines()

g = Graph()

# Preparing the Graph
for line in all_lines:
    edit_line = line.replace(', ',',')
    words = edit_line.split(' ')
    parent_bag_name = words[0] + ' ' + words[1]
    
    contain_clause = ''


    for each in words[4:]:
        contain_clause += each + ' '
    contain_clause = contain_clause[:-2]


    for item in contain_clause.split(','):
        if item[0] != 'n':
            count_of_item = int( item[0] )
            wordes = item.split(' ')
            child_bag_name = wordes[1] + ' ' + wordes[2]
            g.add_edge(parent_bag_name, child_bag_name, count_of_item )


'''
    PART ONE
'''
def inspect_vertex( vert ):
    if vert.get_id() == 'shiny gold':
        return True
    else:
        if len(vert.get_connections()) == 0:
            if vert.get_id() == 'shiny gold':
                return True
            else:
                return False
        else:
            for w in vert.get_connections():       
                if inspect_vertex( w ):
                    return True
                else:
                    pass
            return False


count = 0 
for v in g:
    if inspect_vertex(v):
        count += 1

count -= 1 # Since the rule with 'Shiny Gold' is also counted
print(count)

'''
    PART TWO
'''
def count_bags( vert ):
    
    if len(vert.get_connections()) == 0:
        return 1
    else:
        vert_totals = 0
        for w in vert.get_connections():   
            vert_totals += vert.neighbors[w] * count_bags( w )
        return vert_totals + 1

shiny = g.vert_dict['shiny gold']
print(count_bags(shiny) - 1 )   # Remove parent shiny bag


