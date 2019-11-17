import numpy as np 

input_data = 312051

def spiral_grid_distance(x):
    ring_no = np.ceil(np.sqrt(x))//2
    ring_offset = (x - (2*ring_no - 1)**2) % (4*(2*ring_no-1)+4)
    side_distance = np.abs(ring_offset%(2*ring_no) - ring_no)
    return(ring_no + side_distance)

def sum_spiral(limit):
    cells = {(0,0):1}
    x = 1
    y = 0

    direction_x = 1
    direction_y = 0 
    while True:
        csum = 0
        # Somar todos os valores próximos
        for sdx in range(-1,2):
            for sdy in range(-1,2):
                try:
                    csum += cells[(x+sdx,y+sdy)]
                except:
                    pass
        cells[(x,y)] = csum

        if csum > limit:
            break
            
        # Identificar próximo movimento
        dxn = -direction_y
        dyn = direction_x
        # verifica se podemos virar
        try:
            lhs = cells[(x+dxn,y+dyn)]
        except:
            # se a célular não for identificada, significa quee podemos virar
            direction_x = dxn
            direction_y = dyn

        # mover para a próxima célula e continuar
        x = x + direction_x
        y = y + direction_y
    
    return(csum)


print(spiral_grid_distance(input_data))
print(sum_spiral(input_data))