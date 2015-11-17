import random
total_list=['uninfected']*900 +['LTBI']*90 +['TB']*10
year=0
while year!=20:
    print(total_list)
    print( [total_list.count('uninfected'), total_list.count( 'LTBI'),total_list.count('TB')])
    for i in range(len(total_list)):
        if total_list[i]=='uninfected':
            if int(random.random()*100)==1:
                total_list[i]='LTBI'
        elif total_list[i]=='LTBI':
            if int(random.random()*100)==1:
                total_list[i]='TB'
        else:
            total_list[i]='LTBI'
    year=year+1
