#!/usr/bin/env python3
"""
Script to provide statistics about
Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    stats = nginx_collection.count_documents({})
    print(f"{stats} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        countMethods = nginx_collection.count_documents({'method': method})
        print(f"\tmethod {method}: {countMethods}")
    statusCount = nginx_collection.count_documents({'path': '/status'})
    print(f"{statusCount} status check")
    print("IPs:")
    ipsAggregation = nginx_collection.aggregate(
        [
            {
                '$group': {'_id': '$ip', 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10
            }
        ])

    for ip in ipsAggregation:
        ip_request = ip['_id']
        ip_request_count = ip['totalRequests']
        print(f"\t{ip_request}: {ip_request_count}")
