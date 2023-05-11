
# # Version 1-All differences


students = {
    'Minəxanım Hacımuradova':[0, 7, 5, 6, 4, 4],
    'Lala Taghiyeva':[2, 5, 3, 7, 1, 3],
    'Yusif Ağasalamlı':[3, 4, 2, 3, 2, 2],
    'Həbibə Məmmədli':[3, 6, 2, 3, 2, 7],
    'Niyyət Rzayev':[3, 6, 4, 5, 6, 4],
    'Adil Rəhimov':[4, 5, 4, 3, 2, 5],
    'Riyad Əhmədov':[4, 5, 5, 4, 4, 6],
    'Ləman Rəhimli':[4, 6, 3, 5, 4, 4],
    'Riyad Əbdürəhimov':[4, 6, 4, 5, 7, 6],
    'İlyas Abbasov':[4, 6, 5, 6, 3, 3],
    'Lalə Məmmədli':[4, 8, 6, 6, 4, 2],
    'Anar Əhmədov':[5, 7, 5, 6, 6, 3],
    'Mahmizər Həsənova':[6, 4, 3, 7, 5, 4],
    'Mədinə Abdulsəmədova':[6, 7, 5, 4, 6, 3]
}


def ikitalebekiyasla( tv1, tv2 ):
    fark = 0
    for i in range(6):
        fark += abs(tv1[i] - tv2[i])
    return fark
distances={}
for name1,list1 in students.items():
    for name2,list2 in students.items():
        if name1!=name2:
            distance=ikitalebekiyasla(list1,list2)
            distances[(name1,name2)]=distance
            
for (name1,name2),distance in distances.items():
    print(f"{name1}"+"-"+f"{name2}:{distance}")


# # Version 2- Minimum differences 

# In[80]:


students = {
   'Minəxanım Hacımuradova':[0, 7, 5, 6, 4, 4],
   'Lala Taghiyeva':[2, 5, 3, 7, 1, 3],
   'Yusif Ağasalamlı':[3, 4, 2, 3, 2, 2],
   'Həbibə Məmmədli':[3, 6, 2, 3, 2, 7],
   'Niyyət Rzayev':[3, 6, 4, 5, 6, 4],
   'Adil Rəhimov':[4, 5, 4, 3, 2, 5],
   'Riyad Əhmədov':[4, 5, 5, 4, 4, 6],
   'Ləman Rəhimli':[4, 6, 3, 5, 4, 4],
   'Riyad Əbdürəhimov':[4, 6, 4, 5, 7, 6],
   'İlyas Abbasov':[4, 6, 5, 6, 3, 3],
   'Lalə Məmmədli':[4, 8, 6, 6, 4, 2],
   'Anar Əhmədov':[5, 7, 5, 6, 6, 3],
   'Mahmizər Həsənova':[6, 4, 3, 7, 5, 4],
   'Mədinə Abdulsəmədova':[6, 7, 5, 4, 6, 3]
}

def ikitalebekiyasla(tv1, tv2):
   fark = 0
   for i in range(6):
       fark += abs(tv1[i] - tv2[i])
   return fark

for name1, list1 in students.items():
   min_dist = float('inf')
   min_student = ''
   for name2, list2 in students.items():
       if name1 != name2:
           distance = ikitalebekiyasla(list1, list2)
           if distance < min_dist:
               min_dist = distance
               min_student = name2
   print(f"{name1}  similar  with student {min_student}{min_dist}")



# In[40]:




