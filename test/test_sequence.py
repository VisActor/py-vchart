import unittest
from unittest.mock import patch

from pyvchart import options as opts
from pyvchart.charts import Bar, Dot, Link, Sequence
from pyvchart.commons.utils import JsCode
from pyvchart.globals import ChartType

TEST_REGISTER_DATA = [
    {"start_time": 1662300000, "end_time": 1662303600, "value": 1},
    {"start_time": 1662501600, "end_time": 1662505200, "value": 1},
]
TEST_IM_DATA = [
    {"start_time": 1662177600, "end_time": 1662181200, "value": 1},
    {"start_time": 1662210000, "end_time": 1662213600, "value": 1},
    {"start_time": 1662246000, "end_time": 1662249600, "value": 1},
    {"start_time": 1662278400, "end_time": 1662282000, "value": 1},
    {"start_time": 1662310800, "end_time": 1662314400, "value": 1},
    {"start_time": 1662343200, "end_time": 1662346800, "value": 1},
    {"start_time": 1662379200, "end_time": 1662382800, "value": 1},
    {"start_time": 1662411600, "end_time": 1662415200, "value": 1},
    {"start_time": 1662444000, "end_time": 1662447600, "value": 1},
]
TEST_COMMENT_DATA = [
    {"start_time": 1662048000, "end_time": 1662051600, "value": 0},
    {"start_time": 1662051600, "end_time": 1662055200, "value": 0},
    {"start_time": 1662055200, "end_time": 1662058800, "value": 0},
    {"start_time": 1662058800, "end_time": 1662062400, "value": 0},
    {"start_time": 1662062400, "end_time": 1662066000, "value": 0},
    {"start_time": 1662066000, "end_time": 1662069600, "value": 0},
    {"start_time": 1662069600, "end_time": 1662073200, "value": 0},
    {"start_time": 1662073200, "end_time": 1662076800, "value": 0},
    {"start_time": 1662076800, "end_time": 1662080400, "value": 1},
    {"start_time": 1662080400, "end_time": 1662084000, "value": 0},
    {"start_time": 1662084000, "end_time": 1662087600, "value": 0},
    {"start_time": 1662087600, "end_time": 1662091200, "value": 0},
    {"start_time": 1662091200, "end_time": 1662094800, "value": 0},
    {"start_time": 1662094800, "end_time": 1662098400, "value": 0},
    {"start_time": 1662098400, "end_time": 1662102000, "value": 0},
    {"start_time": 1662102000, "end_time": 1662105600, "value": 0},
    {"start_time": 1662105600, "end_time": 1662109200, "value": 0},
    {"start_time": 1662109200, "end_time": 1662112800, "value": 0},
    {"start_time": 1662112800, "end_time": 1662116400, "value": 0},
    {"start_time": 1662116400, "end_time": 1662120000, "value": 0},
    {"start_time": 1662120000, "end_time": 1662123600, "value": 0},
    {"start_time": 1662123600, "end_time": 1662127200, "value": 0},
    {"start_time": 1662127200, "end_time": 1662130800, "value": 1},
    {"start_time": 1662130800, "end_time": 1662134400, "value": 0},
    {"start_time": 1662134400, "end_time": 1662138000, "value": 0},
    {"start_time": 1662138000, "end_time": 1662141600, "value": 0},
    {"start_time": 1662141600, "end_time": 1662145200, "value": 0},
    {"start_time": 1662145200, "end_time": 1662148800, "value": 0},
    {"start_time": 1662148800, "end_time": 1662152400, "value": 0},
    {"start_time": 1662152400, "end_time": 1662156000, "value": 0},
    {"start_time": 1662156000, "end_time": 1662159600, "value": 0},
    {"start_time": 1662159600, "end_time": 1662163200, "value": 0},
    {"start_time": 1662163200, "end_time": 1662166800, "value": 0},
    {"start_time": 1662166800, "end_time": 1662170400, "value": 0},
    {"start_time": 1662170400, "end_time": 1662174000, "value": 0},
    {"start_time": 1662174000, "end_time": 1662177600, "value": 0},
    {"start_time": 1662177600, "end_time": 1662181200, "value": 1},
    {"start_time": 1662181200, "end_time": 1662184800, "value": 0},
    {"start_time": 1662184800, "end_time": 1662188400, "value": 0},
    {"start_time": 1662188400, "end_time": 1662192000, "value": 0},
    {"start_time": 1662192000, "end_time": 1662195600, "value": 0},
    {"start_time": 1662195600, "end_time": 1662199200, "value": 0},
    {"start_time": 1662199200, "end_time": 1662202800, "value": 0},
    {"start_time": 1662202800, "end_time": 1662206400, "value": 0},
    {"start_time": 1662206400, "end_time": 1662210000, "value": 0},
    {"start_time": 1662210000, "end_time": 1662213600, "value": 0},
    {"start_time": 1662213600, "end_time": 1662217200, "value": 0},
    {"start_time": 1662217200, "end_time": 1662220800, "value": 0},
    {"start_time": 1662220800, "end_time": 1662224400, "value": 0},
    {"start_time": 1662224400, "end_time": 1662228000, "value": 0},
    {"start_time": 1662228000, "end_time": 1662231600, "value": 1},
    {"start_time": 1662231600, "end_time": 1662235200, "value": 0},
    {"start_time": 1662235200, "end_time": 1662238800, "value": 0},
    {"start_time": 1662238800, "end_time": 1662242400, "value": 0},
    {"start_time": 1662242400, "end_time": 1662246000, "value": 0},
    {"start_time": 1662246000, "end_time": 1662249600, "value": 0},
    {"start_time": 1662249600, "end_time": 1662253200, "value": 0},
    {"start_time": 1662253200, "end_time": 1662256800, "value": 0},
    {"start_time": 1662256800, "end_time": 1662260400, "value": 0},
    {"start_time": 1662260400, "end_time": 1662264000, "value": 0},
    {"start_time": 1662264000, "end_time": 1662267600, "value": 0},
    {"start_time": 1662267600, "end_time": 1662271200, "value": 0},
    {"start_time": 1662271200, "end_time": 1662274800, "value": 0},
    {"start_time": 1662274800, "end_time": 1662278400, "value": 0},
    {"start_time": 1662278400, "end_time": 1662282000, "value": 1},
    {"start_time": 1662282000, "end_time": 1662285600, "value": 0},
    {"start_time": 1662285600, "end_time": 1662289200, "value": 0},
    {"start_time": 1662289200, "end_time": 1662292800, "value": 0},
    {"start_time": 1662292800, "end_time": 1662296400, "value": 0},
    {"start_time": 1662296400, "end_time": 1662300000, "value": 0},
    {"start_time": 1662300000, "end_time": 1662303600, "value": 0},
    {"start_time": 1662303600, "end_time": 1662307200, "value": 0},
    {"start_time": 1662307200, "end_time": 1662310800, "value": 0},
    {"start_time": 1662310800, "end_time": 1662314400, "value": 0},
    {"start_time": 1662314400, "end_time": 1662318000, "value": 0},
    {"start_time": 1662318000, "end_time": 1662321600, "value": 0},
    {"start_time": 1662321600, "end_time": 1662325200, "value": 0},
    {"start_time": 1662325200, "end_time": 1662328800, "value": 0},
    {"start_time": 1662328800, "end_time": 1662332400, "value": 1},
    {"start_time": 1662332400, "end_time": 1662336000, "value": 0},
    {"start_time": 1662336000, "end_time": 1662339600, "value": 0},
    {"start_time": 1662339600, "end_time": 1662343200, "value": 0},
    {"start_time": 1662343200, "end_time": 1662346800, "value": 0},
    {"start_time": 1662346800, "end_time": 1662350400, "value": 0},
    {"start_time": 1662350400, "end_time": 1662354000, "value": 0},
    {"start_time": 1662354000, "end_time": 1662357600, "value": 0},
    {"start_time": 1662357600, "end_time": 1662361200, "value": 0},
    {"start_time": 1662361200, "end_time": 1662364800, "value": 0},
    {"start_time": 1662364800, "end_time": 1662368400, "value": 0},
    {"start_time": 1662368400, "end_time": 1662372000, "value": 0},
    {"start_time": 1662372000, "end_time": 1662375600, "value": 0},
    {"start_time": 1662375600, "end_time": 1662379200, "value": 0},
    {"start_time": 1662379200, "end_time": 1662382800, "value": 1},
    {"start_time": 1662382800, "end_time": 1662386400, "value": 0},
    {"start_time": 1662386400, "end_time": 1662390000, "value": 0},
    {"start_time": 1662390000, "end_time": 1662393600, "value": 0},
    {"start_time": 1662393600, "end_time": 1662397200, "value": 0},
    {"start_time": 1662397200, "end_time": 1662400800, "value": 0},
    {"start_time": 1662400800, "end_time": 1662404400, "value": 0},
    {"start_time": 1662404400, "end_time": 1662408000, "value": 0},
    {"start_time": 1662408000, "end_time": 1662411600, "value": 0},
    {"start_time": 1662411600, "end_time": 1662415200, "value": 0},
    {"start_time": 1662415200, "end_time": 1662418800, "value": 0},
    {"start_time": 1662418800, "end_time": 1662422400, "value": 0},
    {"start_time": 1662422400, "end_time": 1662426000, "value": 0},
    {"start_time": 1662426000, "end_time": 1662429600, "value": 0},
    {"start_time": 1662429600, "end_time": 1662433200, "value": 1},
    {"start_time": 1662433200, "end_time": 1662436800, "value": 0},
    {"start_time": 1662436800, "end_time": 1662440400, "value": 0},
    {"start_time": 1662440400, "end_time": 1662444000, "value": 0},
    {"start_time": 1662444000, "end_time": 1662447600, "value": 0},
    {"start_time": 1662447600, "end_time": 1662451200, "value": 0},
    {"start_time": 1662451200, "end_time": 1662454800, "value": 0},
    {"start_time": 1662454800, "end_time": 1662458400, "value": 0},
    {"start_time": 1662458400, "end_time": 1662462000, "value": 0},
    {"start_time": 1662462000, "end_time": 1662465600, "value": 0},
    {"start_time": 1662465600, "end_time": 1662469200, "value": 0},
    {"start_time": 1662469200, "end_time": 1662472800, "value": 0},
    {"start_time": 1662472800, "end_time": 1662476400, "value": 0},
    {"start_time": 1662476400, "end_time": 1662480000, "value": 0},
    {"start_time": 1662480000, "end_time": 1662483600, "value": 0},
    {"start_time": 1662483600, "end_time": 1662487200, "value": 0},
    {"start_time": 1662487200, "end_time": 1662490800, "value": 0},
    {"start_time": 1662490800, "end_time": 1662494400, "value": 0},
    {"start_time": 1662494400, "end_time": 1662498000, "value": 0},
    {"start_time": 1662498000, "end_time": 1662501600, "value": 0},
    {"start_time": 1662501600, "end_time": 1662505200, "value": 0},
    {"start_time": 1662505200, "end_time": 1662508800, "value": 0},
    {"start_time": 1662508800, "end_time": 1662512400, "value": 0},
    {"start_time": 1662512400, "end_time": 1662516000, "value": 0},
    {"start_time": 1662516000, "end_time": 1662519600, "value": 0},
    {"start_time": 1662519600, "end_time": 1662523200, "value": 0},
    {"start_time": 1662523200, "end_time": 1662526800, "value": 0},
    {"start_time": 1662526800, "end_time": 1662530400, "value": 0},
    {"start_time": 1662530400, "end_time": 1662534000, "value": 0},
    {"start_time": 1662534000, "end_time": 1662537600, "value": 0},
    {"start_time": 1662537600, "end_time": 1662541200, "value": 0},
    {"start_time": 1662541200, "end_time": 1662544800, "value": 0},
    {"start_time": 1662544800, "end_time": 1662548400, "value": 0},
    {"start_time": 1662548400, "end_time": 1662552000, "value": 0},
    {"start_time": 1662552000, "end_time": 1662555600, "value": 0},
    {"start_time": 1662555600, "end_time": 1662559200, "value": 0},
    {"start_time": 1662559200, "end_time": 1662562800, "value": 0},
    {"start_time": 1662562800, "end_time": 1662566400, "value": 0},
    {"start_time": 1662566400, "end_time": 1662570000, "value": 0},
    {"start_time": 1662570000, "end_time": 1662573600, "value": 0},
    {"start_time": 1662573600, "end_time": 1662577200, "value": 0},
    {"start_time": 1662577200, "end_time": 1662580800, "value": 0},
    {"start_time": 1662580800, "end_time": 1662584400, "value": 0},
    {"start_time": 1662584400, "end_time": 1662588000, "value": 0},
    {"start_time": 1662588000, "end_time": 1662591600, "value": 0},
    {"start_time": 1662591600, "end_time": 1662595200, "value": 0},
    {"start_time": 1662595200, "end_time": 1662598800, "value": 0},
    {"start_time": 1662598800, "end_time": 1662602400, "value": 0},
    {"start_time": 1662602400, "end_time": 1662606000, "value": 0},
    {"start_time": 1662606000, "end_time": 1662609600, "value": 0},
    {"start_time": 1662609600, "end_time": 1662613200, "value": 0},
    {"start_time": 1662613200, "end_time": 1662616800, "value": 0},
    {"start_time": 1662616800, "end_time": 1662620400, "value": 0},
    {"start_time": 1662620400, "end_time": 1662624000, "value": 0},
    {"start_time": 1662624000, "end_time": 1662627600, "value": 0},
    {"start_time": 1662627600, "end_time": 1662631200, "value": 0},
    {"start_time": 1662631200, "end_time": 1662634800, "value": 0},
    {"start_time": 1662634800, "end_time": 1662638400, "value": 0},
    {"start_time": 1662638400, "end_time": 1662642000, "value": 0},
    {"start_time": 1662642000, "end_time": 1662645600, "value": 0},
    {"start_time": 1662645600, "end_time": 1662649200, "value": 0},
    {"start_time": 1662649200, "end_time": 1662652800, "value": 0},
    {"start_time": 1662652800, "end_time": 1662656400, "value": 0},
]
TEST_DATA_DOT_SERIES_DATA = [
    {
        "id": "713019502467512xxxx",
        "type": "user_did",
        "dots": [
            {
                "event_time": 1662061124,
                "node_name": "713019502467512xxxx_1662061124_login_device",
                "action_type": "login_device",
                "children": [{"action_type": "login_device"}],
            }
        ],
    },
    {
        "id": "683827422612367xxxx",
        "type": "user_did",
        "dots": [
            {
                "event_time": 1662321122,
                "node_name": "683827422612367xxxx_1662321122_login_device",
                "action_type": "login_device",
                "children": [{"action_type": "login_device"}],
            },
            {
                "event_time": 1662301120,
                "node_name": "683827422612367xxxx_1662301120_registry_device",
                "action_type": "registry_device",
                "children": [{"action_type": "registry_device"}],
            },
            {
                "event_time": 1662503541,
                "node_name": "683827422612367xxxx_1662503541_registry_device",
                "action_type": "registry_device",
                "children": [{"action_type": "registry_device"}],
            },
            {
                "event_time": 1662311121,
                "node_name": "683827422612367xxxx_1662311121_login_device",
                "action_type": "login_device",
                "children": [{"action_type": "login_device"}],
            },
            {
                "event_time": 1662161125,
                "node_name": "683827422612367xxxx_1662161125_login_device",
                "action_type": "login_device",
                "children": [{"action_type": "login_device"}],
            },
        ],
    },
    {
        "id": "bcb395f84ae8882de39d2a8e68d459c177a7b5a0b6884047b0fce1f28d21xxxx",
        "type": "user_email",
        "dots": [
            {
                "event_time": 1662331123,
                "node_name": "bcb395f84ae8882de39d2a8e68d459c177a7b5a0b"
                "6884047b0fce1f28d21xxxx_1662331123_binding_email",
                "action_type": "binding_email",
                "children": [{"action_type": "binding_email"}],
            }
        ],
    },
    {
        "id": "93.23.xxx.xx_20200615",
        "type": "IP",
        "dots": [
            {
                "event_time": 1662361127,
                "node_name": "93.23.xxx.xx_20200615_1662361127_registry_ip",
                "action_type": "registry_ip",
                "children": [{"action_type": "registry_ip"}],
            }
        ],
    },
    {
        "id": "683827957407865xxxx",
        "type": "user_id",
        "dots": [
            {
                "event_time": 1662311121,
                "node_name": "683827957407865xxxx_1662311121_login_device",
                "action_type": "login_device",
                "children": [{"action_type": "login_device"}],
            }
        ],
    },
    {
        "id": "713019589280868xxxx",
        "type": "user_id",
        "dots": [
            {
                "event_time": 1662061124,
                "node_name": "713019589280868xxxx_1662061124_login_device",
                "action_type": "login_device",
                "children": [{"action_type": "login_device"}],
            }
        ],
    },
    {
        "id": "25328254226993xxxx",
        "type": "user_id",
        "dots": [
            {
                "event_time": 1662321122,
                "node_name": "25328254226993xxxx_1662321122_login_device",
                "action_type": "login_device",
                "children": [{"action_type": "login_device"}],
            }
        ],
    },
    {
        "id": "683827420033672xxxx",
        "type": "user_id",
        "dots": [
            {
                "event_time": 1662346668,
                "node_name": "683827420033672xxxx_1662346668_im",
                "action_type": "im",
                "children": [{"action_type": "im", "msg_id": 800000}],
            },
            {
                "event_time": 1662480000,
                "node_name": "683827420033672xxxx_1662480000_combine",
                "action_type": "combine",
                "children": [
                    {"action_type": "invite", "placeholder": '"placeholder"'},
                    {"action_type": "invite", "placeholder": '"placeholder"'},
                    {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
                    {
                        "action_type": "report",
                        "content": "report context in string",
                        "report_type": "user",
                        "target": "user_id",
                    },
                    {"action_type": "follow", "is_unfollow": False, "source": 1},
                    {"action_type": "invite", "placeholder": '"placeholder"'},
                    {"action_type": "follow", "is_unfollow": False, "source": 1},
                    {"action_type": "invite", "placeholder": '"placeholder"'},
                    {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
                    {
                        "action_type": "report",
                        "content": "report context in string",
                        "report_type": "user",
                        "target": "user_id",
                    },
                    {"action_type": "invite", "placeholder": '"placeholder"'},
                    {"action_type": "follow", "is_unfollow": False, "source": 1},
                    {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
                    {"action_type": "follow", "is_unfollow": False, "source": 1},
                    {
                        "action_type": "report",
                        "content": "report context in string",
                        "report_type": "user",
                        "target": "user_id",
                    },
                    {"action_type": "follow", "is_unfollow": False, "source": 1},
                    {
                        "action_type": "report",
                        "content": "report context in string",
                        "report_type": "user",
                        "target": "user_id",
                    },
                    {
                        "action_type": "report",
                        "content": "report context in string",
                        "report_type": "user",
                        "target": "user_id",
                    },
                    {
                        "action_type": "report",
                        "content": "report context in string",
                        "report_type": "user",
                        "target": "user_id",
                    },
                    {"action_type": "invite", "placeholder": '"placeholder"'},
                    {"action_type": "follow", "is_unfollow": False, "source": 1},
                    {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
                    {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
                    {"action_type": "invite", "placeholder": '"placeholder"'},
                    {"action_type": "follow", "is_unfollow": False, "source": 1},
                    {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
                    {
                        "action_type": "report",
                        "content": "report context in string",
                        "report_type": "user",
                        "target": "user_id",
                    },
                    {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
                    {"action_type": "invite", "placeholder": '"placeholder"'},
                    {"action_type": "follow", "is_unfollow": False, "source": 1},
                    {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
                    {
                        "action_type": "report",
                        "content": "report context in string",
                        "report_type": "user",
                        "target": "user_id",
                    },
                ],
            },
            {
                "event_time": 1662380000,
                "node_name": "683827420033672xxxx_1662380000_comment",
                "action_type": "comment",
                "children": [
                    {
                        "action_type": "comment",
                        "comment_id": 3000,
                        "content": "some comment from tiktok user",
                        "video_id": 90000001,
                        "is_delete": False,
                    }
                ],
            },
            {
                "event_time": 1662280000,
                "node_name": "683827420033672xxxx_1662280000_comment",
                "action_type": "comment",
                "children": [
                    {
                        "action_type": "comment",
                        "comment_id": 3000,
                        "content": "some comment from tiktok user",
                        "video_id": 90000001,
                        "is_delete": False,
                    }
                ],
            },
            {
                "event_time": 1662246669,
                "node_name": "683827420033672xxxx_1662246669_im",
                "action_type": "im",
                "children": [{"action_type": "im", "msg_id": 800000}],
            },
            {
                "event_time": 1662380001,
                "node_name": "683827420033672xxxx_1662380001_im",
                "action_type": "im",
                "children": [{"action_type": "im", "msg_id": 800000}],
            },
            {
                "event_time": 1662130000,
                "node_name": "683827420033672xxxx_1662130000_comment",
                "action_type": "comment",
                "children": [
                    {
                        "action_type": "comment",
                        "comment_id": 3000,
                        "content": "some comment from tiktok user",
                        "video_id": 90000001,
                        "is_delete": False,
                    }
                ],
            },
            {
                "event_time": 1662080000,
                "node_name": "683827420033672xxxx_1662080000_comment",
                "action_type": "comment",
                "children": [
                    {
                        "action_type": "comment",
                        "comment_id": 3000,
                        "content": "some comment from tiktok user",
                        "video_id": 90000001,
                        "is_delete": False,
                    }
                ],
            },
            {
                "event_time": 1662413334,
                "node_name": "683827420033672xxxx_1662413334_im",
                "action_type": "im",
                "children": [{"action_type": "im", "msg_id": 800000}],
            },
            {
                "event_time": 1662313335,
                "node_name": "683827420033672xxxx_1662313335_im",
                "action_type": "im",
                "children": [{"action_type": "im", "msg_id": 800000}],
            },
            {
                "event_time": 1662230000,
                "node_name": "683827420033672xxxx_1662230000_comment",
                "action_type": "comment",
                "children": [
                    {
                        "action_type": "comment",
                        "comment_id": 3000,
                        "content": "some comment from tiktok user",
                        "video_id": 90000001,
                        "is_delete": False,
                    }
                ],
            },
            {
                "event_time": 1662503541,
                "node_name": "683827420033672xxxx_1662503541_registry_device",
                "action_type": "registry_device",
                "children": [{"action_type": "registry_device"}],
            },
            {
                "event_time": 1662180000,
                "node_name": "683827420033672xxxx_1662180000_comment",
                "action_type": "comment",
                "children": [
                    {
                        "action_type": "comment",
                        "comment_id": 3000,
                        "content": "some comment from tiktok user",
                        "video_id": 90000001,
                        "is_delete": False,
                    }
                ],
            },
            {
                "event_time": 1662430000,
                "node_name": "683827420033672xxxx_1662430000_comment",
                "action_type": "comment",
                "children": [
                    {
                        "action_type": "comment",
                        "comment_id": 3000,
                        "content": "some comment from tiktok user",
                        "video_id": 90000001,
                        "is_delete": False,
                    }
                ],
            },
            {
                "event_time": 1662446667,
                "node_name": "683827420033672xxxx_1662446667_im",
                "action_type": "im",
                "children": [{"action_type": "im", "msg_id": 800000}],
            },
            {
                "event_time": 1662280002,
                "node_name": "683827420033672xxxx_1662280002_im",
                "action_type": "im",
                "children": [{"action_type": "im", "msg_id": 800000}],
            },
            {
                "event_time": 1662180003,
                "node_name": "683827420033672xxxx_1662180003_im",
                "action_type": "im",
                "children": [{"action_type": "im", "msg_id": 800000}],
            },
            {
                "event_time": 1662213336,
                "node_name": "683827420033672xxxx_1662213336_im",
                "action_type": "im",
                "children": [{"action_type": "im", "msg_id": 800000}],
            },
            {
                "event_time": 1662330000,
                "node_name": "683827420033672xxxx_1662330000_comment",
                "action_type": "comment",
                "children": [
                    {
                        "action_type": "comment",
                        "comment_id": 3000,
                        "content": "some comment from tiktok user",
                        "video_id": 90000001,
                        "is_delete": False,
                    }
                ],
            },
            {
                "event_time": 1662161125,
                "node_name": "683827420033672xxxx_1662161125_login_device",
                "action_type": "login_device",
                "children": [{"action_type": "login_device"}],
            },
        ],
    },
    {
        "id": "683827468797481xxxx",
        "type": "user_id",
        "dots": [
            {
                "event_time": 1662346668,
                "node_name": "683827468797481xxxx_1662346668_im",
                "action_type": "im",
                "children": [{"action_type": "im", "msg_id": 800000}],
            },
            {
                "event_time": 1662480000,
                "node_name": "683827468797481xxxx_1662480000_combine",
                "action_type": "combine",
                "children": [
                    {"action_type": "switch_accoount"},
                    {"action_type": "switch_accoount"},
                    {"action_type": "enter_personal_detail"},
                    {"action_type": "invite", "placeholder": '"placeholder"'},
                    {"action_type": "invite", "placeholder": '"placeholder"'},
                    {"action_type": "switch_accoount"},
                    {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
                    {"action_type": "enter_personal_detail"},
                    {
                        "action_type": "report",
                        "content": "report context in string",
                        "report_type": "user",
                        "target": "user_id",
                    },
                    {"action_type": "follow", "is_unfollow": False, "source": 1},
                    {"action_type": "enter_personal_detail"},
                    {
                        "action_type": "post_video",
                        "video_id": 987654,
                        "is_delete": True,
                    },
                    {
                        "action_type": "post_video",
                        "video_id": 987654,
                        "is_delete": True,
                    },
                    {"action_type": "invite", "placeholder": '"placeholder"'},
                    {"action_type": "follow", "is_unfollow": False, "source": 1},
                    {"action_type": "invite", "placeholder": '"placeholder"'},
                    {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
                    {"action_type": "switch_accoount"},
                    {
                        "action_type": "post_video",
                        "video_id": 987654,
                        "is_delete": True,
                    },
                    {
                        "action_type": "report",
                        "content": "report context in string",
                        "report_type": "user",
                        "target": "user_id",
                    },
                    {"action_type": "invite", "placeholder": '"placeholder"'},
                    {
                        "action_type": "post_video",
                        "video_id": 987654,
                        "is_delete": True,
                    },
                    {"action_type": "follow", "is_unfollow": False, "source": 1},
                    {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
                    {"action_type": "follow", "is_unfollow": False, "source": 1},
                    {
                        "action_type": "report",
                        "content": "report context in string",
                        "report_type": "user",
                        "target": "user_id",
                    },
                    {
                        "action_type": "post_video",
                        "video_id": 987654,
                        "is_delete": True,
                    },
                    {"action_type": "follow", "is_unfollow": False, "source": 1},
                    {
                        "action_type": "report",
                        "content": "report context in string",
                        "report_type": "user",
                        "target": "user_id",
                    },
                    {
                        "action_type": "report",
                        "content": "report context in string",
                        "report_type": "user",
                        "target": "user_id",
                    },
                    {"action_type": "switch_accoount"},
                    {
                        "action_type": "post_video",
                        "video_id": 987654,
                        "is_delete": True,
                    },
                    {
                        "action_type": "report",
                        "content": "report context in string",
                        "report_type": "user",
                        "target": "user_id",
                    },
                    {"action_type": "invite", "placeholder": '"placeholder"'},
                    {"action_type": "follow", "is_unfollow": False, "source": 1},
                    {"action_type": "switch_accoount"},
                    {"action_type": "switch_accoount"},
                    {"action_type": "switch_accoount"},
                    {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
                    {"action_type": "enter_personal_detail"},
                    {"action_type": "enter_personal_detail"},
                    {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
                    {"action_type": "invite", "placeholder": '"placeholder"'},
                    {"action_type": "follow", "is_unfollow": False, "source": 1},
                    {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
                    {"action_type": "switch_accoount"},
                    {"action_type": "switch_accoount"},
                    {"action_type": "enter_personal_detail"},
                    {
                        "action_type": "report",
                        "content": "report context in string",
                        "report_type": "user",
                        "target": "user_id",
                    },
                    {
                        "action_type": "post_video",
                        "video_id": 987654,
                        "is_delete": True,
                    },
                    {"action_type": "switch_accoount"},
                    {"action_type": "enter_personal_detail"},
                    {"action_type": "switch_accoount"},
                    {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
                    {
                        "action_type": "post_video",
                        "video_id": 987654,
                        "is_delete": True,
                    },
                    {"action_type": "enter_personal_detail"},
                    {"action_type": "enter_personal_detail"},
                    {"action_type": "invite", "placeholder": '"placeholder"'},
                    {"action_type": "follow", "is_unfollow": False, "source": 1},
                    {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
                    {
                        "action_type": "report",
                        "content": "report context in string",
                        "report_type": "user",
                        "target": "user_id",
                    },
                    {
                        "action_type": "post_video",
                        "video_id": 987654,
                        "is_delete": True,
                    },
                    {"action_type": "enter_personal_detail"},
                    {"action_type": "enter_personal_detail"},
                    {
                        "action_type": "post_video",
                        "video_id": 987654,
                        "is_delete": True,
                    },
                    {"action_type": "enter_personal_detail"},
                    {
                        "action_type": "post_video",
                        "video_id": 987654,
                        "is_delete": True,
                    },
                    {
                        "action_type": "post_video",
                        "video_id": 987654,
                        "is_delete": True,
                    },
                    {
                        "action_type": "post_video",
                        "video_id": 987654,
                        "is_delete": True,
                    },
                ],
            },
            {
                "event_time": 1662080000,
                "node_name": "683827468797481xxxx_1662080000_combine",
                "action_type": "combine",
                "children": [
                    {
                        "action_type": "change_profile",
                        "old_signature": "1",
                        "new_signature": "2",
                        "old_nickname": "3",
                        "new_nickname": "4",
                        "old_avatar_uri": "5",
                        "new_avatar_uri": "6",
                    },
                    {
                        "action_type": "comment",
                        "comment_id": 3000,
                        "content": "some comment from tiktok user",
                        "video_id": 90000001,
                        "is_delete": False,
                    },
                ],
            },
            {
                "event_time": 1662380000,
                "node_name": "683827468797481xxxx_1662380000_combine",
                "action_type": "combine",
                "children": [
                    {
                        "action_type": "comment",
                        "comment_id": 3000,
                        "content": "some comment from tiktok user",
                        "video_id": 90000001,
                        "is_delete": False,
                    },
                    {
                        "action_type": "change_profile",
                        "old_signature": "1",
                        "new_signature": "2",
                        "old_nickname": "3",
                        "new_nickname": "4",
                        "old_avatar_uri": "5",
                        "new_avatar_uri": "6",
                    },
                ],
            },
            {
                "event_time": 1662280000,
                "node_name": "683827468797481xxxx_1662280000_combine",
                "action_type": "combine",
                "children": [
                    {
                        "action_type": "comment",
                        "comment_id": 3000,
                        "content": "some comment from tiktok user",
                        "video_id": 90000001,
                        "is_delete": False,
                    },
                    {
                        "action_type": "change_profile",
                        "old_signature": "1",
                        "new_signature": "2",
                        "old_nickname": "3",
                        "new_nickname": "4",
                        "old_avatar_uri": "5",
                        "new_avatar_uri": "6",
                    },
                ],
            },
            {
                "event_time": 1662246669,
                "node_name": "683827468797481xxxx_1662246669_im",
                "action_type": "im",
                "children": [{"action_type": "im", "msg_id": 800000}],
            },
            {
                "event_time": 1662380001,
                "node_name": "683827468797481xxxx_1662380001_im",
                "action_type": "im",
                "children": [{"action_type": "im", "msg_id": 800000}],
            },
            {
                "event_time": 1662130000,
                "node_name": "683827468797481xxxx_1662130000_comment",
                "action_type": "comment",
                "children": [
                    {
                        "action_type": "comment",
                        "comment_id": 3000,
                        "content": "some comment from tiktok user",
                        "video_id": 90000001,
                        "is_delete": False,
                    }
                ],
            },
            {
                "event_time": 1662413334,
                "node_name": "683827468797481xxxx_1662413334_im",
                "action_type": "im",
                "children": [{"action_type": "im", "msg_id": 800000}],
            },
            {
                "event_time": 1662313335,
                "node_name": "683827468797481xxxx_1662313335_im",
                "action_type": "im",
                "children": [{"action_type": "im", "msg_id": 800000}],
            },
            {
                "event_time": 1662301120,
                "node_name": "683827468797481xxxx_1662301120_registry_device",
                "action_type": "registry_device",
                "children": [{"action_type": "registry_device"}],
            },
            {
                "event_time": 1662361127,
                "node_name": "683827468797481xxxx_1662361127_registry_ip",
                "action_type": "registry_ip",
                "children": [{"action_type": "registry_ip"}],
            },
            {
                "event_time": 1662230000,
                "node_name": "683827468797481xxxx_1662230000_comment",
                "action_type": "comment",
                "children": [
                    {
                        "action_type": "comment",
                        "comment_id": 3000,
                        "content": "some comment from tiktok user",
                        "video_id": 90000001,
                        "is_delete": False,
                    }
                ],
            },
            {
                "event_time": 1662180000,
                "node_name": "683827468797481xxxx_1662180000_combine",
                "action_type": "combine",
                "children": [
                    {
                        "action_type": "change_profile",
                        "old_signature": "1",
                        "new_signature": "2",
                        "old_nickname": "3",
                        "new_nickname": "4",
                        "old_avatar_uri": "5",
                        "new_avatar_uri": "6",
                    },
                    {
                        "action_type": "comment",
                        "comment_id": 3000,
                        "content": "some comment from tiktok user",
                        "video_id": 90000001,
                        "is_delete": False,
                    },
                ],
            },
            {
                "event_time": 1662430000,
                "node_name": "683827468797481xxxx_1662430000_comment",
                "action_type": "comment",
                "children": [
                    {
                        "action_type": "comment",
                        "comment_id": 3000,
                        "content": "some comment from tiktok user",
                        "video_id": 90000001,
                        "is_delete": False,
                    }
                ],
            },
            {
                "event_time": 1662446667,
                "node_name": "683827468797481xxxx_1662446667_im",
                "action_type": "im",
                "children": [{"action_type": "im", "msg_id": 800000}],
            },
            {
                "event_time": 1662331123,
                "node_name": "683827468797481xxxx_1662331123_binding_email",
                "action_type": "binding_email",
                "children": [{"action_type": "binding_email"}],
            },
            {
                "event_time": 1662280002,
                "node_name": "683827468797481xxxx_1662280002_im",
                "action_type": "im",
                "children": [{"action_type": "im", "msg_id": 800000}],
            },
            {
                "event_time": 1662180003,
                "node_name": "683827468797481xxxx_1662180003_im",
                "action_type": "im",
                "children": [{"action_type": "im", "msg_id": 800000}],
            },
            {
                "event_time": 1662213336,
                "node_name": "683827468797481xxxx_1662213336_im",
                "action_type": "im",
                "children": [{"action_type": "im", "msg_id": 800000}],
            },
            {
                "event_time": 1662330000,
                "node_name": "683827468797481xxxx_1662330000_comment",
                "action_type": "comment",
                "children": [
                    {
                        "action_type": "comment",
                        "comment_id": 3000,
                        "content": "some comment from tiktok user",
                        "video_id": 90000001,
                        "is_delete": False,
                    }
                ],
            },
        ],
    },
]
TEST_DATA_LINK_SERIES_DATA = [
    {
        "from": "683827468797481xxxx_1662346668_im",
        "to": "683827420033672xxxx_1662346668_im",
        "action_type": "im",
        "children": [{"action_type": "im", "msg_id": 800000}],
    },
    {
        "from": "683827468797481xxxx_1662480000_combine",
        "to": "683827420033672xxxx_1662480000_combine",
        "action_type": "combine",
        "children": [
            {"action_type": "switch_accoount"},
            {"action_type": "switch_accoount"},
            {"action_type": "enter_personal_detail"},
            {"action_type": "invite", "placeholder": "placeholder"},
            {"action_type": "invite", "placeholder": "placeholder"},
            {"action_type": "switch_accoount"},
            {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
            {"action_type": "enter_personal_detail"},
            {
                "action_type": "report",
                "content": "report context in string",
                "report_type": "user",
                "target": "user_id",
            },
            {"action_type": "follow", "is_unfollow": False, "source": 1},
            {"action_type": "enter_personal_detail"},
            {"action_type": "post_video", "video_id": 987654, "is_delete": True},
            {"action_type": "post_video", "video_id": 987654, "is_delete": True},
            {"action_type": "invite", "placeholder": "placeholder"},
            {"action_type": "follow", "is_unfollow": False, "source": 1},
            {"action_type": "invite", "placeholder": "placeholder"},
            {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
            {"action_type": "switch_accoount"},
            {"action_type": "post_video", "video_id": 987654, "is_delete": True},
            {
                "action_type": "report",
                "content": "report context in string",
                "report_type": "user",
                "target": "user_id",
            },
            {"action_type": "invite", "placeholder": "placeholder"},
            {"action_type": "post_video", "video_id": 987654, "is_delete": True},
            {"action_type": "follow", "is_unfollow": False, "source": 1},
            {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
            {"action_type": "follow", "is_unfollow": False, "source": 1},
            {
                "action_type": "report",
                "content": "report context in string",
                "report_type": "user",
                "target": "user_id",
            },
            {"action_type": "post_video", "video_id": 987654, "is_delete": True},
            {"action_type": "follow", "is_unfollow": False, "source": 1},
            {
                "action_type": "report",
                "content": "report context in string",
                "report_type": "user",
                "target": "user_id",
            },
            {
                "action_type": "report",
                "content": "report context in string",
                "report_type": "user",
                "target": "user_id",
            },
            {"action_type": "switch_accoount"},
            {"action_type": "post_video", "video_id": 987654, "is_delete": True},
            {
                "action_type": "report",
                "content": "report context in string",
                "report_type": "user",
                "target": "user_id",
            },
            {"action_type": "invite", "placeholder": "placeholder"},
            {"action_type": "follow", "is_unfollow": False, "source": 1},
            {"action_type": "switch_accoount"},
            {"action_type": "switch_accoount"},
            {"action_type": "switch_accoount"},
            {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
            {"action_type": "enter_personal_detail"},
            {"action_type": "enter_personal_detail"},
            {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
            {"action_type": "invite", "placeholder": "placeholder"},
            {"action_type": "follow", "is_unfollow": False, "source": 1},
            {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
            {"action_type": "switch_accoount"},
            {"action_type": "switch_accoount"},
            {"action_type": "enter_personal_detail"},
            {
                "action_type": "report",
                "content": "report context in string",
                "report_type": "user",
                "target": "user_id",
            },
            {"action_type": "post_video", "video_id": 987654, "is_delete": True},
            {"action_type": "switch_accoount"},
            {"action_type": "enter_personal_detail"},
            {"action_type": "switch_accoount"},
            {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
            {"action_type": "post_video", "video_id": 987654, "is_delete": True},
            {"action_type": "enter_personal_detail"},
            {"action_type": "enter_personal_detail"},
            {"action_type": "invite", "placeholder": "placeholder"},
            {"action_type": "follow", "is_unfollow": False, "source": 1},
            {"action_type": "like", "video_id": 1234567890, "is_cancel": True},
            {
                "action_type": "report",
                "content": "report context in string",
                "report_type": "user",
                "target": "user_id",
            },
            {"action_type": "post_video", "video_id": 987654, "is_delete": True},
            {"action_type": "enter_personal_detail"},
            {"action_type": "enter_personal_detail"},
            {"action_type": "post_video", "video_id": 987654, "is_delete": True},
            {"action_type": "enter_personal_detail"},
            {"action_type": "post_video", "video_id": 987654, "is_delete": True},
            {"action_type": "post_video", "video_id": 987654, "is_delete": True},
            {"action_type": "post_video", "video_id": 987654, "is_delete": True},
        ],
    },
    {
        "from": "683827468797481xxxx_1662380000_combine",
        "to": "683827420033672xxxx_1662380000_comment",
        "action_type": "combine",
        "children": [
            {
                "action_type": "comment",
                "comment_id": 3000,
                "content": "some comment from tiktok user",
                "video_id": 90000001,
                "is_delete": False,
            },
            {
                "action_type": "change_profile",
                "old_signature": "1",
                "new_signature": "2",
                "old_nickname": "3",
                "new_nickname": "4",
                "old_avatar_uri": "5",
                "new_avatar_uri": "6",
            },
        ],
    },
    {
        "from": "683827468797481xxxx_1662280000_combine",
        "to": "683827420033672xxxx_1662280000_comment",
        "action_type": "combine",
        "children": [
            {
                "action_type": "comment",
                "comment_id": 3000,
                "content": "some comment from tiktok user",
                "video_id": 90000001,
                "is_delete": False,
            },
            {
                "action_type": "change_profile",
                "old_signature": "1",
                "new_signature": "2",
                "old_nickname": "3",
                "new_nickname": "4",
                "old_avatar_uri": "5",
                "new_avatar_uri": "6",
            },
        ],
    },
    {
        "from": "683827468797481xxxx_1662246669_im",
        "to": "683827420033672xxxx_1662246669_im",
        "action_type": "im",
        "children": [{"action_type": "im", "msg_id": 800000}],
    },
    {
        "from": "683827468797481xxxx_1662380001_im",
        "to": "683827420033672xxxx_1662380001_im",
        "action_type": "im",
        "children": [{"action_type": "im", "msg_id": 800000}],
    },
    {
        "from": "683827468797481xxxx_1662130000_comment",
        "to": "683827420033672xxxx_1662130000_comment",
        "action_type": "comment",
        "children": [
            {
                "action_type": "comment",
                "comment_id": 3000,
                "content": "some comment from tiktok user",
                "video_id": 90000001,
                "is_delete": False,
            }
        ],
    },
    {
        "from": "683827468797481xxxx_1662080000_combine",
        "to": "683827420033672xxxx_1662080000_comment",
        "action_type": "combine",
        "children": [
            {
                "action_type": "change_profile",
                "old_signature": "1",
                "new_signature": "2",
                "old_nickname": "3",
                "new_nickname": "4",
                "old_avatar_uri": "5",
                "new_avatar_uri": "6",
            },
            {
                "action_type": "comment",
                "comment_id": 3000,
                "content": "some comment from tiktok user",
                "video_id": 90000001,
                "is_delete": False,
            },
        ],
    },
    {
        "from": "683827468797481xxxx_1662413334_im",
        "to": "683827420033672xxxx_1662413334_im",
        "action_type": "im",
        "children": [{"action_type": "im", "msg_id": 800000}],
    },
    {
        "from": "683827468797481xxxx_1662313335_im",
        "to": "683827420033672xxxx_1662313335_im",
        "action_type": "im",
        "children": [{"action_type": "im", "msg_id": 800000}],
    },
    {
        "from": "25328254226993xxxx_1662321122_login_device",
        "to": "683827422612367xxxx_1662321122_login_device",
        "action_type": "login_device",
        "children": [{"action_type": "login_device"}],
    },
    {
        "from": "683827468797481xxxx_1662301120_registry_device",
        "to": "683827422612367xxxx_1662301120_registry_device",
        "action_type": "registry_device",
        "children": [{"action_type": "registry_device"}],
    },
    {
        "from": "683827468797481xxxx_1662361127_registry_ip",
        "to": "93.23.xxx.xx_20200615_1662361127_registry_ip",
        "action_type": "registry_ip",
        "children": [{"action_type": "registry_ip"}],
    },
    {
        "from": "683827468797481xxxx_1662230000_comment",
        "to": "683827420033672xxxx_1662230000_comment",
        "action_type": "comment",
        "children": [
            {
                "action_type": "comment",
                "comment_id": 3000,
                "content": "some comment from tiktok user",
                "video_id": 90000001,
                "is_delete": False,
            }
        ],
    },
    {
        "from": "713019589280868xxxx_1662061124_login_device",
        "to": "713019502467512xxxx_1662061124_login_device",
        "action_type": "login_device",
        "children": [{"action_type": "login_device"}],
    },
    {
        "from": "683827420033672xxxx_1662503541_registry_device",
        "to": "683827422612367xxxx_1662503541_registry_device",
        "action_type": "registry_device",
        "children": [{"action_type": "registry_device"}],
    },
    {
        "from": "683827468797481xxxx_1662180000_combine",
        "to": "683827420033672xxxx_1662180000_comment",
        "action_type": "combine",
        "children": [
            {
                "action_type": "change_profile",
                "old_signature": "1",
                "new_signature": "2",
                "old_nickname": "3",
                "new_nickname": "4",
                "old_avatar_uri": "5",
                "new_avatar_uri": "6",
            },
            {
                "action_type": "comment",
                "comment_id": 3000,
                "content": "some comment from tiktok user",
                "video_id": 90000001,
                "is_delete": False,
            },
        ],
    },
    {
        "from": "683827468797481xxxx_1662430000_comment",
        "to": "683827420033672xxxx_1662430000_comment",
        "action_type": "comment",
        "children": [
            {
                "action_type": "comment",
                "comment_id": 3000,
                "content": "some comment from tiktok user",
                "video_id": 90000001,
                "is_delete": False,
            }
        ],
    },
    {
        "from": "683827468797481xxxx_1662446667_im",
        "to": "683827420033672xxxx_1662446667_im",
        "action_type": "im",
        "children": [{"action_type": "im", "msg_id": 800000}],
    },
    {
        "from": "683827468797481xxxx_1662331123_binding_email",
        "to": "bcb395f84ae8882de39d2a8e68d459c177a7b5a0b6"
        "884047b0fce1f28d21xxxx_1662331123_binding_email",
        "action_type": "binding_email",
        "children": [{"action_type": "binding_email"}],
    },
    {
        "from": "683827468797481xxxx_1662280002_im",
        "to": "683827420033672xxxx_1662280002_im",
        "action_type": "im",
        "children": [{"action_type": "im", "msg_id": 800000}],
    },
    {
        "from": "683827468797481xxxx_1662180003_im",
        "to": "683827420033672xxxx_1662180003_im",
        "action_type": "im",
        "children": [{"action_type": "im", "msg_id": 800000}],
    },
    {
        "from": "683827957407865xxxx_1662311121_login_device",
        "to": "683827422612367xxxx_1662311121_login_device",
        "action_type": "login_device",
        "children": [{"action_type": "login_device"}],
    },
    {"from": None, "to": None},
    {
        "from": "683827468797481xxxx_1662213336_im",
        "to": "683827420033672xxxx_1662213336_im",
        "action_type": "im",
        "children": [{"action_type": "im", "msg_id": 800000}],
    },
    {
        "from": "683827468797481xxxx_1662330000_comment",
        "to": "683827420033672xxxx_1662330000_comment",
        "action_type": "comment",
        "children": [
            {
                "action_type": "comment",
                "comment_id": 3000,
                "content": "some comment from tiktok user",
                "video_id": 90000001,
                "is_delete": False,
            }
        ],
    },
    {
        "from": "683827420033672xxxx_1662161125_login_device",
        "to": "683827422612367xxxx_1662161125_login_device",
        "action_type": "login_device",
        "children": [{"action_type": "login_device"}],
    },
]

TEST_CHART_DATA = [
    opts.BaseDataOpts(
        id_="register",
        values=TEST_REGISTER_DATA,
    ),
    opts.BaseDataOpts(
        id_="im",
        values=TEST_IM_DATA,
    ),
    opts.BaseDataOpts(
        id_="comment",
        values=TEST_COMMENT_DATA,
    ),
    opts.BaseDataOpts(
        id_="dataDotSeries",
        values=TEST_DATA_DOT_SERIES_DATA,
    ),
    opts.BaseDataOpts(
        id_="dataLinkSeries",
        values=TEST_DATA_LINK_SERIES_DATA,
    ),
]


def _gen_bar(data_id: str, x_field_name: str, y_field_name) -> dict:
    b = (
        Bar()
        .set_xy_field(x_field_name=x_field_name, y_field_name=y_field_name)
        .set_bar_spec(
            data_id=data_id,
            label_opts=opts.LabelOpts(
                style_opts=opts.BaseStyleOpts(
                    is_visible=False,
                    fill="black",
                )
            ),
        )
        .set_global_options(
            height=40,
            padding_opts=10,
            tooltip_opts=opts.TooltipOpts(
                is_visible=True,
                mark_opts=opts.TooltipCustomOpts(
                    title_value="bar info",
                    content=[
                        opts.TooltipCustomStyleOpts(
                            key="start_time",
                            value=JsCode("datum => datum['start_time']"),
                        ),
                        opts.TooltipCustomStyleOpts(
                            key="start_time_stamp",
                            value=JsCode("datum => datum['start_time']"),
                        ),
                        opts.TooltipCustomStyleOpts(
                            key="end_time",
                            value=JsCode("datum => datum['end_time']"),
                        ),
                        opts.TooltipCustomStyleOpts(
                            key="end_time_stamp",
                            value=JsCode("datum => datum['end_time']"),
                        ),
                        opts.TooltipCustomStyleOpts(
                            key="value",
                            value=JsCode("datum => datum['value']"),
                        ),
                    ],
                ),
            ),
        )
    )
    return b.options


def _gen_dot() -> dict:
    d = (
        Dot()
        .set_xy_field(x_field_name="event_time", y_field_name="id")
        .set_global_options(
            tooltip_opts=opts.TooltipOpts(
                mark_opts=opts.TooltipCustomOpts(
                    title_value="event info",
                    content=[
                        opts.TooltipCustomStyleOpts(
                            is_has_shape=True,
                            shape_type="square",
                            key=JsCode("datum => datum['type']"),
                            value=JsCode("datum => datum['id']"),
                        ),
                        opts.TooltipCustomStyleOpts(
                            is_has_shape=False,
                            key="event_time_stamp",
                            value=JsCode("datum => datum['event_time']"),
                        ),
                        opts.TooltipCustomStyleOpts(
                            is_has_shape=True,
                            shape_type="square",
                            key="action_type",
                            value=JsCode("datum => datum['action_type']"),
                        ),
                        opts.TooltipCustomStyleOpts(
                            is_has_shape=True,
                            shape_type="square",
                            key="children",
                            value=JsCode("datum => datum['children']"),
                        ),
                    ],
                )
            )
        )
        .set_dot_spec(
            data_id="dataDotSeries",
            series_group_field="type",
            title_field="type",
            sub_title_field="id",
            dot_type_field="action_type",
            high_light_series_group="IP",
            clip_height=1000,
            title_opts=opts.DotTitleOpts(
                style=opts.BaseStyleOpts(fill="rgba(46, 47, 50)"),
            ),
            sub_title_opts=opts.DotSubTitleOpts(
                style=opts.BaseStyleOpts(
                    fill="rgba(46, 47, 50)",
                    dy=7,
                ),
            ),
            symbol_opts=opts.DotTitleOpts(
                style=opts.BaseStyleOpts(
                    dx=-20,
                ),
            ),
        )
    )
    return d.options


def _gen_link() -> dict:
    link_c = (
        Link()
        .set_link_spec(
            data_id="dataLinkSeries",
            dot_series_index=3,
            from_field="from",
            to_field="to",
            dot_type_field="action_type",
        )
        .set_global_options(
            tooltip_opts=opts.TooltipOpts(
                mark_opts=opts.TooltipCustomOpts(
                    title_value="link info",
                    content=[
                        opts.TooltipCustomStyleOpts(
                            is_has_shape=True,
                            shape_type="square",
                            key="time",
                            value=JsCode("datum => datum['from'].split('_')[1]"),
                        ),
                        opts.TooltipCustomStyleOpts(
                            is_has_shape=False,
                            key="time_stamp",
                            value=JsCode("datum => datum['from'].split('_')[1]"),
                        ),
                        opts.TooltipCustomStyleOpts(
                            is_has_shape=True,
                            shape_type="square",
                            key="type",
                            value=JsCode("datum => datum['action_type']"),
                        ),
                        opts.TooltipCustomStyleOpts(
                            is_has_shape=True,
                            shape_type="square",
                            key="from",
                            value=JsCode("datum => datum['from']"),
                        ),
                        opts.TooltipCustomStyleOpts(
                            is_has_shape=True,
                            shape_type="square",
                            key="to",
                            value=JsCode("datum => datum['to']"),
                        ),
                    ],
                )
            )
        )
    )
    return link_c.options


class TestSequenceChart(unittest.TestCase):

    @patch("pyvchart.render.engine.write_utf8_html_file")
    def test_sequence_base(self, fake_writer):
        c = (
            Sequence()
            .set_data(data=TEST_CHART_DATA)
            .set_sequence_spec(
                append_padding={"left": 80, "right": 80},
                series=[
                    _gen_bar(
                        data_id="register",
                        x_field_name="start_time",
                        y_field_name="end_time",
                    ),
                    _gen_bar(
                        data_id="im", x_field_name="start_time", y_field_name="end_time"
                    ),
                    _gen_bar(
                        data_id="comment",
                        x_field_name="start_time",
                        y_field_name="value",
                    ),
                    _gen_dot(),
                    _gen_link(),
                ],
            )
            .set_global_options(
                data_zoom_opts=[
                    opts.DataZoomOpts(
                        orient="top",
                        # xAxisIndex: 0
                        region_index=[1, 2, 3, 4],
                        start=0.1,
                        end_value=1662351800,
                        start_text_format_method=JsCode("text => Math.floor(text)"),
                        end_text_format_method=JsCode("text => Math.floor(text)"),
                    )
                ],
                axes_opts=[
                    opts.AxesTimeOpts(
                        base_axes_opts=opts.BaseAxesOpts(orient="top"),
                        layers=[
                            opts.AxesLayerOpts(tick_step=28800, time_format="%H:%M"),
                            opts.AxesLayerOpts(tick_step=86400, time_format="%Y%m%d"),
                        ],
                    )
                ],
                scroll_bar_opts=[
                    opts.ScrollBarOpts(
                        is_visible=False,
                        start=0,
                        end=0.3,
                        # roam: true
                        filter_mode="axis",
                        region_index=4,
                        axis_index=4,
                    )
                ],
            )
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertGreater(len(content), 1000)
        self.assertEqual(c.options.get("type"), ChartType.SEQUENCE)
