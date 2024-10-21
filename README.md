# assignment-1
# Rule Engine with AST

## 📜 Overview
This project is a 3-tier rule engine application that determines user eligibility based on attributes like age, department, income, etc. The rule engine uses an *Abstract Syntax Tree (AST)* to represent and evaluate conditional rules.

## 🛠️ Features
- *Dynamic Rule Creation:* Convert rule strings into an AST structure.
- *Rule Evaluation:* Evaluate user data against complex conditions using logical operators like AND/OR.
- *Data Flexibility:* Supports dynamic attributes like age, department, and more.

## 📦 Project Structure
- Node: Class definition to represent the nodes in the AST.
- create_rule(rule_string): Function to build the rule tree from a rule string.
- evaluate_rule(node, data): Function to evaluate the AST against user data.
- *Test Cases*: Sample rule and data to test the functionality.

## 🚀 Getting Started

### Prerequisites
- *Python 3.x* installed on your system.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/sadiyarajgoli/assignments.git
   cd assignments

2. Install any dependencies (none required for basic functionality).



🔧 Usage

1. Create a Rule Tree: The create_rule(rule_string) function builds an Abstract Syntax Tree (AST) from the given rule. Example:

rule_string = "age > 30 AND department = 'Sales'"
rule_tree = create_rule(rule_string)


2. Evaluate a Rule: Use the evaluate_rule(node, data) function to check if user data matches the conditions of the rule:

sample_data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
result = evaluate_rule(rule_tree, sample_data)
print("Evaluation Result:", result)



🧪 Test Cases

The code includes a basic test case to validate the functionality of the rule engine:

rule_string = "age > 30 AND department = 'Sales'"
sample_data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}

rule_tree = create_rule(rule_string)
result = evaluate_rule(rule_tree, sample_data)
print("Evaluation Result:", result)  # Expected output: True



⚙️ Functions Explained

1. Node Class: Represents a node in the AST, which can be an operator or operand.


2. create_rule(rule_string): Converts rule strings into a structured AST.


3. evaluate_rule(node, data): Recursively evaluates the AST against the user data.

# assignment-2

# 🌦️ Real-Time Weather Monitoring System

## 📜 Overview
This project is a real-time weather data processing system that fetches weather conditions for multiple cities using the *OpenWeatherMap API*. It provides summarized insights using rollups and aggregates, and allows for alerting based on user-defined thresholds.

## 🛠️ Features
- *Real-Time Data Retrieval:* Continuously fetches weather data from the OpenWeatherMap API for specified cities.
- *Data Summaries:* Generates daily summaries including average temperature, max/min temperature, and dominant weather conditions.
- *Alerting System:* Triggers alerts based on user-defined thresholds for temperature and specific weather conditions.
- *Visualization:* Optional setup to visualize daily trends and historical weather data.

## 📦 Project Structure
- get_weather_data(city): Function to fetch weather data for a specified city.
- daily_summaries: Dictionary to store weather summaries for each city.
- *Alert System*: Customizable alert thresholds for extreme weather conditions.

## 🚀 Getting Started

### Prerequisites
- *Python 3.x* installed on your system.
- *API Key* from OpenWeatherMap. Sign up at [OpenWeatherMap](https://openweathermap.org/) to get your free API key.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. Install the required Python libraries:

pip install requests



🔧 Usage

1. Setup API Key: Open the code file and replace 'your_api_key_here' with your actual OpenWeatherMap API key:

API_KEY = 'your_actual_api_key'


2. Fetch Weather Data: Use the get_weather_data() function to fetch data for cities:

cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
for city in cities:
    weather_data = get_weather_data(city)
    print(f"Weather in {city}: {weather_data}")


3. Daily Weather Summaries: Automatically process and store daily weather summaries for the specified cities:

daily_summaries = {}  # Dictionary to hold weather data

# Loop through each city and store their data in daily_summaries
for city in cities:
    weather_data = get_weather_data(city)
    if weather_data:
        main_weather = weather_data['weather'][0]['main']
        current_temp = weather_data['main']['temp']
        feels_like_temp = weather_data['main']['feels_like']
        timestamp = weather_data['dt']
        daily_summaries[city] = {
            'main_weather': main_weather,
            'current_temp': current_temp,
            'feels_like_temp': feels_like_temp,
            'timestamp': timestamp
        }
print(daily_summaries)



🧪 Test Cases

Test the data retrieval and processing by fetching weather data for the cities:

Check the console output to see if the weather data is being fetched successfully.

Verify that the daily summaries are correctly populated with temperature and condition details.


⚙️ Functions Explained

1. get_weather_data(city): Fetches real-time weather data from the OpenWeatherMap API for a specific city.


2. Daily Summaries: Generates rollups of temperature and weather conditions for easy analysis.


3. Alerting System: Configurable alerts for temperature spikes and extreme conditions.


