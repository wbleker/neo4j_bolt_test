# neo4j_bolt_test
Testing Neo4j bolt driver

Found that the driver does not work well with int values if you insert key value pairs
Problem was seen when upgrading from 1.5.3 to 1.6.0, also in 1.7.x we see the problem

Included in this repo a simple test script with example data

## Error message
Database exception:
Failed to read from defunct connection Address(host='127.0.0.1', port=7687)
