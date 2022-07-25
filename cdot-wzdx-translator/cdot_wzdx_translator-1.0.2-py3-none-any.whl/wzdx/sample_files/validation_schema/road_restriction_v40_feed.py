road_restriction_v40_schema_string = {
    "$id": "https://raw.githubusercontent.com/usdot-jpo-ode/wzdx/main/schemas/4.0/RoadRestrictionFeed.json",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "WZDx v4.0 Road Restriction Feed",
    "description": "The GeoJSON output of a WZDx road restriction data feed (v4.0)",
    "type": "object",
    "properties": {
        "feed_info": {
            "$ref": "https://raw.githubusercontent.com/usdot-jpo-ode/wzdx/main/schemas/4.0/FeedInfo.json"
        },
        "type": {
            "description": "The GeoJSON type",
            "enum": [
                "FeatureCollection"
            ]
        },
        "features": {
            "description": "An array of GeoJSON Feature objects which represent WZDx restriction road events",
            "type": "array",
            "items": {
                "allOf": [
                    {
                        "properties": {
                            "properties": {
                                "properties": {
                                    "core_details": {
                                        "properties": {
                                            "event_type": {
                                                "const": "restriction"
                                            }
                                        },
                                        "required": ["event_type"]
                                    }
                                },
                                "required": ["core_details"]
                            }
                        },
                        "required": ["properties"]
                    },
                    {
                        "$ref": "https://raw.githubusercontent.com/usdot-jpo-ode/wzdx/main/schemas/4.0/RoadEventFeature.json"
                    }
                ]
            }
        },
        "bbox": {
            "$ref": "https://raw.githubusercontent.com/usdot-jpo-ode/wzdx/main/schemas/4.0/BoundingBox.json"
        }
    },
    "required": [
        "feed_info",
        "type",
        "features"
    ]
}
