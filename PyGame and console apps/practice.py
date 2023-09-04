def add_results():
    data8 = input('Whatever u like ')
    
    with open('hey', 'a') as f:
        f.write(data8)
    pass

add_results()

def open():
    with open('hey', 'a') as f:
        f.write("Maricon")