from bs4 import BeautifulSoup

class HtmlCollector:
    @classmethod
    def collect_essential_information(cls, html: str) -> str:
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.find('ytd-app')
        likes = body.find_all('div',class_='yt-spec-button-shape-next__button-text-content')
        total_comments = body.find_all('yt-formatted-string', class_='count-text style-scope ytd-comments-header-renderer')
        comments = body.find_all('ytd-comment-thread-renderer', class_='style-scope ytd-item-section-renderer')
        
        
        essential_information = str(likes) + str(total_comments) +str(comments)
        return essential_information