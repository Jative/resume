from tkinter import *
from tkinter import messagebox as mb
import sys
import os

Math = Tk()
Math['bg'] = "gray10"
Math.title("Математика")
Math.resizable(False, False)

def exit_program():
    sys.exit()

def Algebra_program():
    Math.destroy()
    Algebra = Tk()
    Algebra['bg'] = "gray10"
    Algebra.title("Алгебра")

    def back_program():
        Algebra.destroy()
        os.system("All_Math.py")
    
    def sqrt_in_sqrt_program():
        Algebra.destroy()
        sqrt_in_sqrt = Tk()
        sqrt_in_sqrt.title("Сложный корень")
        sqrt_in_sqrt['bg'] = "gray10"
        sqrt_in_sqrt.geometry("340x350")
        sqrt_in_sqrt.resizable(False, False)
        
        def calc_sqrt_in_sqrt():
            info_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "Сложный корень вида √(A ± √B)\nможет быть преобразован таким образом:", bg = "gray10", fg = "gray70")
            formula_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "√(A ± √B)  =", bg = "gray10", fg = "gray70")
            bigsqrt1_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "√(", font = 30, bg = "gray10", fg = "gray70")
            bigsqrt2_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = ") ± √(", font = 30, bg = "gray10", fg = "gray70")
            bigskobka1_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = ")", font = 30, bg = "gray10", fg = "gray70")
            verh1_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "A + √(A²-B)", bg = "gray10", fg = "gray70")
            palka1_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "----------------------------------------------------------------", font = "Consolas 1", bg = "gray10", fg = "gray70")
            niz1_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "2", bg = "gray10", fg = "gray70")
            verh2_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "A - √(A²-B)", bg = "gray10", fg = "gray70")
            palka2_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "----------------------------------------------------------------", font = "Consolas 1", bg = "gray10", fg = "gray70")
            niz2_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "2", bg = "gray10", fg = "gray70")
            txt2_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "Для твоего случая это:", bg = "gray10", fg = "gray70")
        
            A_sqrt_in_sqrt = ent1_sqrt_in_sqrt.get()
            znak_sqrt_in_sqrt = ent2_sqrt_in_sqrt.get()
            B_sqrt_in_sqrt = ent3_sqrt_in_sqrt.get()
        
            bigsqrt3_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "√(", font = 30, bg = "gray10", fg = "gray70")
            bigsqrt4_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = ") "+znak_sqrt_in_sqrt+" √(", font = 30, bg = "gray10", fg = "gray70")
            bigskobka2_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = ")", font = 30, bg = "gray10", fg = "gray70")
            ravno1_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "=", bg = "gray10", fg = "gray70")
            verh3_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = A_sqrt_in_sqrt+" + √("+A_sqrt_in_sqrt+"²-"+B_sqrt_in_sqrt+")", bg = "gray10", fg = "gray70")
            palka3_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "-------------------------------------------------------------------------------", font = "Consolas 1", bg = "gray10", fg = "gray70")
            niz3_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "2", bg = "gray10", fg = "gray70")
            verh4_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = A_sqrt_in_sqrt+" - √("+A_sqrt_in_sqrt+"²-"+B_sqrt_in_sqrt+")", bg = "gray10", fg = "gray70")
            palka4_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "-----------------------------------------------------------------------------", font = "Consolas 1", bg = "gray10", fg = "gray70")
            niz4_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "2", bg = "gray10", fg = "gray70")
        
            bigsqrt5_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "√(", font = 30, bg = "gray10", fg = "gray70")
            bigsqrt6_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = ") "+znak_sqrt_in_sqrt+" √(", font = 30, bg = "gray10", fg = "gray70")
            bigskobka3_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = ")", font = 30, bg = "gray10", fg = "gray70")
            ravno2_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "=", bg = "gray10", fg = "gray70")
            verh5_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = A_sqrt_in_sqrt+" + √("+str(int(A_sqrt_in_sqrt) ** 2 - int(B_sqrt_in_sqrt))+")", bg = "gray10", fg = "gray70")
            palka5_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "-----------------------------------------------------------------", font = "Consolas 1", bg = "gray10", fg = "gray70")
            niz5_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "2", bg = "gray10", fg = "gray70")
            verh6_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = A_sqrt_in_sqrt+" - √("+str(int(A_sqrt_in_sqrt) ** 2 - int(B_sqrt_in_sqrt))+")", bg = "gray10", fg = "gray70")
            palka6_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "-----------------------------------------------------------------", font = "Consolas 1", bg = "gray10", fg = "gray70")
            niz6_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "2", bg = "gray10", fg = "gray70")
        
            shitinsqrt1_sqrt_in_sqrt = str(int((int(A_sqrt_in_sqrt) + (int(A_sqrt_in_sqrt) ** 2 - int(B_sqrt_in_sqrt)) ** 0.5) / 2))
            shitinsqrt2_sqrt_in_sqrt = str(int((int(A_sqrt_in_sqrt) - (int(A_sqrt_in_sqrt) ** 2 - int(B_sqrt_in_sqrt)) ** 0.5) / 2))
        
            if (int(A_sqrt_in_sqrt) ** 2 - int(B_sqrt_in_sqrt)) ** 0.5 % 1 != 0:
                mb.showwarning("Внимание!","Скорее всего, что-то идёт не так\nСтоит проверить введённые значения\nБудет рассчитан примерный результат")
            a_sqrt_in_sqrt = str(int(shitinsqrt1_sqrt_in_sqrt) ** 0.5)
            b_sqrt_in_sqrt = str(int(shitinsqrt2_sqrt_in_sqrt) ** 0.5)
            if float(a_sqrt_in_sqrt) % 1 != 0:
                a1_sqrt_in_sqrt = "√("+shitinsqrt1_sqrt_in_sqrt+")"
            if float(a_sqrt_in_sqrt) % 1 == 0:
                a1_sqrt_in_sqrt = str(int(float(a_sqrt_in_sqrt)))   
            if float(b_sqrt_in_sqrt) % 1 != 0:
                b1_sqrt_in_sqrt = "√("+shitinsqrt2_sqrt_in_sqrt+")"
            if float(b_sqrt_in_sqrt) % 1 == 0:
                b1_sqrt_in_sqrt = str(int(float(b_sqrt_in_sqrt)))
            if znak_sqrt_in_sqrt == "+":    
                resultint_sqrt_in_sqrt = a1_sqrt_in_sqrt+" + "+b1_sqrt_in_sqrt
                if float(a_sqrt_in_sqrt) % 1 == 0 and float(b_sqrt_in_sqrt) % 1 == 0:
                    resultint_sqrt_in_sqrt = str(int(float(a_sqrt_in_sqrt) + float(b_sqrt_in_sqrt)))
            if znak_sqrt_in_sqrt == "-":    
                resultint_sqrt_in_sqrt = a1_sqrt_in_sqrt+" - "+b1_sqrt_in_sqrt
                if float(a_sqrt_in_sqrt) % 1 == 0 and float(b_sqrt_in_sqrt) % 1 == 0:
                    resultint_sqrt_in_sqrt = str(int(float(a_sqrt_in_sqrt) - float(b_sqrt_in_sqrt)))
                    
            preresult_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "√("+shitinsqrt1_sqrt_in_sqrt+") "+znak_sqrt_in_sqrt+" √("+shitinsqrt2_sqrt_in_sqrt+") = "+a1_sqrt_in_sqrt+" "+znak_sqrt_in_sqrt+" "+b1_sqrt_in_sqrt+"  =", bg = "gray10", fg = "gray70")
            result_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = resultint_sqrt_in_sqrt, bg = "gray10", fg = "red")
            if A_sqrt_in_sqrt == "" or B_sqrt_in_sqrt == "":
                mb.showerror("Ошибка!", "Укажи числа!")
                return
            if znak_sqrt_in_sqrt != "-" and znak_sqrt_in_sqrt != "+":
                mb.showerror("Ошибка!", "Указан неверный знак!")
                return
            mtxt1_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "√("+A_sqrt_in_sqrt+" "+znak_sqrt_in_sqrt+" √"+B_sqrt_in_sqrt+") =", bg = "gray10", fg = "gray70")
            
            info_sqrt_in_sqrt.place(x=50, y=90)
            #Записываю формулу(пипец, девочки)
            formula_sqrt_in_sqrt.place(x=36, y=134)
            bigsqrt1_sqrt_in_sqrt.place(x=106, y=132)
            verh1_sqrt_in_sqrt.place(x=124, y=125)
            palka1_sqrt_in_sqrt.place(x=121, y=141)
            niz1_sqrt_in_sqrt.place(x=151, y=146)
            bigsqrt2_sqrt_in_sqrt.place(x=188, y=132)
            verh2_sqrt_in_sqrt.place(x=228, y=125)
            palka2_sqrt_in_sqrt.place(x=225, y=141)
            niz2_sqrt_in_sqrt.place(x=255, y=146)
            bigskobka1_sqrt_in_sqrt.place(x=291, y=132)
            #Остальное
            txt2_sqrt_in_sqrt.place(x=105, y=162)
            #*плАчу*
            mtxt1_sqrt_in_sqrt.place(x=15, y=192)
            bigsqrt3_sqrt_in_sqrt.place(x=95, y=189)
            verh3_sqrt_in_sqrt.place(x=113, y=181)
            palka3_sqrt_in_sqrt.place(x=110, y=198)
            niz3_sqrt_in_sqrt.place(x=148, y=203)
            bigsqrt4_sqrt_in_sqrt.place(x=191, y=189)
            verh4_sqrt_in_sqrt.place(x=231, y=182)
            palka4_sqrt_in_sqrt.place(x=228, y=198)
            niz4_sqrt_in_sqrt.place(x=266, y=203)
            bigskobka2_sqrt_in_sqrt.place(x=306, y=189)
            ravno1_sqrt_in_sqrt.place(x=320, y=189)
            #*рыдаю*
            bigsqrt5_sqrt_in_sqrt.place(x=70, y=232)
            verh5_sqrt_in_sqrt.place(x=88, y=223)
            palka5_sqrt_in_sqrt.place(x=85, y=240)
            niz5_sqrt_in_sqrt.place(x=115, y=245)
            bigsqrt6_sqrt_in_sqrt.place(x=151, y=231)
            verh6_sqrt_in_sqrt.place(x=191, y=223)
            palka6_sqrt_in_sqrt.place(x=188, y=240)
            niz6_sqrt_in_sqrt.place(x=218, y=245)
            bigskobka3_sqrt_in_sqrt.place(x=253, y=231)
            ravno2_sqrt_in_sqrt.place(x=267, y=231)
            #Финалка
            preresult_sqrt_in_sqrt.place(x=100, y=271)
            result_sqrt_in_sqrt.place(x=140, y=301)
        txt_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "Введи известные данные:", bg = "gray10", fg = "gray70")
        
        sqrt1_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "√(", bg = "gray10", fg = "gray70", font = 15)
        sqrt2_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = "√", bg = "gray10", fg = "gray70", font = 15)
        skobka_sqrt_in_sqrt = Label(sqrt_in_sqrt, text = ")", bg = "gray10", fg = "gray70", font = 15)
        ent1_sqrt_in_sqrt = Entry(sqrt_in_sqrt, width = 2, borderwidth = 2, bg = "gray60", fg = "gray10")
        ent2_sqrt_in_sqrt = Entry(sqrt_in_sqrt, width = 1, borderwidth = 2, bg = "gray60", fg = "gray10")
        ent3_sqrt_in_sqrt = Entry(sqrt_in_sqrt, width = 2, borderwidth = 2, bg = "gray60", fg = "gray10")
        
        ent1_sqrt_in_sqrt.insert(0, "8")
        ent2_sqrt_in_sqrt.insert(0, "+")
        ent3_sqrt_in_sqrt.insert(0, "28")
        
        btn_sqrt_in_sqrt = Button(sqrt_in_sqrt, text = "Решить!", width = 15, command = calc_sqrt_in_sqrt, borderwidth = 4, bg = "gray60", fg = "gray10")
        
        txt_sqrt_in_sqrt.place(x=100, y=5)
        sqrt1_sqrt_in_sqrt.place(x=120, y=30)
        ent1_sqrt_in_sqrt.place(x=140, y=30)
        ent2_sqrt_in_sqrt.place(x=160, y=30)
        sqrt2_sqrt_in_sqrt.place(x=170, y=30)
        ent3_sqrt_in_sqrt.place(x=185, y=30)
        skobka_sqrt_in_sqrt.place(x=202, y=30)
        btn_sqrt_in_sqrt.place(x=113, y=60)

        sqrt_in_sqrt.mainloop()
    
    btn_sqrt_in_sqrt = Button(Algebra, text = "Сложный корень", command = sqrt_in_sqrt_program, borderwidth = 4, bg = "gray60", fg = "gray10", font = "Consolas", width=40)
    btn_back_program = Button(Algebra, text = "Назад", command = back_program, borderwidth = 4, bg = "gray60", fg = "gray10", font = "Consolas", width=40)
    
    btn_sqrt_in_sqrt.grid(row=0, column=0, padx=5, pady=5)
    btn_back_program.grid(row=1, column=0, padx=5, pady=5)

    Algebra.mainloop()

def Geometry_program():
    Math.destroy()
    Geometry = Tk()
    Geometry['bg'] = "gray10"
    Geometry.title("Геометрия")

    def back_program():
        Geometry.destroy()
        os.system("All_Math.py")

    def cos_pl_program():
        Geometry.destroy()
        cos_pl = Tk()
        cos_pl.title("Поиск косинуса угла между плоскостями")
        cos_pl.geometry("460x500")
        cos_pl.resizable(False, False)
        cos_pl['bg'] = "gray10"

        def calc():
            info = Label(cos_pl, text = "Если заданы уравнения плоскостей вида\nA₁x + B₁y + C₁z + D₁ = 0 и A₂x + B₂y + C₂z + D₂ = 0,\nто угол между плоскостями можно найти,\nиспользуя следующую формулу:", bg = "gray10", fg = "gray70")
            cos_alpha = Label(cos_pl, text = "                                          cos α =", bg = "gray10", fg = "gray70")
            formula_1 = Label(cos_pl, text = "|A₁·A₂ + B₁·B₂ + C₁·C₂|", bg = "gray10", fg = "gray70")
            formula_2 = Label(cos_pl, text = "√(A₁² + B₁² + C₁²)·√(A₂² + B₂² + C₂²)", bg = "gray10", fg = "gray70")
            s1 = fentry.get()
            s2 = sentry.get()
            
            if s1[0] == "-":
            	a=int(s1[1]); b=int(s1[4]); c=int(s1[7])
            	a = -a
            	a = "(" + str(a) + ")"
            	z1 = s1[3]; z2 = s1[6]
            if s1[0] != "-":	
                a = int(s1[0]); b=int(s1[3]); c=int(s1[6])
                z1 = s1[2]; z2 = s1[5]
            if z1 == "-":
                b = -b
                b = "(" + str(b) + ")"
            if z2 == "-":
                c = -c
                c = "(" + str(c) + ")"        	     	  	

            if s2[0] == "-":
                d=int(s2[1]); e=int(s2[4]); f=int(s2[7])
                d = -d
                d = "(" + str(d) + ")"
                z3 = s2[3]; z4 = s2[6]  	
            if s2[0] != "-":	
                d=int(s2[0]); e=int(s2[3]); f=int(s2[6])
                z3 = s2[2]; z4 = s2[5]
            if z3 == "-":
                e = -e
                e = "(" + str(e) + ")"
            if z4 == "-":
                f = -f
                f = "(" + str(f) + ")"
                

            if s1[0] == "-":
                a1=int(s1[1]); b1=int(s1[4]); c1=int(s1[7])
                a1 = -a1
                z1 = s1[3]; z2 = s1[6]
            if s1[0] != "-":
                a1 = int(s1[0]); b1=int(s1[3]); c1=int(s1[6])
                z1 = s1[2]; z2 = s1[5]
            if z1 == "-":
                b1 = -b1
            if z2 == "-":
                c1 = -c1       	     	  	

            if s2[0] == "-":
                d1=int(s2[1]); e1=int(s2[4]); f1=int(s2[7])
                d1 = -d1
                z3 = s2[3]; z4 = s2[6]  	
            if s2[0] != "-":	
                d1=int(s2[0]); e1=int(s2[3]); f1=int(s2[6])
                z3 = s2[2]; z4 = s2[5]
            if z3 == "-":
                e1 = -e1
            if z4 == "-":
                f1 = -f1

            r = a1*d1 + b1*e1 + c1*f1
            r1 = a1**2 + b1**2 + c1**2
            r2 = d1**2 + e1**2 + f1**2
            if r < 0:
                m = -r
            elif r >= 0:
                m = r	
            m1 = (r1*r2)**0.5
            if m1%1 == 0:
                m1 = int(m1)
            elif m1%1 != 0:
                m1 = "√("+str(int(r1*r2))+")"
            a = str(a);b = str(b);c = str(c);d = str(d);e = str(e);f = str(f)
            
            ravno1 = Label(cos_pl, text = "=                                                           ", bg = "gray10", fg = "gray70")
            ravno2 = Label(cos_pl, text = "=                                                           ", bg = "gray10", fg = "gray70")
            s1_1 = Label(cos_pl, text = "Для твоего случая это:\n\n|"+a+"·"+d+"+"+b+"·"+e+"+"+c+"·"+f+"|", bg = "gray10", fg = "gray70")
            s1_2 = Label(cos_pl, text = "√("+a+"² + "+b+"² + "+c+"²)·√("+d+"² + "+e+"² + "+f+"²)", bg = "gray10", fg = "gray70")
            s2_1 = Label(cos_pl, text = "\n|"+str(r)+"|", bg = "gray10", fg = "gray70")
            s2_2 = Label(cos_pl, text = "√("+str(r1)+")·√("+str(r2)+")", bg = "gray10", fg = "gray70")
            s3_1 = Label(cos_pl, text = "\n" + str(m), bg = "gray10", fg = "red")
            s3_2 = Label(cos_pl, text = str(m1), bg = "gray10", fg = "red", width= 10)
            line = Label(cos_pl, text = "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", bg = "gray10", fg = "gray70", font = "Consolas 1")
            line_1 = Label(cos_pl, text = "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", bg = "gray10", fg = "gray70", font = "Consolas 1")
            line_2 = Label(cos_pl, text = "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", bg = "gray10", fg = "gray70", font = "Consolas 1")
            line_3 = Label(cos_pl, text = "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", bg = "gray10", fg = "gray70", font = "Consolas 1")

            info.grid(row=4, column=0, columnspan=2, pady=5)
            cos_alpha.grid(row = 5, column = 0, rowspan=3)
            formula_1.grid(row=5, column=1)
            line.grid(row=6, column=1)
            formula_2.grid(row=7, column=1)
            s1_1.grid(row=8, column=0)
            line_1.grid(row=9, column=0)
            s1_2.grid(row=10, column=0)
            ravno1.grid(row=9, column=1)
            s2_1.grid(row=11, column=0)
            line_2.grid(row=12, column=0)
            s2_2.grid(row=13, column=0)
            ravno2.grid(row=12, column=1)
            s3_1.grid(row=14, column=0)
            line_3.grid(row=15, column=0)
            s3_2.grid(row=16, column=0)

        ftxt = Label(cos_pl, text = "Введи уравнения плоскостей:\n(числа не больше 9 и не меньше -9)", bg = "gray10", fg = "gray70")
        fentry = Entry(cos_pl, width = 30, borderwidth = 4, bg = "gray60", fg = "gray10")
        sentry = Entry(cos_pl, width = 30, borderwidth = 4, bg = "gray60", fg = "gray10")
        btn_cos_pl = Button(cos_pl, text = "Найти косинус!", width = 20, command = calc, borderwidth = 4, bg = "gray60", fg = "gray10")
        
        fentry.insert(0, "1x+1y+1z+1=0")
        sentry.insert(0, "1x+1y+1z+2=0")
        
        ftxt.grid(row=0, column=0, columnspan=2, pady=5)
        fentry.grid(row=1, column=0, padx=20, pady=5)
        sentry.grid(row=1, column=1, padx=20, pady=5)
        btn_cos_pl.grid(row=2, column=0, columnspan=2, pady=5)
        
        cos_pl.mainloop()
    
    def pythagoras_program():
        Geometry.destroy()
        pythagoras = Tk()
        pythagoras.title("Стороны прямоугольного треугольника")
        pythagoras.geometry("405x300")
        pythagoras.resizable(False, False)
        pythagoras['bg'] = "gray10"
        
        def calc_pythagoras():
            A_pythagoras = entry1_pythagoras.get()
            B_pythagoras = entry2_pythagoras.get()
            C_pythagoras = entry3_pythagoras.get()

            if A_pythagoras == B_pythagoras == "" or B_pythagoras == C_pythagoras == "" or A_pythagoras == C_pythagoras == "":
                mb.showerror("Извините!", "Этих данных недостаточно!")
            if A_pythagoras != "" and B_pythagoras != "" and C_pythagoras != "":
                mb.showerror("Молодец!", "Ну и что мне с этими данными теперь делать?\nМой программист не учил меня осуществлять проверку.")
        
        
            if A_pythagoras == "":
                C_in_square_pythagoras = str(int(C_pythagoras) ** 2)
                B_in_square_pythagoras = str(int(B_pythagoras) ** 2)
                sqrt_shit_pythagoras = str(int(C_in_square_pythagoras) - int(B_in_square_pythagoras))
                if int(sqrt_shit_pythagoras) < 0:
                    mb.showerror("Ошибка!", "Невозможно найти корень из отрицательного числа!")
                if int(sqrt_shit_pythagoras) >=0:
                    final_dibil = str(int(float(sqrt_shit_pythagoras) ** 0.5))
                    if (int(sqrt_shit_pythagoras)**0.5)%1 > 0:
                        final_dibil = "√(" + str(int(sqrt_shit_pythagoras)) + ")"
                
                ftxt_pythagoras = Label(pythagoras, text = "a² = c² - b²  =>", bg = "gray10", fg = "gray70")
                ftxt_1_pythagoras = Label(pythagoras, text = "a = √(c² - b²)  =>", bg = "gray10", fg = "gray70")
                mtxt_pythagoras = Label(pythagoras, text = "a = √("+C_pythagoras+"² - "+B_pythagoras+"²) = √("+C_in_square_pythagoras+" - "+B_in_square_pythagoras+") = √("+sqrt_shit_pythagoras+")  =                        ", bg = "gray10", fg = "gray70")        
                result = Label(pythagoras, text = final_dibil+"                      ", bg = "gray10", fg = "red")
        
            if B_pythagoras == "":
                C_in_square_pythagoras = str(int(C_pythagoras) ** 2)
                A_in_square_pythagoras = str(int(A_pythagoras) ** 2)
                sqrt_shit_pythagoras = str(int(C_in_square_pythagoras) - int(A_in_square_pythagoras))
                if int(sqrt_shit_pythagoras) < 0:
                    mb.showerror("Ошибка!", "Невозможно найти корень из отрицательного числа!")
                if int(sqrt_shit_pythagoras) >=0:
                    final_dibil = str(int(float(sqrt_shit_pythagoras) ** 0.5))
                    if (int(sqrt_shit_pythagoras)**0.5)%1 > 0:
                        final_dibil = "√(" + str(int(sqrt_shit_pythagoras)) + ")"
                
                ftxt_pythagoras = Label(pythagoras, text = "b² = c² - a²  =>", bg = "gray10", fg = "gray70")
                ftxt_1_pythagoras = Label(pythagoras, text = "b = √(c² - a²)  =>", bg = "gray10", fg = "gray70")
                mtxt_pythagoras = Label(pythagoras, text = "b = √("+C_pythagoras+"² - "+A_pythagoras+"²) = √("+C_in_square_pythagoras+" - "+A_in_square_pythagoras+") = √("+sqrt_shit_pythagoras+")  =                        ", bg = "gray10", fg = "gray70")        
                result = Label(pythagoras, text = final_dibil+"                      ", bg = "gray10", fg = "red")
        
            if C_pythagoras == "":
                A_in_square_pythagoras = str(int(A_pythagoras) ** 2)
                B_in_square_pythagoras = str(int(B_pythagoras) ** 2)
                sqrt_shit_pythagoras = str(int(A_in_square_pythagoras) + int(B_in_square_pythagoras))
                if int(sqrt_shit_pythagoras) < 0:
                    mb.showerror("Ошибка!", "Невозможно найти корень из отрицательного числа!")
                if int(sqrt_shit_pythagoras) >=0:
                    final_dibil = str(int(float(sqrt_shit_pythagoras) ** 0.5))
                    if (int(sqrt_shit_pythagoras)**0.5)%1 > 0:
                        final_dibil = "√(" + str(int(sqrt_shit_pythagoras)) + ")"
                
                ftxt_pythagoras = Label(pythagoras, text = "c² = a² + b²  =>", bg = "gray10", fg = "gray70")
                ftxt_1_pythagoras = Label(pythagoras, text = "c = √(a² + b²)  =>", bg = "gray10", fg = "gray70")
                mtxt_pythagoras = Label(pythagoras, text = "c = √("+A_pythagoras+"² + "+B_pythagoras+"²) = √("+A_in_square_pythagoras+" + "+B_in_square_pythagoras+") = √("+sqrt_shit_pythagoras+")  =                        ", bg = "gray10", fg = "gray70")        
                result = Label(pythagoras, text = final_dibil+"                      ", bg = "gray10", fg = "red")
        
            ftxt_pythagoras.place(x=165, y=175)
            ftxt_1_pythagoras.place(x=160, y=200)
            mtxt_pythagoras.place(x=90, y=225)
            result.place(x=185, y=250)
        
        txt_pythagoras = Label(pythagoras, text = "Введи известные данные:", bg = "gray10", fg = "gray70")
        txt2_pythagoras = Label(pythagoras, text = "Для твоего случая это:", bg = "gray10", fg = "gray70")
        info_pythagoras = Label(pythagoras, text = "В прямоугольном треугольнике, длины катетов которого равны a и b,\nа длина гипотенузы — c, по т. Пифагора выполнено соотношение:\na²+b²=c²", bg = "gray10", fg = "gray70")
        A_txt_pythagoras = Label(pythagoras, text = "a =", bg = "gray10", fg = "gray70")
        B_txt_pythagoras = Label(pythagoras, text = "b =", bg = "gray10", fg = "gray70")
        C_txt_pythagoras = Label(pythagoras, text = "c =", bg = "gray10", fg = "gray70")
        entry1_pythagoras = Entry(pythagoras, width = 6, borderwidth = 4, bg = "gray60", fg = "gray10")
        entry2_pythagoras = Entry(pythagoras, width = 6, borderwidth = 4, bg = "gray60", fg = "gray10")
        entry3_pythagoras = Entry(pythagoras, width = 6, borderwidth = 4, bg = "gray60", fg = "gray10")
        btn_pythagoras = Button(pythagoras, text = "Найти!", command = calc_pythagoras, borderwidth = 4, bg = "gray60", fg = "gray10")
        
        info_pythagoras.place(x=5, y=5)
        txt_pythagoras.place(x=130, y=50)
        A_txt_pythagoras.place(x=30, y=75)
        entry1_pythagoras.place(x=60, y=75)
        B_txt_pythagoras.place(x=160, y=75)
        entry2_pythagoras.place(x=190, y=75)
        C_txt_pythagoras.place(x=290, y=75)
        entry3_pythagoras.place(x=320, y=75)
        btn_pythagoras.place(x=175, y=110)
        txt2_pythagoras.place(x=135, y=145)
        
        
        pythagoras.mainloop()

    btn_cos_pl_program = Button(Geometry, text = "Косинус угла между плоскостями", command = cos_pl_program, borderwidth = 4, bg = "gray60", fg = "gray10", font = "Consolas", width=40)
    btn_pythagoras_program = Button(Geometry, text = "Стороны прямоугольного треугольника", command = pythagoras_program, borderwidth = 4, bg = "gray60", fg = "gray10", font = "Consolas", width=40)
    btn_back_program = Button(Geometry, text = "Назад", command = back_program, borderwidth = 4, bg = "gray60", fg = "gray10", font = "Consolas", width=40)

    btn_cos_pl_program.grid(row=0, column=0, padx=5, pady=5)
    btn_pythagoras_program.grid(row=1, column=0, padx=5, pady=5)
    btn_back_program.grid(row=2, column=0, padx=5, pady=5)

    Geometry.mainloop()    

btn_Algebra_program = Button(Math, text = "Алгебра", command = Algebra_program, borderwidth = 4, bg = "gray60", fg = "gray10", font = "Consolas", width=20, height=10)
btn_Geometry_program = Button(Math, text = "Геометрия", command = Geometry_program, borderwidth = 4, bg = "gray60", fg = "gray10", font = "Consolas", width=20, height=10)
btn_exit_program = Button(Math, text = "Выход", command = exit_program, borderwidth = 4, bg = "gray60", fg = "gray10", font = "Consolas", width=43, height=2)

btn_Algebra_program.grid(row=0, column=0, padx=5, pady=5)
btn_Geometry_program.grid(row=0, column=1, padx=5, pady=5)
btn_exit_program.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

Math.mainloop()
