import re

def obj2off(objpath, offpath):
    '''
    将obj文件转换为off文件
    :param objpath: .obj文件的路径
    :param offpath: .off文件的路径的保存地址
    :return: 无
    '''
    line = ""

    vset = []
    fset = []
    with open(objpath,'r') as f:
        lines = f.readlines()
    p = re.compile(r'/+')
    space = re.compile(r' +')

    for line in lines:
        #拿到obj文件中一行，作为一个字符串
        tailMark = " "
        line = line+tailMark
        if line[0]!='v' and line[0]!='f' :
            continue

        parameters = space.split(line.strip())
        if parameters[0] == "v":   #如果是顶点的话
                Point = []
                Point.append(eval( parameters[1]) )
                Point.append(eval( parameters[2]) )
                Point.append(eval( parameters[3]) )
                vset.append(Point)

        elif parameters[0] == "f":   #如果是面的话，存放顶点的索引
                vIndexSets = []          #临时存放点的集合
                for i in range(1,len(parameters) ):
                    x = parameters[i]
                    ans = p.split(x)[0]
                    index = eval(ans)
                    index -= 1          #因为顶点索引在obj文件中是从1开始的，而我们存放的顶点是从0开始的，因此要减1
                    vIndexSets.append(index)

                fset.append(vIndexSets)

    with open(offpath, 'w') as out:
        out = open(offpath, 'w')
        out.write("OFF\n")
        out.write(str(vset.__len__()) + " " + str(fset.__len__()) + " 0\n")
        for j in range(len(vset)):
            out.write(str(vset[j][0]) + " " + str(vset[j][1]) + " " + str(vset[j][2]) + "\n")

        for i in range(len(fset)):
            s = str(len( fset[i] ))
            for j in range( len( fset[i] ) ):
                s = s+ " "+ str(fset[i][j])
            s += "\n"
            out.write(s)

    print("{} 转换成 {} 成功！".format( p.split(objpath)[-1], p.split(offpath)[-1] ))

obj2off('C:/Users/GEL/Desktop/CGAL-5.0.3-examples/CGAL-5.0.3/examples/Surface_mesh_parameterization/build/data/LSCM_bunny.obj', 'C:/Users/GEL/Desktop/CGAL-5.0.3-examples/CGAL-5.0.3/examples/Surface_mesh_parameterization/build/data/LSCM_bunny.off')