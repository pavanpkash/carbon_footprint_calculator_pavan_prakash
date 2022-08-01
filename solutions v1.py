final_vehicle_emissions = 1
total_electricity_emissions = 1
co2_from_gas = 1
total_flight_emissions = 1

# starts here

carbon_footprint = final_vehicle_emissions + total_electricity_emissions + co2_from_gas + total_flight_emissions
print("Your total carbon footprint is", carbon_footprint, "kg of CO2 emitted per year.")

if carbon_footprint < 8600:
    print("\nAwesome! This is less than the average carbon footprint in New Zealand, which is 8,600 kg.")
    print("""Here are some solutions to help lower this:
          - Use more economic forms of transport, including biking, walking, electric vehicles and even public transport
          - Use less LPG gas
          - Plant more trees""")
elif carbon_footprint > 8600:
    print("\nThis is greater than the average carbon footprint in New Zealand, which is 8,600kg.")
    print("Here are some solutions to help lower this:"
          """- Use more economic forms of transport, including biking, walking, electric vehicles and even public transport
          - Use less LPG gas
          - Plant more trees""")
