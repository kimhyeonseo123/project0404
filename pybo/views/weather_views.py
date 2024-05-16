from flask import Flask, Blueprint, render_template
import pandas as pd
import requests
import json
import math

bp = Blueprint("weather", __name__,url_prefix="/weather")
df = pd.read_excel("pybo/static/others/기상청.xlsx")
df1 = df.copy()
df2 = df1.drop(df1.columns[7:-3],axis="columns")
df3 = df2.drop(df2.columns[[0,-1]],axis="columns")
df4 = df2.rename(columns={"격자 X":"X", "격자 Y":"Y", "경도(초/100)":"경도", "위도(초/100)":"위도"})

@bp.route("/item/<date>/<address>")
def get_weather(date,address):
    url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"
    api="lYpdH2z0c4YDM0WcMCtOi%2Baj7wPCNFoUo%2Fszm78VdyspB%2BXcW2kCfyRehT534Nzae%2By%2F641YNaZHO3dPMdeqNQ%3D%3D"
    api1 = get(address)
    s_type="JSON"
    date=date
    nx = api1[0]
    ny = api1[1]


    url = f'{url}?serviceKey={api}&pageNo=1&numOfRows=1000&dataType=JSON&base_date={date}&base_time=0600&nx={nx}&ny={ny}'


    response = requests.get(url)
    json_bytes=response.content
    json_str = json_bytes.decode("utf-8")
    weather = json.loads(json_str)
    item = weather["response"]["body"]["items"]["item"]
    return item
    
    

def change(city):
    dic1 = {
        "서울":"서울특별시",
        "경기":"경기도",
        "부산":"부산광역시",
        "강원":"강원특별자치도",
        "인천":"인천광역시",
        "대구":"대구광역시",
        "광주":"광주광역시",
        "대전":"대전광역시",
        "울산":"울산광역시",
        "제주":"제주특별자치도",
        "세종":"세종특별자치시",
        "충남":"충청남도",
        "충북":"충청북도",
        "전남":"전라남도",
        "전북":"전라북도",
        "경남":"경상남도",
        "경북":"경상북도",
        
    }
    
    try:
        return dic1[city]
    except KeyError as e:
        return city

def get(address):
    arr = address.split(" ")
    
    size = len(arr)
    
    change(arr[0])
    
    cond1 = df4["1단계"].str.contains(arr[0])
    
    val = ""
    
    if size ==1:
        cond2_na = df4["2단계"].isnull()
        cond3_na = df4["3단계"].isnull()
        val = df4.loc[cond1&cond2_na&cond3_na]
        
    elif size ==2:
        cond2 = df4["2단계"].str.contains(arr[1])
        cond3_na = df4["3단계"].isnull()
        val = df4.loc[cond1&cond2&cond3_na]
        
    elif size==3:
        cond2 = df4["2단계"].str.contains(arr[1])
        cond3 = df4["3단계"].str.contains(arr[2])
        val = df4.loc[cond1&cond2&cond3]
        
    idx = val.index.tolist()[0]
    
    return val.loc[idx,"X"],val.loc[idx,"Y"]