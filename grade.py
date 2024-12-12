pro = int(input('enter project marks '))
inte = int(input('enter internal marks '))
ext = int(input('enter external marks '))
if (pro > 50 and inte > 50 and ext > 50):
   total = ((70 / 100) * pro + (10 / 100) * inte + (20 / 100) * ext)
   print(f'total:{total}')
   if total > 90:
       print('A grade')
   elif total > 80:
       print('B grade')
   else:
       print('C grade')
else:
   if pro < 50:
       print('failed in project')
   if inte < 50:
       print('failed in internal')
   if ext < 50:
       print('failed in external'