from urllib import response
from urllib.request import urlopen
import json
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF

URL = 'https://services.swpc.noaa.gov/json/solar-cycle/predicted-solar-cycle.json'

drawing = Drawing(400, 200)

pred = []
high = []
low = []
times = []

with urlopen(URL) as resp:
    data = json.load(resp)
    
    for i in range(len(data)):
        pred.append(data[i]['predicted_f10.7'])
        high.append(data[i]['high_f10.7'])
        low.append(data[i]['low_f10.7'])
        t = data[i]['time-tag'].split(sep='-')
        times.append(float(t[0]) + float(t[1])/12.0)

lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = [
    list(zip(times, pred)),
    list(zip(times, high)),
    list(zip(times, low))]
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green

drawing.add(lp)
drawing.add(String(250, 150, 'Sunspots', fontSize=14, fillColor=colors.red))

renderPDF.drawToFile(drawing, 'report2.pdf', 'Sunspots')
