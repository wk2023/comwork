
user_0={
    
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
    }
'''
print(user_0['username'])
for key,value in user_0.items():
    print('\nkey: '+key)
    print('value: '+value)
   

for key in user_0:
    print(key)
   # print(value)
    
users=['erermi01','enrico01','fermi01']
for user in users:
    print(user)
 
alien_0={'color':'green','point':5}
alien_1={'color':'yellow','point':10}
alien_2={'color':'red','point':15}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
    '''
aliens=[]
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print('   ,,,,,,')
print('total number of aliens:'+str(len(aliens)))

    
