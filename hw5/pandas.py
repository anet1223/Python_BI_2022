#!/usr/bin/env python
# coding: utf-8

# # Работа с реальными данными

# Импорт библиотек

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Функции read_gff и read_bed6 для чтения соответствующих форматов. Функция read_gff оставляет в колонке с атрибутами только данные о типе рРНК одной короткой строкой (16S, 23S, 5S)

# In[ ]:


def read_gff(file):
    col_names = ['seqid', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase', 'RNA type']
    df = pd.read_csv(file,sep='\t', comment='#', low_memory=False, header=None, names=col_names)
    # удаление всей лишней информации из атрибутов
    df['RNA type'] = [x.split('_')[-0] for x in df['RNA type']]
    df['RNA type'] = [x.split('=')[-1] for x in df['RNA type']]
    return df
def read_bed6(file):
    col_n = ['seqid', 'start', 'end', 'name', 'score', 'strand']
    df = pd.read_csv(file, sep='\t', comment='#', header=None,names=col_n)
    return df


# Загрузка файлов в дата фреймы

# In[ ]:


df1 = read_gff(r'C:\Users\к164\Downloads\rrna_annotation.gff')
df2 = read_bed6(r'C:\Users\к164\Downloads\alignment.bed')


# Подсчет типов РНК

# In[ ]:


new = df1.groupby(['seqid','RNA type'], as_index = False)      .aggregate({'type':'count'})      .rename(columns ={'type':'Count', 'seqid':'Sequence'})
new.head()


# График по типу РНК

# In[ ]:


sns.barplot(x = 'Sequence', y = 'Count', hue = 'RNA type', data = new)
plt.xticks(rotation=90)
plt.title('RNA type count')


# Пересечение референса и прочтений

# In[ ]:


merge_df = pd.merge(df2,df1, how='inner', on = 'seqid')
new_merge = merge_df.query('start_x<=start_y and end_x>=end_y')
new_merge


# # Кастомизация графиков

# Загрузка и преобразование дата фрейма

# In[2]:


vol = pd.read_csv(r'C:\Users\к164\Downloads\diffexpr_data.tsv.gz',sep='\t')
# создание столбца с значимостью изменений
vol['result'] = 0
r1 = vol.query('logFC>=0 and log_pval>=0.05')[['result']]
r1['result'] = 'Significantly upregulated'
r2 = vol.query('logFC>=0 and log_pval<=0.05')[['result']]
r2['result'] = 'Non-significantly upregulated'
r3 = vol.query('logFC<0 and log_pval>0.05')[['result']]
r3['result'] = 'Significantly downregulated'
r4 = vol.query('logFC<0 and log_pval<0.05')[['result']]
r4['result'] = 'Non-significantly downregulated'
new = pd.concat([r1,r2,r3,r4])
vol = pd.merge(vol, new, left_index=True, right_index=True)
vol = vol.rename(columns = {'result_y':'Expression'})
vol


# In[3]:


# определение границ линий
max_FC = max(vol.logFC)
min_FC = min(vol.logFC)
max_p = max(vol.log_pval)
min_p = min(vol.log_pval)


# График

# In[29]:


# размер графика
plt.rcParams["figure.figsize"] = (20,10)
# пунктирные линии
plt.plot([min_FC,max_FC], [0.05,0.05], color='grey', linestyle='dashed',lw = 2)
plt.plot([0,0], [max_p,min_p],color='grey', linestyle='dashed',lw = 2)
plt.annotate('p value = 0.05', xy=(6.5, 1),fontsize=18,color='grey',fontweight="bold")
# scatter plot
sns.scatterplot(x = 'logFC', y = 'log_pval', data = vol, hue = 'Expression',
                hue_order = ['Significantly downregulated','Significantly upregulated',
                            'Non-significantly downregulated','Non-significantly upregulated'])
plt.xlabel("log\u2082(fold change)", fontsize=20, fontweight="bold",style='italic')
plt.ylabel("-log\u2081\u2080 p-value corrected", fontsize=20, fontweight="bold",style='italic')
plt.legend(fontsize=20, title = None, shadow =4)
plt.title('Volcano plot',fontsize=30, fontweight="bold",style='italic' )
plt.ylim(-5,119)
plt.minorticks_on()
plt.tick_params(axis='both', which='major', labelsize=16)
# анотация отдельных генов. Значение позиций были получены через query, но запросы я не сохранила, чтобы не перегружать код. 
arrowprops = {'arrowstyle': '->','linewidth':'4', 'color':'red'}
plt.annotate('UMOD',xy=(min_FC, 52),xytext=(min_FC, 60),arrowprops=arrowprops, fontsize=15,fontweight="bold")
plt.annotate('MUC7',xy=(-9.196, 3),xytext=(-9.196, 10),arrowprops=arrowprops,fontsize=15,fontweight="bold")
plt.annotate('ZIC5',xy=(4.2767, 5),xytext=(4.2767, 15),arrowprops=arrowprops,fontsize=15,fontweight="bold")
plt.annotate('ZIC2',xy=(4.5719, 3),xytext=(4.5719, 12),arrowprops=arrowprops,fontsize=15,fontweight="bold")


# # Pie chart

# In[30]:


fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe = ['other', 'BMW', 'FORD',
        'TESLA', 'JAGUAR', 'MERCEDES']

data = [225, 90, 50, 60, 100, 5]
autopr = [42.45, 16.98, 9.43, 11.32, 18.87, 0.94]
explode = (0.1, 0.05, 0.05, 0.05,0.05,0.05)

wedges, texts = ax.pie(data, startangle=-40, explode = explode, wedgeprops=dict(width=0.9))

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(str(recipe[i]+'\n'+ str(autopr[i])+'%'), xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)



# In[ ]:




