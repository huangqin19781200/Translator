from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.tmt.v20180321 import tmt_client, models
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import json

from config import *


class AppFunctions():
    # 通过选项盒选择语言
    def select_language(self, select: str) -> tuple[str, str]:
        if select == "English  >>  中文":
            return 'en', 'zh'
        
        if select == "中文  >>  English":
            return 'zh', 'en'
        
        if select == "Русский  >>  中文":
            return 'ru', 'zh'
        
        if select == "中文  >>  Русский":
            return 'zh', 'ru'
        
        if select == "日本語  >>  中文":
            return 'ja', 'zh'
        
        if select == "中文  >>  日本語":
            return 'zh', 'ja'
    
    # 执行翻译功能
    def translate(self, source_text: str, selecte: str) -> str:
        source, target = AppFunctions.select_language(self, selecte)
        try:
            cred = credential.Credential(Settings.SecretId, Settings.SecretKey)

            httpProfile = HttpProfile()
            httpProfile.endpoint = "tmt.tencentcloudapi.com"

            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile

            client = tmt_client.TmtClient(cred, "ap-beijing", clientProfile)

            req = models.TextTranslateRequest()
            req.SourceText = source_text
            req.Source = source
            req.Target = target
            req.ProjectId = 0

            resp = client.TextTranslate(req)
            data = json.loads(resp.to_json_string())
            target_text = str(data['TargetText'])

            # 日志记录
            logging.info(
                f"Setting:\n# source language: {source}\n# target language: {target}\n# input: {source_text}\n# output: {target_text}"
            )

            return target_text
    
        except TencentCloudSDKException as error:
            logging.error(error)
            return str(error)
