'''Transformação dos Dados'''
import re
from src.contracts.extract_contract import ExtractContract
from src.contracts.transform_contract import TransformContract
from src.errors.transform_error import TransformError

class TransformHtml:
    '''Classe responsável por receber o o ExtractContract para aplicar transformação e devolver o TransformContract'''
    def transform(self, extract_contract: ExtractContract):
        try:
            transformed_information = self.__filter(extract_contract)

            transfomed_data_contract = TransformContract(
                load_content=transformed_information
            )
            return transfomed_data_contract
        
        except Exception as exception:
            raise TransformError(str(exception)) from exception

    def __filter(self, extract_contract: ExtractContract):
        raw_information = extract_contract.raw_information
        extraction_date = extract_contract.extraction_date

        transfomed_information = []

        for data in raw_information:
            transformed_data = {
                "title": self.__collect_title(data),
                "channel": self.__collect_channel_name(data),
                "channel_link": self.__collect_chanell_link(data),
                "video_link": self.__collect_video_link(data),
                "views": self.__collect_views(data),
                "video_time": self.__collect_video_time(data),
                "time_online": self.__collect_time_online(data),
                "extraction_date": extraction_date
            }
            
            transfomed_information.append(transformed_data)

        return transfomed_information

    def __collect_title(self, text):
        match = None
        match = re.search(r'title="([^"]+)"', text)
        if match:
            title = match.group(1)
            return title
        
        return None
    
    def __collect_channel_name(self, text):
        match = None
        if text != None:
            match = re.search('" style="text-align: left;" title="([^"]*)"', text)
        if match:
            channel_name = match.group(1)
            return channel_name
        
        return None
        
    def __collect_chanell_link(self, text):
        match = None
        match = re.search('"><a class="yt-simple-endpoint style-scope yt-formatted-string" href="([^"]*)"', text)
        if match:
            href = 'https://www.youtube.com' + match.group(1)      
            return href
        
        return None
    
    def __collect_video_link(self, text):
        match = None
        match = re.search('class="yt-simple-endpoint style-scope ytd-video-renderer" href="([^"]*)"', text)
        if match:
            href = 'https://www.youtube.com' + match.group(1)      
            return href
        
        return None
    
    def __collect_views(self, text):
        match = None
        match = re.search(r'(\d{1,3}(?:\.\d{3})*(?:,\d+)?) visualizações', text)
        if match:
            views = match.group(1).replace(".", "").replace(",", ".")
            views = int(views)
            return views
        
        return None
    
    def __collect_video_time(self,text):
        match = None
        match = re.search(r'</div>time="([^"]+)"', text)
        if match:
            video_time = match.group(1)      
            return video_time
        
        return None
    
    def __collect_time_online(self, text):
        match = None
        match = re.search(r'há (.{1,50}?)"', text)
        if match:
            time_online = match.group(1)
            return time_online
            
        return None