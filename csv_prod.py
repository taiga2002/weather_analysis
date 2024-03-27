import pygrib
import csv

def extract_grib2_data_to_csv(filename, output_csv):
    try:
        with pygrib.open(filename) as grib_file, open(output_csv, mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            # Write CSV headers
            csv_writer.writerow(["Parameter Name", "Unit", "Value", "Date"])
            
            for i, grib_message in enumerate(grib_file, start=1):
                # Extract necessary data from each message
                data = {
                    "name": grib_message.name,
                    "unit": grib_message.units,
                    "value": grib_message.values.mean(),  # Example: taking the mean value
                    "date": grib_message.analDate.strftime("%Y-%m-%d %H:%M:%S")
                }
                # Write data to CSV
                csv_writer.writerow([data["name"], data["unit"], data["value"], data["date"]])

    except Exception as e:
        print(f"An error occurred: {e}")

# Replace with your GRIB2 file path and CSV file path
if __name__ == "__main__":
    input_filename = "gsm_jp/Z__C_RJTD_20221013000000_GSM_GPV_Rjp_Gll0p1deg_Lsurf_FD0000-0100_grib2.bin"
    output_csv = "grib2_data.csv"
    extract_grib2_data_to_csv(input_filename, output_csv)
