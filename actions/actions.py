# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionFacilitySearch(Action):

    def name(self) -> Text:
        return "action_facility_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        facility_address = {
            "Hà Nội": "Bệnh viện Bạch Mai, 78 Giải Phóng, Đồng Tâm, Hai Bà Trưng, Hà Nội",
            "Thái Nguyên": "Bệnh viện Đa khoa Trung ương Thái Nguyên, 479 Lương Ngọc Quyến, Phan Đình Phùng, Thành phố Thái Nguyên",
            "Đồng Nai": "Bệnh viện Đa khoa tỉnh Đồng Nai, Số 02 - Đường Đồng Khởi, Phường Tam Hòa, TP Biên Hòa, Đồng Nai",
            "Khánh Hòa": "Bệnh viện Bệnh nhiệt đới Khánh Hòa, 7455+3M2, Diên An, Diên Khánh, Khánh Hòa",
            "Thái Bình": "Bệnh viện Đa khoa tỉnh Thái Bình, 530 Lý Bôn, P. Quan Trung, Thái Bình",
            "Lạng Sơn": "Bệnh viện Đa khoa tỉnh Lạng Sơn, Thôn Đại Sơn Xã, Hợp Thành, Cao Lộc, Lạng Sơn",
            "Huế": "Bệnh viện Đa khoa Trung ương Huế, 16 Lê Lợi - TP Huế",
            "Cần Thơ": "Bệnh viện Trung ương Cần Thơ, 315 Đường Nguyễn Văn Linh, Phường An Khánh, Ninh Kiều, Cần Thơ",
        }
        facility = tracker.get_slot("facility_type")
        location = tracker.get_slot("location")
        address = facility_address.get(location)
        dispatcher.utter_message(text=f"Đây là địa chỉ của {facility}: {address}")

        return [SlotSet("address", address)]


class BotInformAboutSymptomp(Action):

    def name(self) -> Text:
        return "bot_inform_about_symptomp"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):

        dispatcher.utter_message(text="Ok. bạn đợi tí, để mình viết ra.")
        dispatcher.utter_message(text="Đây nhé, hơi dài. Nhưng mình tóm tắt lại phần nào rồi.")
        dispatcher.utter_message(text="Các triệu chứng thường gặp nhất: sốt, ho, mệt mỏi, mất vị giác hoặc khứu giác.")
        dispatcher.utter_message(text="""Các triệu chứng ít gặp hơn: đau đầu, đau họng, đau nhức, tiêu chảy, da nổi mẩn
                                         hay ngón tay hoặc ngón chân bị tấy đỏ hoặc tím tái, mắt đỏ hoặc ngứa.""")
        dispatcher.utter_message(text="""Các triệu chứng nghiêm trọng: khó thở, mất khả năng nói hay cử động hoặc thấy
                                        lú lẫn, đau ngực.""")



