import folium

# Function to create the map and initialize the folium object
def create_map():
    # Initialize the map centered around Idaho Falls
    idaho_falls_map = folium.Map(location=[43.4917, -112.0339], zoom_start=13)
    
    # Add a title using a popup with a hidden marker
    folium.Marker(
        location=[43.4917, -112.0339],  # Place the marker at the center of the map
        popup="<b>Idaho Falls Attractions and Hotels Map</b>",  # Title in bold
        icon=folium.Icon(icon="info-sign", color="green", icon_color="white"),
    ).add_to(idaho_falls_map)
    
    return idaho_falls_map

# Function to add attractions with a Ferris wheel icon
def add_attractions(idaho_falls_map):
    attractions = [
        {"name": "Idaho Falls Zoo", "location": [43.47206566631062, -112.0413570606256]},
        {"name": "Museum of Idaho", "location": [43.490400544655685, -112.03819196062487]},
        {"name": "Snake River Greenbelt", "location": [43.48813860321409, -112.04716816062499]},
        {"name": "East Idaho Aquarium", "location": [43.51096875718292, -112.02165620295328]},
        {"name": "ARTitorium on Broadway", "location": [43.49098263828596, -112.04019223178943]},
        {"name": "Russ A Freeman Park", "location": [43.514615775515615, -112.05154234528224]},
        {"name": "Tautphaus Park", "location": [43.47374154273006, -112.03937153179001]},
        {"name": "Collector Corner Museum", "location": [43.493403179862206, -112.01369200295393]},
        {"name": "Giant Eagle Waterfall Nest", "location": [43.48813850692783, -112.04938004897912]},
        {"name": "Japanese Friendship Garden", "location": [43.4924324855378, -112.044917503806]},
        {"name": "Ka-Ko-Jo's", "location": [43.48033667504942, -111.98934293365004]},
        {"name": "Keefer Island", "location": [43.50250108419817, -112.04614748968483]},
        {"name": "Blast Off", "location": [43.51360530977793, -112.00992134343447]},
        {"name": "The Waterfront at Snake River Landing", "location": [43.4774653417705, -112.05800208946094]},
        {"name": "Melaleuca Field", "location": [43.504506173433256, -112.03837977898324]},
        {"name": "The Art Museum of Eastern Idaho", "location": [43.490167346650345, -112.04539428761234]},
        {"name": "Heritage Park", "location": [43.46971415744128, -112.0648040317903]},
        {"name": "Joe Marmo/Wayne Lehto Ice Arena", "location": [43.47164452391423, -112.04004559809894]},
        {"name": "iJump Trampoline Park", "location": [43.508340711709174, -111.97969132682239]},
        {"name": "The Colonial Theater", "location": [43.493363705995186, -112.04138392029884]},
    ]
    
    # Loop to add each attraction to the map
    for attraction in attractions:
        folium.Marker(
            location=attraction["location"],
            popup=attraction["name"],
            icon=folium.Icon(color="blue", icon="cloud"),
        ).add_to(idaho_falls_map)

# Function to add hotels with a hotel icon
def add_hotels(idaho_falls_map):
    hotels = [
        {"name": "Hilton Garden Inn", "location": [43.4994955848344, -112.04542936080489]},
        {"name": "Fairfield Inn & Suites", "location": [43.4946866175997, -112.05228000705836]},
        {"name": "Best Western Driftwood Inn", "location": [43.49772758486033, -112.04427858412146]},
        {"name": "La Quinta Inn & Suites by Wyndham", "location": [43.47548828241006, -111.9818109710153]},
        {"name": "Residence Inn", "location": [43.49289953768794, -112.04606896716803]},
        {"name": "Hampton Inn Idaho Falls/Airport", "location": [43.498043187488676, -112.04715422192811]},
        {"name": "Shilo Inns Suites Hotel", "location": [43.50198092072456, -112.04760584910859]},
        {"name": "Comfort Suites", "location": [43.49640023166118, -112.04504458042125]},
        {"name": "Home2 Suites by Hilton", "location": [43.48252517159487, -112.05641868188958]},
        {"name": "Candlewood Suites", "location": [43.48380946394333, -112.04719626769251]},
        {"name": "Destinations Inn", "location": [43.491001057612294, -112.04040963852246]},
        {"name": "Comfort Inn", "location": [43.49594418694011, -112.05482614449369]},
        {"name": "Holiday Inn Express & Suites", "location": [43.476876253551765, -111.99151171305091]},
        {"name": "Super 8 by Wyndham", "location": [43.49935352662375, -112.04743879121385]},
        {"name": "My Place Hotel", "location": [43.4862339957528, -112.05794530008974]},
        {"name": "Tru by Hilton", "location": [43.49827387111419, -112.04557253178909]},
        {"name": "Econo Lodge", "location": [43.49793358842568, -112.05637611829549]},
        {"name": "Motel West", "location": [43.4969761388452, -112.06005538016502]},
        {"name": "Motel 6", "location": [43.5059123742227, -112.05319071848879]},
        {"name": "Fairfield Inn & Suites", "location": [43.49465492178426, -112.05230446062471]},
    ]
    
    # Loop to add each hotel to the map
    for hotel in hotels:
        folium.Marker(
            location=hotel["location"],
            popup=hotel["name"],
            icon=folium.Icon(color="red", icon="home"),
        ).add_to(idaho_falls_map)

# Main function to generate the map and save it
def main():
    # Create the map
    idaho_falls_map = create_map()

    # Add attractions to the map
    add_attractions(idaho_falls_map)

    # Add hotels to the map
    add_hotels(idaho_falls_map)

    # Save the map as an HTML file
    idaho_falls_map.save("idaho_falls_landmarker_map.html")
    print("Map has been saved as 'idaho_falls_landmarker_map.html'. Open it in a browser to view.")

# Run the main function
if __name__ == "__main__":
    main()
