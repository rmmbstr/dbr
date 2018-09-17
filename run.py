import numpy as np
import csv
from tkinter import filedialog
from tkinter import *


def randomize(gender, center, randomset):
    delta_1 = 5
    delta_2 = 5
    delta_3 = 5

    # treat_a=0 treat_b=1
    # male=0 female=1
    # center0=0 center1=1

    # randomset[center, gender, treat]
    # randomset[0, 0, 0] = 0
    # randomset[0, 1, 0] = 0
    # randomset[1, 0, 0] = 0
    # randomset[1, 1, 0] = 0
    # randomset[0, 0, 1] = 0
    # randomset[0, 1, 1] = 0
    # randomset[1, 0, 1] = 0
    # randomset[1, 1, 1] = 0
    d1 = randomset[center][gender][0] - randomset[center][gender][1]
    d2 = randomset[center][0][0] + randomset[center][1][0] - randomset[center][0][1] - randomset[center][1][1]
    d3 = randomset[0][0][0] + randomset[0][1][0] + randomset[1][0][0] + randomset[1][1][0] - randomset[0][0][1] - \
         randomset[0][1][1] - randomset[1][0][1] - randomset[1][1][1]
    if np.abs(d1) >= delta_1:
        if d1 > 0:
            randomset[center][gender][1] = randomset[center][gender][1] + 1
        else:
            randomset[center][gender][0] = randomset[center][gender][0] + 1
    elif np.abs(d2) >= delta_2:
        if d2 > 0:
            randomset[center][gender][1] = randomset[center][gender][1] + 1
        else:
            randomset[center][gender][0] = randomset[center][gender][0] + 1
    elif np.abs(d3) >= delta_3:
        if d3 > 0:
            randomset[center][gender][1] = randomset[center][gender][1] + 1
        else:
            randomset[center][gender][0] = randomset[center][gender][0] + 1
    else:
        treat = np.random.choice([0, 1])
        randomset[center][gender][treat] = randomset[center][gender][treat] + 1
    return randomset


if __name__ == '__main__':
    # randomset = {0: {0: {0: 0, 1: 0}, 1: {0: 0, 1: 0}}, 1: {0: {0: 0, 1: 0}, 1: {0: 0, 1: 0}}}
    randomset = {'param': {'gender': {'classify': ['male', 'female'],
                                      'level': 0},
                           'age': {'classify': ['young', 'old'],
                                   'level': 1},
                           'center': {'classify': ['c1', 'c2'],
                                      'level': 2}, },
                 'delta': [5, 5, 3, 3],  # delta level 0-total
                 'data': {[0, 0, 0]: [0, 1], [0, 0, 1]: [1, 1]}}  # data level 0-max: A,B
    def add1():
        gender = 0
        center = 0
        randomize(gender, center, randomset)
        v1.set(randomset[0][0][0])
        v2.set(randomset[0][0][1])
        # print(randomset)


    def add2():
        gender = 1
        center = 0
        randomize(gender, center, randomset)
        v3.set(randomset[0][1][0])
        v4.set(randomset[0][1][1])
        # print(randomset)

    def add3():
        gender = 0
        center = 1
        randomize(gender, center, randomset)
        v5.set(randomset[1][0][0])
        v6.set(randomset[1][0][1])
        # print(randomset)

    def add4():
        gender = 1
        center = 1
        randomize(gender, center, randomset)
        v7.set(randomset[1][1][0])
        v8.set(randomset[1][1][1])
        # print(randomset)

    def save_csv():
        data = [['0' for col in range(3)] for row in range(3)]
        data[0] = ['treat_a,treat_b', 'center1', 'center2']
        data[1][0] = 'male'
        data[1][1] = str(randomset[0][0][0])+','+str(randomset[0][0][1])
        data[1][2] = str(randomset[1][0][0])+','+str(randomset[1][0][1])
        data[2][0] = 'female'
        data[2][1] = str(randomset[0][1][0]) + ',' + str(randomset[0][1][1])
        data[2][2] = str(randomset[1][1][0]) + ',' + str(randomset[1][1][1])
        filename = filedialog.asksaveasfilename(filetypes=[('csv文件', '.csv')])
        if filename != '':
            with open(filename, 'w', newline='') as csvfile:
                w = csv.writer(csvfile)
                for row in data:
                    w.writerow(row)

    def save_json():
        pass


    root = Tk()
    root.geometry('500x500')
    v1 = StringVar(root)
    v2 = StringVar(root)
    v3 = StringVar(root)
    v4 = StringVar(root)
    v5 = StringVar(root)
    v6 = StringVar(root)
    v7 = StringVar(root)
    v8 = StringVar(root)

    Label(root, text='center1', height=1).grid(row=3, column=1, padx=10, pady=10)
    Label(root, text='center2', height=1).grid(row=8, column=1, padx=10, pady=10)
    Label(root, text='male', height=1).grid(row=2, column=2, padx=10, pady=10)
    Label(root, text='female', height=1).grid(row=4, column=2, padx=10, pady=10)
    Label(root, text='male', height=1).grid(row=7, column=2, padx=10, pady=10)
    Label(root, text='female', height=1).grid(row=9, column=2, padx=10, pady=10)
    Label(root, text='treat_a', height=1).grid(row=1, column=4, padx=10, pady=10)
    Label(root, text='traet_b', height=1).grid(row=2, column=4, padx=10, pady=10)
    Label(root, text='treat_a', height=1).grid(row=4, column=4, padx=10, pady=10)
    Label(root, text='traet_b', height=1).grid(row=5, column=4, padx=10, pady=10)
    Label(root, text='treat_a', height=1).grid(row=6, column=4, padx=10, pady=10)
    Label(root, text='traet_b', height=1).grid(row=7, column=4, padx=10, pady=10)
    Label(root, text='treat_a', height=1).grid(row=9, column=4, padx=10, pady=10)
    Label(root, text='traet_b', height=1).grid(row=10, column=4, padx=10, pady=10)
    Label(root, textvariable=v1, height=1).grid(row=1, column=5, padx=10, pady=10)
    Label(root, textvariable=v2, height=1).grid(row=2, column=5, padx=10, pady=10)
    Label(root, textvariable=v3, height=1).grid(row=4, column=5, padx=10, pady=10)
    Label(root, textvariable=v4, height=1).grid(row=5, column=5, padx=10, pady=10)
    Label(root, textvariable=v5, height=1).grid(row=6, column=5, padx=10, pady=10)
    Label(root, textvariable=v6, height=1).grid(row=7, column=5, padx=10, pady=10)
    Label(root, textvariable=v7, height=1).grid(row=9, column=5, padx=10, pady=10)
    Label(root, textvariable=v8, height=1).grid(row=10, column=5, padx=10, pady=10)

    Button(root, text='add', height=1, command=add1).grid(row=2, column=3, padx=10, pady=10)
    Button(root, text='add', height=1, command=add2).grid(row=4, column=3, padx=10, pady=10)
    Button(root, text='add', height=1, command=add3).grid(row=7, column=3, padx=10, pady=10)
    Button(root, text='add', height=1, command=add4).grid(row=9, column=3, padx=10, pady=10)
    # Button(root, text='保存', height=1, command=save,).grid(row=1, column=6, padx=10, pady=10)

    menu = Menu(root)

    fileMenu = Menu(menu, tearoff=0)
    fileMenu.add_command(label='新建')
    fileMenu.add_command(label='打开')
    fileMenu.add_command(label='保存', command=save_json)
    fileMenu.add_command(label='导出至csv', command=save_csv)
    menu.add_cascade(label='文件', menu=fileMenu)

    root.config(menu=menu)
    # for j in range(1):
    #     randomset = {0: {0: {0: 0, 1: 0}, 1: {0: 0, 1: 0}}, 1: {0: {0: 0, 1: 0}, 1: {0: 0, 1: 0}}}
    #     gender = 0
    #     center = 0
    #     for i in range(100):
    #         gender = np.random.choice([0, 1],p=[0.6,0.4])
    #         center = np.random.choice([0, 1],p=[0.3,0.7])
    #         randomize(gender, center, randomset)
    #     print(json.dumps(randomset,indent=1))
    root.mainloop()

