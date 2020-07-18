# -*- coding: utf-8 -*-
import scrapy
import json


class ListingsSpider(scrapy.Spider):
    name = 'listings'
    allowed_domains = ['www.centris.ca']

    position = {
        'startPosition': 0
    }
    query = {
        "query": {
            "UseGeographyShapes": 0,
            "Filters": [
                {
                    "MatchType": "CityDistrictAll",
                    "Text": "Montréal (All boroughs)",
                    "Id": 5
                }
            ],
            "FieldsValues": [
                {
                    "fieldId": "CityDistrictAll",
                    "value": 5,
                    "fieldConditionId": "",
                    "valueConditionId": ""
                },
                {
                    "fieldId": "SellingType",
                    "value": "Rent",
                    "fieldConditionId": "",
                    "valueConditionId": ""
                },
                {
                    "fieldId": "Category",
                    "value": "Residential",
                    "fieldConditionId": "",
                    "valueConditionId": ""
                },
                {
                    "fieldId": "LandArea",
                    "value": "SquareFeet",
                    "fieldConditionId": "IsLandArea",
                    "valueConditionId": ""
                },
                {
                    "fieldId": "RentPrice",
                    "value": 0,
                    "fieldConditionId": "ForRent",
                    "valueConditionId": ""
                },
                {
                    "fieldId": "RentPrice",
                    "value": 15000,
                    "fieldConditionId": "ForRent",
                    "valueConditionId": ""
                }
            ]
        },
        "isHomePage": True
    }

    def start_requests(self):
        yield scrapy.Request(
            url='https://www.centris.ca/property/UpdateQuery',
            method='POST',
            body=json.dumps(self.query),
            headers={
                # 'Accept': '*/*',
                'Content-Type': 'application/json',
                # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
                # 'Request-Context':'appId=cid-v1:2684eb29-d3fa-4ed4-812c-34e60716263c'
                # 'Connection': 'keep-alive'
            },
            callback=self.update_query
        )

    def update_query(self, response):
        yield scrapy.Request(
            url='https://www.centris.ca/Property/GetInscriptions',
            method='POST',
            body=json.dumps(self.position),
            headers={
                'Content-Type': 'application/json',
            },
            callback=self.parse
        )

    def parse(self, response):
        print(response.body)
