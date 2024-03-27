# Import necessary libraries
import os
import subprocess  # Used for executing a shell command
import pygrib  # Used for reading GRIB files

# Function to read ground point value (GPV) data from a GRIB2 file
def read_gpv_file():
    # Get the current working directory
    cwd = os.getcwd()
    
    # URL of the GRIB2 file to download. This file contains surface data for 2020/08/01 at 15:00 UTC.
    url_surf = 'http://database.rish.kyoto-u.ac.jp/arch/jmadata/data/gpv/original/2020/08/01/Z__C_RJTD_20200801060000_GSM_GPV_Rjp_Lsurf_FD0000-0312_grib2.bin'
    
    # Create a file path for the downloaded file in the current working directory
    file_surf = os.path.join(cwd, os.path.basename(url_surf))

    # Check if the file already exists to avoid re-downloading
    if not os.path.exists(file_surf):
        # Use curl command to download the file. Output and errors are suppressed.
        subprocess.run(['curl', '-O', url_surf], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, cwd=cwd)

    # Open the downloaded GRIB2 file for reading
    grbs = pygrib.open(file_surf)
    # Select all messages that match the parameter "Pressure reduced to MSL"
    prmsl_fc0 = grbs.select(parameterName='Pressure reduced to MSL')
    # Print the number of messages found and their content
    print(len(prmsl_fc0))
    print(prmsl_fc0)

# This ensures that the read_gpv_file function is called when the script is executed directly.
if __name__ == "__main__":
    read_gpv_file()