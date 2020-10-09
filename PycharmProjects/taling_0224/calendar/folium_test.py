import folium
map = folium.Map(location=[37.498, 127.027], zoom_start=17) # zoom_start: 확대

map.save("map.html")

# 왼쪽에 탐색기로 열면 그 파일이 열림 (file path> map.html)

# 강남역 -> 바로 map에 찍히려면 API를 활요해야 함