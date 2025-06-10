import pandas as pd

def article_views(views: pd.DataFrame) -> pd.Series:
    df = views[views['author_id'] == views['viewer_id']]
    unique_id = df['author_id'].unique()
    return pd.DataFrame(unique_id, columns = ['id']).sort_values(by = ['id'])
