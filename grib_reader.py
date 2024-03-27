# Import the pygrib library, which is used for reading and writing GRIB (GRIdded Binary) files. GRIB files are commonly used in meteorology to store historical and forecast weather data.
import pygrib

# A function to write the content of GRIB2 messages to a file.
def write_grib2_data_to_file(filename, output_filename):
    try:
        # Open the GRIB file for reading and the output file for writing.
        with pygrib.open(filename) as grib_file, open(output_filename, 'w') as output_file:
            # Iterate over each GRIB message in the GRIB file.
            for i, grib_message in enumerate(grib_file, start=1):
                # Write the message number and its content to the output file.
                output_file.write(f"Message {i}:\n")
                output_file.write(f"{grib_message}\n\n")
    except Exception as e:
        # If an error occurs, open the output file again and write the error message.
        with open(output_filename, 'w') as output_file:
            output_file.write(f"An error occurred: {e}\n")

# This block executes if the script is run directly, not imported as a module.
if __name__ == "__main__":
    # Specify the paths to the input GRIB2 file and the output file.
    # (Please change teh input_filename and output_filename accordingly)
    input_filename = "gsm_jp/Z__C_RJTD_20221013000000_GSM_GPV_Rjp_Gll0p1deg_Lsurf_FD0000-0100_grib2.bin"
    output_filename = "grib2_data_output.txt"
    # Call the function defined above with the specified filenames.
    write_grib2_data_to_file(input_filename, output_filename)
    
    # Open the GRIB file again for reading a specific parameter.
    grbs = pygrib.open(input_filename)
    # Select the first GRIB message that matches the specified parameter name and forecast time.
    prmsl_fc0 = grbs.select(parameterName='Pressure reduced to MSL', forecastTime=0)[0]
    # Extract data (values, latitudes, longitudes) from the selected GRIB message.
    values, lats, lons = prmsl_fc0.data()
    # Print the values to the console.
    print(values)
