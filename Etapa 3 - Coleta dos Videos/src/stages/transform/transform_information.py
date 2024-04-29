import json
import re
from typing import Dict
from src.errors.transform_error import TransformError

class TransformInformation:

    def tranform(self) -> None:
        try:
            local = 'Etapa 3 - Coleta dos Videos\\src\\data\\transformed_data.json'
            
            with open('Etapa 3 - Coleta dos Videos\\src\\data\\extract_data.json', 'r', encoding='utf-8') as file:
                data = json.load(file)

            with open(local, 'w', encoding='utf-8') as file:
                file.write('')

            transformed_data = []
            with open(local, 'a', encoding='utf-8') as file:
                for channel_informations in data:
                    transformed_data.append(self.__filter(channel_informations))

                json.dump(transformed_data, file, ensure_ascii=False,indent=4)
        
        except Exception as exception:
            raise TransformError(str(exception)) from exception

    def __filter(self, channel_informations) -> Dict:
        essential_information = channel_informations['essential_information']
        transformed_data = {
            'video_id': channel_informations['video_id'],
            'channel': channel_informations['channel'],
            'extraction_date': channel_informations['extraction_date'],   
            'likes': self.__collect_likes(essential_information),
            'total_comments': self.__collect_total_comments(essential_information),
            'tags': self.__collect_tags(essential_information),
        }

        return transformed_data

    def __collect_likes(self,text) -> str:
        match = None
        match = re.search(r'>Inscrito</span></div>, <div class=\"yt-spec-button-shape-next__button-text-content\">(.{0,10}?)<',text, re.DOTALL)
        if match:
            likes = match.group(1)

            return likes
        
        return None

    def __collect_total_comments(self,text) -> str:
        match = None
        match = re.search(r'<span class=\"style-scope yt-formatted-string\" dir=\"auto\">(.{0,10}?)</span><span', text, re.DOTALL)
        if match:
            total_comments = match.group(1)
            return total_comments
        
        return None

    def __collect_tags(self,text) -> str:
        match = None
        match = re.findall(r'#(.{0,30}?)<',text, re.DOTALL)
        if match:
            comments = match
            return comments
        
        return None
