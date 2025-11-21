# create a csr matrix from an array


import numpy as np

from scipy.sparse import csr_matrix

arr = np.array([0, 0, 0, 0, 0, 1, 1,0, 2])

print(csr_matrix(arr))



import numpy as np

from scipy.sparse import csr_matrix

arr = np.array([1,2,3,4,5,56,6])

print(csr_matrix(arr))



# sparse matrix method


import numpy as np

from scipy.sparse import csr_matrix

arr = np.array([[0,0,0],[0,0,1],[1,0,2]])

print(csr_matrix(arr).data)


import numpy as np

from scipy.sparse import csr_matrix

arr = ([[0,0,1,2],[0,3,9,0],[6,7,8,0]])

print(csr_matrix(arr).data) 




import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0,0,0], [0,0,1], [1,0,2]])

mat = csr_matrix(arr)
mat.eliminate_zeros()

print(mat)



import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0,0,0], [0,0,1], [1,0,2]])

mat = csr_matrix(arr)
mat.sum_duplicates()

print(mat)



import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0,0,0], [0,0,1], [1,0,2]])

newarr = csr_matrix(arr).tocsc()

print(newarr)



import numpy as np
from scipy.sparse import csr_matrix

arr = ([[1,2,3], [4,5,6], [8,9,0]])

newarr = csr_matrix(arr).tocsc()

print(newarr)