# Snowflake Setup

## Setting up an integration user

Here is the SQL to make an integration environment in Snowflake for this source via an ACCOUNTADMIN. Be sure to give a real password.

```sql
CREATE WAREHOUSE INTEGRATION_TEST_WAREHOUSE_NORMALIZATION WITH WAREHOUSE_SIZE = 'XSMALL' WAREHOUSE_TYPE = 'STANDARD' AUTO_SUSPEND = 600 AUTO_RESUME = TRUE;

CREATE DATABASE INTEGRATION_TEST_NORMALIZATION;

CREATE ROLE INTEGRATION_TESTER_NORMALIZATION;

GRANT ALL PRIVILEGES ON WAREHOUSE INTEGRATION_TEST_WAREHOUSE_NORMALIZATION TO ROLE INTEGRATION_TESTER_NORMALIZATION;
GRANT ALL PRIVILEGES ON DATABASE INTEGRATION_TEST_NORMALIZATION TO ROLE INTEGRATION_TESTER_NORMALIZATION;
GRANT ALL PRIVILEGES ON FUTURE SCHEMAS IN DATABASE INTEGRATION_TEST_NORMALIZATION TO ROLE INTEGRATION_TESTER_NORMALIZATION;
GRANT ALL PRIVILEGES ON FUTURE TABLES IN DATABASE INTEGRATION_TEST_NORMALIZATION TO ROLE INTEGRATION_TESTER_NORMALIZATION;

# Add real password here and remove this comment
CREATE USER INTEGRATION_TEST_USER_NORMALIZATION PASSWORD='test' DEFAULT_ROLE=INTEGRATION_TESTER_NORMALIZATION DEFAULT_WAREHOUSE=INTEGRATION_TEST_WAREHOUSE_NORMALIZATION MUST_CHANGE_PASSWORD=false;

GRANT ROLE INTEGRATION_TESTER_NORMALIZATION TO USER INTEGRATION_TEST_USER_NORMALIZATION;

CREATE SCHEMA INTEGRATION_TEST_NORMALIZATION.TEST_SCHEMA;
```

If you ever need to start over, use this:
```sql
DROP DATABASE IF EXISTS INTEGRATION_TEST_NORMALIZATION;
DROP USER IF EXISTS INTEGRATION_TEST_USER_NORMALIZATION;
DROP ROLE IF EXISTS INTEGRATION_TESTER_NORMALIZATION;
DROP WAREHOUSE IF EXISTS INTEGRATION_TEST_WAREHOUSE_NORMALIZATION;
```