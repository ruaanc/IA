class State(object):
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbors(self, states):
        for state in states:
            self.neighbors.append({
                "state": state[0], 
                "cost": state[1], 
                "heuristic": state[2]
                })
        
        
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


def search(initial_state, goal):
    frontier = [{
        "state": initial_state, 
        "cost": 0, 
        "heuristic": 460
        }]
    explored = set()

    while True:
        print(frontier)

        if len(frontier) == 0:
            return False

        selected = choose_state(frontier)
        explored.add(selected["state"])

        if selected["state"] == goal:
            return selected

        for neighbor in selected["state"].neighbors:
            if neighbor["state"] in explored:
                continue
            else:
                flag = False
                for element in frontier:
                    if neighbor["state"] == element["state"]:
                        flag = True
                        element_time = element["cost"] + element["heuristic"]
                        neighbor_time = neighbor["cost"] + selected["cost"] + neighbor["heuristic"]
                        if element_time >= neighbor_time:
                            frontier.remove(element)
                            frontier.append({
                                "state": neighbor["state"], 
                                "cost": neighbor["cost"] + selected["cost"], 
                                "heuristic": neighbor["heuristic"]
                            })    
                if flag == False:
                    frontier.append({
                        "state": neighbor["state"], 
                        "cost": neighbor["cost"] + selected["cost"], 
                        "heuristic": neighbor["heuristic"]
                    })                        
    return frontier


def choose_state(frontier):
    lower = frontier[0]

    for element in frontier:
        element_time = element["cost"] + element["heuristic"]
        lower_time = lower["cost"] + lower["heuristic"]
        if element_time < lower_time:
            lower = element

    print(lower["state"])
    frontier.clear()
    return lower


joao_pessoa = State("João Pessoa")
campina_grande = State("Campina Grande")
itabaiana = State("Itabaiana")
santa_rita = State("Santa Rita")
mamanguape = State("Mamanguape")
guarabira = State("Guarabira")
areia = State("Areia")
picui = State("Picui")
soledade = State("Soledade")
coxixola = State("Coxixola")
patos = State("Patos")
monteiro = State("Monteiro")
catole = State("Catolé do Rocha")
pombal = State("Pombal")
itaporanga = State("Itaporanga")
sousa = State("Sousa")
cajazeiras = State("Cajazeiras")

joao_pessoa.add_neighbors([
    [campina_grande,125,300], 
    [itabaiana,68,360], 
    [santa_rita,26,451]
])

campina_grande.add_neighbors([
    [joao_pessoa, 125, 300], 
    [itabaiana, 65, 360], 
    [areia, 40, 316], 
    [coxixola, 128, 232], 
    [soledade, 58, 243]
])

itabaiana.add_neighbors([
    [joao_pessoa, 68, 460], 
    [campina_grande, 65, 300]
])

santa_rita.add_neighbors([
    [joao_pessoa, 26, 451], 
    [mamanguape, 38, 380]
])

mamanguape.add_neighbors([
    [santa_rita, 38, 451], 
    [guarabira, 42, 340]
])

guarabira.add_neighbors([
    [mamanguape, 42, 380], 
    [areia, 41, 316]
])

areia.add_neighbors([
    [guarabira, 41, 340], 
    [campina_grande, 40, 316]
])

picui.add_neighbors([
    [soledade, 69, 250]
])

soledade.add_neighbors([
    [campina_grande, 58, 300], 
    [patos, 177, 122], 
    [picui, 69, 250]
])
coxixola.add_neighbors([
    [campina_grande, 128, 232], 
    [monteiro, 83, 195]
])
patos.add_neighbors([
    [soledade, 177, 243], 
    [pombal, 71, 55], 
    [itaporanga, 108, 65]
])

monteiro.add_neighbors([
    [coxixola, 83, 232], 
    [itaporanga, 224, 65]
])

catole.add_neighbors([
    [pombal, 57, 55]
])
pombal.add_neighbors([
    [catole, 57, 110], 
    [patos, 71, 122], 
    [sousa, 56, 20]
])
itaporanga.add_neighbors([
    [patos, 108, 122], 
    [monteiro, 224, 195]
])
sousa.add_neighbors([
    [pombal, 56, 55],
    [cajazeiras, 43, 0]

])
cajazeiras.add_neighbors([
    [sousa, 43, 20], 
    [itaporanga, 121, 65]
])

result = search(joao_pessoa, cajazeiras)
print(result)

