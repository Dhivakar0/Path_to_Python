import requests
from datetime import datetime
import smtplib
import time

my_email = "pythontestingku@gmail.com"
password = "hxjrbvjgxvqbneqj"
recipient_email = "pythontestingkudaan@yahoo.com"
MY_LAT = 11
MY_LONG = 17


# Your position is within +5 or -5 degrees of the ISS position.
def iss_is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(f"ISS Position: Latitude: {iss_latitude}, Longitude: {iss_longitude}")

    if MY_LAT + 5 >= iss_latitude >= MY_LAT - 5 and MY_LONG + 5 >= iss_longitude >= MY_LONG - 5:
        print("ISS is close to your location!")
        return True
    else:
        print("ISS is not close to your location.")
        return False


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()

    # Get sunrise and sunset times
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    print(f"Sunrise: {sunrise}, Sunset: {sunset}, Time Now: {time_now}")

    # Check if it's dark (before sunrise or after sunset)
    if time_now >= sunset or time_now <= sunrise:
        print("It is dark!")
        return True
    else:
        print("It is not dark.")
        return False


while True:
    # Check if ISS is close and it's dark
    print("Checking conditions...")
    if iss_is_close() and is_dark():
        try:
            print("Conditions met. Sending email...")
            # Send email notification
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=recipient_email,
                    msg="Subject: Look up!\n\nThe ISS is close to your location. Just go and look up in the sky now!"
                )
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")

    # Wait for 60 seconds before checking again
    time.sleep(60)
