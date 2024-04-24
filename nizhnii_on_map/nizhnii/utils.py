import folium
from nizhnii.models import InterestingPlacesModel, Groups


def get_map() -> str:
    """
    Возвращает HTML код карты со всеми маркерами
    """
    places = InterestingPlacesModel.objects.all()
    groups = Groups.objects.all()

    nizhnii_map = folium.Map(location=[56.314063, 43.993167], zoom_start=13)  # дом связи
    #

    # folium.TileLayer('stamen_terrain', attr='Stamen').add_to(nizhnii_map)
    folium.TileLayer('cartodbpositron').add_to(nizhnii_map)  # Карта без деталей рельефа
    # folium.TileLayer('cartodbdark_matter').add_to(nizhnii_map)  # Темная карта
    folium.TileLayer('openstreetmap').add_to(nizhnii_map)  # Обычная карта

    # Создаю группы и присваиваю их карте
    for group in groups:
        setattr(get_map, group.name, folium.FeatureGroup(name=group.name))
        getattr(get_map, group.name).add_to(nizhnii_map)

    # Создаю маркеры в определенных группах
    for place in places:
        coordinates = place.latitude, place.longitude
        group_name = place.group.name
        label = f'<h3>{place.name}</h3><p style=font-size:13px>{place.description}</p>'
        icon = folium.CustomIcon(place.group.icon, icon_size=(50, 50))
        tooltip = place.name

        folium.Marker(coordinates,
                      popup=folium.Popup(label, max_width=300),
                      icon=icon,
                      tooltip=tooltip).add_to(getattr(get_map, group_name))

    folium.LayerControl().add_to(nizhnii_map)

    return nizhnii_map._repr_html_()
