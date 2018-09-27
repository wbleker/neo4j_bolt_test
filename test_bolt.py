#!/usr/local/bin/python

from neo4j.v1 import GraphDatabase
import sys


def main():
  if len(sys.argv) < 3:
    print("\nNeed some arguments to work with")
    sys.exit("Usage: %s <servername> <port> \n" % sys.argv[0])

  neoserver=sys.argv[1]
  neoport=sys.argv[2]

  data = {1: 'bla', '2': 'lala'}
  print(data)

  uri = "bolt://"+neoserver+":"+neoport
  print ("\nChecking server: %s on port %s \n %s \n\n" % (neoserver, neoport, uri))

  driver = GraphDatabase.driver(uri)

  try:
	  test_query(driver, data)
  except Exception: #or AssertionError
    import traceback
    traceback.print_exc(limit=0)

def execute_query_neo4j(driver, cypher, **kwargs):
  with driver.session() as sess:
    try:
      return sess.run(cypher, kwargs)
    except Exception as e:
      print(f'Database exception:\n{e}')

def test_query(driver, data):
  print('running test_query')
  query = '''
    FOREACH ( k in keys({data}) |
      CREATE(e:TestData {name: k, value: COALESCE({data}[k],'')}))
          '''
  resp = execute_query_neo4j(driver, query, data=data)

if __name__ == '__main__':
  main()
