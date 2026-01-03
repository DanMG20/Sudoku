diag = [1,2,3]

for q_index, quadrant in enumerate(diag):
            base_row = (q_index // 3 ) * 3 
            base_col = (q_index % 3 ) * 3 
            print(base_row,base_col)