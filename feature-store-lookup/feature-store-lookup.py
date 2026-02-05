def feature_store_lookup(feature_store, requests, defaults):
    """
    Join offline user features with online request-time features.
    """
    # We have the feature store (which is old), we have requests which are new and defaults as per when we have a new user
    results = []

    for request in requests:
        user_id = request["user_id"]

        offline = feature_store.get(user_id, defaults)
        online = request["online_features"]

        combined = {**offline, **online}
        results.append(combined)

    return results
