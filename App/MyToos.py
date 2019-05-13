'''
@Author: Mr Bean
@Date: 2019-05-12 00:44:18
@LastEditors: Mr Bean
@LastEditTime: 2019-05-12 00:51:41
@Description: 自定义静态工具类
'''

import re
from pypinyin import lazy_pinyin, Style


class KTools(object):
    """ 自定义工具类 """

    @staticmethod
    def cnToPinYin(hanZi):
        '''
        汉字转拼音首字母

        Params:
          hanZi - 需要转换的汉字

        Return:
          返回汉字拼音首字母字符串

        '''
        pattern = r"[\(\)\?\*？（） +]"
        tmp_str = ''
        pinyin = lazy_pinyin(hanZi, style=Style.FIRST_LETTER, strict=False)
        for item in pinyin:
            tmp_str += item

        result_str = re.sub(pattern, '', tmp_str)

        return result_str


if __name__ == '__main__':
    s = '你好(是)?**天*（王）加？ sss+++'
    r = KTools.cnToPinYin(s)
    print(r)
