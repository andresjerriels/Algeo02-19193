from cosine_sim import cosine_sim

str1 = input("Masukkan keyword: ")

y1 = ""
y2 = ""
y3 = ""

c1 = cosine_sim(str1, y1)
c2 = cosine_sim(str1, y2)
c3 = cosine_sim(str1, y3)

print(c1, c2, c3)