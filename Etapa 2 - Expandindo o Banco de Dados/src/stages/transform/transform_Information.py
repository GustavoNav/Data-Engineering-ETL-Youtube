import json
import re
from typing import Dict
from src.errors.transform_error import TransformError

class TransformInformation:

    def tranform(self):
        try:
            with open('Etapa 2 - Expandindo o Banco de Dados\\src\\data\\extract_data.json', 'r', encoding='utf-8') as file:
                data = json.load(file)

            with open('Etapa 2 - Expandindo o Banco de Dados\\src\\data\\transformed_data.json', 'w', encoding='utf-8') as file:
                file.write('')

            transformed_data = []
            with open('Etapa 2 - Expandindo o Banco de Dados\\src\\data\\transformed_data.json', 'a', encoding='utf-8') as file:
                for channel_informations in data:
                    transformed_data.append(self.__filter(channel_informations))

                json.dump(transformed_data, file, ensure_ascii=False,indent=4)
        
        except Exception as exception:
            raise TransformError(str(exception)) from exception

    def __filter(self, channel_informations) -> Dict:
        essential_information = channel_informations['essential_information']
        transformed_data = {
            'channel': channel_informations['channel'],
            'extraction_date': channel_informations['extraction_date'],   
            'creation_date': self.__collect_creation_date(essential_information),
            'channel_location': self.__collect_channel_location(essential_information),
            'subscriptions': self.__collect_subscriptions(essential_information),
            'total_videos': self.__collect_total_videos(essential_information),
            'total_views': self.__collect_total_views(essential_information),
            'about': self.__collect_about(essential_information)
        }

        return transformed_data

    def __collect_creation_date(self,text) -> str:
        match = None
        match = re.search(r'<span class=\"\" style=\"\">Inscreveu-se em(.{0,50}?)</span></span></yt-attributed-string>', text,re.DOTALL)
        if match:
            creation_date = match.group(1)
            return creation_date
        
        return None

    def __collect_channel_location(self,text) -> str:
        match = None
        match = re.search(r'</icon-shape></yt-icon-shape></yt-icon>\n</td>\n<td class=\"style-scope ytd-about-channel-renderer\">(.{0,30}?)</td>\n</tr>\n</tbody></table>', text, re.DOTALL)
        if match:
            location = match.group(1)
            return location
        
        return None

    def __collect_subscriptions(self,text) -> str:
        match = None
        match = re.search(r'</td>\n<td class=\"style-scope ytd-about-channel-renderer\">(.{0,50}?)inscritos',text, re.DOTALL)
        if match:
            total_subscriptions = match.group(1).replace('de', '').replace('\u00a0', ' ')
            total_subscriptions = total_subscriptions.strip()
            return total_subscriptions
        
        return None

    def __collect_total_videos(self,text) -> str:
        match = None
        match = re.search(r'<td class="style-scope ytd-about-channel-renderer">(.{0,50}?)vídeos</td>', text, re.DOTALL)
        if match:
            total_videos = match.group(1).strip()
            return total_videos
        
        return None

    def __collect_total_views(self,text) -> str:
        match = None
        match = re.search(r'<td class="style-scope ytd-about-channel-renderer">(.{0,50}?)visualizações</td>', text, re.DOTALL)
        if match:
            total_views = match.group(1).strip()
            return total_views

        return None
    
    def __collect_about(self, text) -> str:
        match = None
        match = re.search(r'<span class=\"yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap\" role=\"text\">(.*?)</span>', text, re.DOTALL)
        if match:
            about = match.group(1).replace('\n', ' ')
            return about
        
        return None