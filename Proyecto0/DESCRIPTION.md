### Description

We want to know the values ​​captured by a sensor, through a web interface, the values ​​can only be accessed by users who are registered and authenticated. In addition, only a set of allowed sensors can record new records.

Basic requirements:

    - The system allows a user to log in and the user session is saved so they don't have to authenticateagain, in each view.
    - The system must allow one or more sensors to register data, and this data must persist.
    - The system should allow users to view the censored data.
    - The system must allow adding new sensors.

Non functional requirements:

- Security - Usability - Maintainability

| Endpoint                | Description                                                                 |
| ----------------------- | --------------------------------------------------------------------------- |
| /push-weather - GET     | Push weather info to the database if the sensor has been registered         |
| /get-weather - GET      | Returns recorded data, if the user is logged.                               |
| /sign-in - POST         | Log-In if the user has been added through user-register endpoint            |
| /sensor-register - POST | Adds a new sensor to the allowed sensors collection, receives MAC direction |
| /user-register - POST   | Adds a new user, receives username and password                             |

Backend -> Flask, see views.py for endpoints details.
Frontend -> ReactJS
