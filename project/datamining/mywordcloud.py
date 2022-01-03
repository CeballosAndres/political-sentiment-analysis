<<<<<<< HEAD
from matplotlib.colors import ListedColormap
import nltk
from nltk.corpus import stopwords
import pandas as pd
from wordcloud import WordCloud


class MyWordCloud:
    def __init__(self, comments=None):
        self.comments = comments.dropna()
        self.c_sw = pd.read_csv('project/datamining/cstm_stopwords.csv')
        # obtain a list of not wanted words in spanish (castellanno)
        self.stopwords_sp = set(stopwords.words('spanish'))
        # add our custom stopwords
        self.stopwords_sp.update(self.c_sw.words)


    def save_cloud(self, width, colormap, text, max_words, filename, height=775):
        # Create wordcloud object
        wordcloud_ = WordCloud(min_word_length=4, background_color='white', max_words=max_words, stopwords=self.stopwords_sp,
                               collocations=True, width=width, height=height, colormap=colormap).generate(text)
        # Save generated wordcloud as image in static folder
        wordcloud_.to_file('project/static/img/%s.png' % filename)

    def generate_wordcloud(self, max_words=30):
=======
import pandas as pd
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords

class MyWordCloud:
    def __init__(self, comments = None):  
        self.comments = comments.dropna()
        self.c_sw = pd.read_csv('./project/datamining/cstm_stopwords.csv')
        #obtain a list of not wanted words in spanish (castellanno)
        nltk.download('stopwords')
        self.stopwords_sp = set(stopwords.words('spanish'))
        #add our custom stopwords
        self.stopwords_sp.update(self.c_sw.words)

    def generate_wordcloud(self, max_words = 30):
>>>>>>> main
        # filter the candidate, and create a list of messages
        text = self.comments.message.tolist()
        text = map(str, text)
        # join the list and lowercase all the words
        text = ' '.join(text).lower()
<<<<<<< HEAD
        # Define custom Colormap
        cmap = ListedColormap(["#fd9d48", "#fd6648", "#ffd160"])
        # Call helper to save wordcloud images
        for filename, width in zip(["foo", "foo1"], [8424, 4039]):
            self.save_cloud(width, cmap, text, max_words, filename)
=======
        #create the wordcloud object
        wordcloud = WordCloud(min_word_length = 4, background_color='white', max_words=max_words,
                          stopwords = self.stopwords_sp, collocations=True, width=1920, height=1080).generate(text)
        return wordcloud.words_
>>>>>>> main


if __name__ == "__main__":
    path = './project/static/04 Datos Limpios.xlsx'
    df = pd.read_excel(path, sheet_name='Comments')
    wc = MyWordCloud(df)
<<<<<<< HEAD
    print(wc.generate_wordcloud())
=======
    print(wc.generate_wordcloud())
>>>>>>> main
