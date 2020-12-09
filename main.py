#!/usr/bin/env python3
# coding: utf-8

from pyld import jsonld
import json

data = {}

with open('trace.json') as json_file:
    data = json.load(json_file)

context = {
    "s": "http://schema.org/",
    "ex": "http://example.com/ns#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",

    "url": "@id",

    "id": {
        "@id": "s:identifier",
        "@type": "xsd:integer"
    },
    "title": {
        "@id": "s:name",
        "@type": "xsd:string"
    },
    "body": {
        "@id": "s:description",
        "@type": "xsd:string"
    },
    "author_association": {
        "@id": "ex:authorAssociation",
        "@type": "xsd:string"
    },
    "html_url": {
        "@id": "s:url",
        "@type": "xsd:anyURI"
    },
    "closed_at": {
        "@id": "s:endDate",
        "@type": "xsd:dateTimeStamp"
    },
    "user": {
        "@id": "s:creator",
        "@type": "ex:User",
    },
    "assignees": {
         "@id": "s:assignee",
         "@type": "ex:User"
    },
    "repository_url": {
        "@type": "@id",
        "@reverse": "ex:issue"
    },
    "labels" : {
        "@id" : "ex:label",
    },
    "name": {
        "@id": "s:name",
        "@type": "xsd:string"
    },
    "description": {
        "@id": "s:description",
        "@type": "xsd:string"
    },
    "issue_url": {
        "@type": "@id",
        "@reverse": "ex:comment"
    },
    "created_at": {
        "@id": "s:startDate",
        "@type": "xsd:dateTimeStamp"
    },
    "state": "@type",
    "open": "ex:OpenIssue",
    "closed": "ex:ClosedIssue"
}

#compacted = jsonld.compact(data, context)

#print(json.dumps(compacted, indent=2))

expanded = jsonld.expand(data, {'expandContext': context})

#print(json.dumps(expanded, indent=2))
normalized = jsonld.normalize(expanded, {'algorithm': 'URDNA2015', 'format': 'application/n-quads'})
#print(normalized)

f = open("machin.nq", "a")
f.write(normalized)
f.close()
