# FTDE3-Project1-BatchProcessing

## Project Overview

This project is designed to extract data from a transactional PostgreSQL database and load it into a data warehouse also in PostgreSQL. The process involves batch processing to handle large volumes of data efficiently.

### Note

Put config.json inside file with the following format:

```
{
    // Your database source info
    "marketplace_prod": {
        "host": "",
        "db": "",
        "user": "",
        "password": "",
        "port": ""
    },
    // Your data warehouse info
    "dwh": {
        "host": "",
        "db": "",
        "user": "",
        "password": "",
        "port": ""
    }
}
```