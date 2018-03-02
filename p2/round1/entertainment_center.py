# -*- coding: utf-8 -*-

from fresh_tomatoes import open_movies_page
from media import Movie
import json
import sys
import os


movies_data = [{
    "title": u"看不见的客人",
    "poster_image_url": u"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2498971355.jpg",
    "story_line": u"艾德里安（马里奥·卡萨斯 Mario Casas 饰）经营着一间科技公司，事业蒸蒸日上，家中有美丽贤惠的妻子和活泼可爱的女儿，事业家庭双丰收的他是旁人羡慕的对象。然而，野心勃勃的艾德里安并未珍惜眼前来之不易的生活，一直以来，他和一位名叫劳拉（芭芭拉·蓝妮 Bárbara Lennie 饰）的女摄影师保持着肉体关系。\n某日幽会过后，两人驱车离开别墅，却在路上发生了车祸，为了掩盖事件的真相，两人决定将在车祸中死去的青年丹尼尔联同他的车一起沉入湖底。之后，劳拉遇见了一位善良的老人，老人将劳拉坏掉的车拉回家中修理，然而，令劳拉没有想到的是，这位老人，竟然就是丹尼尔的父亲。",
    "trailer_url": u"http://v.youku.com/v_show/id_XMjk5OTYyOTA1Mg==.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.2"
}, {
    "title": u"低俗小说",
    "poster_image_url": u"https://img3.doubanio.com/view/photo/s_ratio_poster/public/p1910902213.jpg",
    "story_line": u"《低俗小说》由“文森特和马沙的妻子”、“金表”、“邦妮的处境”三个故事以及影片首尾的序幕和尾声五个部分组成。看似独立的小故事里面，却又有环环相扣的人和事。\n盗贼“小南瓜”和“小兔子”在早餐店里打劫，却遇上了天大的麻烦——黑社会成员朱尔斯（塞缪尔•杰克逊Samuel L. Jackson饰）和文森特（约翰•特拉沃尔塔John Travolta饰）在店内用餐，可谓天外有天。二人是否会放过两名小盗贼？\n而文森特是黑社会大哥马沙•华莱士（文•瑞姆斯Ving Rhames饰）的手下，马沙下命令让他陪妻子一个晚上，明知如有雷池必死无疑，但面对马沙妻子美艳诱惑，文森特该怎么办。\n文森特的故事还没完，拳击手布奇（布鲁斯•威利斯Bruce Willis饰）的出现将令他的人生从此改变。布奇有一块祖传金表，就是因为这块金表，他和马沙分享了一个耻辱的秘密。",
    "trailer_url": u"http://v.youku.com/v_show/id_XMTcwODg4MDAzNg==.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.2"
}, {
    "title": u"寻梦环游记",
    "poster_image_url": u"https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2503997609.jpg",
    "story_line": u"热爱音乐的米格尔（安东尼·冈萨雷兹 Anthony Gonzalez 配音）不幸地出生在一个视音乐为洪水猛兽的大家庭之中，一家人只盼着米格尔快快长大，好继承家里传承了数代的制鞋产业。一年一度的亡灵节即将来临，每逢这一天，去世的亲人们的魂魄便可凭借着摆在祭坛上的照片返回现世和生者团圆。\n在一场意外中，米格尔竟然穿越到了亡灵国度之中，在太阳升起之前，他必须得到一位亲人的祝福，否则就将会永远地留在这个世界里。米格尔决定去寻找已故的歌神德拉库斯（本杰明·布拉特 Benjamin Bratt 配音），因为他很有可能就是自己的祖父。途中，米格尔邂逅了落魄乐手埃克托（盖尔·加西亚·贝纳尔 Gael García Bernal 配音），也渐渐发现了德拉库斯隐藏已久的秘密。",
    "trailer_url": u"http://v.youku.com/v_show/id_XMzE4Nzc5MTE5Mg==.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.1"
}]


class EntertainmentCenter():
    def __init__(self, movies_data=None):
        self.movies = []
        for m in movies_data:
            title = m['title']
            story_line = m['story_line']
            poster_image_url = m['poster_image_url']
            trailer_url = m['trailer_url']
            if sys.version < '3':
                title = title.encode('utf8')
                story_line = story_line.encode('utf8')
                poster_image_url = poster_image_url.encode('utf8')
                trailer_url = trailer_url.encode('utf8')
            movie = Movie(title,story_line,poster_image_url,trailer_url)
            self.movies.append(movie)
    
    def play(self):
        open_movies_page(self.movies)


if __name__ == '__main__':
    e_center = EntertainmentCenter(movies_data)
    e_center.play()