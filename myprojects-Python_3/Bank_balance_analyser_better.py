#!/usr/bin/env python
# coding: utf-8

# In[84]:


import os.path
import pandas


# In[85]:


#file_path = r'C:\Users\Arpan Ghosh\Desktop\baba.xlsx'
file_path = input("Enter the path of .xlsx excel file : ")
start_date = input("Enter the start date in YYYY-MM-DD format [Default first Entry] : ")
end_date = input("Enter the end date in YYYY-MM-DD format [Default end Entry] : ")
choice = input('Group by what? [D : Date / M : Month / W : Week / Y : Year] : ')
row_foot = input("Skip row and footer count seperated by space [ default 19 2 ] : ")
if row_foot == '':
    row_foot = '19 2'
skip_r = int(row_foot.split()[0])
skip_f = int(row_foot.split()[1])
data = pandas.read_excel(file_path,skiprows=skip_r,skipfooter=skip_f)
try:
    data['Debit'] = data['        Debit']
except KeyError as e:
    print(e)
data['Credit'] = data['Credit'].apply(lambda x: 0 if x == ' ' else x)
data['Debit'] = data['Debit'].apply(lambda x: 0 if x == ' ' else x)
data.sort_values("Value Date",ascending = True, inplace = True) 
data.reset_index()
if start_date == '':
    start_date = str(data['Value Date'].min().date())
if end_date == '':
    end_date = str(data['Value Date'].max().date())


# In[86]:


data['year_month_date'] = data['Value Date'].dt.to_period("D")
data['year_month'] = data['Value Date'].dt.to_period("M")
data['year'] = data['Value Date'].dt.to_period("Y")
data['week'] = data['Value Date'].dt.year.apply(str)+'_'+data['Value Date'].dt.week.apply(str)
#data['year_month_1'] = data['Value Date'].dt.month_name(locale = 'English') 



# In[87]:


condition_1 = data['year_month_date']>=pandas.Period(start_date,'D')
condition_2 = data['year_month_date']<=pandas.Period(end_date,'D')
data = data[condition_1 & condition_2]


# In[88]:


if choice == 'W':
    data_gb = data.groupby('week')
elif choice == 'M':
    data_gb = data.groupby('year_month')
elif choice == 'Y':
    data_gb = data.groupby('year')
elif choice == 'D':
    data_gb = data.groupby('year_month_date')
else:
    print("Wrong Choice !")
    exit()


# In[143]:


credit,debit,key_list = [],[],[]
Total_C = 0
Total_D = 0
count = 0
for key,df in data_gb:
    C = sum(df['Credit'].apply(lambda x: 0 if (x == ' ') else x).tolist())
    D = sum(df['Debit'].apply(lambda x: 0 if (x == ' ') else x).tolist())
    Total_C += C
    Total_D += D
    count += 1
    credit.append(C)
    debit.append(D)
    key_list.append(key)
summary = pandas.DataFrame({'key':key_list,'credit':credit,'debit':debit})
#summary.year_month = summary['key'].apply(pandas.Period.to_timestamp)
if choice == 'W':
    summary['key_year'] = summary['key']
    summary['key_week'] = summary['key']
    summary['key_year'] = summary['key_year'].apply(lambda x : int(x.split('_')[0]))
    summary.key_year = summary.key_year.astype(int)
    summary['key_week'] = summary['key_week'].apply(lambda x : int(x.split('_')[1]))
    summary.key_week = summary.key_week.astype(int)
    summary = summary.sort_values(['key_year','key_week'])
    summary.drop(columns=['key_week', 'key_year'])
else:
    summary = summary.sort_values('key',ascending = False)

if choice == 'W':
    summary['key_'] = summary['key']
elif choice == 'M':
    summary['key_'] = summary['key'].apply(lambda x : x.strftime("%Y-%b"))
elif choice == 'Y':
    summary['key_'] = summary['key'].apply(lambda x : x.strftime("%Y"))
elif choice == 'D':
    summary['key_'] = summary['key'].apply(lambda x : x.strftime("%Y-%b-%d"))
if choice != 'W':
    ax = summary.plot(kind = 'bar',figsize=(20,10),x = 'key',grid = False,title = 'Bank data Analyser by Arpan Ghosh',logy = True)
else:
    ax = summary.plot(kind = 'bar',figsize=(20,10),grid = False,title = 'Bank data Analyser by Arpan Ghosh',logy = True)
ax.set_xticklabels(summary['key_'])
if choice == 'W':
    ax.set_xlabel("Year_Week-number")
    what = 'week'
elif choice == 'M':
    ax.set_xlabel("Year_Month-name")
    what = 'month'
elif choice == 'Y':
    ax.set_xlabel("Year")
    what = 'year'
elif choice == 'D':
    ax.set_xlabel("Date")
    what = 'day'

ax.set_ylabel("Expense in LOG scale")
#ax.set_ylim(0, 3000)
figure = ax.get_figure()
Max_C = data[data.Credit == data.Credit.max()]
Max_D = data[data.Debit == data.Debit.max()]
info = "Total Credit over the given Period : "+str(round(Total_C,3))+'\n'+"Total Debit over the given Period : "+str(round(Total_D,3))+'\n'+"Average Credit per "+what+" Over the given period : "+str(round((Total_C/count),3))+'\n'+"Average Debit per "+what+" Over the given period :"+str(round(Total_D/count,3))+'\n'+"Average Retention per "+what+" Over the given period : "+str(round((Total_C-Total_D)/count,3))+'\n'+"Standard Deviation of Credit : "+str(round(summary.credit.std(ddof=0),4))+'\n'+"Standard Deviation of Debit : "+str(round(summary.debit.std(ddof=0),4))+'\n'+"Maximum Balance was in this period : "+str(data[data.Balance == data.Balance.max()]['Balance'].to_list()[0])+'\n'+"Minimum Balance was in this period : "+str(data[data.Balance == data.Balance.min()]['Balance'].to_list()[0])+'\n'
info += "Maximum Credit was caused on "+str(Max_C['Value Date'].to_list()[0])+" by reference "+str(Max_C['Ref No./Cheque No.'].to_list()[0])+" because "+str(Max_C['Description'].to_list()[0])+' making balance '+str(Max_C['Balance'].to_list()[0])+'\n'+"Maximum Debit was caused on "+str(Max_D['Value Date'].to_list()[0])
info += " by reference "+str(Max_D['Ref No./Cheque No.'].to_list()[0])+" because "
info += str(Max_D['Description'].to_list()[0])+' making balance '+str(Max_D['Balance'].to_list()[0])+'\n'
print(info)
out_path = os.path.abspath(os.path.join(file_path, os.pardir))
if os.path.exists(out_path+'\\chart.pdf'):
    inp = input("File already exists ! want to replace ? (Y/N) : ")
    if inp == 'Y' or inp == 'y':
        out_path_pdf = out_path+'\\chart.pdf'
        out_path_txt = out_path+'\\chart.txt'
    else:
        name = input("Enter the file name only : ")
        out_path_pdf = out_path+"\\"+name+".pdf"
        out_path_txt = out_path+"\\"+name+".txt"
else:
    out_path_pdf = out_path+'\\chart.pdf'
    out_path_txt = out_path+'\\chart.txt'
out = open(out_path_txt,'w')
out.write(info)
out.close()
figure.savefig(out_path_pdf)

