from akn_to_owl import parser, owltojson, jsonltolynx
import json 

def main():
    # Step 1: Parse XML data
    #parser.parse_xml('data/akn/19410716_041U0633_VIGENZA_20220922.xml', output_file='data/jsonl/copyright_law.jsonl')
    
    # Step 2: Prepare ontologies for loading in doccano
    creation_classes, creation_properties = owltojson.ontojson('data/ttl/copyrightonto-creationmodel.ttl')
    action_classes, action_properties = owltojson.ontojson('data/ttl/copyrightonto-actionsmodel.ttl')
    right_classes, right_properties = owltojson.ontojson('data/ttl/copyrightonto-rightsmodel.ttl')
    mediavaluechain_classes, mediavaluechain_properties = owltojson.ontojson('data/ttl/mediavaluechain.ttl')
    

    
    classes = {**creation_classes, **action_classes, **right_classes, **mediavaluechain_classes}
    properties = {**creation_properties, **action_properties, **right_properties, **mediavaluechain_properties}

    # Reset the ids
    for i, c in enumerate(classes.values()):
        c['suffix_key'] = str(i + 1)

    # Reset the ids
    for i, p in enumerate(properties.values()):
        p['suffix_key'] = str(i + 1)

    # Save the classes to a file as a list of dictionaries
    with open("data/json/classes.json", "w") as f:
        json.dump(list(classes.values()), f)

    with open("data/json/properties.json", "w") as f:
        json.dump(list(properties.values()), f)

    
    #owltojson.ontojson('data/ttl/cdm.ttl')


    # Step 4: Upload or send data to a web application through an API
    #functions.send_data(transformed_data, 'http://api.example.com')

    #jsonltolynx.convert_jsonl_to_lynx('data/jsonl/annotated/admin.jsonl',
    #                                    'data/rdf/lynx.rdf', "http://lynx-project.eu/doc/samples/")


    


if __name__ == '__main__':
    main()
