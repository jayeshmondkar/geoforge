def compute_visibility(total_queries, competitor_wins, target_wins):
    if total_queries == 0:
        return 0

    visibility = (target_wins / total_queries) * 100

    return round(visibility)