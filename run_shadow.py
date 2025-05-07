# !/usr/bin/env -S python3 -B

from time import time
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr

tk = TkDrawer()
try:
    for name in ["king", "ccc", "cube", "box"]:
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        polyedr = Polyedr(f"data/{name}.geom")
        try:
            special_area = polyedr.total_area()
            print(f"Сумма площадей граней с \"особенной\" вершиной x > -2:"
                  f" {special_area}")
        except Exception as f:
            print(f"Не удалось вычислить площадь: {f}")

        polyedr.draw(tk)
        input("Hit 'Return' to continue -> ")

except Exception as f:
    print(f"\nОшибка: {f}")
finally:
    tk.close()
