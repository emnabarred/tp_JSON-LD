#!/usr/bin/env python3
# coding: utf-8

from pyld import jsonld
import json

data = {}

with open('trace.json') as json_file:
    data = json.load(json_file)

context = {
    "@base": "http://example.com/",
    "ex:": "http://exampe.com/ns#",
    "s": "http://schema.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",

    "user": "ex:user",
    "issue": "ex:issue",
    "closedIssue" : "ex:ClosedIssue",
    "openIssue" : "ex:OpenIssue",
    "comment": "ex:comment",
    "label": "ex:label",
    "creator": "s:creator",
    "assignee": "s:assignee",

    "title": "s:name",
    "body": "s:description",
    "created_at": "s:startDate",
    "created_at": "xsd:dateTimeStamp",
    "url": "xsd:anyURI",
    "url": "s:url",
    "author_association": "ex:authorAssociation",
    "author_association": "xsd:string",
    "closed_at":"s:endDate",
    "closed_at":"xsd:dateTimeStamp",
    "login": "xsd:string",
    "login": "s:accountid",
    "id" : "s:identifiier",
    "identifier": "@id"
}

expanded = jsonld.expand(data, {'expandContext': context})

#print(json.dumps(expanded, indent=2))
normalized = jsonld.normalize(expanded, {'algorithm': 'URDNA2015', 'format': 'application/n-quads'})
print(json.dumps(normalized, indent=2))