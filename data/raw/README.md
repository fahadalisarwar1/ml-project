# Data

This section provides information about the data. 
## Data Sources
The data for the labs comes from 4 different sources which are:

- Real-time telemetry data collected from machines,
- Error messages,
- Failure history and,
- Machine information such as type and age.


### Telemetry Data
The first data source is the telemetry time-series data which consists of voltage, rotation, pressure and vibration measurements collected from 100 machines in real time averaged over every hour collected during the year 2015.

> Total Number of telemetry records: 876100

### Error Data
The second major data source is the error logs. These are non-breaking errors thrown while the machine is still operational and do not constitute as failures. The error date and times are rounded to the closest hour since the telemetry data is collected at an hourly rate.
> Total Number of error records: 3919
> Error types: 5


### Machines Data
This data set includes some information about the machines which are model type and age which is years in service.

> Total number of machines: 100

### Failures Data
These are the records of machine failures. Each record has a date and time and machine ID.

> Total number of failures: 719

