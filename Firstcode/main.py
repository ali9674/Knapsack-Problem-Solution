import math
import numpy as np



def simulatedAnnealing(weights,values,maxCapacity,initial_temperature,cooling_rate):
   try:

       current_solution = np.random.randint(0,2,len(weights)) # 0 ile 1 arası len(weight) kadar değer üret
       current_cost = (current_solution * values ) # mevcut çözümün değerleriyle birlikte çarpma

       temperature = initial_temperature # başlangıc sıcaklıgı ayarlama
        # iteration starts

       while temperature >30:
           flip_index = np.random.randint(len(current_solution)) # mevcut çözümden rastgele index seçme
           neighbour_solution = current_solution #bir başka çözüm için önceki çözümü değişkene yükle( veriyi işlemek için)
           neighbour_solution[flip_index] =  1- neighbour_solution[flip_index]  #  flip_indexte seçtiğim elemanın tersini alıyorum 1->0  0 ->1
           neighbour_cost = (neighbour_solution * values) #rasrgele aldıgımız komşu çözümü değerler ile çarpıyoruz eleman elemana

           if (len(current_cost) != len(neighbour_cost)): # mevcut çözüm eleman sayısı  komşu çözümden  eşit mi !
               continue

               # np.random.rand() 0.35499503777073527 bu tarrz sayılar döndürür 0 ile 1 arasında onun kontrolu yapılıyor burada VVVV
               #sum()  toplam value yi döndürüyor                                               vv (komşu total value-current total value)/100
           if ( (sum(neighbour_cost)> sum(current_cost) ) or (np.random.rand() < math.exp( ( sum(neighbour_cost)-sum(current_cost))/temperature))):
               current_solution = neighbour_solution # eğer komşu çözümün total valuesi  currentden büyükse  currente komşuyu ata !
               current_cost = neighbour_cost #mevcut maaliyeti komşu maaliyet ile değiştir


           temperature = temperature * cooling_rate #sıcaklık değişimi              # end of the while loop

       return (current_solution,current_cost) #        solution = currentSolution; totalValue = currentCost olarak return edildi



   except Exception as  e:     # hata varsa fırlat !!
       print('Error in simulatedAnnealing:')
       print(e)




n=30 # the  capacity of bag

# all objects vvvv
weights = np.array([4, 2, 5, 8, 3, 7, 9, 6, 1, 10, 5, 3, 8, 2, 7, 4, 6, 9, 2, 1,6, 3, 8, 4, 7, 2, 9, 5, 10, 1])

values = np.array([7, 3, 10, 6, 2, 8, 12, 9, 1, 15, 8, 4, 11, 3, 10, 6, 9, 13, 3, 2, 11, 5, 12, 7, 10, 3, 14, 8, 16, 1])


max_capacity =sum(weights)/2

print("'Generated Data:  ")
print("Object   | Weight    | Value ")
for i in range(n):
   if i<9:
    print(f"{i+1}        |      {weights[i]}    |      {values[i]}")
   else:
       print(f"{i + 1}       |      {weights[i]}    |      {values[i]}")
#-----------------------------------------------------------------------------

initial_temperature = 100
cooling_rate = 0.9
#print("'Running simulatedAnnealing...")

solution,totalvalue = simulatedAnnealing(weights,values,max_capacity,100,0.95)
print("simulatedAnnealing completed successfully.")

print(" ")
print("Final Solution: ",end=" ")
print('Object   |    In Knapsack')
for i in range(n):
    if i<9:
      print(f"{i+1}        |     {solution[i]}")
    else :
        print(f"{i + 1}       |     {solution[i]}")

print(f"Total Value : { int(sum(totalvalue))}")










