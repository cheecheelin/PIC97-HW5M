import plotly 
import plotly.plotly as py 
py.sign_in('cheecheelin','br1lrimfku')
import plotly.tools as tls 
from plotly.graph_objs import Data, Layout, Figure 
from plotly.graph_objs import Scatter 
from plotly.graph_objs import XAxis, YAxis
from plotly.graph_objs import Line, Marker
from plotly.graph_objs import Histogram 
from plotly.graph_objs import XBins, Annotations, Font

rawdata = py.get_figure('dfreder1','69') # print(importthis.to_string())
datalist= rawdata.get_data()
post1900=[i for i in datalist[0]['x'] if i>=1900 and i<=2010]
mydata= map(str, post1900)
d= {x:mydata.count(x) for x in mydata}
#sorting by date 
a=[]
b=[]
for k in sorted(d):
    a.append(k)
    b.append(d[k])

for i in range(len(b)):
    if i!=0:
        b[i]+=b[i-1]
    else:
        b[i]=b[i]
# print a,b




fig= Figure(
    data=Data([Scatter(x=a,y=b,
                       line=Line(color='orange'),
                       fill='tozeroy',
                      )]), 
    layout=Layout(
        height=400,
        width=600,
        font=Font(
        family="Times New Roman",
        ),
        title='Total Bridges Built in CA Since 1900',
        xaxis1=XAxis(
            title='Year',
            nticks=12
        ),
        yaxis1=YAxis(
            title='Total Bridges'
        )
    )
)

py.iplot(fig,filename='helloitme')