
#Class to create weather data
class WeatherDataFetcher:
    def __init__(self, temperature, condition, humidity, city):
        self.temperature=temperature
        self.condition=condition
        self.city=city
        self.humidity=humidity
   
# Class to parse weather data
class DataParser: 
    def __init__(self,data,is_detailed):
        if not data:
            return "Weather data not available"
        if is_detailed:
            print(f"\nCity:{data.city}\nTemperature:{data.temperature}\nCondition:{data.condition}\nHumidity:{data.humidity}%")
        else:
             print(f"\nCity:{data.city}\nTemperature:{data.temperature}")
  
weather_data=[
    WeatherDataFetcher(70, "Sunny", 50, "New York"),
    WeatherDataFetcher(60, "Cloudy", 65, "London"),
    WeatherDataFetcher(75, "Rainy", 70, "Tokyo")]


def main():
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        for my_city in weather_data:
            if my_city.city==city:
                if city.lower() == 'exit':
                    break
                detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
                if detailed == 'yes':
                    DataParser(my_city, True)
                else:
                    DataParser(my_city, False)
               

if __name__ == "__main__":
    main()
 