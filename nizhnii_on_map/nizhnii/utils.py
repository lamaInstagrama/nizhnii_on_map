import folium
from nizhnii.models import InterestingPlacesModel, Groups


def get_map() -> str:
    """
    Возвращает HTML код карты со всеми маркерами
    """
    places = InterestingPlacesModel.objects.all()
    groups = Groups.objects.all()

    nizhnii_map = folium.Map(location=[56.314063, 43.993167])  # дом связи

    # Создаю группы и присваиваю их карте
    for group in groups:
        setattr(get_map, group.name, folium.FeatureGroup(name=group.name))
        getattr(get_map, group.name).add_to(nizhnii_map)

    # Создаю маркеры в определенных группах
    for place in places:
        coordinates = place.latitude, place.longitude
        group_name = place.group.name
        label = f'<h1>{place.name}</h1><p>{place.description}</p>'

        folium.Marker(coordinates,
                      popup=folium.Popup(label, max_width=300)).add_to(getattr(get_map, group_name))

    folium.LayerControl().add_to(nizhnii_map)

    return nizhnii_map._repr_html_()
