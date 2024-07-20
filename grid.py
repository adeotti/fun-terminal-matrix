import sys
import numpy as np


class Game:
    def __init__(self,size) :
        self.size = size 

    def board(self) -> np.ndarray  : 
        np.set_printoptions(suppress=True,linewidth=np.nan,threshold=sys.maxsize)
        np.random.seed(42)
        matrix = np.random.randint(0,self.size[0], size=self.size)  
        return matrix

    def theme(self) :  
        matrix = self.board()
        matrix = np.vectorize("{:02d}".format)(matrix)
        
        def theme_grid(map) -> str :
            size = map.shape # Columns to Yellow
            map = map.flatten()
            map = np.array(map, dtype='<U20') 

            map[6::7] = ["\033[33m" + element + "\033[0m" for element in map[6::7]]
            map[48::49] = [element.replace("\033[33m","\033[31m") for element in map[48::49] ] # Last row to red 
            map = map.reshape(size)
            
            for i in range(6,len(map),7): # Row to Yellow
                map[i,:] = ["\033[33m" + element + "\033[0m" for element in map[i,:]]
            map[-1] = [element.replace("\033[33m","\033[31m") for element in map[-1]] # Last column to red
            output = ("\n".join(" ".join(row) for row in map))
            return output
        return  theme_grid(matrix)

    def Subgrid(self, CONST = 7, MAX_COL_END = 56, ZERO = 0 ) -> list[np.array]:
        map = self.board()
        row_start = ZERO
        row_end = CONST
        col_start = ZERO
        col_end = CONST
        subgrid = []

        while len(subgrid) < len(map) :
            subgrid.append(map[row_start:row_end,col_start:col_end]
                            )
            col_start += CONST
            col_end += CONST
            if col_end == MAX_COL_END :
                col_start = ZERO
                col_end = CONST
                row_start += CONST
                row_end += CONST

        # dict style { element_index : element } --  might be helpful later...maybe
        dict_subgrid = { i : subgrid[i] for i in range(len(subgrid)) } 
        dict_subgrid = {key : value.tolist() for key,value in dict_subgrid.items() }  
        assert len(subgrid) == len(map)
        return subgrid  

# base size : 49,49
 

 




    
    
 