from rdflib import Graph, Namespace

graph = Graph()
graph.parse("countrues_info.ttl")


query = """
    SELECT ?country ?country_name
    WHERE {
        ?country :uses_currency ?currency ;
                 :country_name ?country_name .
        ?currency :currency_code ?currency_code .
        FILTER(?currency_code = "USD")
    }
"""

results = graph.query(query)

print(results)

for row in results:
    print(f"country name: {row['country_name']}, country link: {row['country']}")

