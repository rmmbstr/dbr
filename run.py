import numpy as np
import csv
from tkinter import filedialog
from tkinter import *
import pickle

class Dataset:
    def __init__(self, deltas, levels, randoms):
        self.delta = deltas
        self.level = levels
        self.random = randoms
    def getdelta(self):
        return self.delta
    def getlevel(self):
        return self.level
    def getrandom(self):
        return self.random


def randomize(age, gender, center, randomset):

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
    d1 = randomset[center][gender][age][0] - randomset[center][gender][age][1]
    d2 = randomset[center][gender][0][0] + randomset[center][gender][1][0] - randomset[center][gender][0][1] - randomset[center][gender][1][1]
    d3 = randomset[center][0][0][0] + randomset[center][0][1][0] + randomset[center][1][0][0] + randomset[center][1][1][0] - randomset[center][0][0][1] - \
         randomset[center][0][1][1] - randomset[center][1][0][1] - randomset[center][1][1][1]
    d4 = randomset[0][0][0][0]+randomset[0][0][1][0]+randomset[0][1][0][0]+randomset[0][1][1][0]+randomset[1][0][0][0]+\
         randomset[1][0][1][0]+randomset[1][1][0][0]+randomset[1][1][1][0]-randomset[0][0][0][1]-randomset[0][0][1][1]-\
         randomset[0][1][0][1]-randomset[0][1][1][1]-randomset[1][0][0][1]-randomset[1][0][1][1]-randomset[1][1][0][1]-\
         randomset[1][1][1][1]
    if np.abs(d1) >= delta_1:
        if d1 > 0:
            randomset[center][gender][age][1] = randomset[center][gender][age][1] + 1
        else:
            randomset[center][gender][age][0] = randomset[center][gender][age][0] + 1
    elif np.abs(d2) >= delta_2:
        if d2 > 0:
            randomset[center][gender][age][1] = randomset[center][gender][age][1] + 1
        else:
            randomset[center][gender][age][0] = randomset[center][gender][age][0] + 1
    elif np.abs(d3) >= delta_3:
        if d3 > 0:
            randomset[center][gender][age][1] = randomset[center][gender][age][1] + 1
        else:
            randomset[center][gender][age][0] = randomset[center][gender][age][0] + 1
    elif np.abs(d4) >= delta_4:
        if d4 > 0:
            randomset[center][gender][age][1] = randomset[center][gender][age][1] + 1
        else:
            randomset[center][gender][age][0] = randomset[center][gender][age][0] + 1
    else:
        treat = np.random.choice([0, 1])
        randomset[center][gender][age][treat] = randomset[center][gender][age][treat] + 1
    return randomset


def save_setup(initroot, e1, e2, e3, de1, de2, de3, de4):
    global delta_1, delta_2, delta_3, delta_4, level_1, level_2, level_3, randomset
    randomset = {0:
                     {0: {0: {0: 0, 1: 0},
                          1: {0: 0, 1: 0}},
                      1: {0: {0: 0, 1: 0},
                          1: {0: 0, 1: 0}}},
                 1: {0: {0: {0: 0, 1: 0},
                         1: {0: 0, 1: 0}},
                     1: {0: {0: 0, 1: 0},
                         1: {0: 0, 1: 0}}}
                 }
    delta_1 = int(de1)
    delta_2 = int(de2)
    delta_3 = int(de3)
    delta_4 = int(de4)
    level_1 = e1
    level_2 = e2
    level_3 = e3
    initroot.destroy()
    random_window()

def init(initroot):

    Label(initroot, text="分层因素：从重要至次要").grid(row=0)
    Label(initroot, text="因素1").grid(row=1, column=0)
    Label(initroot, text="因素2").grid(row=2, column=0)
    Label(initroot, text="因素3").grid(row=3, column=0)
    Label(initroot, text="全部").grid(row=4, column=0)
    Label(initroot, text="δ").grid(row=1, column=2)
    Label(initroot, text="δ").grid(row=2, column=2)
    Label(initroot, text="δ").grid(row=3, column=2)
    Label(initroot, text="δ").grid(row=4, column=2)

    e1 = Entry(initroot)
    e2 = Entry(initroot)
    e3 = Entry(initroot)
    # e4 = Entry(initroot)

    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=3, column=1)
    # e4.grid(row=4, column=1)

    de1 = Entry(initroot)
    de2 = Entry(initroot)
    de3 = Entry(initroot)
    de4 = Entry(initroot)

    de1.grid(row=1, column=3)
    de2.grid(row=2, column=3)
    de3.grid(row=3, column=3)
    de4.grid(row=4, column=3)

    Button(initroot, text='确定', command=lambda : save_setup(initroot, e1.get(),e2.get(),e3.get(),de1.get(),de2.get(),de3.get(),de4.get())).grid(row=5, column=1, sticky=W, pady=4)

    initroot.mainloop()


def random_window():
    root = Tk()
    root.geometry('500x750')

    # randomset = {'param': {'gender': {'classify': ['male', 'female'],
    #                                   'level': 0},
    #                        'age': {'classify': ['young', 'old'],
    #                                'level': 1},
    #                        'center': {'classify': ['c1', 'c2'],
    #                                   'level': 2}, },
    #              'delta': [5, 5, 3, 3],  # delta level 0-total
    #              'data': {[0, 0, 0]: [0, 1], [0, 0, 1]: [1, 1]}}  # data level 0-max: A,B

    def add1():
        age = 0
        gender = 0
        center = 0
        randomize(age, gender, center, randomset)
        v1.set(randomset[center][gender][age][0])
        v2.set(randomset[center][gender][age][1])
        # print(randomset)


    def add2():
        age = 1
        gender = 0
        center = 0
        randomize(age, gender, center, randomset)
        v3.set(randomset[center][gender][age][0])
        v4.set(randomset[center][gender][age][1])
        # print(randomset)

    def add3():
        age = 0
        gender = 1
        center = 0
        randomize(age, gender, center, randomset)
        v5.set(randomset[center][gender][age][0])
        v6.set(randomset[center][gender][age][1])
        # print(randomset)

    def add4():
        age = 1
        gender = 1
        center = 0
        randomize(age, gender, center, randomset)
        v7.set(randomset[center][gender][age][0])
        v8.set(randomset[center][gender][age][1])
        # print(randomset)


    def add5():
        age = 0
        gender = 0
        center = 1
        randomize(age, gender, center, randomset)
        v9.set(randomset[center][gender][age][0])
        v10.set(randomset[center][gender][age][1])

    def add6():
        age = 1
        gender = 0
        center = 1
        randomize(age, gender, center, randomset)
        v11.set(randomset[center][gender][age][0])
        v12.set(randomset[center][gender][age][1])

    def add7():
        age = 0
        gender = 1
        center = 1
        randomize(age, gender, center, randomset)
        v13.set(randomset[center][gender][age][0])
        v14.set(randomset[center][gender][age][1])

    def add8():
        age = 1
        gender = 1
        center = 1
        randomize(age, gender, center, randomset)
        v15.set(randomset[center][gender][age][0])
        v16.set(randomset[center][gender][age][1])

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

    v1 = StringVar(root)
    v2 = StringVar(root)
    v3 = StringVar(root)
    v4 = StringVar(root)
    v5 = StringVar(root)
    v6 = StringVar(root)
    v7 = StringVar(root)
    v8 = StringVar(root)
    v9 = StringVar(root)
    v10 = StringVar(root)
    v11 = StringVar(root)
    v12 = StringVar(root)
    v13 = StringVar(root)
    v14 = StringVar(root)
    v15 = StringVar(root)
    v16 = StringVar(root)

    # global level_1,level_2,level_3
    Label(root, text=level_3+'1', height=1).grid(row=3, column=1, padx=10, pady=10)
    Label(root, text=level_3+'2', height=1).grid(row=11, column=1, padx=10, pady=10)
    Label(root, text=level_2+'1', height=1).grid(row=1, column=2, padx=10, pady=10)
    Label(root, text=level_2+'2', height=1).grid(row=5, column=2, padx=10, pady=10)
    Label(root, text=level_2+'1', height=1).grid(row=9, column=2, padx=10, pady=10)
    Label(root, text=level_2+'2', height=1).grid(row=13, column=2, padx=10, pady=10)

    Label(root, text=level_1+'1', height=1).grid(row=0, column=3, padx=10, pady=10)
    Label(root, text=level_1+'2', height=1).grid(row=2, column=3, padx=10, pady=10)
    Label(root, text=level_1+'1', height=1).grid(row=4, column=3, padx=10, pady=10)
    Label(root, text=level_1+'2', height=1).grid(row=6, column=3, padx=10, pady=10)
    Label(root, text=level_1+'1', height=1).grid(row=8, column=3, padx=10, pady=10)
    Label(root, text=level_1+'2', height=1).grid(row=10, column=3, padx=10, pady=10)
    Label(root, text=level_1+'1', height=1).grid(row=12, column=3, padx=10, pady=10)
    Label(root, text=level_1+'2', height=1).grid(row=14, column=3, padx=10, pady=10)

    Label(root, text='treat_a', height=1).grid(row=0, column=5, padx=10, pady=10)
    Label(root, text='traet_b', height=1).grid(row=0, column=7, padx=10, pady=10)
    Label(root, text='treat_a', height=1).grid(row=2, column=5, padx=10, pady=10)
    Label(root, text='traet_b', height=1).grid(row=2, column=7, padx=10, pady=10)
    Label(root, text='treat_a', height=1).grid(row=4, column=5, padx=10, pady=10)
    Label(root, text='traet_b', height=1).grid(row=4, column=7, padx=10, pady=10)
    Label(root, text='treat_a', height=1).grid(row=6, column=5, padx=10, pady=10)
    Label(root, text='traet_b', height=1).grid(row=6, column=7, padx=10, pady=10)
    Label(root, text='treat_a', height=1).grid(row=8, column=5, padx=10, pady=10)
    Label(root, text='traet_b', height=1).grid(row=8, column=7, padx=10, pady=10)
    Label(root, text='treat_a', height=1).grid(row=10, column=5, padx=10, pady=10)
    Label(root, text='traet_b', height=1).grid(row=10, column=7, padx=10, pady=10)
    Label(root, text='treat_a', height=1).grid(row=12, column=5, padx=10, pady=10)
    Label(root, text='traet_b', height=1).grid(row=12, column=7, padx=10, pady=10)
    Label(root, text='treat_a', height=1).grid(row=14, column=5, padx=10, pady=10)
    Label(root, text='traet_b', height=1).grid(row=14, column=7, padx=10, pady=10)
    Label(root, textvariable=v1, height=1).grid(row=0, column=6, padx=10, pady=10)
    Label(root, textvariable=v2, height=1).grid(row=0, column=8, padx=10, pady=10)
    Label(root, textvariable=v3, height=1).grid(row=2, column=6, padx=10, pady=10)
    Label(root, textvariable=v4, height=1).grid(row=2, column=8, padx=10, pady=10)
    Label(root, textvariable=v5, height=1).grid(row=4, column=6, padx=10, pady=10)
    Label(root, textvariable=v6, height=1).grid(row=4, column=8, padx=10, pady=10)
    Label(root, textvariable=v7, height=1).grid(row=6, column=6, padx=10, pady=10)
    Label(root, textvariable=v8, height=1).grid(row=6, column=8, padx=10, pady=10)
    Label(root, textvariable=v9, height=1).grid(row=8, column=6, padx=10, pady=10)
    Label(root, textvariable=v10, height=1).grid(row=8, column=8, padx=10, pady=10)
    Label(root, textvariable=v11, height=1).grid(row=10, column=6, padx=10, pady=10)
    Label(root, textvariable=v12, height=1).grid(row=10, column=8, padx=10, pady=10)
    Label(root, textvariable=v13, height=1).grid(row=12, column=6, padx=10, pady=10)
    Label(root, textvariable=v14, height=1).grid(row=12, column=8, padx=10, pady=10)
    Label(root, textvariable=v15, height=1).grid(row=14, column=6, padx=10, pady=10)
    Label(root, textvariable=v16, height=1).grid(row=14, column=8, padx=10, pady=10)

    Button(root, text='add', height=1, command=add1).grid(row=0, column=4, padx=10, pady=10)
    Button(root, text='add', height=1, command=add2).grid(row=2, column=4, padx=10, pady=10)
    Button(root, text='add', height=1, command=add3).grid(row=4, column=4, padx=10, pady=10)
    Button(root, text='add', height=1, command=add4).grid(row=6, column=4, padx=10, pady=10)
    Button(root, text='add', height=1, command=add5).grid(row=8, column=4, padx=10, pady=10)
    Button(root, text='add', height=1, command=add6).grid(row=10, column=4, padx=10, pady=10)
    Button(root, text='add', height=1, command=add7).grid(row=12, column=4, padx=10, pady=10)
    Button(root, text='add', height=1, command=add8).grid(row=14, column=4, padx=10, pady=10)

    v1.set(randomset[0][0][0][0])
    v2.set(randomset[0][0][0][1])
    v3.set(randomset[0][0][1][0])
    v4.set(randomset[0][0][1][1])
    v5.set(randomset[0][1][0][0])
    v6.set(randomset[0][1][0][1])
    v7.set(randomset[0][1][1][0])
    v8.set(randomset[0][1][1][1])
    v9.set(randomset[1][0][0][0])
    v10.set(randomset[1][0][0][1])
    v11.set(randomset[1][0][1][0])
    v12.set(randomset[1][0][1][1])
    v13.set(randomset[1][1][0][0])
    v14.set(randomset[1][1][0][1])
    v15.set(randomset[1][1][1][0])
    v16.set(randomset[1][1][1][1])
    # Button(root, text='保存', height=1, command=save,).grid(row=1, column=6, padx=10, pady=10)

    # for j in range(1):
    #     randomset = {0: {0: {0: 0, 1: 0}, 1: {0: 0, 1: 0}}, 1: {0: {0: 0, 1: 0}, 1: {0: 0, 1: 0}}}
    #     gender = 0
    #     center = 0
    #     for i in range(100):
    #         gender = np.random.choice([0, 1],p=[0.6,0.4])
    #         center = np.random.choice([0, 1],p=[0.3,0.7])
    #         randomize(gender, center, randomset)
    #     print(json.dumps(randomset,indent=1))
    menu = Menu(root)

    fileMenu = Menu(menu, tearoff=0)
    fileMenu.add_command(label='新建', command=lambda: init(root))
    fileMenu.add_command(label='打开', command=lambda: load_pickle(root))
    fileMenu.add_command(label='保存', command=save_pickle)
    # fileMenu.add_command(label='导出至csv')
    menu.add_cascade(label='文件', menu=fileMenu)

    root.config(menu=menu)
    root.mainloop()


def save_pickle():
    r = Dataset([delta_1,delta_2,delta_3,delta_4],[level_1,level_2,level_3],randomset)
    filename = filedialog.asksaveasfilename()
    if filename != '':
        with open(filename, 'wb') as pkfile:
            pickle.dump(r, pkfile, 0)


def load_pickle(root):
    filename = filedialog.askopenfilename()
    # print(filename)
    if filename != '':
        with open(filename, 'rb') as pkfile:
            r = pickle.load(pkfile)
        global delta_1,delta_2,delta_3,delta_4,level_1,level_2,level_3, randomset
        delta_1 = r.getdelta()[0]
        delta_2 = r.getdelta()[1]
        delta_3 = r.getdelta()[2]
        delta_4 = r.getdelta()[3]
        level_1 = r.getlevel()[0]
        level_2 = r.getlevel()[1]
        level_3 = r.getlevel()[2]
        randomset = r.getrandom()
        root.destroy()
        random_window()
if __name__ == '__main__':
    root = Tk()
    root.geometry('500x400')
    menu = Menu(root)

    fileMenu = Menu(menu, tearoff=0)
    fileMenu.add_command(label='新建', command=lambda: init(root))
    fileMenu.add_command(label='打开', command=lambda: load_pickle(root))
    fileMenu.add_command(label='保存', command=save_pickle)
    # fileMenu.add_command(label='导出至csv')
    menu.add_cascade(label='文件', menu=fileMenu)

    root.config(menu=menu)
    root.mainloop()
