import marimo

__generated_with = "0.9.17"
app = marimo.App()


@app.cell
def __(mo):
    mo.md("""#3D Geometry File Formats""")
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ## About STL

        STL is a simple file format which describes 3D objects as a collection of triangles.
        The acronym STL stands for "Simple Triangle Language", "Standard Tesselation Language" or "STereoLitography"[^1].

        [^1]: STL was invented for – and is still widely used – for 3D printing.
        """
    )
    return


@app.cell
def __(mo, show):
    mo.show_code(show("data/teapot.stl", theta=45.0, phi=30.0, scale=2))
    return


@app.cell
def __(mo):
    with open("data/teapot.stl", mode="rt", encoding="utf-8") as _file:
        teapot_stl = _file.read()

    teapot_stl_excerpt = teapot_stl[:723] + "..." + teapot_stl[-366:]

    mo.md(
        f"""
    ## STL ASCII Format

    The `data/teapot.stl` file provides an example of the STL ASCII format. It is quite large (more than 60000 lines) and looks like that:
    """
    +
    f"""```
    {teapot_stl_excerpt}
    ```
    """
    +

    """
    """
    )
    return teapot_stl, teapot_stl_excerpt


@app.cell
def __(mo):
    mo.md(f"""

      - Study the [{mo.icon("mdi:wikipedia")} STL (file format)](https://en.wikipedia.org/wiki/STL_(file_format)) page (or other online references) to become familiar the format.

      - Create a STL ASCII file `"data/cube.stl"` that represents a cube of unit length  
        (💡 in the simplest version, you will need 12 different facets).

      - Display the result with the function `show` (make sure to check different angles).
    """)
    return


@app.cell
def __(show):
    #On crée un fichier cube.stl et on écrit en STL ASCII un cube de longueur 1 avec 12 triangles
    fichier_cube = open("data\cube.stl", "w")
    fichier_cube.write("solid cube \n")
    fichier_cube.write("facet normal 0 0 -1 \n\touter loop \n\t\tvertex 1 0 0 \n\t\tvertex 0 0 0 \n\t\tvertex 0 1 0 \n\tendloop \nendfacet \n")
    fichier_cube.write("facet normal 0 0 -1 \n\touter loop \n\t\tvertex 1 0 0 \n\t\tvertex 0 1 0 \n\t\tvertex 1 1 0 \n\tendloop \nendfacet \n")
    fichier_cube.write("facet normal 1 0 0 \n\touter loop \n\t\tvertex 1 0 0 \n\t\tvertex 1 1 0 \n\t\tvertex 1 1 1 \n\tendloop \nendfacet \n")
    fichier_cube.write("facet normal 0 1 0 \n\touter loop \n\t\tvertex 1 1 0 \n\t\tvertex 0 1 0 \n\t\tvertex 0 1 1 \n\tendloop \nendfacet \n")
    fichier_cube.write("facet normal -1 0 0 \n\touter loop \n\t\tvertex 0 1 0 \n\t\tvertex 0 0 0 \n\t\tvertex 0 0 1 \n\tendloop \nendfacet \n")
    fichier_cube.write("facet normal 0 -1 0 \n\touter loop \n\t\tvertex 0 0 0 \n\t\tvertex 1 0 0 \n\t\tvertex 1 0 1 \n\tendloop \nendfacet \n")
    fichier_cube.write("facet normal 1 0 0 \n\touter loop \n\t\tvertex 1 0 0 \n\t\tvertex 1 1 1 \n\t\tvertex 1 0 1 \n\tendloop \nendfacet \n")
    fichier_cube.write("facet normal 0 1 0 \n\touter loop \n\t\tvertex 1 1 0 \n\t\tvertex 0 1 1 \n\t\tvertex 1 1 1 \n\tendloop \nendfacet \n")
    fichier_cube.write("facet normal -1 0 0 \n\touter loop \n\t\tvertex 0 1 0 \n\t\tvertex 0 0 1 \n\t\tvertex 0 1 1 \n\tendloop \nendfacet \n")
    fichier_cube.write("facet normal 0 -1 0 \n\touter loop \n\t\tvertex 0 0 0 \n\t\tvertex 1 0 1 \n\t\tvertex 0 0 1 \n\tendloop \nendfacet \n")
    fichier_cube.write("facet normal 0 0 1 \n\touter loop \n\t\tvertex 1 0 1 \n\t\tvertex 1 1 1 \n\t\tvertex 0 1 1 \n\tendloop \nendfacet \n")
    fichier_cube.write("facet normal 0 0 1 \n\touter loop \n\t\tvertex 1 0 1 \n\t\tvertex 0 1 1 \n\t\tvertex 0 0 1 \n\tendloop \nendfacet \n")
    fichier_cube.write("endsolid cube")
    fichier_cube.close()
    # On montre le résultat
    show('data\cube.stl',theta= 60,phi =30, scale=1)
    return (fichier_cube,)


@app.cell
def __(mo):
    mo.md(r"""## STL & NumPy""")
    return


@app.cell
def __(mo):
    mo.md(rf"""

    ### NumPy to STL

    Implement the following function:

    ```python
    def make_STL(triangles, normals=None, name=""):
        pass # 🚧 TODO!
    ```

    #### Parameters

      - `triangles` is a NumPy array of shape `(n, 3, 3)` and data type `np.float32`,
         which represents a sequence of `n` triangles (`triangles[i, j, k]` represents 
         is the `k`th coordinate of the `j`th point of the `i`th triangle)

      - `normals` is a NumPy array of shape `(n, 3)` and data type `np.float32`;
         `normals[i]` represents the outer unit normal to the `i`th facet.
         If `normals` is not specified, it should be computed from `triangles` using the 
         [{mo.icon("mdi:wikipedia")} right-hand rule](https://en.wikipedia.org/wiki/Right-hand_rule).

      - `name` is the (optional) solid name embedded in the STL ASCII file.

    #### Returns

      - The STL ASCII description of the solid as a string.

    #### Example

    Given the two triangles that make up a flat square:

    ```python

    square_triangles = np.array(
        [
            [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]],
            [[1.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]],
        ],
        dtype=np.float32,
    )
    ```

    then printing `make_STL(square_triangles, name="square")` yields
    ```
    solid square
      facet normal 0.0 0.0 1.0
        outer loop
          vertex 0.0 0.0 0.0
          vertex 1.0 0.0 0.0
          vertex 0.0 1.0 0.0
        endloop
      endfacet
      facet normal 0.0 0.0 1.0
        outer loop
          vertex 1.0 1.0 0.0
          vertex 0.0 1.0 0.0
          vertex 1.0 0.0 0.0
        endloop
      endfacet
    endsolid square
    ```

    """)
    return


@app.cell
def __(np):
    def make_STL(triangles, normals=None, name=""):
        fichier = open(f"{name}.stl", "w")
        fichier.write(f'solid {name} \n')
        for i in range(len(triangles)):
            if normals == None :
                #on définit les coordonnées du vecteur normal au plan
                X = (triangles[i][1][1]-triangles[i][0][1])*(triangles[i][2][2]-triangles[i][0][2]) - (triangles[i][1][2]-triangles[i][0][2])*(triangles[i][2][1]-triangles[i][0][1])
                Y = (triangles[i][1][2]-triangles[i][0][2])*(triangles[i][2][0]-triangles[i][0][0]) - (triangles[i][1][0]-triangles[i][0][0])*(triangles[i][2][2]-triangles[i][0][2])
                Z = (triangles[i][1][0]-triangles[i][0][0])*(triangles[i][2][1]-triangles[i][0][1]) - (triangles[i][1][1]-triangles[i][0][1])*(triangles[i][2][0]-triangles[i][0][0]) 
                norme = np.sqrt(X**2 + Y**2 + Z**2)
                fichier.write(f"facet normal {X/norme} {Y/norme} {Z/norme} \n\touter loop \n")
            else :
                fichier.write(f"facet normal {normals[i][0]} {normals[i][1]} {normals[i][2]} \n\touter loop \n")
            for j in range(3):
                fichier.write("\t\tvertex")
                for k in range(3):
                    fichier.write(f" {triangles[i][j][k]}")
                fichier.write("\n")
            fichier.write("\tendloop \nendfacet \n")
        fichier.write(f"endsolid {name}")
        fichier.close()
        fichier = open(f"{name}.stl", "r")
        return f"{fichier.read()}"
    return (make_STL,)


@app.cell
def __(make_STL, np, show):
    #on test la fonction
    square_triangles = np.array([[[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]],[[1.0, 1.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]]],dtype=np.float32)
    print(make_STL(square_triangles, name ="square"))

    show('square.stl',theta= 60,phi =30, scale=1)
    return (square_triangles,)


@app.cell
def __(mo):
    mo.md(
        """
        ### STL to NumPy

        Implement a `tokenize` function


        ```python
        def tokenize(stl):
            pass # 🚧 TODO!
        ```

        that is consistent with the following documentation:


        #### Parameters

          - `stl`: a Python string that represents a STL ASCII model.

        #### Returns

          - `tokens`: a list of STL keywords (`solid`, `facet`, etc.) and `np.float32` numbers.

        #### Example

        For the ASCII representation the square `data/square.stl`, printing the tokens with

        ```python
        with open("data/square.stl", mode="rt", encoding="us-ascii") as square_file:
            square_stl = square_file.read()
        tokens = tokenize(square_stl)
        print(tokens)
        ```

        yields

        ```python
        ['solid', 'square', 'facet', 'normal', np.float32(0.0), np.float32(0.0), np.float32(1.0), 'outer', 'loop', 'vertex', np.float32(0.0), np.float32(0.0), np.float32(0.0), 'vertex', np.float32(1.0), np.float32(0.0), np.float32(0.0), 'vertex', np.float32(0.0), np.float32(1.0), np.float32(0.0), 'endloop', 'endfacet', 'facet', 'normal', np.float32(0.0), np.float32(0.0), np.float32(1.0), 'outer', 'loop', 'vertex', np.float32(1.0), np.float32(1.0), np.float32(0.0), 'vertex', np.float32(0.0), np.float32(1.0), np.float32(0.0), 'vertex', np.float32(1.0), np.float32(0.0), np.float32(0.0), 'endloop', 'endfacet', 'endsolid', 'square']
        ```
        """
    )
    return


@app.cell
def __(np):
    def tokenize(stl):
        liste = stl.split()
        for i in range(len(liste)):
            if (liste[i] == 'vertex') or (liste[i] == 'normal') :
                for r in range(3):
                    liste[i+r +1] = np.float32(float(liste[i+r+1]))
        return liste

    #On test la fonction
    with open("data\square.stl", mode="rt", encoding="us-ascii") as square_file:
        square_stl = square_file.read()

    print(square_stl)
    tokens = tokenize(square_stl)
    print(tokens)
    return square_file, square_stl, tokenize, tokens


@app.cell
def __(mo):
    mo.md(
        """
        Implement a `parse` function


        ```python
        def parse(tokens):
            pass # 🚧 TODO!
        ```

        that is consistent with the following documentation:


        #### Parameters

          - `tokens`: a list of tokens

        #### Returns

        A `triangles, normals, name` triple where

          - `triangles`: a `(n, 3, 3)` NumPy array with data type `np.float32`,

          - `normals`: a `(n, 3)` NumPy array with data type `np.float32`,

          - `name`: a Python string.

        #### Example

        For the ASCII representation `square_stl` of the square,
        tokenizing then parsing

        ```python
        with open("data/square.stl", mode="rt", encoding="us-ascii") as square_file:
            square_stl = square_file.read()
        tokens = tokenize(square_stl)
        triangles, normals, name = parse(tokens)
        print(repr(triangles))
        print(repr(normals))
        print(repr(name))
        ```

        yields

        ```python
        array([[[0., 0., 0.],
                [1., 0., 0.],
                [0., 1., 0.]],

               [[1., 1., 0.],
                [0., 1., 0.],
                [1., 0., 0.]]], dtype=float32)
        array([[0., 0., 1.],
               [0., 0., 1.]], dtype=float32)
        'square'
        ```
        """
    )
    return


@app.cell
def __(np, square_stl, tokenize):
    def parse(tokens):
        normals = []
        name = tokens[1]
        sommets_trg = []
        for i in range(len(tokens)):
            if (tokens[i] == 'vertex'):
                sommet_trg = []
                for r in range(3):
                    sommet_trg.append(tokens[i+r+1])
                sommets_trg.append(sommet_trg)
            if (tokens[i] == 'normal') :
                sommet_nrm = []
                for r in range(3) :
                    sommet_nrm.append(tokens[i+r+1])
                normals.append(sommet_nrm)

        triangles = np.array(sommets_trg).reshape((len(sommets_trg)//3, 3, 3))
        return triangles, np.array(normals), name

    #On teste la fonction
    token = tokenize(square_stl)
    triangles, normals, name = parse(token)
    print(repr(triangles))
    print(repr(normals))
    print(repr(name))

    #test 2
    """with open("data/teapot.stl", mode="rt", encoding="us-ascii") as teapot_file:
        teapot = teapot_file.read()
    tokens_teapot = tokenize(teapot)
    triangles_t, normals_t, name_t = parse(tokens_teapot)
    print(repr(triangles_t))
    print(repr(normals_t))
    print(repr(name_t))"""
    return name, normals, parse, token, triangles


@app.cell
def __(mo):
    mo.md(
        rf"""
    ## Rules & Diagnostics



        Make diagnostic functions that check whether a STL model satisfies the following rules

          - **Positive octant rule.** All vertex coordinates are non-negative.

          - **Orientation rule.** All normals are (approximately) unit vectors and follow the [{mo.icon("mdi:wikipedia")} right-hand rule](https://en.wikipedia.org/wiki/Right-hand_rule).

          - **Shared edge rule.** Each triangle edge appears exactly twice.

          - **Ascending rule.** the z-coordinates of (the barycenter of) each triangle are a non-decreasing sequence.

    When the rule is broken, make sure to display some sensible quantitative measure of the violation (in %).

    For the record, the `data/teapot.STL` file:

      - 🔴 does not obey the positive octant rule,
      - 🟠 almost obeys the orientation rule, 
      - 🟢 obeys the shared edge rule,
      - 🔴 does not obey the ascending rule.

    Check that your `data/cube.stl` file does follow all these rules, or modify it accordingly!

    """
    )
    return


@app.cell
def __(np, parse, tokenize):
    def diagnostic(stl_file):
        with open(stl_file, mode="rt", encoding="us-ascii") as file:
            stl = file.read()
        tokens = tokenize(stl)
        triangles, normals, name = parse(tokens)
        #Positive octant rule
        nb_erreurs = 0
        total_coordonnées_sommets = 0
        for triangle in triangles :
            for i in range(3):
                for j in range(3):
                    if triangle[i][j] < 0 :
                        nb_erreurs += 1
                    total_coordonnées_sommets += 1
        print("la règle positive octant est violée à" , (nb_erreurs/total_coordonnées_sommets)*100 , "%")

        #Orientation rule. All normals are (approximately) unit vectors and follow the  right-hand rule.
        nb_erreurs_2 = 0
        nb_erreurs_2_bis = 0
        total_normes = 0
        for norme in normals :
            val_norme = np.sqrt(norme[0]**2 + norme[1]**2 + norme[2]**2)
            if val_norme != 1 :
                nb_erreurs_2 += 1
            total_normes += 1
        print("la règle de l'orientation pour les vecteurs unitaires est violée à", (nb_erreurs_2/total_normes)*100 , "%" )
        for i in range(len(triangles)) :
            X = (triangles[i][1][1]-triangles[i][0][1])*(triangles[i][2][2]-triangles[i][0][2]) - (triangles[i][1][2]-triangles[i][0][2])*(triangles[i][2][1]-triangles[i][0][1])
            Y = (triangles[i][1][2]-triangles[i][0][2])*(triangles[i][2][0]-triangles[i][0][0]) - (triangles[i][1][0]-triangles[i][0][0])*(triangles[i][2][2]-triangles[i][0][2])
            Z = (triangles[i][1][0]-triangles[i][0][0])*(triangles[i][2][1]-triangles[i][0][1]) - (triangles[i][1][1]-triangles[i][0][1])*(triangles[i][2][0]-triangles[i][0][0]) 
            norme = [X,Y,Z]
            if (Y*normals[i][0] != X*normals[i][1]) or (normals[i][0]*Z != X*normals[i][2]) or (normals[i][2]*Y != normals[i][1]*Z) or (normals[i][0]*X < 0):
                    nb_erreurs_2_bis += 1

        print("la règle de l'orientation pour la règle de la main droite est violée à", (nb_erreurs_2_bis/total_normes)*100 , "%" )

        #Shared edge rule. Each triangle edge appears exactly twice.
        edges = {}
        nb_erreurs_3 = 0
        """for triangle in triangles :
            if ([triangle[0],triangle[1]] in edges) or ([str(triangle[1]),str(triangle[0])] in edges) :
                edges[[str(triangle[0]),str(triangle[1])]] += 1
            else :
                edges[[str(triangle[0]),str(triangle[1])]] = 1

            if ([str(triangle[0]),str(triangle[2])] in edges) or ([str(triangle[2]),str(triangle[0])] in edges):
                edges[[str(triangle[0]),str(triangle[2])]] += 1
            else :
                edges[[str(triangle[0]),str(triangle[2])]] = 1

            if ([str(triangle[2]),str(triangle[1])] in edges) or ([str(triangle[1]),str(triangle[2])] in edges)  :
                edges[[str(triangle[2]),str(triangle[1])]] += 1
            else :
                edges[[str(triangle[2]),str(triangle[1])]] = 1

        for _, n in edges.items():
            if n != 2 :
                nb_erreurs_3 += 1
        print("la règle shared edge est violée à", (nb_erreurs_3/len(edges))*100 , "%" )"""
        #Je voulais créer un dictionnaire où les clés seraient les couples de sommets (edges) et les valeurs leur nombre d'apparition

        #Ascending rule. the z-coordinates of (the barycenter of) each triangle are a non-decreasing sequence.
        nb_erreurs_4 = 0
        total_triangles = len(triangles)
        z_coordinates = []
        for triangle in triangles :
            z_coordinates.append((triangle[0][2] + triangle[1][2] + triangle[2][2])/3)
        for i in range(len( z_coordinates) - 1):
            if z_coordinates[i] > z_coordinates[i+1]:
                nb_erreurs_4 += 1
        print("la règle de l'ascendence est violée à", (nb_erreurs_4/total_triangles)*100 , "%" )

    #On teste la fonction
    diagnostic('data/teapot.stl')
    return (diagnostic,)


@app.cell
def __(mo):
    mo.md(
    rf"""
    ## OBJ Format

    The OBJ format is an alternative to the STL format that looks like this:

    ```
    # OBJ file format with ext .obj
    # vertex count = 2503
    # face count = 4968
    v -3.4101800e-003 1.3031957e-001 2.1754370e-002
    v -8.1719160e-002 1.5250145e-001 2.9656090e-002
    v -3.0543480e-002 1.2477885e-001 1.0983400e-003
    v -2.4901590e-002 1.1211138e-001 3.7560240e-002
    v -1.8405680e-002 1.7843055e-001 -2.4219580e-002
    ...
    f 2187 2188 2194
    f 2308 2315 2300
    f 2407 2375 2362
    f 2443 2420 2503
    f 2420 2411 2503
    ```

    This content is an excerpt from the `data/bunny.obj` file.

    """
    )
    return


@app.cell
def __(mo, show):
    mo.show_code(show("data/bunny.obj", scale="1.5"))
    return


@app.cell
def __(mo):
    mo.md(
        """
        Study the specification of the OBJ format (search for suitable sources online),
        then develop a `OBJ_to_STL` function that is rich enough to convert the OBJ bunny file into a STL bunny file.
        """
    )
    return


@app.cell
def __(make_STL, mo, np, show):
    def OBJ_to_STL(obj_file) :
        vertices = []
        faces = [] #une face est définie par trois sommets, elle correspond à un triangle du format STL
        with open(obj_file, mode="rt", encoding="us-ascii") as file:
            obj = file.read()
        l = obj.split()
        for i in range(len(l)) :
            if l[i] == 'v' :
                vertices.append([np.float32(float(l[i+1])) , np.float32(float(l[i+2])) , np.float32(float(l[i+3]))])
            if l[i] == 'f' :
                a = int(l[i+1])
                b = int(l[i+2])
                c = int(l[i+3])
                faces.append([vertices[a -1] , vertices[b -1], vertices[c-1]])
        stl_file = make_STL(np.array(faces), name = obj_file)
        return stl_file

    #On teste la fonction
    OBJ_to_STL('data/bunny.obj')
    mo.show_code(show("data/bunny.obj.stl", scale="1.5"))
    return (OBJ_to_STL,)


@app.cell
def __(mo):
    mo.md(
        rf"""
    ## Binary STL

    Since the STL ASCII format can lead to very large files when there is a large number of facets, there is an alternate, binary version of the STL format which is more compact.

    Read about this variant online, then implement the function

    ```python
    def STL_binary_to_text(stl_filename_in, stl_filename_out):
        pass  # 🚧 TODO!
    ```

    that will convert a binary STL file to a ASCII STL file. Make sure that your function works with the binary `data/dragon.stl` file which is an example of STL binary format.

    💡 The `np.fromfile` function may come in handy.

        """
    )
    return


@app.cell
def __(mo, show):
    mo.show_code(show("data/dragon.stl", theta=75.0, phi=-20.0, scale=1.7))
    return


@app.cell
def __(make_STL, mo, np, show):
    def STL_binary_to_text(stl_filename_in, stl_filename_out):
        with open(stl_filename_in, mode="rb") as file:
            _ = file.read(80) #on lit juste l'entête
            n = np.fromfile(file, dtype=np.uint32, count=1)[0] #nombre de faces dans le fichier
            normals = []
            faces = []
            for i in range(n):
                normals.append(np.fromfile(file, dtype=np.float32, count=3))
                faces.append(np.fromfile(file, dtype=np.float32, count=9).reshape(3, 3))
                _ = file.read(2) # short unsigned number 'attribute byte count'
        stl_text = make_STL(faces, normals)
        with open(stl_filename_out, mode="wt", encoding="utf-8") as file:
            file.write(stl_text)

    # On teste la fonction
    STL_binary_to_text('data/dragon.stl','data/dragon_ascii.stl')
    mo.show_code(show("data/dragon_ascii.stl", theta=75.0, phi=-20.0, scale=1.7))
    return (STL_binary_to_text,)


@app.cell
def __(mo):
    mo.md(rf"""## Constructive Solid Geometry (CSG)

    Have a look at the documentation of [{mo.icon("mdi:github")}fogleman/sdf](https://github.com/fogleman/) and study the basics. At the very least, make sure that you understand what the code below does:
    """)
    return


@app.cell
def __(X, Y, Z, box, cylinder, mo, show, sphere):
    demo_csg = sphere(1) & box(1.5)
    _c = cylinder(0.5)
    demo_csg = demo_csg - (_c.orient(X) | _c.orient(Y) | _c.orient(Z))
    demo_csg.save('output/demo-csg.stl', step=0.05)
    mo.show_code(show("output/demo-csg.stl", theta=45.0, phi=45.0, scale=1.0))
    return (demo_csg,)


@app.cell
def __(mo):
    mo.md("""ℹ️ **Remark.** The same result can be achieved in a more procedural style, with:""")
    return


@app.cell
def __(
    box,
    cylinder,
    difference,
    intersection,
    mo,
    orient,
    show,
    sphere,
    union,
):
    demo_csg_alt = difference(
        intersection(
            sphere(1),
            box(1.5),
        ),
        union(
            orient(cylinder(0.5), [1.0, 0.0, 0.0]),
            orient(cylinder(0.5), [0.0, 1.0, 0.0]),
            orient(cylinder(0.5), [0.0, 0.0, 1.0]),
        ),
    )
    demo_csg_alt.save("output/demo-csg-alt.stl", step=0.05)
    mo.show_code(show("output/demo-csg-alt.stl", theta=45.0, phi=45.0, scale=1.0))
    return (demo_csg_alt,)


@app.cell
def __(mo):
    mo.md(
        rf"""
    ## JupyterCAD

    [JupyterCAD](https://github.com/jupytercad/JupyterCAD) is an extension of the Jupyter lab for 3D geometry modeling.

      - Use it to create a JCAD model that correspond closely to the `output/demo_csg` model;
    save it as `data/demo_jcad.jcad`.

      - Study the format used to represent JupyterCAD files (💡 you can explore the contents of the previous file, but you may need to create some simpler models to begin with).

      - When you are ready, create a `jcad_to_stl` function that understand enough of the JupyterCAD format to convert `"data/demo_jcad.jcad"` into some corresponding STL file.
    (💡 do not tesselate the JupyterCAD model by yourself, instead use the `sdf` library!)


        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        Un fichier JupyterCAD est stocké dans un dictionnaire. 
        Ce dictionnaire contient comme clés : metadata qui renvoit à un dictionnaire, objects qui a comme valeur une liste de dictionnaires, options et output qui ont comme clés des dictionnaires et schemaVersion qui a comme valeur une chaine str.
        """
    )
    return


@app.cell
def __(csg_file):
    def jcad_to_stl(jcad_file, stl_file):
        with open(jcad_file, mode="rt") as file:
            data = file.read()
        objects = []
        positions = {}
        for shape in data.get('objects', []):
            if shape['name'] == 'Box':
                objects.append(f"box([{shape['Height']}, {shape['Lenght']}, {shape['Width']}]);")
                positions['Box'] = shape['Position']
            elif shape['name'] == 'Sphere':
                objects.append(f"sphere({shape['Radius']});")
                positions['Sphere'] = shape['Position']
            elif shape['name'] == 'Cylinder 1':
                objects.append(f"cylinder(h={shape['Height']}, r={shape['Radius']});")
                positions['Cylinder 1'] = shape['Position']
            elif shape['name'] == 'Cylinder 2':
                objects.append(f"cylinder(h={shape['Height']}, r={shape['Radius']});")
                positions['Cylinder 2'] = shape['Position']
            elif shape['name'] == 'Cylinder 3':
                objects.append(f"cylinder(h={shape['Height']}, r={shape['Radius']});")
                positions['Cylinder 3'] = shape['Position']

            #objectif : recréer un fichier csg
            
        csg_file.save("output/demo-csg-alt.stl", step=0.05)
    #On teste le modèle
    #jcad_to_stl('data/demo_jcad.jcad', 'data/demo_jcad_to_stl.stl')
    return (jcad_to_stl,)


@app.cell
def __(mo):
    mo.md("""## Appendix""")
    return


@app.cell
def __(mo):
    mo.md("""### Dependencies""")
    return


@app.cell
def __():
    # Python Standard Library
    import json

    # Marimo
    import marimo as mo

    # Third-Party Librairies
    import numpy as np
    import matplotlib.pyplot as plt
    import mpl3d
    from mpl3d import glm
    from mpl3d.mesh import Mesh
    from mpl3d.camera import Camera

    import meshio

    np.seterr(over="ignore")  # 🩹 deal with a meshio false warning

    import sdf
    from sdf import sphere, box, cylinder
    from sdf import X, Y, Z
    from sdf import intersection, union, orient, difference

    mo.show_code()
    return (
        Camera,
        Mesh,
        X,
        Y,
        Z,
        box,
        cylinder,
        difference,
        glm,
        intersection,
        json,
        meshio,
        mo,
        mpl3d,
        np,
        orient,
        plt,
        sdf,
        sphere,
        union,
    )


@app.cell
def __(mo):
    mo.md(r"""### STL Viewer""")
    return


@app.cell
def __(Camera, Mesh, glm, meshio, mo, plt):
    def show(
        filename,
        theta=0.0,
        phi=0.0,
        scale=1.0,
        colormap="viridis",
        edgecolors=(0, 0, 0, 0.25),
        figsize=(6, 6),
    ):
        fig = plt.figure(figsize=figsize)
        ax = fig.add_axes([0, 0, 1, 1], xlim=[-1, +1], ylim=[-1, +1], aspect=1)
        ax.axis("off")
        camera = Camera("ortho", theta=theta, phi=phi, scale=scale)
        mesh = meshio.read(filename)
        vertices = glm.fit_unit_cube(mesh.points)
        faces = mesh.cells[0].data
        vertices = glm.fit_unit_cube(vertices)
        mesh = Mesh(
            ax,
            camera.transform,
            vertices,
            faces,
            cmap=plt.get_cmap(colormap),
            edgecolors=edgecolors,
        )
        return mo.center(fig)

    mo.show_code()
    return (show,)


@app.cell
def __(mo, show):
    mo.show_code(show("data/teapot.stl", theta=45.0, phi=30.0, scale=2))
    return


if __name__ == "__main__":
    app.run()
