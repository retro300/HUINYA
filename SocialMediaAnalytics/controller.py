import pandas as pd
from models import Post

class DataController:
    def __init__(self, posts):
        self.df = pd.DataFrame([vars(post) for post in posts])
    
    def aggregate_data(self):
        result = {
            'total_posts': len(self.df),
            'average_likes': self.df['likes'].mean(),
            'average_dislikes': self.df['dislikes'].mean(),
            'max_likes': self.df['likes'].max(),
            'min_likes': self.df['likes'].min()
        }
        return result