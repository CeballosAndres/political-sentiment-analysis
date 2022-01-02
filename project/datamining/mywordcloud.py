from matplotlib.colors import ListedColormap
import nltk
from nltk.corpus import stopwords
import pandas as pd
from wordcloud import WordCloud


class MyWordCloud:
    def __init__(self, comments=None):
        self.comments = comments.dropna()
        self.c_sw = pd.read_csv('cstm_stopwords.csv')
        # obtain a list of not wanted words in spanish (castellanno)
        nltk.download('stopwords')
        self.stopwords_sp = set(stopwords.words('spanish'))
        # add our custom stopwords
        self.stopwords_sp.update(self.c_sw.words)


    def save_cloud(self, width, colormap, text, max_words, filename, height=775):
        # Create wordcloud object
        wordcloud_ = WordCloud(min_word_length=4, background_color='white', max_words=max_words, stopwords=self.stopwords_sp,
                               collocations=True, width=width, height=height, colormap=colormap).generate(text)
        # Save generated wordcloud as image in static folder
        wordcloud_.to_file('../static/img/%s.png' % filename)

    def generate_wordcloud(self, max_words=30):
        # filter the candidate, and create a list of messages
        text = self.comments.message.tolist()
        text = map(str, text)
        # join the list and lowercase all the words
        text = ' '.join(text).lower()
        # Define custom Colormap
        cmap = ListedColormap(["#fd9d48", "#fd6648", "#ffd160"])
        # Call helper to save wordcloud images
        for filename, width in zip(["foo", "foo1"], [6424, 3039]):
            self.save_cloud(width, cmap, text, max_words, filename)


if __name__ == "__main__":
    path = './project/static/04 Datos Limpios.xlsx'
    df = pd.read_excel(path, sheet_name='Comments')
    wc = MyWordCloud(df)
    print(wc.generate_wordcloud())
