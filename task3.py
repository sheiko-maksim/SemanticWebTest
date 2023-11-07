from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd


sparql = SPARQLWrapper("http://dbpedia.org/sparql")


query = """
    PREFIX dbr: <http://dbpedia.org/resource/>
    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX dbp: <http://dbpedia.org/property/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    
    SELECT DISTINCT ?diseaseLabel ?cause
    WHERE {
        ?diseaseLabel a dbo:Disease ;
           dbp:field dbr:Gastroenterology ;
           dbo:medicalCause ?cause .
    }
    """

sparql.setQuery(query)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

df = pd.DataFrame(columns=["Disease", "Cause"])


# Extract and print the results
for result in results["results"]["bindings"]:
    disease_label = result["diseaseLabel"]["value"]
    cause_label = result["cause"]["value"]
    print(f"Disease: {disease_label}, Cause {cause_label}")
