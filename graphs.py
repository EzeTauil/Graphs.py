from tkinter.font import names
import matplotlib.pyplot as plt
sales = {
    "2018":10000,
    "2019":25000,
    "2020":17000,
    "2021":28000
}

names= list(sales.keys())
values = list(sales.values())

plt.barh(range(len(sales)),values,tick_label =names,color =["blue","red","teal","crimson"])
plt.grid(True)
plt.xticks(rotation=90)
plt.title("Ventas de productos (2018-2021)",loc="left",fontdict={"fontsize":14,"fontweight":"bold","color":"tab:green"})
plt.xlabel("Años",color="teal",size=120)
plt.ylabel("Cantidad",color = "teal", size = 12)

plt.show()